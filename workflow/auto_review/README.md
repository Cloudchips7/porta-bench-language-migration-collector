# Auto Review Workflow

`workflow/auto_review` is the machine-assisted review workflow for Porta-Bench
language-migration candidates. It turns snapshot-ready PR metadata into
review-tool-compatible JSON labels by combining deterministic evidence packs,
heuristic prefill, LLM review, schema checks, and final result export.

This workflow does not collect GitHub PRs or create repository snapshots by
itself. It expects the collector/enrichment pipeline to have already produced:

- `data/raw/pr_metadata/<subtype>/<instance_id>.json`
- `data/raw/repo_snapshots/<subtype>/<snapshot_bundle>/r0`
- `data/raw/repo_snapshots/<subtype>/<snapshot_bundle>/rn`

Supported subtypes:

- `py2_py3`
- `cpp_python`
- `java_python`
- `python_cpp`
- `python_java`

## Directory Layout

```text
workflow/auto_review/
|-- README.md
|-- run_auto_review.py
|-- cleanup_negative_snapshots.py
|-- start_remaining_auto_review.ps1
|-- workflow预览.png
|-- configs/
|   |-- pipeline_config.json
|   `-- output_schema.json
`-- prompts/
    |-- review_system_prompt.md
    `-- review_user_prompt.md
```

| Path | Purpose |
| --- | --- |
| `run_auto_review.py` | Main entry point for evidence building, heuristic review, LLM review, self-check, final merge, and batch runs. |
| `cleanup_negative_snapshots.py` | Maintenance helper for summarizing labels and optionally deleting snapshots/archive bundles for reviewed negative samples. Use dry-run first. |
| `start_remaining_auto_review.ps1` | PowerShell launcher for background batch runs across remaining subtypes. |
| `workflow预览.png` | Workflow preview image used during local discussion/documentation. |
| `configs/pipeline_config.json` | Runtime configuration: model provider, env file, API key names, base URL/model env names, concurrency, timeout, and truncation limits. |
| `configs/output_schema.json` | Required final review fields and allowed enum values. |
| `prompts/review_system_prompt.md` | System prompt with positive/negative/uncertain judgment policy. |
| `prompts/review_user_prompt.md` | User prompt describing the review fields to fill. |

## Runtime Configuration

Current default configuration is in
`workflow/auto_review/configs/pipeline_config.json`.

The checked-in default uses an OpenAI-compatible chat-completions endpoint:

```json
{
  "model_provider": "openai_compatible",
  "model_name": "gpt-5.4",
  "env_file": ".env",
  "api_key_priority": ["DEFAULT_LLM_API_KEY2"],
  "base_url_env_name": "DEFAULT_LLM_BASE_URL2",
  "model_env_name": "DEFAULT_LLM_MODEL_NAME2"
}
```

Secrets are not committed. Put keys in the repository root `.env` file or export
them in the shell environment. Environment variables override values loaded from
`.env`.

Example `.env`:

```text
DEFAULT_LLM_API_KEY2=...
DEFAULT_LLM_BASE_URL2=https://example-compatible-endpoint/v1
DEFAULT_LLM_MODEL_NAME2=gpt-5.4
```

Python package requirements:

```powershell
pip install openai zhipuai
```

`zhipuai` is kept for compatibility with older GLM-based runs; the default
provider is currently `openai_compatible`.

## Main Pipeline

Run from the repository root.

### 1. Build Evidence

Creates a compact evidence pack from PR metadata, changed files, selected patch
snippets, and r0/rn file previews.

```powershell
python workflow\auto_review\run_auto_review.py --stage build-evidence --instance-id py2_py3__amillb__pgMapMatch__pr34
```

Output:

```text
data/auto_review/evidence/<subtype>/<instance_id>.json
```

### 2. Heuristic Review

Creates a deterministic prefill without calling an LLM.

```powershell
python workflow\auto_review\run_auto_review.py --stage heuristic-review --instance-id py2_py3__amillb__pgMapMatch__pr34
```

Output:

```text
data/auto_review/drafts/<subtype>/<instance_id>.heuristic.json
```

### 3. LLM Review

Calls the configured model and stores the raw answer plus parsed JSON.

```powershell
python workflow\auto_review\run_auto_review.py --stage llm-review --instance-id py2_py3__amillb__pgMapMatch__pr34
```

Output:

```text
data/auto_review/drafts/<subtype>/<instance_id>.llm.json
```

### 4. Self Check

Merges heuristic and LLM fields, forces deterministic subtype direction fields,
checks enum values, and validates required fields against `output_schema.json`.

```powershell
python workflow\auto_review\run_auto_review.py --stage self-check --instance-id py2_py3__amillb__pgMapMatch__pr34
```

Output:

```text
data/auto_review/drafts/<subtype>/<instance_id>.checked.json
```

### 5. Merge Results

Writes the final review JSON and a trace file showing which intermediate files
were used.

```powershell
python workflow\auto_review\run_auto_review.py --stage merge-results --instance-id py2_py3__amillb__pgMapMatch__pr34
```

Outputs:

```text
data/auto_review/final/by_instance/<instance_id>.json
data/auto_review/final/traces/<instance_id>.json
```

### Run One Instance End-to-End

```powershell
python workflow\auto_review\run_auto_review.py --stage run-all --instance-id py2_py3__amillb__pgMapMatch__pr34 --attempts 3
```

### Run a Batch

```powershell
python workflow\auto_review\run_auto_review.py --stage run-batch --subtype py2_py3 --limit 30 --workers 2 --attempts 3 --resume
```

Batch summary output:

```text
data/auto_review/final/batch_runs/<subtype>__limit<N>.json
```

Batch options:

| Option | Meaning |
| --- | --- |
| `--limit N` | Process at most `N` snapshot-ready instances. `0` means no explicit limit. |
| `--workers N` | Parallel worker count. |
| `--attempts N` | Retry count for each instance. |
| `--resume` | Skip instances that already have final output. |
| `--reviewer-filter NAME` | Only process instances whose existing `data/review_results/by_instance` reviewer matches `NAME`. |
| `--write-review-results` | Also write final JSON into `data/review_results/by_instance`. Use only after reviewing quality because this touches the manual/web annotation result area. |

## Stages That Do Not Need an API Key

These stages can be used for local validation without model access:

- `build-evidence`
- `heuristic-review`
- `self-check` after an LLM draft exists
- `merge-results` after a checked draft exists

These stages need model credentials:

- `llm-review`
- `run-all`
- `run-batch`

## Maintenance Helper

Summarize final auto-review labels:

```powershell
python workflow\auto_review\cleanup_negative_snapshots.py --mode stats
```

Dry-run deletion of negative snapshots:

```powershell
python workflow\auto_review\cleanup_negative_snapshots.py --mode delete --label negative --subtype py2_py3 --limit 5
```

Actually delete matched snapshot/archive directories only after inspecting the
dry-run output:

```powershell
python workflow\auto_review\cleanup_negative_snapshots.py --mode delete --label negative --subtype py2_py3 --limit 5 --apply
```

The delete mode is intentionally explicit. It can remove directories under
`data/raw/repo_snapshots` and `data/raw/repo_snapshot_archives`, then update
snapshot list files. Do not run it with `--apply` until the dry-run result is
confirmed.

## Validation Commands

Basic smoke tests:

```powershell
python -m py_compile workflow\auto_review\run_auto_review.py workflow\auto_review\cleanup_negative_snapshots.py
python workflow\auto_review\run_auto_review.py --help
python workflow\auto_review\cleanup_negative_snapshots.py --help
```

Local no-API sample validation, assuming the metadata and snapshots exist:

```powershell
python workflow\auto_review\run_auto_review.py --stage build-evidence --instance-id py2_py3__amillb__pgMapMatch__pr34
python workflow\auto_review\run_auto_review.py --stage heuristic-review --instance-id py2_py3__amillb__pgMapMatch__pr34
```

`data/auto_review/` is generated output. Review it before copying anything into
`data/review_results/by_instance`.

## Review Policy

The prompts intentionally use conservative annotation rules:

- A positive cross-language sample needs evidence that a source-language
  implementation is replaced, translated, or clearly handed over to a target
  implementation.
- Wrappers, bindings, bridges, clients, parsers, code generators, CI changes,
  docs, and examples are not positive by themselves.
- If evidence is mixed, prefer `uncertain` over guessing a positive label.
- For `py2_py3`, the workflow forces `python` version `2` to `python` version
  `3` direction fields.

Final output fields are constrained by `configs/output_schema.json` so they can
be consumed by the review tooling and later `apply-review`/packaging steps.
