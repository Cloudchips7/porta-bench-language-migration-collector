# python_java 进度看板

- 更新时间: `2026-04-18 15:28:32`
- 触发节点: `package`

## 阶段状态

| 节点 | 状态 | 说明 |
| --- | --- | --- |
| `collect` | `done` | unique=723 |
| `enrich` | `done` | records=150/150 |
| `export-review` | `done` | rows=32 |
| `apply-review` | `pending` | processed=0 |
| `package` | `done` | stats=yes |

## 数量概览

- Collect 候选: 150/723 [####................] 21%
- Enrich 完成: 150/150 [####################] 100%
- Enrich 候选: 32/150 [####................] 21%
- 人工已标注: 0/32 [....................] 0%
- Processed 保留: 0/32 [....................] 0%

## 中间产物

- Collect 索引: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\raw\pr_metadata\python_java\collect_index.jsonl`
- Enrich 索引: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\raw\pr_metadata\python_java\enriched_index.jsonl`
- Review CSV: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\review\python_java_manual_review.csv`
- Processed JSONL: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\processed\python_java_candidates.jsonl`
- Stats JSON: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\stats\python_java_stats.json`

## 当前阻塞

- 暂无已记录的 enrich 错误。

## 统计快照

- raw_pr_count: `800`
- unique_pr_count: `723`
- collect_candidate_count: `150`
- auto_filtered_candidate_count: `32`
- auto_excluded_count: `118`
- enrich_error_count: `0`
- manual_positive_count: `0`
- manual_negative_count: `0`
- manual_uncertain_count: `0`
- processed_candidate_count: `0`
