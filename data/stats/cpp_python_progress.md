# cpp_python 进度看板

- 更新时间: `2026-04-11 22:45:06`
- 触发节点: `package`

## 阶段状态

| 节点 | 状态 | 说明 |
| --- | --- | --- |
| `collect` | `done` | unique=10 |
| `enrich` | `done` | records=5/5 |
| `export-review` | `done` | rows=0 |
| `apply-review` | `pending` | processed=0 |
| `package` | `done` | stats=yes |

## 数量概览

- Collect 候选: 5/10 [##########..........] 50%
- Enrich 完成: 5/5 [####################] 100%
- Enrich 候选: 0/5 [....................] 0%
- 人工已标注: 0/0 [....................] 0%
- Processed 保留: 0/0 [....................] 0%

## 中间产物

- Collect 索引: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\raw\pr_metadata\cpp_python\collect_index.jsonl`
- Enrich 索引: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\raw\pr_metadata\cpp_python\enriched_index.jsonl`
- Review CSV: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\review\cpp_python_manual_review.csv`
- Processed JSONL: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\processed\cpp_python_candidates.jsonl`
- Stats JSON: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\stats\cpp_python_stats.json`

## 当前阻塞

- `cpp_python__arendst__Tasmota__pr24599`: git clone failed: Cloning into 'C:\Users\86136\AppData\Local\Temp\porta_bench_umd8fnu9\repo'... fatal: unable to access 'https://github.com/arendst/Tasmota.git/': Failed to connect to github.com port 443 after 21123 ms: Could not connect to server
- `cpp_python__hdtv-tool__hdtv__pr52`: git clone failed: Cloning into 'C:\Users\86136\AppData\Local\Temp\porta_bench_cx9h86a6\repo'... fatal: unable to access 'https://github.com/hdtv-tool/hdtv.git/': Failed to connect to github.com port 443 after 21125 ms: Could not connect to server
- `cpp_python__openvdb__fvdb-core__pr595`: git clone failed: Cloning into 'C:\Users\86136\AppData\Local\Temp\porta_bench_knauahyt\repo'... fatal: unable to access 'https://github.com/openvdb/fvdb-core.git/': Failed to connect to github.com port 443 after 21076 ms: Could not connect to server
- `cpp_python__pespila__max-min-hill-climbing-algorithm__pr2`: git clone failed: Cloning into 'C:\Users\86136\AppData\Local\Temp\porta_bench_cfguxz4m\repo'... fatal: unable to access 'https://github.com/pespila/max-min-hill-climbing-algorithm.git/': Failed to connect to github.com port 443 after 21097 ms: Could not connect to server
- `cpp_python__taco-project__FlexKV__pr127`: git clone failed: Cloning into 'C:\Users\86136\AppData\Local\Temp\porta_bench_om63a949\repo'... fatal: unable to access 'https://github.com/taco-project/FlexKV.git/': Failed to connect to github.com port 443 after 21060 ms: Could not connect to server

## 统计快照

- raw_pr_count: `100`
- unique_pr_count: `10`
- collect_candidate_count: `5`
- auto_filtered_candidate_count: `0`
- auto_excluded_count: `0`
- enrich_error_count: `5`
- manual_positive_count: `0`
- manual_negative_count: `0`
- manual_uncertain_count: `0`
- processed_candidate_count: `0`
