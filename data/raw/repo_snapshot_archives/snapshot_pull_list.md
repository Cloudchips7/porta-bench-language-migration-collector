# Repo Snapshot Pull List

## Recommended: rebuild snapshots from GitHub, no manual zip transfer

For large batches, do not send `data/raw/repo_snapshots` as a zip file.
After pulling this repository, a teammate can rebuild the same local snapshot
directories from the original GitHub repositories with:

```powershell
powershell -ExecutionPolicy Bypass -File data/raw/repo_snapshot_archives/pull_snapshots_from_github.ps1 -All
```

Restore only one subtype:

```powershell
powershell -ExecutionPolicy Bypass -File data/raw/repo_snapshot_archives/pull_snapshots_from_github.ps1 -Subtype py2_py3
```

Restore only one sample:

```powershell
powershell -ExecutionPolicy Bypass -File data/raw/repo_snapshot_archives/pull_snapshots_from_github.ps1 -InstanceId py2_py3__Ananay28425__Sequence-LLM__pr3
```

The script reads `snapshot_clone_list.json`, clones the original GitHub repo,
checks out `base_sha` into `r0`, and checks out `final_sha` into `rn`.
Progress is logged to `logs/pull_snapshots_from_github.log`.


这个目录专门存放可提交到 GitHub 的快照归档，以及让队友一键恢复的脚本。

- 更新时间: `2026-04-21T20:00:42`
- 快照总数: `399`

## 一键恢复

拉取仓库更新后，在项目根目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File data/raw/repo_snapshot_archives/pull_and_restore_snapshot_archives.ps1 -All
```

如果只恢复某一种 subtype：

```powershell
powershell -ExecutionPolicy Bypass -File data/raw/repo_snapshot_archives/pull_and_restore_snapshot_archives.ps1 -Subtype py2_py3
```

如果只恢复一个具体样本：

```powershell
powershell -ExecutionPolicy Bypass -File data/raw/repo_snapshot_archives/pull_and_restore_snapshot_archives.ps1 -InstanceId py2_py3__example__repo__pr1
```

## 当前可拉取快照

| instance_id | subtype | repo | pr | archive parts | manifest |
| --- | --- | --- | --- | --- | --- |
| `cpp_python__AMD-AGI__Primus-Turbo__pr276` | `cpp_python` | `AMD-AGI/Primus-Turbo` | `276` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__AMD-AGI__Primus-Turbo__pr276/manifest.json` |
| `cpp_python__AcePeak__naturo__pr186` | `cpp_python` | `AcePeak/naturo` | `186` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__AcePeak__naturo__pr186/manifest.json` |
| `cpp_python__Azure__azure-dev__pr7652` | `cpp_python` | `Azure/azure-dev` | `7652` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__Azure__azure-dev__pr7652/manifest.json` |
| `cpp_python__BirolLab__btllib__pr145` | `cpp_python` | `BirolLab/btllib` | `145` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__BirolLab__btllib__pr145/manifest.json` |
| `cpp_python__CERT-Polska__mwdb-core__pr1151` | `cpp_python` | `CERT-Polska/mwdb-core` | `1151` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__CERT-Polska__mwdb-core__pr1151/manifest.json` |
| `cpp_python__EGA-archive__crypt4gh__pr53` | `cpp_python` | `EGA-archive/crypt4gh` | `53` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__EGA-archive__crypt4gh__pr53/manifest.json` |
| `cpp_python__InsightSoftwareConsortium__ITK__pr6022` | `cpp_python` | `InsightSoftwareConsortium/ITK` | `6022` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__InsightSoftwareConsortium__ITK__pr6022/manifest.json` |
| `cpp_python__InsightSoftwareConsortium__ITK__pr6029` | `cpp_python` | `InsightSoftwareConsortium/ITK` | `6029` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__InsightSoftwareConsortium__ITK__pr6029/manifest.json` |
| `cpp_python__NanoComp__meep__pr3190` | `cpp_python` | `NanoComp/meep` | `3190` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__NanoComp__meep__pr3190/manifest.json` |
| `cpp_python__NatLabRockies__openstudio-mcp__pr46` | `cpp_python` | `NatLabRockies/openstudio-mcp` | `46` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__NatLabRockies__openstudio-mcp__pr46/manifest.json` |
| `cpp_python__NatLabRockies__openstudio-mcp__pr49` | `cpp_python` | `NatLabRockies/openstudio-mcp` | `49` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__NatLabRockies__openstudio-mcp__pr49/manifest.json` |
| `cpp_python__Nisoku__Saikuro__pr2` | `cpp_python` | `Nisoku/Saikuro` | `2` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__Nisoku__Saikuro__pr2/manifest.json` |
| `cpp_python__Open-CMSIS-Pack__devtools__pr2420` | `cpp_python` | `Open-CMSIS-Pack/devtools` | `2420` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__Open-CMSIS-Pack__devtools__pr2420/manifest.json` |
| `cpp_python__PlainsightAI__openfilter__pr75` | `cpp_python` | `PlainsightAI/openfilter` | `75` | `2` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__PlainsightAI__openfilter__pr75/manifest.json` |
| `cpp_python__Project-N-E-K-O__N.E.K.O__pr656` | `cpp_python` | `Project-N-E-K-O/N.E.K.O` | `656` | `3` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__Project-N-E-K-O__N.E.K.O__pr656/manifest.json` |
| `cpp_python__ROCm__aiter__pr2255` | `cpp_python` | `ROCm/aiter` | `2255` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__ROCm__aiter__pr2255/manifest.json` |
| `cpp_python__ROCm__aiter__pr2341` | `cpp_python` | `ROCm/aiter` | `2341` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__ROCm__aiter__pr2341/manifest.json` |
| `cpp_python__ROCm__aiter__pr2395` | `cpp_python` | `ROCm/aiter` | `2395` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__ROCm__aiter__pr2395/manifest.json` |
| `cpp_python__ROCm__aiter__pr2425` | `cpp_python` | `ROCm/aiter` | `2425` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__ROCm__aiter__pr2425/manifest.json` |
| `cpp_python__ROCm__aiter__pr2486` | `cpp_python` | `ROCm/aiter` | `2486` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__ROCm__aiter__pr2486/manifest.json` |
| `cpp_python__ROCm__aiter__pr2498` | `cpp_python` | `ROCm/aiter` | `2498` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__ROCm__aiter__pr2498/manifest.json` |
| `cpp_python__ROCm__aiter__pr2603` | `cpp_python` | `ROCm/aiter` | `2603` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__ROCm__aiter__pr2603/manifest.json` |
| `cpp_python__RustPython__RustPython__pr7368` | `cpp_python` | `RustPython/RustPython` | `7368` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__RustPython__RustPython__pr7368/manifest.json` |
| `cpp_python__SpM-lab__sparse-ir-rs__pr213` | `cpp_python` | `SpM-lab/sparse-ir-rs` | `213` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__SpM-lab__sparse-ir-rs__pr213/manifest.json` |
| `cpp_python__anagrambuild__swig-ts__pr118` | `cpp_python` | `anagrambuild/swig-ts` | `118` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__anagrambuild__swig-ts__pr118/manifest.json` |
| `cpp_python__anagrambuild__swig-ts__pr120` | `cpp_python` | `anagrambuild/swig-ts` | `120` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__anagrambuild__swig-ts__pr120/manifest.json` |
| `cpp_python__anagrambuild__swig-ts__pr123` | `cpp_python` | `anagrambuild/swig-ts` | `123` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__anagrambuild__swig-ts__pr123/manifest.json` |
| `cpp_python__anagrambuild__swig-ts__pr124` | `cpp_python` | `anagrambuild/swig-ts` | `124` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__anagrambuild__swig-ts__pr124/manifest.json` |
| `cpp_python__anagrambuild__swig-ts__pr126` | `cpp_python` | `anagrambuild/swig-ts` | `126` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__anagrambuild__swig-ts__pr126/manifest.json` |
| `cpp_python__anagrambuild__swig-ts__pr128` | `cpp_python` | `anagrambuild/swig-ts` | `128` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__anagrambuild__swig-ts__pr128/manifest.json` |
| `cpp_python__anagrambuild__swig-ts__pr129` | `cpp_python` | `anagrambuild/swig-ts` | `129` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__anagrambuild__swig-ts__pr129/manifest.json` |
| `cpp_python__anagrambuild__swig-ts__pr130` | `cpp_python` | `anagrambuild/swig-ts` | `130` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__anagrambuild__swig-ts__pr130/manifest.json` |
| `cpp_python__anagrambuild__swig-ts__pr131` | `cpp_python` | `anagrambuild/swig-ts` | `131` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__anagrambuild__swig-ts__pr131/manifest.json` |
| `cpp_python__anagrambuild__swig-ts__pr132` | `cpp_python` | `anagrambuild/swig-ts` | `132` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__anagrambuild__swig-ts__pr132/manifest.json` |
| `cpp_python__apache__tsfile__pr767` | `cpp_python` | `apache/tsfile` | `767` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__apache__tsfile__pr767/manifest.json` |
| `cpp_python__bayesianbandits__bayesianbandits__pr216` | `cpp_python` | `bayesianbandits/bayesianbandits` | `216` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__bayesianbandits__bayesianbandits__pr216/manifest.json` |
| `cpp_python__bazelbuild__bazel-central-registry__pr7732` | `cpp_python` | `bazelbuild/bazel-central-registry` | `7732` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__bazelbuild__bazel-central-registry__pr7732/manifest.json` |
| `cpp_python__chezou__Mykytea-python__pr35` | `cpp_python` | `chezou/Mykytea-python` | `35` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__chezou__Mykytea-python__pr35/manifest.json` |
| `cpp_python__chezou__Mykytea-python__pr36` | `cpp_python` | `chezou/Mykytea-python` | `36` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__chezou__Mykytea-python__pr36/manifest.json` |
| `cpp_python__chezou__Mykytea-python__pr37` | `cpp_python` | `chezou/Mykytea-python` | `37` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__chezou__Mykytea-python__pr37/manifest.json` |
| `cpp_python__chezou__Mykytea-python__pr38` | `cpp_python` | `chezou/Mykytea-python` | `38` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__chezou__Mykytea-python__pr38/manifest.json` |
| `cpp_python__chromebrew__chromebrew__pr15088` | `cpp_python` | `chromebrew/chromebrew` | `15088` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__chromebrew__chromebrew__pr15088/manifest.json` |
| `cpp_python__clearlydefined__curated-data__pr32363` | `cpp_python` | `clearlydefined/curated-data` | `32363` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__clearlydefined__curated-data__pr32363/manifest.json` |
| `cpp_python__corazawaf__libcoraza__pr53` | `cpp_python` | `corazawaf/libcoraza` | `53` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__corazawaf__libcoraza__pr53/manifest.json` |
| `cpp_python__corazawaf__libcoraza__pr81` | `cpp_python` | `corazawaf/libcoraza` | `81` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__corazawaf__libcoraza__pr81/manifest.json` |
| `cpp_python__corazawaf__libcoraza__pr89` | `cpp_python` | `corazawaf/libcoraza` | `89` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__corazawaf__libcoraza__pr89/manifest.json` |
| `cpp_python__cpinitiative__usaco-guide__pr6124` | `cpp_python` | `cpinitiative/usaco-guide` | `6124` | `3` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__cpinitiative__usaco-guide__pr6124/manifest.json` |
| `cpp_python__dotflow-io__dotflow__pr226` | `cpp_python` | `dotflow-io/dotflow` | `226` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__dotflow-io__dotflow__pr226/manifest.json` |
| `cpp_python__emscripten-forge__recipes__pr5371` | `cpp_python` | `emscripten-forge/recipes` | `5371` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__emscripten-forge__recipes__pr5371/manifest.json` |
| `cpp_python__esa__pykep__pr184` | `cpp_python` | `esa/pykep` | `184` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__esa__pykep__pr184/manifest.json` |
| `cpp_python__ffalcinelli__pydivert__pr78` | `cpp_python` | `ffalcinelli/pydivert` | `78` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__ffalcinelli__pydivert__pr78/manifest.json` |
| `cpp_python__firebase__firebase-unity-sdk__pr1420` | `cpp_python` | `firebase/firebase-unity-sdk` | `1420` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__firebase__firebase-unity-sdk__pr1420/manifest.json` |
| `cpp_python__flwrlabs__flower__pr7003` | `cpp_python` | `flwrlabs/flower` | `7003` | `2` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__flwrlabs__flower__pr7003/manifest.json` |
| `cpp_python__fsspec__gcsfs__pr795` | `cpp_python` | `fsspec/gcsfs` | `795` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__fsspec__gcsfs__pr795/manifest.json` |
| `cpp_python__getditto__quickstart__pr250` | `cpp_python` | `getditto/quickstart` | `250` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__getditto__quickstart__pr250/manifest.json` |
| `cpp_python__gobbleyourdong__tsunami__pr6` | `cpp_python` | `gobbleyourdong/tsunami` | `6` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__gobbleyourdong__tsunami__pr6/manifest.json` |
| `cpp_python__google__crubit__pr693` | `cpp_python` | `google/crubit` | `693` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__google__crubit__pr693/manifest.json` |
| `cpp_python__gyrovorbis__sh4zam__pr53` | `cpp_python` | `gyrovorbis/sh4zam` | `53` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__gyrovorbis__sh4zam__pr53/manifest.json` |
| `cpp_python__home-assistant__buildroot__pr122` | `cpp_python` | `home-assistant/buildroot` | `122` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__home-assistant__buildroot__pr122/manifest.json` |
| `cpp_python__huawei-csl__pto-kernels__pr97` | `cpp_python` | `huawei-csl/pto-kernels` | `97` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__huawei-csl__pto-kernels__pr97/manifest.json` |
| `cpp_python__hw-native-sys__simpler__pr387` | `cpp_python` | `hw-native-sys/simpler` | `387` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__hw-native-sys__simpler__pr387/manifest.json` |
| `cpp_python__hw-native-sys__simpler__pr416` | `cpp_python` | `hw-native-sys/simpler` | `416` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__hw-native-sys__simpler__pr416/manifest.json` |
| `cpp_python__hw-native-sys__simpler__pr511` | `cpp_python` | `hw-native-sys/simpler` | `511` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__hw-native-sys__simpler__pr511/manifest.json` |
| `cpp_python__iflytek__astron-rpa__pr726` | `cpp_python` | `iflytek/astron-rpa` | `726` | `2` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__iflytek__astron-rpa__pr726/manifest.json` |
| `cpp_python__intercepted16__fibrumpdf__pr15` | `cpp_python` | `intercepted16/fibrumpdf` | `15` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__intercepted16__fibrumpdf__pr15/manifest.json` |
| `cpp_python__isair__jarvis__pr188` | `cpp_python` | `isair/jarvis` | `188` | `1` | `data/raw/repo_snapshot_archives/cpp_python/cpp_python__isair__jarvis__pr188/manifest.json` |
| `java_python__CXwudi__youcal__pr43` | `java_python` | `CXwudi/youcal` | `43` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__CXwudi__youcal__pr43/manifest.json` |
| `java_python__CXwudi__youcal__pr49` | `java_python` | `CXwudi/youcal` | `49` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__CXwudi__youcal__pr49/manifest.json` |
| `java_python__FacturAPI__facturapi-docs__pr246` | `java_python` | `FacturAPI/facturapi-docs` | `246` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__FacturAPI__facturapi-docs__pr246/manifest.json` |
| `java_python__HKUDS__CLI-Anything__pr170` | `java_python` | `HKUDS/CLI-Anything` | `170` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__HKUDS__CLI-Anything__pr170/manifest.json` |
| `java_python__MCDxAI__minecraft-dev-mcp__pr6` | `java_python` | `MCDxAI/minecraft-dev-mcp` | `6` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__MCDxAI__minecraft-dev-mcp__pr6/manifest.json` |
| `java_python__PortSwigger__pycript__pr5` | `java_python` | `PortSwigger/pycript` | `5` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__PortSwigger__pycript__pr5/manifest.json` |
| `java_python__RobotLocomotion__drake-ci__pr420` | `java_python` | `RobotLocomotion/drake-ci` | `420` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__RobotLocomotion__drake-ci__pr420/manifest.json` |
| `java_python__TheRenegadeCoder__sample-programs__pr5498` | `java_python` | `TheRenegadeCoder/sample-programs` | `5498` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__TheRenegadeCoder__sample-programs__pr5498/manifest.json` |
| `java_python__TruvetaPublic__OpenLinkToken__pr187` | `java_python` | `TruvetaPublic/OpenLinkToken` | `187` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__TruvetaPublic__OpenLinkToken__pr187/manifest.json` |
| `java_python__TruvetaPublic__OpenLinkToken__pr267` | `java_python` | `TruvetaPublic/OpenLinkToken` | `267` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__TruvetaPublic__OpenLinkToken__pr267/manifest.json` |
| `java_python__Wafler1__transportia__pr14` | `java_python` | `Wafler1/transportia` | `14` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__Wafler1__transportia__pr14/manifest.json` |
| `java_python__amzn__selling-partner-api-sdk__pr722` | `java_python` | `amzn/selling-partner-api-sdk` | `722` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__amzn__selling-partner-api-sdk__pr722/manifest.json` |
| `java_python__antgroup__YASA-Engine__pr81` | `java_python` | `antgroup/YASA-Engine` | `81` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__antgroup__YASA-Engine__pr81/manifest.json` |
| `java_python__apache__fory__pr3537` | `java_python` | `apache/fory` | `3537` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__apache__fory__pr3537/manifest.json` |
| `java_python__asyncapi__generator__pr1767` | `java_python` | `asyncapi/generator` | `1767` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__asyncapi__generator__pr1767/manifest.json` |
| `java_python__aws__aws-durable-execution-docs__pr115` | `java_python` | `aws/aws-durable-execution-docs` | `115` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__aws__aws-durable-execution-docs__pr115/manifest.json` |
| `java_python__aws__aws-durable-execution-docs__pr118` | `java_python` | `aws/aws-durable-execution-docs` | `118` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__aws__aws-durable-execution-docs__pr118/manifest.json` |
| `java_python__aws__aws-durable-execution-docs__pr121` | `java_python` | `aws/aws-durable-execution-docs` | `121` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__aws__aws-durable-execution-docs__pr121/manifest.json` |
| `java_python__aws__aws-durable-execution-docs__pr123` | `java_python` | `aws/aws-durable-execution-docs` | `123` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__aws__aws-durable-execution-docs__pr123/manifest.json` |
| `java_python__b-long__opentdf-python-sdk__pr62` | `java_python` | `b-long/opentdf-python-sdk` | `62` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__b-long__opentdf-python-sdk__pr62/manifest.json` |
| `java_python__bazelbuild__bazel-central-registry__pr6173` | `java_python` | `bazelbuild/bazel-central-registry` | `6173` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__bazelbuild__bazel-central-registry__pr6173/manifest.json` |
| `java_python__chainguard-dev__edu__pr3186` | `java_python` | `chainguard-dev/edu` | `3186` | `2` | `data/raw/repo_snapshot_archives/java_python/java_python__chainguard-dev__edu__pr3186/manifest.json` |
| `java_python__cloudfoundry__php-buildpack__pr1228` | `java_python` | `cloudfoundry/php-buildpack` | `1228` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__cloudfoundry__php-buildpack__pr1228/manifest.json` |
| `java_python__daytonaio__daytona__pr4320` | `java_python` | `daytonaio/daytona` | `4320` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__daytonaio__daytona__pr4320/manifest.json` |
| `java_python__deepfates__cantrip__pr15` | `java_python` | `deepfates/cantrip` | `15` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__deepfates__cantrip__pr15/manifest.json` |
| `java_python__dhyansraj__mcp-mesh__pr586` | `java_python` | `dhyansraj/mcp-mesh` | `586` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__dhyansraj__mcp-mesh__pr586/manifest.json` |
| `java_python__eclipse-ee4j__openmq__pr3017` | `java_python` | `eclipse-ee4j/openmq` | `3017` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__eclipse-ee4j__openmq__pr3017/manifest.json` |
| `java_python__eclipse-lyo__lyo.testsuite__pr235` | `java_python` | `eclipse-lyo/lyo.testsuite` | `235` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__eclipse-lyo__lyo.testsuite__pr235/manifest.json` |
| `java_python__elastic__esql-idea-plugin__pr31` | `java_python` | `elastic/esql-idea-plugin` | `31` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__elastic__esql-idea-plugin__pr31/manifest.json` |
| `java_python__github__awesome-copilot__pr1314` | `java_python` | `github/awesome-copilot` | `1314` | `2` | `data/raw/repo_snapshot_archives/java_python/java_python__github__awesome-copilot__pr1314/manifest.json` |
| `java_python__globalreachtech__tinyradius-netty__pr501` | `java_python` | `globalreachtech/tinyradius-netty` | `501` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__globalreachtech__tinyradius-netty__pr501/manifest.json` |
| `java_python__google__A2UI__pr1015` | `java_python` | `google/A2UI` | `1015` | `3` | `data/raw/repo_snapshot_archives/java_python/java_python__google__A2UI__pr1015/manifest.json` |
| `java_python__googleapis__librarian__pr5205` | `java_python` | `googleapis/librarian` | `5205` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__googleapis__librarian__pr5205/manifest.json` |
| `java_python__gradle__docker-gradle__pr382` | `java_python` | `gradle/docker-gradle` | `382` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__gradle__docker-gradle__pr382/manifest.json` |
| `java_python__imnotnoahhh__vex__pr46` | `java_python` | `imnotnoahhh/vex` | `46` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__imnotnoahhh__vex__pr46/manifest.json` |
| `java_python__inference-sim__inference-sim__pr727` | `java_python` | `inference-sim/inference-sim` | `727` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__inference-sim__inference-sim__pr727/manifest.json` |
| `java_python__jenkinsci__mail-watcher-plugin__pr203` | `java_python` | `jenkinsci/mail-watcher-plugin` | `203` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__jenkinsci__mail-watcher-plugin__pr203/manifest.json` |
| `java_python__local-web-services__local-web-services__pr41` | `java_python` | `local-web-services/local-web-services` | `41` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__local-web-services__local-web-services__pr41/manifest.json` |
| `java_python__logicalclocks__hopsworks-api__pr770` | `java_python` | `logicalclocks/hopsworks-api` | `770` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__logicalclocks__hopsworks-api__pr770/manifest.json` |
| `java_python__ls1intum__Hephaestus__pr620` | `java_python` | `ls1intum/Hephaestus` | `620` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__ls1intum__Hephaestus__pr620/manifest.json` |
| `java_python__ls1intum__edutelligence__pr176` | `java_python` | `ls1intum/edutelligence` | `176` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__ls1intum__edutelligence__pr176/manifest.json` |
| `java_python__microsoft__onnxruntime-genai__pr1939` | `java_python` | `microsoft/onnxruntime-genai` | `1939` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__microsoft__onnxruntime-genai__pr1939/manifest.json` |
| `java_python__modelcontextprotocol__modelcontextprotocol__pr2465` | `java_python` | `modelcontextprotocol/modelcontextprotocol` | `2465` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__modelcontextprotocol__modelcontextprotocol__pr2465/manifest.json` |
| `java_python__modlix-india__nocode-saas__pr2438` | `java_python` | `modlix-india/nocode-saas` | `2438` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__modlix-india__nocode-saas__pr2438/manifest.json` |
| `java_python__mofa-org__mofa__pr114` | `java_python` | `mofa-org/mofa` | `114` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__mofa-org__mofa__pr114/manifest.json` |
| `java_python__nf-core__mcmicro__pr139` | `java_python` | `nf-core/mcmicro` | `139` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__nf-core__mcmicro__pr139/manifest.json` |
| `java_python__openremote__openremote__pr2681` | `java_python` | `openremote/openremote` | `2681` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__openremote__openremote__pr2681/manifest.json` |
| `java_python__openrewrite__rewrite__pr6677` | `java_python` | `openrewrite/rewrite` | `6677` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__openrewrite__rewrite__pr6677/manifest.json` |
| `java_python__openrewrite__rewrite__pr6886` | `java_python` | `openrewrite/rewrite` | `6886` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__openrewrite__rewrite__pr6886/manifest.json` |
| `java_python__openrewrite__rewrite__pr7274` | `java_python` | `openrewrite/rewrite` | `7274` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__openrewrite__rewrite__pr7274/manifest.json` |
| `java_python__optics-dev__Monocle__pr1578` | `java_python` | `optics-dev/Monocle` | `1578` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__optics-dev__Monocle__pr1578/manifest.json` |
| `java_python__pelican-eggs__yolks__pr356` | `java_python` | `pelican-eggs/yolks` | `356` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__pelican-eggs__yolks__pr356/manifest.json` |
| `java_python__redis__agent-memory-server__pr160` | `java_python` | `redis/agent-memory-server` | `160` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__redis__agent-memory-server__pr160/manifest.json` |
| `java_python__rtuszik__photon-docker__pr96` | `java_python` | `rtuszik/photon-docker` | `96` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__rtuszik__photon-docker__pr96/manifest.json` |
| `java_python__rustyrazorblade__easy-db-lab__pr327` | `java_python` | `rustyrazorblade/easy-db-lab` | `327` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__rustyrazorblade__easy-db-lab__pr327/manifest.json` |
| `java_python__sbt__sbt-eclipse__pr469` | `java_python` | `sbt/sbt-eclipse` | `469` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__sbt__sbt-eclipse__pr469/manifest.json` |
| `java_python__sbt__sbt-rjs__pr126` | `java_python` | `sbt/sbt-rjs` | `126` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__sbt__sbt-rjs__pr126/manifest.json` |
| `java_python__snowflakedb__universal-driver__pr333` | `java_python` | `snowflakedb/universal-driver` | `333` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__snowflakedb__universal-driver__pr333/manifest.json` |
| `java_python__svd-ai-lab__sim-cli__pr16` | `java_python` | `svd-ai-lab/sim-cli` | `16` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__svd-ai-lab__sim-cli__pr16/manifest.json` |
| `java_python__torlando-tech__columba__pr416` | `java_python` | `torlando-tech/columba` | `416` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__torlando-tech__columba__pr416/manifest.json` |
| `java_python__typetools__checker-framework__pr7636` | `java_python` | `typetools/checker-framework` | `7636` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__typetools__checker-framework__pr7636/manifest.json` |
| `java_python__wildfly-extras__wildfly-ai-feature-pack__pr225` | `java_python` | `wildfly-extras/wildfly-ai-feature-pack` | `225` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__wildfly-extras__wildfly-ai-feature-pack__pr225/manifest.json` |
| `java_python__ziqizhang__jate__pr62` | `java_python` | `ziqizhang/jate` | `62` | `1` | `data/raw/repo_snapshot_archives/java_python/java_python__ziqizhang__jate__pr62/manifest.json` |
| `py2_py3__AequilibraE__aequilibrae__pr748` | `py2_py3` | `AequilibraE/aequilibrae` | `748` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__AequilibraE__aequilibrae__pr748/manifest.json` |
| `py2_py3__Ananay28425__Sequence-LLM__pr3` | `py2_py3` | `Ananay28425/Sequence-LLM` | `3` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__Ananay28425__Sequence-LLM__pr3/manifest.json` |
| `py2_py3__ChristopherKahler__carl__pr3` | `py2_py3` | `ChristopherKahler/carl` | `3` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__ChristopherKahler__carl__pr3/manifest.json` |
| `py2_py3__Cloud-CV__EvalAI__pr4872` | `py2_py3` | `Cloud-CV/EvalAI` | `4872` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__Cloud-CV__EvalAI__pr4872/manifest.json` |
| `py2_py3__F-a-b-r-i-z-i-o__Parallel-SA-For-Sudoku-Solving__pr3` | `py2_py3` | `F-a-b-r-i-z-i-o/Parallel-SA-For-Sudoku-Solving` | `3` | `4` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__F-a-b-r-i-z-i-o__Parallel-SA-For-Sudoku-Solving__pr3/manifest.json` |
| `py2_py3__FireRedTeam__FireRedASR2S__pr3` | `py2_py3` | `FireRedTeam/FireRedASR2S` | `3` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__FireRedTeam__FireRedASR2S__pr3/manifest.json` |
| `py2_py3__MarkusNeusinger__anyplot__pr1576` | `py2_py3` | `MarkusNeusinger/anyplot` | `1576` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__MarkusNeusinger__anyplot__pr1576/manifest.json` |
| `py2_py3__MarkusNeusinger__anyplot__pr2416` | `py2_py3` | `MarkusNeusinger/anyplot` | `2416` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__MarkusNeusinger__anyplot__pr2416/manifest.json` |
| `py2_py3__MarkusNeusinger__anyplot__pr3601` | `py2_py3` | `MarkusNeusinger/anyplot` | `3601` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__MarkusNeusinger__anyplot__pr3601/manifest.json` |
| `py2_py3__MarkusNeusinger__anyplot__pr4660` | `py2_py3` | `MarkusNeusinger/anyplot` | `4660` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__MarkusNeusinger__anyplot__pr4660/manifest.json` |
| `py2_py3__MarkusNeusinger__anyplot__pr4712` | `py2_py3` | `MarkusNeusinger/anyplot` | `4712` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__MarkusNeusinger__anyplot__pr4712/manifest.json` |
| `py2_py3__MarkusNeusinger__anyplot__pr4866` | `py2_py3` | `MarkusNeusinger/anyplot` | `4866` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__MarkusNeusinger__anyplot__pr4866/manifest.json` |
| `py2_py3__MarkusNeusinger__anyplot__pr4868` | `py2_py3` | `MarkusNeusinger/anyplot` | `4868` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__MarkusNeusinger__anyplot__pr4868/manifest.json` |
| `py2_py3__MarkusNeusinger__anyplot__pr4911` | `py2_py3` | `MarkusNeusinger/anyplot` | `4911` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__MarkusNeusinger__anyplot__pr4911/manifest.json` |
| `py2_py3__MarkusNeusinger__anyplot__pr4966` | `py2_py3` | `MarkusNeusinger/anyplot` | `4966` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__MarkusNeusinger__anyplot__pr4966/manifest.json` |
| `py2_py3__MarkusNeusinger__anyplot__pr5048` | `py2_py3` | `MarkusNeusinger/anyplot` | `5048` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__MarkusNeusinger__anyplot__pr5048/manifest.json` |
| `py2_py3__NetSPI__OCInferno__pr2` | `py2_py3` | `NetSPI/OCInferno` | `2` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__NetSPI__OCInferno__pr2/manifest.json` |
| `py2_py3__Nextdoor__kingpin__pr651` | `py2_py3` | `Nextdoor/kingpin` | `651` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__Nextdoor__kingpin__pr651/manifest.json` |
| `py2_py3__Scopeo__draftnrun__pr565` | `py2_py3` | `Scopeo/draftnrun` | `565` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__Scopeo__draftnrun__pr565/manifest.json` |
| `py2_py3__ansible-collections__community.proxysql__pr179` | `py2_py3` | `ansible-collections/community.proxysql` | `179` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__ansible-collections__community.proxysql__pr179/manifest.json` |
| `py2_py3__borgbackup__borg__pr9516` | `py2_py3` | `borgbackup/borg` | `9516` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__borgbackup__borg__pr9516/manifest.json` |
| `py2_py3__borgbackup__borg__pr9517` | `py2_py3` | `borgbackup/borg` | `9517` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__borgbackup__borg__pr9517/manifest.json` |
| `py2_py3__brave__release-boss__pr87` | `py2_py3` | `brave/release-boss` | `87` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__brave__release-boss__pr87/manifest.json` |
| `py2_py3__claudevervoort__ltiautotest__pr37` | `py2_py3` | `claudevervoort/ltiautotest` | `37` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__claudevervoort__ltiautotest__pr37/manifest.json` |
| `py2_py3__django-crispy-forms__django-crispy-forms__pr1433` | `py2_py3` | `django-crispy-forms/django-crispy-forms` | `1433` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__django-crispy-forms__django-crispy-forms__pr1433/manifest.json` |
| `py2_py3__enthought__apptools__pr90` | `py2_py3` | `enthought/apptools` | `90` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__enthought__apptools__pr90/manifest.json` |
| `py2_py3__flobz__psa_car_controller__pr1132` | `py2_py3` | `flobz/psa_car_controller` | `1132` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__flobz__psa_car_controller__pr1132/manifest.json` |
| `py2_py3__freedomofpress__securedrop__pr4239` | `py2_py3` | `freedomofpress/securedrop` | `4239` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__freedomofpress__securedrop__pr4239/manifest.json` |
| `py2_py3__genoshide__wallet-mcp__pr2` | `py2_py3` | `genoshide/wallet-mcp` | `2` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__genoshide__wallet-mcp__pr2/manifest.json` |
| `py2_py3__google__timesketch__pr3657` | `py2_py3` | `google/timesketch` | `3657` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__google__timesketch__pr3657/manifest.json` |
| `py2_py3__googleapis__python-bigquery-pandas__pr472` | `py2_py3` | `googleapis/python-bigquery-pandas` | `472` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__googleapis__python-bigquery-pandas__pr472/manifest.json` |
| `py2_py3__googleapis__synthtool__pr1398` | `py2_py3` | `googleapis/synthtool` | `1398` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__googleapis__synthtool__pr1398/manifest.json` |
| `py2_py3__hereon-GEMS__pydidas__pr157` | `py2_py3` | `hereon-GEMS/pydidas` | `157` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__hereon-GEMS__pydidas__pr157/manifest.json` |
| `py2_py3__hozn__coilmq__pr37` | `py2_py3` | `hozn/coilmq` | `37` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__hozn__coilmq__pr37/manifest.json` |
| `py2_py3__internetarchive__openlibrary__pr11739` | `py2_py3` | `internetarchive/openlibrary` | `11739` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__internetarchive__openlibrary__pr11739/manifest.json` |
| `py2_py3__jkitchin__vasp__pr60` | `py2_py3` | `jkitchin/vasp` | `60` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__jkitchin__vasp__pr60/manifest.json` |
| `py2_py3__joedemcher__simplelogin-cli__pr2` | `py2_py3` | `joedemcher/simplelogin-cli` | `2` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__joedemcher__simplelogin-cli__pr2/manifest.json` |
| `py2_py3__jwbron__egg__pr517` | `py2_py3` | `jwbron/egg` | `517` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__jwbron__egg__pr517/manifest.json` |
| `py2_py3__kaifcoder__gemini_multipdf_chat__pr17` | `py2_py3` | `kaifcoder/gemini_multipdf_chat` | `17` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__kaifcoder__gemini_multipdf_chat__pr17/manifest.json` |
| `py2_py3__mattyopon__faultray__pr3` | `py2_py3` | `mattyopon/faultray` | `3` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__mattyopon__faultray__pr3/manifest.json` |
| `py2_py3__metno__pyaerocom__pr1679` | `py2_py3` | `metno/pyaerocom` | `1679` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__metno__pyaerocom__pr1679/manifest.json` |
| `py2_py3__metomi__rose__pr2808` | `py2_py3` | `metomi/rose` | `2808` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__metomi__rose__pr2808/manifest.json` |
| `py2_py3__pydantic__logfire__pr1696` | `py2_py3` | `pydantic/logfire` | `1696` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__pydantic__logfire__pr1696/manifest.json` |
| `py2_py3__pyiron__pyfileindex__pr265` | `py2_py3` | `pyiron/pyfileindex` | `265` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__pyiron__pyfileindex__pr265/manifest.json` |
| `py2_py3__python-trio__trio__pr3030` | `py2_py3` | `python-trio/trio` | `3030` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__python-trio__trio__pr3030/manifest.json` |
| `py2_py3__redis__docs__pr2553` | `py2_py3` | `redis/docs` | `2553` | `3` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__redis__docs__pr2553/manifest.json` |
| `py2_py3__sadhgurutech__mailtrim__pr2` | `py2_py3` | `sadhgurutech/mailtrim` | `2` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__sadhgurutech__mailtrim__pr2/manifest.json` |
| `py2_py3__simplejson__simplejson__pr371` | `py2_py3` | `simplejson/simplejson` | `371` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__simplejson__simplejson__pr371/manifest.json` |
| `py2_py3__unrealandychan__learn-python-with-ai__pr2` | `py2_py3` | `unrealandychan/learn-python-with-ai` | `2` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__unrealandychan__learn-python-with-ai__pr2/manifest.json` |
| `py2_py3__yhavin__yardi-sdk__pr2` | `py2_py3` | `yhavin/yardi-sdk` | `2` | `1` | `data/raw/repo_snapshot_archives/py2_py3/py2_py3__yhavin__yardi-sdk__pr2/manifest.json` |
| `python_cpp__256foundation__asic-rs__pr221` | `python_cpp` | `256foundation/asic-rs` | `221` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__256foundation__asic-rs__pr221/manifest.json` |
| `python_cpp__Ahmeth4n__renef__pr41` | `python_cpp` | `Ahmeth4n/renef` | `41` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__Ahmeth4n__renef__pr41/manifest.json` |
| `python_cpp__Azure__azure-dev__pr7617` | `python_cpp` | `Azure/azure-dev` | `7617` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__Azure__azure-dev__pr7617/manifest.json` |
| `python_cpp__Azure__azure-sdk__pr9818` | `python_cpp` | `Azure/azure-sdk` | `9818` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__Azure__azure-sdk__pr9818/manifest.json` |
| `python_cpp__CasperVM__cursed_controls__pr3` | `python_cpp` | `CasperVM/cursed_controls` | `3` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__CasperVM__cursed_controls__pr3/manifest.json` |
| `python_cpp__CiscoDevNet__ansible-aci__pr838` | `python_cpp` | `CiscoDevNet/ansible-aci` | `838` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__CiscoDevNet__ansible-aci__pr838/manifest.json` |
| `python_cpp__EggerMarc__tools-rs__pr37` | `python_cpp` | `EggerMarc/tools-rs` | `37` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__EggerMarc__tools-rs__pr37/manifest.json` |
| `python_cpp__FLOX-Foundation__flox__pr91` | `python_cpp` | `FLOX-Foundation/flox` | `91` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__FLOX-Foundation__flox__pr91/manifest.json` |
| `python_cpp__HHS__simpler-grants-pdf-builder__pr666` | `python_cpp` | `HHS/simpler-grants-pdf-builder` | `666` | `2` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__HHS__simpler-grants-pdf-builder__pr666/manifest.json` |
| `python_cpp__IBM__ai-atlas-nexus__pr165` | `python_cpp` | `IBM/ai-atlas-nexus` | `165` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__IBM__ai-atlas-nexus__pr165/manifest.json` |
| `python_cpp__IBM__granite-workshop__pr146` | `python_cpp` | `IBM/granite-workshop` | `146` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__IBM__granite-workshop__pr146/manifest.json` |
| `python_cpp__Jij-Inc__Qamomile__pr335` | `python_cpp` | `Jij-Inc/Qamomile` | `335` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__Jij-Inc__Qamomile__pr335/manifest.json` |
| `python_cpp__Marve10s__Better-Fullstack__pr150` | `python_cpp` | `Marve10s/Better-Fullstack` | `150` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__Marve10s__Better-Fullstack__pr150/manifest.json` |
| `python_cpp__OpenModelica__OMSimulator__pr1569` | `python_cpp` | `OpenModelica/OMSimulator` | `1569` | `2` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__OpenModelica__OMSimulator__pr1569/manifest.json` |
| `python_cpp__PhillyBikeAction__bikeaction.org__pr228` | `python_cpp` | `PhillyBikeAction/bikeaction.org` | `228` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__PhillyBikeAction__bikeaction.org__pr228/manifest.json` |
| `python_cpp__Qiskit__ecosystem__pr1076` | `python_cpp` | `Qiskit/ecosystem` | `1076` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__Qiskit__ecosystem__pr1076/manifest.json` |
| `python_cpp__ROCm__aiter__pr2341` | `python_cpp` | `ROCm/aiter` | `2341` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__ROCm__aiter__pr2341/manifest.json` |
| `python_cpp__ROCm__rocm-jax__pr379` | `python_cpp` | `ROCm/rocm-jax` | `379` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__ROCm__rocm-jax__pr379/manifest.json` |
| `python_cpp__Second-Hand-Friends__kleinanzeigen-bot__pr986` | `python_cpp` | `Second-Hand-Friends/kleinanzeigen-bot` | `986` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__Second-Hand-Friends__kleinanzeigen-bot__pr986/manifest.json` |
| `python_cpp__Simple-Robotics__pinocchio__pr32` | `python_cpp` | `Simple-Robotics/pinocchio` | `32` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__Simple-Robotics__pinocchio__pr32/manifest.json` |
| `python_cpp__SleipnirGroup__Choreo__pr1452` | `python_cpp` | `SleipnirGroup/Choreo` | `1452` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__SleipnirGroup__Choreo__pr1452/manifest.json` |
| `python_cpp__SzymonPajzert__koryta__pr469` | `python_cpp` | `SzymonPajzert/koryta` | `469` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__SzymonPajzert__koryta__pr469/manifest.json` |
| `python_cpp__anteriorcore__brrr__pr172` | `python_cpp` | `anteriorcore/brrr` | `172` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__anteriorcore__brrr__pr172/manifest.json` |
| `python_cpp__apache__fory__pr3543` | `python_cpp` | `apache/fory` | `3543` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__apache__fory__pr3543/manifest.json` |
| `python_cpp__arendst__Tasmota__pr24599` | `python_cpp` | `arendst/Tasmota` | `24599` | `2` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__arendst__Tasmota__pr24599/manifest.json` |
| `python_cpp__bennettoxford__openprescribing__pr5500` | `python_cpp` | `bennettoxford/openprescribing` | `5500` | `2` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__bennettoxford__openprescribing__pr5500/manifest.json` |
| `python_cpp__blockcell-labs__blockcell__pr61` | `python_cpp` | `blockcell-labs/blockcell` | `61` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__blockcell-labs__blockcell__pr61/manifest.json` |
| `python_cpp__boltffi__boltffi__pr161` | `python_cpp` | `boltffi/boltffi` | `161` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__boltffi__boltffi__pr161/manifest.json` |
| `python_cpp__cabelo__libzupt__pr3` | `python_cpp` | `cabelo/libzupt` | `3` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__cabelo__libzupt__pr3/manifest.json` |
| `python_cpp__canonical__pgbouncer-k8s-operator__pr725` | `python_cpp` | `canonical/pgbouncer-k8s-operator` | `725` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__canonical__pgbouncer-k8s-operator__pr725/manifest.json` |
| `python_cpp__canonical__pgbouncer-k8s-operator__pr733` | `python_cpp` | `canonical/pgbouncer-k8s-operator` | `733` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__canonical__pgbouncer-k8s-operator__pr733/manifest.json` |
| `python_cpp__canonical__postgresql-k8s-operator__pr1447` | `python_cpp` | `canonical/postgresql-k8s-operator` | `1447` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__canonical__postgresql-k8s-operator__pr1447/manifest.json` |
| `python_cpp__canonical__postgresql-operator__pr1614` | `python_cpp` | `canonical/postgresql-operator` | `1614` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__canonical__postgresql-operator__pr1614/manifest.json` |
| `python_cpp__celery__celery__pr10265` | `python_cpp` | `celery/celery` | `10265` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__celery__celery__pr10265/manifest.json` |
| `python_cpp__cmudig__mosaic__pr18` | `python_cpp` | `cmudig/mosaic` | `18` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__cmudig__mosaic__pr18/manifest.json` |
| `python_cpp__config-i1__smooth__pr358` | `python_cpp` | `config-i1/smooth` | `358` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__config-i1__smooth__pr358/manifest.json` |
| `python_cpp__connectrpc__connect-python__pr210` | `python_cpp` | `connectrpc/connect-python` | `210` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__connectrpc__connect-python__pr210/manifest.json` |
| `python_cpp__cpinitiative__usaco-guide__pr6126` | `python_cpp` | `cpinitiative/usaco-guide` | `6126` | `3` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__cpinitiative__usaco-guide__pr6126/manifest.json` |
| `python_cpp__daisytuner__docc__pr629` | `python_cpp` | `daisytuner/docc` | `629` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__daisytuner__docc__pr629/manifest.json` |
| `python_cpp__dance858__Toeplitz-covariance-estimation__pr7` | `python_cpp` | `dance858/Toeplitz-covariance-estimation` | `7` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__dance858__Toeplitz-covariance-estimation__pr7/manifest.json` |
| `python_cpp__docat-org__docat__pr935` | `python_cpp` | `docat-org/docat` | `935` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__docat-org__docat__pr935/manifest.json` |
| `python_cpp__docker-library__official-images__pr21207` | `python_cpp` | `docker-library/official-images` | `21207` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__docker-library__official-images__pr21207/manifest.json` |
| `python_cpp__dynatrace-oss__dtwiz__pr11` | `python_cpp` | `dynatrace-oss/dtwiz` | `11` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__dynatrace-oss__dtwiz__pr11/manifest.json` |
| `python_cpp__elfmz__far2l__pr3346` | `python_cpp` | `elfmz/far2l` | `3346` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__elfmz__far2l__pr3346/manifest.json` |
| `python_cpp__evangelistalab__forte2__pr155` | `python_cpp` | `evangelistalab/forte2` | `155` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__evangelistalab__forte2__pr155/manifest.json` |
| `python_cpp__firebase__firebase-unity-sdk__pr1400` | `python_cpp` | `firebase/firebase-unity-sdk` | `1400` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__firebase__firebase-unity-sdk__pr1400/manifest.json` |
| `python_cpp__flexera-public__policy_templates__pr4296` | `python_cpp` | `flexera-public/policy_templates` | `4296` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__flexera-public__policy_templates__pr4296/manifest.json` |
| `python_cpp__gastongouron__ironpress__pr113` | `python_cpp` | `gastongouron/ironpress` | `113` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__gastongouron__ironpress__pr113/manifest.json` |
| `python_cpp__google__net_http__pr36` | `python_cpp` | `google/net_http` | `36` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__google__net_http__pr36/manifest.json` |
| `python_cpp__greenbone__python-gvm__pr1315` | `python_cpp` | `greenbone/python-gvm` | `1315` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__greenbone__python-gvm__pr1315/manifest.json` |
| `python_cpp__idaholab__civet__pr644` | `python_cpp` | `idaholab/civet` | `644` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__idaholab__civet__pr644/manifest.json` |
| `python_cpp__jelmer__janitor__pr1167` | `python_cpp` | `jelmer/janitor` | `1167` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__jelmer__janitor__pr1167/manifest.json` |
| `python_cpp__jeremiah-k__meshtastic-matrix-relay__pr515` | `python_cpp` | `jeremiah-k/meshtastic-matrix-relay` | `515` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__jeremiah-k__meshtastic-matrix-relay__pr515/manifest.json` |
| `python_cpp__kdeldycke__click-extra__pr1596` | `python_cpp` | `kdeldycke/click-extra` | `1596` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__click-extra__pr1596/manifest.json` |
| `python_cpp__kdeldycke__click-extra__pr1605` | `python_cpp` | `kdeldycke/click-extra` | `1605` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__click-extra__pr1605/manifest.json` |
| `python_cpp__kdeldycke__click-extra__pr1612` | `python_cpp` | `kdeldycke/click-extra` | `1612` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__click-extra__pr1612/manifest.json` |
| `python_cpp__kdeldycke__meta-package-manager__pr1734` | `python_cpp` | `kdeldycke/meta-package-manager` | `1734` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__meta-package-manager__pr1734/manifest.json` |
| `python_cpp__kdeldycke__meta-package-manager__pr1749` | `python_cpp` | `kdeldycke/meta-package-manager` | `1749` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__meta-package-manager__pr1749/manifest.json` |
| `python_cpp__kdeldycke__repomatic__pr2489` | `python_cpp` | `kdeldycke/repomatic` | `2489` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__repomatic__pr2489/manifest.json` |
| `python_cpp__kdeldycke__repomatic__pr2498` | `python_cpp` | `kdeldycke/repomatic` | `2498` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__repomatic__pr2498/manifest.json` |
| `python_cpp__kdeldycke__repomatic__pr2516` | `python_cpp` | `kdeldycke/repomatic` | `2516` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__repomatic__pr2516/manifest.json` |
| `python_cpp__kdeldycke__repomatic__pr2518` | `python_cpp` | `kdeldycke/repomatic` | `2518` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__repomatic__pr2518/manifest.json` |
| `python_cpp__kdeldycke__repomatic__pr2520` | `python_cpp` | `kdeldycke/repomatic` | `2520` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__repomatic__pr2520/manifest.json` |
| `python_cpp__kdeldycke__repomatic__pr2525` | `python_cpp` | `kdeldycke/repomatic` | `2525` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__repomatic__pr2525/manifest.json` |
| `python_cpp__kdeldycke__repomatic__pr2534` | `python_cpp` | `kdeldycke/repomatic` | `2534` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kdeldycke__repomatic__pr2534/manifest.json` |
| `python_cpp__kfoltman__DerpCAM__pr2` | `python_cpp` | `kfoltman/DerpCAM` | `2` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kfoltman__DerpCAM__pr2/manifest.json` |
| `python_cpp__kiwigrid__k8s-sidecar__pr552` | `python_cpp` | `kiwigrid/k8s-sidecar` | `552` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__kiwigrid__k8s-sidecar__pr552/manifest.json` |
| `python_cpp__linto-ai__linto-studio__pr299` | `python_cpp` | `linto-ai/linto-studio` | `299` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__linto-ai__linto-studio__pr299/manifest.json` |
| `python_cpp__matthewmoran__sorta.fit__pr31` | `python_cpp` | `matthewmoran/sorta.fit` | `31` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__matthewmoran__sorta.fit__pr31/manifest.json` |
| `python_cpp__mattolson__agent-sandbox__pr148` | `python_cpp` | `mattolson/agent-sandbox` | `148` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__mattolson__agent-sandbox__pr148/manifest.json` |
| `python_cpp__melihbirim__csvql__pr41` | `python_cpp` | `melihbirim/csvql` | `41` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__melihbirim__csvql__pr41/manifest.json` |
| `python_cpp__micropython__micropython__pr19021` | `python_cpp` | `micropython/micropython` | `19021` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__micropython__micropython__pr19021/manifest.json` |
| `python_cpp__microsoft__agent-framework__pr4979` | `python_cpp` | `microsoft/agent-framework` | `4979` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__microsoft__agent-framework__pr4979/manifest.json` |
| `python_cpp__microsoft__agent-framework__pr5226` | `python_cpp` | `microsoft/agent-framework` | `5226` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__microsoft__agent-framework__pr5226/manifest.json` |
| `python_cpp__mike99mac__minimy-mike99mac__pr21` | `python_cpp` | `mike99mac/minimy-mike99mac` | `21` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__mike99mac__minimy-mike99mac__pr21/manifest.json` |
| `python_cpp__mikebz__djangovue__pr48` | `python_cpp` | `mikebz/djangovue` | `48` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__mikebz__djangovue__pr48/manifest.json` |
| `python_cpp__mikel-brostrom__boxmot__pr2266` | `python_cpp` | `mikel-brostrom/boxmot` | `2266` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__mikel-brostrom__boxmot__pr2266/manifest.json` |
| `python_cpp__mrzimu__uproot-custom__pr42` | `python_cpp` | `mrzimu/uproot-custom` | `42` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__mrzimu__uproot-custom__pr42/manifest.json` |
| `python_cpp__msys2__MINGW-packages__pr28823` | `python_cpp` | `msys2/MINGW-packages` | `28823` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__msys2__MINGW-packages__pr28823/manifest.json` |
| `python_cpp__msys2__MINGW-packages__pr28889` | `python_cpp` | `msys2/MINGW-packages` | `28889` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__msys2__MINGW-packages__pr28889/manifest.json` |
| `python_cpp__nf-core__modules__pr11162` | `python_cpp` | `nf-core/modules` | `11162` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__nf-core__modules__pr11162/manifest.json` |
| `python_cpp__nrfconnect__sdk-nrf__pr28118` | `python_cpp` | `nrfconnect/sdk-nrf` | `28118` | `2` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__nrfconnect__sdk-nrf__pr28118/manifest.json` |
| `python_cpp__oliver-zehentleitner__unicorn-binance-rest-api__pr95` | `python_cpp` | `oliver-zehentleitner/unicorn-binance-rest-api` | `95` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__oliver-zehentleitner__unicorn-binance-rest-api__pr95/manifest.json` |
| `python_cpp__oliver-zehentleitner__unicorn-fy__pr57` | `python_cpp` | `oliver-zehentleitner/unicorn-fy` | `57` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__oliver-zehentleitner__unicorn-fy__pr57/manifest.json` |
| `python_cpp__openRuyi-Project__openRuyi__pr106` | `python_cpp` | `openRuyi-Project/openRuyi` | `106` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openRuyi-Project__openRuyi__pr106/manifest.json` |
| `python_cpp__openedx__XBlock__pr905` | `python_cpp` | `openedx/XBlock` | `905` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openedx__XBlock__pr905/manifest.json` |
| `python_cpp__openedx__codejail__pr296` | `python_cpp` | `openedx/codejail` | `296` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openedx__codejail__pr296/manifest.json` |
| `python_cpp__openedx__event-tracking__pr401` | `python_cpp` | `openedx/event-tracking` | `401` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openedx__event-tracking__pr401/manifest.json` |
| `python_cpp__openedx__opaque-keys__pr439` | `python_cpp` | `openedx/opaque-keys` | `439` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openedx__opaque-keys__pr439/manifest.json` |
| `python_cpp__openedx__openedx-aspects__pr357` | `python_cpp` | `openedx/openedx-aspects` | `357` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openedx__openedx-aspects__pr357/manifest.json` |
| `python_cpp__openedx__openedx-events__pr560` | `python_cpp` | `openedx/openedx-events` | `560` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openedx__openedx-events__pr560/manifest.json` |
| `python_cpp__openedx__openedx-filters__pr350` | `python_cpp` | `openedx/openedx-filters` | `350` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openedx__openedx-filters__pr350/manifest.json` |
| `python_cpp__openedx__openedx-proposals__pr782` | `python_cpp` | `openedx/openedx-proposals` | `782` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openedx__openedx-proposals__pr782/manifest.json` |
| `python_cpp__openedx__platform-plugin-aspects__pr210` | `python_cpp` | `openedx/platform-plugin-aspects` | `210` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openedx__platform-plugin-aspects__pr210/manifest.json` |
| `python_cpp__openedx__xblock-sdk__pr499` | `python_cpp` | `openedx/xblock-sdk` | `499` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openedx__xblock-sdk__pr499/manifest.json` |
| `python_cpp__openhwgroup__cvw__pr1738` | `python_cpp` | `openhwgroup/cvw` | `1738` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openhwgroup__cvw__pr1738/manifest.json` |
| `python_cpp__openwrt__packages__pr29118` | `python_cpp` | `openwrt/packages` | `29118` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openwrt__packages__pr29118/manifest.json` |
| `python_cpp__openwrt__packages__pr29142` | `python_cpp` | `openwrt/packages` | `29142` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__openwrt__packages__pr29142/manifest.json` |
| `python_cpp__pipeshub-ai__pipeshub-ai__pr1853` | `python_cpp` | `pipeshub-ai/pipeshub-ai` | `1853` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__pipeshub-ai__pipeshub-ai__pr1853/manifest.json` |
| `python_cpp__powsybl__pypowsybl__pr1188` | `python_cpp` | `powsybl/pypowsybl` | `1188` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__powsybl__pypowsybl__pr1188/manifest.json` |
| `python_cpp__protocolbuffers__protobuf__pr26744` | `python_cpp` | `protocolbuffers/protobuf` | `26744` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__protocolbuffers__protobuf__pr26744/manifest.json` |
| `python_cpp__radareorg__radare2-bindings__pr241` | `python_cpp` | `radareorg/radare2-bindings` | `241` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__radareorg__radare2-bindings__pr241/manifest.json` |
| `python_cpp__robince__gcmi__pr14` | `python_cpp` | `robince/gcmi` | `14` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__robince__gcmi__pr14/manifest.json` |
| `python_cpp__ros-navigation__navigation2__pr6062` | `python_cpp` | `ros-navigation/navigation2` | `6062` | `2` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__ros-navigation__navigation2__pr6062/manifest.json` |
| `python_cpp__rossumai__rossum-agents__pr366` | `python_cpp` | `rossumai/rossum-agents` | `366` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__rossumai__rossum-agents__pr366/manifest.json` |
| `python_cpp__rovio__rovio-ingest__pr97` | `python_cpp` | `rovio/rovio-ingest` | `97` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__rovio__rovio-ingest__pr97/manifest.json` |
| `python_cpp__stac-utils__rustac__pr1028` | `python_cpp` | `stac-utils/rustac` | `1028` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__stac-utils__rustac__pr1028/manifest.json` |
| `python_cpp__tallclub__matimo__pr77` | `python_cpp` | `tallclub/matimo` | `77` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__tallclub__matimo__pr77/manifest.json` |
| `python_cpp__tektronix__tm_devices__pr570` | `python_cpp` | `tektronix/tm_devices` | `570` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__tektronix__tm_devices__pr570/manifest.json` |
| `python_cpp__tenxyte__tenxyte__pr115` | `python_cpp` | `tenxyte/tenxyte` | `115` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__tenxyte__tenxyte__pr115/manifest.json` |
| `python_cpp__tenxyte__tenxyte__pr116` | `python_cpp` | `tenxyte/tenxyte` | `116` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__tenxyte__tenxyte__pr116/manifest.json` |
| `python_cpp__texus__TGUI__pr351` | `python_cpp` | `texus/TGUI` | `351` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__texus__TGUI__pr351/manifest.json` |
| `python_cpp__usemoss__moss__pr151` | `python_cpp` | `usemoss/moss` | `151` | `1` | `data/raw/repo_snapshot_archives/python_cpp/python_cpp__usemoss__moss__pr151/manifest.json` |
| `python_java__Azure-Samples__Durable-Task-Scheduler__pr243` | `python_java` | `Azure-Samples/Durable-Task-Scheduler` | `243` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__Azure-Samples__Durable-Task-Scheduler__pr243/manifest.json` |
| `python_java__Azure__azure-dev__pr7617` | `python_java` | `Azure/azure-dev` | `7617` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__Azure__azure-dev__pr7617/manifest.json` |
| `python_java__Azure__azure-sdk__pr9818` | `python_java` | `Azure/azure-sdk` | `9818` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__Azure__azure-sdk__pr9818/manifest.json` |
| `python_java__BrokkAi__brokk__pr2760` | `python_java` | `BrokkAi/brokk` | `2760` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__BrokkAi__brokk__pr2760/manifest.json` |
| `python_java__CiscoDevNet__ansible-aci__pr838` | `python_java` | `CiscoDevNet/ansible-aci` | `838` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__CiscoDevNet__ansible-aci__pr838/manifest.json` |
| `python_java__HHS__simpler-grants-pdf-builder__pr666` | `python_java` | `HHS/simpler-grants-pdf-builder` | `666` | `2` | `data/raw/repo_snapshot_archives/python_java/python_java__HHS__simpler-grants-pdf-builder__pr666/manifest.json` |
| `python_java__HHS__simpler-grants-protocol__pr707` | `python_java` | `HHS/simpler-grants-protocol` | `707` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__HHS__simpler-grants-protocol__pr707/manifest.json` |
| `python_java__IBM__ai-atlas-nexus__pr165` | `python_java` | `IBM/ai-atlas-nexus` | `165` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__IBM__ai-atlas-nexus__pr165/manifest.json` |
| `python_java__IBM__granite-workshop__pr146` | `python_java` | `IBM/granite-workshop` | `146` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__IBM__granite-workshop__pr146/manifest.json` |
| `python_java__Jij-Inc__Qamomile__pr335` | `python_java` | `Jij-Inc/Qamomile` | `335` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__Jij-Inc__Qamomile__pr335/manifest.json` |
| `python_java__LiuMengxuan04__MiniCode__pr6` | `python_java` | `LiuMengxuan04/MiniCode` | `6` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__LiuMengxuan04__MiniCode__pr6/manifest.json` |
| `python_java__Marve10s__Better-Fullstack__pr150` | `python_java` | `Marve10s/Better-Fullstack` | `150` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__Marve10s__Better-Fullstack__pr150/manifest.json` |
| `python_java__PhillyBikeAction__bikeaction.org__pr228` | `python_java` | `PhillyBikeAction/bikeaction.org` | `228` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__PhillyBikeAction__bikeaction.org__pr228/manifest.json` |
| `python_java__Qiskit__ecosystem__pr1076` | `python_java` | `Qiskit/ecosystem` | `1076` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__Qiskit__ecosystem__pr1076/manifest.json` |
| `python_java__ROCm__rocm-jax__pr379` | `python_java` | `ROCm/rocm-jax` | `379` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__ROCm__rocm-jax__pr379/manifest.json` |
| `python_java__Second-Hand-Friends__kleinanzeigen-bot__pr986` | `python_java` | `Second-Hand-Friends/kleinanzeigen-bot` | `986` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__Second-Hand-Friends__kleinanzeigen-bot__pr986/manifest.json` |
| `python_java__SzymonPajzert__koryta__pr469` | `python_java` | `SzymonPajzert/koryta` | `469` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__SzymonPajzert__koryta__pr469/manifest.json` |
| `python_java__amzn__selling-partner-api-sdk__pr721` | `python_java` | `amzn/selling-partner-api-sdk` | `721` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__amzn__selling-partner-api-sdk__pr721/manifest.json` |
| `python_java__anteriorcore__brrr__pr172` | `python_java` | `anteriorcore/brrr` | `172` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__anteriorcore__brrr__pr172/manifest.json` |
| `python_java__apache__avro__pr3723` | `python_java` | `apache/avro` | `3723` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__apache__avro__pr3723/manifest.json` |
| `python_java__apache__flink-agents__pr614` | `python_java` | `apache/flink-agents` | `614` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__apache__flink-agents__pr614/manifest.json` |
| `python_java__bennettoxford__openprescribing__pr5500` | `python_java` | `bennettoxford/openprescribing` | `5500` | `2` | `data/raw/repo_snapshot_archives/python_java/python_java__bennettoxford__openprescribing__pr5500/manifest.json` |
| `python_java__blockcell-labs__blockcell__pr61` | `python_java` | `blockcell-labs/blockcell` | `61` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__blockcell-labs__blockcell__pr61/manifest.json` |
| `python_java__boltffi__boltffi__pr161` | `python_java` | `boltffi/boltffi` | `161` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__boltffi__boltffi__pr161/manifest.json` |
| `python_java__canonical__lxd__pr18063` | `python_java` | `canonical/lxd` | `18063` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__canonical__lxd__pr18063/manifest.json` |
| `python_java__canonical__pgbouncer-k8s-operator__pr725` | `python_java` | `canonical/pgbouncer-k8s-operator` | `725` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__canonical__pgbouncer-k8s-operator__pr725/manifest.json` |
| `python_java__canonical__pgbouncer-k8s-operator__pr733` | `python_java` | `canonical/pgbouncer-k8s-operator` | `733` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__canonical__pgbouncer-k8s-operator__pr733/manifest.json` |
| `python_java__canonical__postgresql-k8s-operator__pr1447` | `python_java` | `canonical/postgresql-k8s-operator` | `1447` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__canonical__postgresql-k8s-operator__pr1447/manifest.json` |
| `python_java__canonical__postgresql-operator__pr1614` | `python_java` | `canonical/postgresql-operator` | `1614` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__canonical__postgresql-operator__pr1614/manifest.json` |
| `python_java__celery__celery__pr10265` | `python_java` | `celery/celery` | `10265` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__celery__celery__pr10265/manifest.json` |
| `python_java__cmudig__mosaic__pr18` | `python_java` | `cmudig/mosaic` | `18` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__cmudig__mosaic__pr18/manifest.json` |
| `python_java__connectrpc__connect-python__pr210` | `python_java` | `connectrpc/connect-python` | `210` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__connectrpc__connect-python__pr210/manifest.json` |
| `python_java__cpinitiative__usaco-guide__pr6126` | `python_java` | `cpinitiative/usaco-guide` | `6126` | `3` | `data/raw/repo_snapshot_archives/python_java/python_java__cpinitiative__usaco-guide__pr6126/manifest.json` |
| `python_java__dbos-inc__dbos-transact-java__pr347` | `python_java` | `dbos-inc/dbos-transact-java` | `347` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__dbos-inc__dbos-transact-java__pr347/manifest.json` |
| `python_java__docat-org__docat__pr935` | `python_java` | `docat-org/docat` | `935` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__docat-org__docat__pr935/manifest.json` |
| `python_java__docker-library__official-images__pr21207` | `python_java` | `docker-library/official-images` | `21207` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__docker-library__official-images__pr21207/manifest.json` |
| `python_java__dynatrace-oss__dtwiz__pr11` | `python_java` | `dynatrace-oss/dtwiz` | `11` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__dynatrace-oss__dtwiz__pr11/manifest.json` |
| `python_java__flexera-public__policy_templates__pr4296` | `python_java` | `flexera-public/policy_templates` | `4296` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__flexera-public__policy_templates__pr4296/manifest.json` |
| `python_java__gastongouron__ironpress__pr113` | `python_java` | `gastongouron/ironpress` | `113` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__gastongouron__ironpress__pr113/manifest.json` |
| `python_java__google__net_http__pr36` | `python_java` | `google/net_http` | `36` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__google__net_http__pr36/manifest.json` |
| `python_java__greenbone__python-gvm__pr1315` | `python_java` | `greenbone/python-gvm` | `1315` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__greenbone__python-gvm__pr1315/manifest.json` |
| `python_java__idaholab__civet__pr644` | `python_java` | `idaholab/civet` | `644` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__idaholab__civet__pr644/manifest.json` |
| `python_java__jelmer__janitor__pr1167` | `python_java` | `jelmer/janitor` | `1167` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__jelmer__janitor__pr1167/manifest.json` |
| `python_java__jeremiah-k__meshtastic-matrix-relay__pr515` | `python_java` | `jeremiah-k/meshtastic-matrix-relay` | `515` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__jeremiah-k__meshtastic-matrix-relay__pr515/manifest.json` |
| `python_java__kdeldycke__click-extra__pr1593` | `python_java` | `kdeldycke/click-extra` | `1593` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__click-extra__pr1593/manifest.json` |
| `python_java__kdeldycke__click-extra__pr1594` | `python_java` | `kdeldycke/click-extra` | `1594` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__click-extra__pr1594/manifest.json` |
| `python_java__kdeldycke__click-extra__pr1596` | `python_java` | `kdeldycke/click-extra` | `1596` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__click-extra__pr1596/manifest.json` |
| `python_java__kdeldycke__click-extra__pr1605` | `python_java` | `kdeldycke/click-extra` | `1605` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__click-extra__pr1605/manifest.json` |
| `python_java__kdeldycke__click-extra__pr1612` | `python_java` | `kdeldycke/click-extra` | `1612` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__click-extra__pr1612/manifest.json` |
| `python_java__kdeldycke__meta-package-manager__pr1734` | `python_java` | `kdeldycke/meta-package-manager` | `1734` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__meta-package-manager__pr1734/manifest.json` |
| `python_java__kdeldycke__meta-package-manager__pr1749` | `python_java` | `kdeldycke/meta-package-manager` | `1749` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__meta-package-manager__pr1749/manifest.json` |
| `python_java__kdeldycke__repomatic__pr2489` | `python_java` | `kdeldycke/repomatic` | `2489` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__repomatic__pr2489/manifest.json` |
| `python_java__kdeldycke__repomatic__pr2498` | `python_java` | `kdeldycke/repomatic` | `2498` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__repomatic__pr2498/manifest.json` |
| `python_java__kdeldycke__repomatic__pr2516` | `python_java` | `kdeldycke/repomatic` | `2516` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__repomatic__pr2516/manifest.json` |
| `python_java__kdeldycke__repomatic__pr2518` | `python_java` | `kdeldycke/repomatic` | `2518` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__repomatic__pr2518/manifest.json` |
| `python_java__kdeldycke__repomatic__pr2520` | `python_java` | `kdeldycke/repomatic` | `2520` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__repomatic__pr2520/manifest.json` |
| `python_java__kdeldycke__repomatic__pr2525` | `python_java` | `kdeldycke/repomatic` | `2525` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__repomatic__pr2525/manifest.json` |
| `python_java__kdeldycke__repomatic__pr2534` | `python_java` | `kdeldycke/repomatic` | `2534` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kdeldycke__repomatic__pr2534/manifest.json` |
| `python_java__kfoltman__DerpCAM__pr2` | `python_java` | `kfoltman/DerpCAM` | `2` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kfoltman__DerpCAM__pr2/manifest.json` |
| `python_java__kiwigrid__k8s-sidecar__pr552` | `python_java` | `kiwigrid/k8s-sidecar` | `552` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__kiwigrid__k8s-sidecar__pr552/manifest.json` |
| `python_java__linto-ai__linto-studio__pr299` | `python_java` | `linto-ai/linto-studio` | `299` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__linto-ai__linto-studio__pr299/manifest.json` |
| `python_java__matthewmoran__sorta.fit__pr31` | `python_java` | `matthewmoran/sorta.fit` | `31` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__matthewmoran__sorta.fit__pr31/manifest.json` |
| `python_java__mattolson__agent-sandbox__pr148` | `python_java` | `mattolson/agent-sandbox` | `148` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__mattolson__agent-sandbox__pr148/manifest.json` |
| `python_java__membrowse__membrowse-action__pr128` | `python_java` | `membrowse/membrowse-action` | `128` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__membrowse__membrowse-action__pr128/manifest.json` |
| `python_java__microsoft__agent-framework__pr4979` | `python_java` | `microsoft/agent-framework` | `4979` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__microsoft__agent-framework__pr4979/manifest.json` |
| `python_java__microsoft__agent-framework__pr5215` | `python_java` | `microsoft/agent-framework` | `5215` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__microsoft__agent-framework__pr5215/manifest.json` |
| `python_java__microsoft__agent-framework__pr5226` | `python_java` | `microsoft/agent-framework` | `5226` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__microsoft__agent-framework__pr5226/manifest.json` |
| `python_java__mike99mac__minimy-mike99mac__pr21` | `python_java` | `mike99mac/minimy-mike99mac` | `21` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__mike99mac__minimy-mike99mac__pr21/manifest.json` |
| `python_java__mikebz__djangovue__pr48` | `python_java` | `mikebz/djangovue` | `48` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__mikebz__djangovue__pr48/manifest.json` |
| `python_java__mikel-brostrom__boxmot__pr2266` | `python_java` | `mikel-brostrom/boxmot` | `2266` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__mikel-brostrom__boxmot__pr2266/manifest.json` |
| `python_java__mongodb-developer__jedee__pr41` | `python_java` | `mongodb-developer/jedee` | `41` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__mongodb-developer__jedee__pr41/manifest.json` |
| `python_java__mozilla-ai__cq__pr176` | `python_java` | `mozilla-ai/cq` | `176` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__mozilla-ai__cq__pr176/manifest.json` |
| `python_java__msys2__MINGW-packages__pr28823` | `python_java` | `msys2/MINGW-packages` | `28823` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__msys2__MINGW-packages__pr28823/manifest.json` |
| `python_java__msys2__MINGW-packages__pr28889` | `python_java` | `msys2/MINGW-packages` | `28889` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__msys2__MINGW-packages__pr28889/manifest.json` |
| `python_java__nf-core__modules__pr11162` | `python_java` | `nf-core/modules` | `11162` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__nf-core__modules__pr11162/manifest.json` |
| `python_java__ninia__jep__pr632` | `python_java` | `ninia/jep` | `632` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__ninia__jep__pr632/manifest.json` |
| `python_java__nrfconnect__sdk-nrf__pr28118` | `python_java` | `nrfconnect/sdk-nrf` | `28118` | `2` | `data/raw/repo_snapshot_archives/python_java/python_java__nrfconnect__sdk-nrf__pr28118/manifest.json` |
| `python_java__oliver-zehentleitner__unicorn-fy__pr57` | `python_java` | `oliver-zehentleitner/unicorn-fy` | `57` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__oliver-zehentleitner__unicorn-fy__pr57/manifest.json` |
| `python_java__openRuyi-Project__openRuyi__pr106` | `python_java` | `openRuyi-Project/openRuyi` | `106` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openRuyi-Project__openRuyi__pr106/manifest.json` |
| `python_java__openedx__XBlock__pr905` | `python_java` | `openedx/XBlock` | `905` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openedx__XBlock__pr905/manifest.json` |
| `python_java__openedx__codejail__pr296` | `python_java` | `openedx/codejail` | `296` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openedx__codejail__pr296/manifest.json` |
| `python_java__openedx__event-tracking__pr401` | `python_java` | `openedx/event-tracking` | `401` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openedx__event-tracking__pr401/manifest.json` |
| `python_java__openedx__opaque-keys__pr439` | `python_java` | `openedx/opaque-keys` | `439` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openedx__opaque-keys__pr439/manifest.json` |
| `python_java__openedx__openedx-aspects__pr357` | `python_java` | `openedx/openedx-aspects` | `357` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openedx__openedx-aspects__pr357/manifest.json` |
| `python_java__openedx__openedx-events__pr560` | `python_java` | `openedx/openedx-events` | `560` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openedx__openedx-events__pr560/manifest.json` |
| `python_java__openedx__openedx-filters__pr350` | `python_java` | `openedx/openedx-filters` | `350` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openedx__openedx-filters__pr350/manifest.json` |
| `python_java__openedx__openedx-proposals__pr782` | `python_java` | `openedx/openedx-proposals` | `782` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openedx__openedx-proposals__pr782/manifest.json` |
| `python_java__openedx__platform-plugin-aspects__pr210` | `python_java` | `openedx/platform-plugin-aspects` | `210` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openedx__platform-plugin-aspects__pr210/manifest.json` |
| `python_java__openedx__xblock-sdk__pr499` | `python_java` | `openedx/xblock-sdk` | `499` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openedx__xblock-sdk__pr499/manifest.json` |
| `python_java__openhwgroup__cvw__pr1738` | `python_java` | `openhwgroup/cvw` | `1738` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openhwgroup__cvw__pr1738/manifest.json` |
| `python_java__openwrt__packages__pr29118` | `python_java` | `openwrt/packages` | `29118` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openwrt__packages__pr29118/manifest.json` |
| `python_java__openwrt__packages__pr29142` | `python_java` | `openwrt/packages` | `29142` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__openwrt__packages__pr29142/manifest.json` |
| `python_java__pipeshub-ai__pipeshub-ai__pr1853` | `python_java` | `pipeshub-ai/pipeshub-ai` | `1853` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__pipeshub-ai__pipeshub-ai__pr1853/manifest.json` |
| `python_java__powsybl__pypowsybl__pr1188` | `python_java` | `powsybl/pypowsybl` | `1188` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__powsybl__pypowsybl__pr1188/manifest.json` |
| `python_java__protocolbuffers__protobuf__pr26744` | `python_java` | `protocolbuffers/protobuf` | `26744` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__protocolbuffers__protobuf__pr26744/manifest.json` |
| `python_java__pybotters__pybotters__pr555` | `python_java` | `pybotters/pybotters` | `555` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__pybotters__pybotters__pr555/manifest.json` |
| `python_java__pydantic__pydantic-ai-harness__pr206` | `python_java` | `pydantic/pydantic-ai-harness` | `206` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__pydantic__pydantic-ai-harness__pr206/manifest.json` |
| `python_java__rossumai__rossum-agents__pr366` | `python_java` | `rossumai/rossum-agents` | `366` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__rossumai__rossum-agents__pr366/manifest.json` |
| `python_java__rovio__rovio-ingest__pr97` | `python_java` | `rovio/rovio-ingest` | `97` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__rovio__rovio-ingest__pr97/manifest.json` |
| `python_java__stac-utils__rustac__pr1028` | `python_java` | `stac-utils/rustac` | `1028` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__stac-utils__rustac__pr1028/manifest.json` |
| `python_java__tallclub__matimo__pr77` | `python_java` | `tallclub/matimo` | `77` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__tallclub__matimo__pr77/manifest.json` |
| `python_java__tektronix__tm_devices__pr570` | `python_java` | `tektronix/tm_devices` | `570` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__tektronix__tm_devices__pr570/manifest.json` |
| `python_java__tenxyte__tenxyte__pr115` | `python_java` | `tenxyte/tenxyte` | `115` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__tenxyte__tenxyte__pr115/manifest.json` |
| `python_java__tenxyte__tenxyte__pr116` | `python_java` | `tenxyte/tenxyte` | `116` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__tenxyte__tenxyte__pr116/manifest.json` |
| `python_java__tzafon__lightcone__pr16` | `python_java` | `tzafon/lightcone` | `16` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__tzafon__lightcone__pr16/manifest.json` |
| `python_java__usemoss__moss__pr151` | `python_java` | `usemoss/moss` | `151` | `1` | `data/raw/repo_snapshot_archives/python_java/python_java__usemoss__moss__pr151/manifest.json` |
| `python_java__vercel__vercel__pr15913` | `python_java` | `vercel/vercel` | `15913` | `2` | `data/raw/repo_snapshot_archives/python_java/python_java__vercel__vercel__pr15913/manifest.json` |
