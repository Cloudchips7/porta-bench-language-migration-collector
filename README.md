# Porta-Bench Language Migration Collector

This repository contains a data collection pipeline for Porta-Bench scenario 2: language migration.

Current focus:
- `py2 -> py3`
- `cpp -> python`

Current collection priority:
- First stabilize `py2 -> py3` (`version_migration`)
- Then extend the same pipeline to `cpp -> python` (`cross_language_migration`)

The project is organized around a single main script:
- `需求文档/download_repo.py`

Supported stages:
- `collect`: search GitHub PRs and save raw candidate results
- `enrich`: fetch PR metadata, apply automatic filters, and save `r0` / `rn` snapshots
- `export-review`: export candidate instances to CSV for manual review
- `apply-review`: convert reviewed CSV results into processed candidate files
- `package`: generate stats and final dataset files

Directory overview:
- `configs/`: query groups, review schema, and collection limits
- `data/raw/`: raw search results, PR metadata, and repository snapshots
- `data/review/`: manual review CSV files
- `data/processed/`: processed candidates and final packaged dataset
- `data/stats/`: json stats plus subtype progress boards
- `logs/`: stage logs
- `需求文档/`: source PPT and the main collection script
- `语言变化迁移样本标注规范_v1.md`: annotation guideline for the language-migration scenario
- `项目进度看板.md`: top-level visual dashboard generated after each stage run

Example commands:

```powershell
python "需求文档/download_repo.py" --stage collect --subtype py2_py3
python "需求文档/download_repo.py" --stage enrich --subtype py2_py3
python "需求文档/download_repo.py" --stage export-review --subtype py2_py3
python "需求文档/download_repo.py" --stage apply-review --subtype py2_py3 --review-file data/review/py2_py3_manual_review.csv
python "需求文档/download_repo.py" --stage package --subtype py2_py3
```

Ad hoc query mode:

```powershell
python "需求文档/download_repo.py" --stage collect --subtype py2_py3 --query "is:pr is:merged language:Python (\"python 3\" OR py3)"
```

Notes:
- GitHub authentication can come from `需求文档/Tokens.txt` or `GITHUB_PAT_TOKEN`
- Review labels should use `positive`, `negative`, or `uncertain`
- Review CSV now includes taxonomy and benchmark-readiness fields such as `migration_type`, `reproducible`, `issue_rewrite_ready`, and `leakage_risk`
- Generated runtime files are kept under `data/` and `logs/`
