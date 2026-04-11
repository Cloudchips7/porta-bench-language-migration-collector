# cpp_python 进度看板

- 更新时间: `2026-04-12 01:27:32`
- 触发节点: `package`

## 阶段状态

| 节点 | 状态 | 说明 |
| --- | --- | --- |
| `collect` | `done` | unique=24 |
| `enrich` | `done` | records=8/8 |
| `export-review` | `done` | rows=6 |
| `apply-review` | `pending` | processed=0 |
| `package` | `done` | stats=yes |

## 数量概览

- Collect 候选: 8/24 [#######.............] 33%
- Enrich 完成: 8/8 [####################] 100%
- Enrich 候选: 6/8 [###############.....] 75%
- 人工已标注: 0/6 [....................] 0%
- Processed 保留: 0/6 [....................] 0%

## 中间产物

- Collect 索引: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\raw\pr_metadata\cpp_python\collect_index.jsonl`
- Enrich 索引: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\raw\pr_metadata\cpp_python\enriched_index.jsonl`
- Review CSV: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\review\cpp_python_manual_review.csv`
- Processed JSONL: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\processed\cpp_python_candidates.jsonl`
- Stats JSON: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\stats\cpp_python_stats.json`

## 当前阻塞

- 暂无已记录的 enrich 错误。

## 统计快照

- raw_pr_count: `200`
- unique_pr_count: `24`
- collect_candidate_count: `8`
- auto_filtered_candidate_count: `6`
- auto_excluded_count: `2`
- enrich_error_count: `0`
- manual_positive_count: `0`
- manual_negative_count: `0`
- manual_uncertain_count: `0`
- processed_candidate_count: `0`
