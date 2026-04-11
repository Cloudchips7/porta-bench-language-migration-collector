# py2_py3 进度看板

- 更新时间: `2026-04-11 22:45:06`
- 触发节点: `package`

## 阶段状态

| 节点 | 状态 | 说明 |
| --- | --- | --- |
| `collect` | `done` | unique=70 |
| `enrich` | `done` | records=5/5 |
| `export-review` | `done` | rows=0 |
| `apply-review` | `pending` | processed=0 |
| `package` | `done` | stats=yes |

## 数量概览

- Collect 候选: 5/70 [#...................] 7%
- Enrich 完成: 5/5 [####################] 100%
- Enrich 候选: 0/5 [....................] 0%
- 人工已标注: 0/0 [....................] 0%
- Processed 保留: 0/0 [....................] 0%

## 中间产物

- Collect 索引: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\raw\pr_metadata\py2_py3\collect_index.jsonl`
- Enrich 索引: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\raw\pr_metadata\py2_py3\enriched_index.jsonl`
- Review CSV: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\review\py2_py3_manual_review.csv`
- Processed JSONL: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\processed\py2_py3_candidates.jsonl`
- Stats JSON: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\stats\py2_py3_stats.json`

## 当前阻塞

- `py2_py3__BU-Neuromics__terminal_quest__pr2`: git clone failed: Cloning into 'C:\Users\86136\AppData\Local\Temp\porta_bench_jn0gb3fc\repo'... fatal: unable to access 'https://github.com/BU-Neuromics/terminal_quest.git/': Failed to connect to github.com port 443 after 21079 ms: Could not connect to server
- `py2_py3__arild__csp-presentation__pr2`: git clone failed: Cloning into 'C:\Users\86136\AppData\Local\Temp\porta_bench_pfnjhkc5\repo'... fatal: unable to access 'https://github.com/arild/csp-presentation.git/': Failed to connect to github.com port 443 after 21083 ms: Could not connect to server
- `py2_py3__lijunzh__SeisCM__pr2`: git clone failed: Cloning into 'C:\Users\86136\AppData\Local\Temp\porta_bench_49n1y8z9\repo'... fatal: unable to access 'https://github.com/lijunzh/SeisCM.git/': Failed to connect to github.com port 443 after 21095 ms: Could not connect to server
- `py2_py3__mwyau__PyStormTracker__pr2`: git clone failed: Cloning into 'C:\Users\86136\AppData\Local\Temp\porta_bench_5k5gmxyc\repo'... fatal: unable to access 'https://github.com/mwyau/PyStormTracker.git/': Failed to connect to github.com port 443 after 21073 ms: Could not connect to server

## 统计快照

- raw_pr_count: `100`
- unique_pr_count: `70`
- collect_candidate_count: `5`
- auto_filtered_candidate_count: `0`
- auto_excluded_count: `1`
- enrich_error_count: `4`
- manual_positive_count: `0`
- manual_negative_count: `0`
- manual_uncertain_count: `0`
- processed_candidate_count: `0`
