# python_cpp 进度看板

- 更新时间: `2026-04-18 15:04:05`
- 触发节点: `package`

## 阶段状态

| 节点 | 状态 | 说明 |
| --- | --- | --- |
| `collect` | `done` | unique=696 |
| `enrich` | `done` | records=150/150 |
| `export-review` | `done` | rows=29 |
| `apply-review` | `pending` | processed=0 |
| `package` | `done` | stats=yes |

## 数量概览

- Collect 候选: 150/696 [####................] 22%
- Enrich 完成: 150/150 [####################] 100%
- Enrich 候选: 29/150 [####................] 19%
- 人工已标注: 0/29 [....................] 0%
- Processed 保留: 0/29 [....................] 0%

## 中间产物

- Collect 索引: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\raw\pr_metadata\python_cpp\collect_index.jsonl`
- Enrich 索引: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\raw\pr_metadata\python_cpp\enriched_index.jsonl`
- Review CSV: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\review\python_cpp_manual_review.csv`
- Processed JSONL: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\processed\python_cpp_candidates.jsonl`
- Stats JSON: `D:\thecourceofdasi\TeacherWangWork\SWEbench（zzc）\data\stats\python_cpp_stats.json`

## 当前阻塞

- `python_cpp__texus__TGUI__pr351`: git clone failed: Cloning into 'D:\thecourceofdasi\TeacherWangWork\SWEbench锛坺zc锛塡tmp\porta_bench_9chcj32h\repo'... fatal: unable to access 'https://github.com/texus/TGUI.git/': schannel: failed to receive handshake, SSL/TLS connection failed

## 统计快照

- raw_pr_count: `800`
- unique_pr_count: `696`
- collect_candidate_count: `150`
- auto_filtered_candidate_count: `29`
- auto_excluded_count: `120`
- enrich_error_count: `1`
- manual_positive_count: `0`
- manual_negative_count: `0`
- manual_uncertain_count: `0`
- processed_candidate_count: `0`
