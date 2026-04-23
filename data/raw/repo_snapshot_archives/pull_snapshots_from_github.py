#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import logging
import shutil
import subprocess
import tempfile
import time
from datetime import datetime
from pathlib import Path
from typing import Any


ARCHIVE_TOOL_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = ARCHIVE_TOOL_DIR.parents[2]
DATA_DIR = PROJECT_ROOT / "data"
PR_METADATA_DIR = DATA_DIR / "raw" / "pr_metadata"
SNAPSHOT_DIR = DATA_DIR / "raw" / "repo_snapshots"
TMP_DIR = PROJECT_ROOT / "tmp"
LOG_DIR = PROJECT_ROOT / "logs"
CLONE_LIST_PATH = ARCHIVE_TOOL_DIR / "snapshot_clone_list.json"

SUPPORTED_SUBTYPES = ["py2_py3", "cpp_python", "java_python", "python_cpp", "python_java"]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def dump_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def project_relpath(path: Path) -> str:
    return path.relative_to(PROJECT_ROOT).as_posix()


def normalize_relpath(value: str) -> str:
    return value.replace("\\", "/").lstrip("/")


def configure_logger() -> logging.Logger:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("pull_snapshots_from_github")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler = logging.FileHandler(LOG_DIR / "pull_snapshots_from_github.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def metadata_paths() -> list[Path]:
    paths: list[Path] = []
    for subtype in SUPPORTED_SUBTYPES:
        paths.extend(sorted((PR_METADATA_DIR / subtype).glob(f"{subtype}__*.json")))
    return paths


def build_clone_list(include_only_existing_snapshots: bool = True) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for metadata_path in metadata_paths():
        metadata = load_json(metadata_path)
        instance_id = metadata.get("instance_id") or metadata_path.stem
        subtype = metadata.get("subtype") or instance_id.split("__", 1)[0]
        repo = metadata.get("repo", {})
        paths = metadata.get("paths", {})
        r0_rel = normalize_relpath(paths.get("r0_path", ""))
        rn_rel = normalize_relpath(paths.get("rn_path", ""))
        if not r0_rel or not rn_rel:
            continue
        r0_path = PROJECT_ROOT / r0_rel
        rn_path = PROJECT_ROOT / rn_rel
        if include_only_existing_snapshots and not (r0_path.exists() and rn_path.exists()):
            continue
        clone_url = repo.get("clone_url") or ""
        if not clone_url and repo.get("full_name"):
            clone_url = f"https://github.com/{repo['full_name']}.git"
        if not clone_url:
            continue
        entries.append(
            {
                "instance_id": instance_id,
                "subtype": subtype,
                "repo_full_name": repo.get("full_name", metadata.get("repo_full_name", "")),
                "clone_url": clone_url,
                "base_sha": metadata.get("base_sha", ""),
                "final_sha": metadata.get("final_sha", ""),
                "snapshot_root_relpath": normalize_relpath(str(Path(r0_rel).parent)),
                "r0_path": r0_rel,
                "rn_path": rn_rel,
                "metadata_path": project_relpath(metadata_path),
            }
        )
    entries.sort(key=lambda item: item["instance_id"])
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "description": "Clone list for rebuilding data/raw/repo_snapshots from original GitHub repositories without sharing snapshot zip files.",
        "count": len(entries),
        "entries": entries,
    }


def run_git(args: list[str], cwd: Path | None = None) -> None:
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} failed: {result.stderr.strip()}")


def clone_repo(clone_url: str, repo_dir: Path) -> None:
    run_git(["git", "clone", "--no-checkout", "--filter=blob:none", clone_url, str(repo_dir)])


def ensure_commit_available(repo_dir: Path, sha: str) -> None:
    check = subprocess.run(["git", "cat-file", "-e", sha], cwd=repo_dir, capture_output=True, text=True)
    if check.returncode == 0:
        return
    run_git(["git", "fetch", "--depth", "1", "origin", sha], cwd=repo_dir)


def assert_under_snapshot_dir(path: Path) -> None:
    resolved = path.resolve()
    snapshot_root = SNAPSHOT_DIR.resolve()
    if resolved != snapshot_root and snapshot_root not in resolved.parents:
        raise RuntimeError(f"Refusing to modify path outside repo_snapshots: {path}")


def checkout_and_copy(repo_dir: Path, sha: str, destination: Path, force: bool) -> None:
    if destination.exists():
        if not force:
            return
        assert_under_snapshot_dir(destination)
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    ensure_commit_available(repo_dir, sha)
    run_git(["git", "checkout", "--force", sha], cwd=repo_dir)
    shutil.copytree(
        repo_dir,
        destination,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache", ".mypy_cache"),
    )


def select_entries(payload: dict[str, Any], args: argparse.Namespace) -> list[dict[str, Any]]:
    entries = payload.get("entries", [])
    if args.instance_id:
        entries = [item for item in entries if item["instance_id"] == args.instance_id]
    elif args.subtype:
        entries = [item for item in entries if item["subtype"] == args.subtype]
    elif not args.all:
        raise RuntimeError("Use --all, --subtype, or --instance-id.")
    if args.limit:
        entries = entries[: args.limit]
    return entries


def restore_entry(entry: dict[str, Any], force: bool, logger: logging.Logger) -> str:
    r0_path = PROJECT_ROOT / normalize_relpath(entry["r0_path"])
    rn_path = PROJECT_ROOT / normalize_relpath(entry["rn_path"])
    if r0_path.exists() and rn_path.exists() and not force:
        return "skipped_existing"
    if not entry.get("base_sha") or not entry.get("final_sha"):
        raise RuntimeError("Missing base_sha or final_sha in clone list entry.")

    TMP_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="snapshot_clone_", dir=str(TMP_DIR)) as temp_dir:
        repo_dir = Path(temp_dir) / "repo"
        logger.info("Cloning %s for %s", entry["repo_full_name"], entry["instance_id"])
        clone_repo(entry["clone_url"], repo_dir)
        checkout_and_copy(repo_dir, entry["base_sha"], r0_path, force=force)
        checkout_and_copy(repo_dir, entry["final_sha"], rn_path, force=force)
    return "restored"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rebuild data/raw/repo_snapshots from original GitHub repositories.")
    parser.add_argument("--build-list", action="store_true", help="Generate snapshot_clone_list.json from local metadata.")
    parser.add_argument("--include-missing", action="store_true", help="When building list, include metadata even if local snapshots are missing.")
    parser.add_argument("--all", action="store_true", help="Restore every entry in snapshot_clone_list.json.")
    parser.add_argument("--subtype", default="", help="Restore one subtype, e.g. py2_py3.")
    parser.add_argument("--instance-id", default="", help="Restore one instance id.")
    parser.add_argument("--limit", type=int, default=0, help="Optional max entries to restore.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing r0/rn directories.")
    parser.add_argument("--sleep-sec", type=float, default=0.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logger = configure_logger()

    if args.build_list:
        payload = build_clone_list(include_only_existing_snapshots=not args.include_missing)
        dump_json(CLONE_LIST_PATH, payload)
        logger.info("Wrote %s entries to %s", payload["count"], CLONE_LIST_PATH)
        return

    if not CLONE_LIST_PATH.exists():
        raise FileNotFoundError(f"Missing clone list: {CLONE_LIST_PATH}. Run --build-list first.")

    payload = load_json(CLONE_LIST_PATH)
    entries = select_entries(payload, args)
    if not entries:
        logger.info("No matching entries.")
        return

    started_at = time.time()
    restored = 0
    skipped = 0
    failed = 0
    total = len(entries)
    for index, entry in enumerate(entries, start=1):
        item_started = time.time()
        try:
            status = restore_entry(entry, force=args.force, logger=logger)
            if status == "restored":
                restored += 1
            else:
                skipped += 1
            logger.info(
                "[%s/%s] %s %s elapsed=%.1fs",
                index,
                total,
                status,
                entry["instance_id"],
                time.time() - item_started,
            )
        except Exception as exc:  # noqa: BLE001
            failed += 1
            logger.exception("[%s/%s] failed %s: %s", index, total, entry.get("instance_id"), exc)
        if args.sleep_sec:
            time.sleep(args.sleep_sec)

    logger.info(
        "Finished. total=%s restored=%s skipped=%s failed=%s elapsed=%.1fs",
        total,
        restored,
        skipped,
        failed,
        time.time() - started_at,
    )


if __name__ == "__main__":
    main()
