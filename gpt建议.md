明白了。你们第二部分其实不是“泛泛地做编程语言”，而是要做 **Porta-Bench 里的“语言变化带来的迁移”** 这一支。演示文稿里已经把它列成三大场景之一，并且明确写了你们这支现在还缺搜索 query、人工评估规则、运行过滤和数据构造细则。

我先把你这部分用一句话说透：

**你们要做的是：从 GitHub 上找出“因为语言或语言版本变化而发生迁移”的真实 PR，把它们整理成 benchmark 样本，让模型去完成迁移，并用测试验证“旧功能没坏、新迁移生效”。** 这和普通修 bug 不一样，它关注的是“从旧语言/旧版本迁到新语言/新版本”。

---

## 一、先把概念学会

### 1）什么叫“语言变化带来的迁移”

最核心的定义是：

> **代码原来依赖某种语言特性、语法、运行时或生态，现在目标语言/目标版本变了，仓库必须修改，才能继续正确工作。**

这里的“语言变化”至少有两种：

**第一种：同一种语言，不同版本迁移**
比如 `Python 2 -> Python 3`。
这类任务的本质是：

* 语言还是 Python
* 但语法、标准库、字符串/字节语义、迭代器行为、异常写法等变了
* 所以代码和测试都要适配

**第二种：跨语言迁移**
比如你们 PPT 里举的 `C++ -> Python`。
这类任务的本质是：

* 核心实现语言真的变了
* 可能是重写、替换、移植、绑定层改造
* 修改范围一般更大，难度也更高

你们 PPT 现在把这两种都放进了“语言变化”这个场景里。

---

### 2）这类任务和另外两类任务有什么边界

这个边界你一定要懂，不然后面人工筛 PR 会乱。

**语言变化迁移** 关注的是：

* 编程语言本身变了，或者语言主版本变了
* 代码语法、运行时语义、标准库接口、构建方式因此变化

**框架变化迁移** 关注的是：

* 语言不一定变
* 但框架换了
  比如 `PyTorch -> TensorFlow`、`Django -> Flask`、`Pandas -> Polars`。这在你们 PPT 里被单独列为第三类。

**OS 变化迁移** 关注的是：

* 语言不一定变
* 平台变了
  比如 Linux 到 Windows。这个在 PPT 里第一类已经单独展开了。

所以你筛样本时要问自己一句：

> 这次 PR 的核心困难，主要是语言/语言版本导致的吗？

如果答案不是，那它就不该进你们第二部分。

---

### 3）你们这部分最重要的几个术语

#### source language / source version

迁移前的语言与版本。
例如：

* Python 2.7
* C++11
* Python 3.8

#### target language / target version

迁移后的语言与版本。
例如：

* Python 3.10
* Python
* C++17

你们 PPT 里已经明确写了，场景二人工评估时要确定 `source language`、`target language` 以及对应 version。

#### migration type

这其实是你们现在最该补的一列元数据。
我建议你们把“语言变化”再拆成至少两类：

* **Version migration**：同语言版本迁移，比如 py2->py3
* **Cross-language migration**：跨语言迁移，比如 cpp->python

不然你们后面把这两类混在一起做统计，结果会非常乱，因为它们的难度和修改范围不是一个量级。

#### pass2pass

原来就通过的测试，迁移后还要通过。
意思是：**旧功能不能被你迁坏。**

#### fail2pass

新加的、专门验证迁移需求的测试。
意思是：**原仓库在新环境下不行，迁移后必须行。**

PPT 里 Porta-Bench 的整体任务格式和 BeyondSWE 一样，都强调 issue-style 输入、环境构造和测试验证；你们现在第二部分也明确要做条件过滤、PR 过滤、运行过滤，以及后续实验测评。

#### rewrite issue

你们拿到的是 PR，不是 benchmark 输入。
所以要把 PR 改写成 issue 风格的问题描述，让模型“看起来像在解决一个迁移需求”，而不是直接看到答案。

这一步的关键是：

* 说清当前行为
* 说清期望行为
* 给出最小复现方式
* 不泄露具体 patch 思路

这和 OS 部分的人工检查逻辑是一样的，只不过你们要改成语言迁移版。

---

## 二、你这部分真正要做的，不是“收 PR”这么简单

你们 PPT 里对场景二写得很短，但其实背后至少有 5 个子任务。

### 任务 1：先把“语言迁移”定义清楚

这是最先要做的。

你现在最需要和学长确认的一件事是：

**你们第二部分到底要不要同时做**

* py2 -> py3 这种“版本迁移”
* cpp -> python 这种“跨语言迁移”

我的建议是：

**先把范围收紧。优先做“版本迁移”，再决定要不要扩展到“跨语言迁移”。**

原因很简单：

* `py2 -> py3` 更容易搜到真实 PR
* Docker 和测试更容易跑
* 修改范围通常没那么大
* 更容易形成稳定的 benchmark 规则

而 `cpp -> python` 往往会遇到：

* 重写比例过大
* 性能目标变化
* 接口可能一起变化
* 测试不一定能直接复用
* 很容易变成“新项目重写”，而不是“迁移”

所以对学生小组来说，**先做版本迁移是最稳的**。

---

### 任务 2：设计一个可执行的 taxonomy

也就是给“语言变化迁移”做分类标准。

我建议你们至少这样分：

#### A. 同语言版本迁移

例如：

* Python 2 -> Python 3
* C++11 -> C++17
* Java 8 -> Java 17

这类样本的核心特征是：

* 主语言不变
* 主要变化来自语法/标准库/运行时/工具链版本

#### B. 跨语言实现迁移

例如：

* C++ -> Python
* JavaScript -> TypeScript
* Shell -> Python

这类样本的核心特征是：

* 主实现语言真的变了
* 通常涉及更大规模的重写

#### C. 语言互操作层迁移

这个先不用一定做，但概念上要知道。
例如：

* C 扩展改成 pybind11
* 旧 binding 层迁到新 binding 方式
* JNI / FFI 封装重构

如果你们一上来就全收，会很难控质量。
所以最务实的是：

**第一版 benchmark 先只收 A；B 作为扩展。**

---

## 三、你在人工筛 PR 时，到底看什么

你后面大概率最常做的是人工检查。
这里我给你一个非常实用的判断框架。

### 一个 PR 可以进“语言迁移”的 5 个必要条件

#### 1. 迁移原因必须和语言/版本变化直接相关

比如：

* “Support Python 3”
* “Drop Python 2 compatibility”
* “Port implementation from C++ to Python”
* “Make code compatible with Python 3.12”
* “Update syntax for new language version”

如果只是：

* 修一个普通 bug
* 升某个库版本
* 改 CI
* 改框架 API

那通常不算语言迁移。

#### 2. PR 要有明确 source 和 target

你要能标出来：

* source language/version 是什么
* target language/version 是什么

如果这两项标不清，这个样本后面就很难评测。你们 PPT 也明确把这件事列成了场景二人工评估的一部分。

#### 3. 改动要真的是“适配”，不是“顺手重构”

很多 PR 会写得像迁移，但本质是大重构。
你要看核心 patch 是否主要在做：

* 语法替换
* API 适配
* 运行时语义兼容
* 构建/配置适配
* 测试适配

如果 PR 大部分是重命名、代码风格整理、架构重写，那不适合做 benchmark。

#### 4. 必须能构造可执行验证

也就是这个 PR 最终得能被变成：

* issue 风格描述
* 复现脚本
* pass2pass / fail2pass
* 可运行环境

如果没有测试、没有可运行环境、依赖已经失效，这条样本质量就很差。

#### 5. 不能明显泄露答案

如果 PR 标题/描述直接把解法说穿了，比如：

* “replace xrange with range”
* “use six.moves for …”
* “convert all print statements to function calls”

那你们 rewrite issue 时要小心，别把 gold patch 思路直接抄进 benchmark 输入。

---

## 四、你们第二部分建议怎么做：一个现实的工作流

你可以把自己的工作分成 6 步。

### 第一步：先定范围

你先去和学长确认一句：

> 第二部分第一版是只做 Python 版本迁移，还是同时做跨语言迁移？

我真心建议你先推动一个更稳的方案：

**第一版：只做 Python 2 -> 3，或 Python 主版本/次版本兼容迁移。**

这样你们更容易：

* 统一环境
* 统一测试框架
* 统一人工审核标准
* 更快出结果

---

### 第二步：设计搜索 query

PPT 里已经把“search query? 哪些 keyword 比较合适？”点出来了，这说明你们现在正缺这一步。

GitHub 支持对 issues / PR 做 qualifier 和布尔搜索，所以你们完全可以用“语言 + 迁移关键词”的结构化查询，而不是纯手搜。([GitHub Docs][1])

对你们第二部分，我建议先做两组 query。

#### A. Python 2 -> 3 版本迁移

可以围绕这些词组合：

* `is:pr`
* `"python 3"`
* `"python3"`
* `"py3"`
* `"py2"`
* `"python 2"`
* `"drop python 2"`
* `"support python 3"`
* `"port to python 3"`
* `"migrate to python 3"`
* `"2to3"`
* `"six"`
* `"future"`
* `"unicode"`
* `"bytes"`
* `"iteritems"`
* `"xrange"`

你真正搜的时候，不是一次全扔进去，而是做多轮召回。

比如思路上像：

* 强召回：`is:pr "python 3"`
* 中等精度：`is:pr "support python 3"`
* 高精度：`is:pr "drop python 2" "python 3"`

#### B. 跨语言迁移

围绕这些词组合：

* `is:pr`
* `"port to python"`
* `"rewrite in python"`
* `"python implementation"`
* `"replace c++"`
* `"migrate from c++"`
* `"cpp to python"`
* `"reimplement in python"`

但我要提醒你：
**这组 query 噪声会很大。**
所以如果你们人力有限，优先先做 A。

---

### 第三步：做三层过滤

你们 PPT 里已经有 `Conditional Filter -> PR Filter -> 运行过滤` 这条链。
你第二部分可以直接照着做，只是把规则语言化。

#### 1. 条件过滤

筛仓库本身是否合格，比如：

* public license
* stars > 5
* 有测试
* 有明确 PR
* 仓库还能拉下来
* 依赖大致还能装

#### 2. PR 过滤

筛 PR 是否真的是语言迁移。
这一步主要靠人工。

#### 3. 运行过滤

把 PR 前后的版本都跑起来。
PPT 里场景二明确写了：本地配 Docker 跑，目标是每个场景收 150~200+。

你的核心目标不是“PR 看起来像”，而是：

> pre-commit / post-commit 两个状态都能被复现，并且测试差异可观测。

---

### 第四步：做人工标注

这一步你可以做成表格，字段我建议这样设计：

* repo_name
* repo_url
* pr_url
* commit_before
* commit_after
* source_language
* source_version
* target_language
* target_version
* migration_type

  * version_migration / cross_language_migration
* affected_files
* test_framework
* build_system
* issue_rewrite_ready
* reproducible
* leakage_risk
* notes

这个表会救你命。
因为到后面你会同时面对几十条 PR，没有结构化字段会乱掉。

---

### 第五步：把 PR 改写成 benchmark 样本

一条合格 PR，最后要被整理成一个 instance。
一个 instance 至少要有：

#### 1. issue-style 描述

写成：

* 问题背景
* 当前行为
* 预期行为
* 最小复现脚本

#### 2. 环境

优先 Docker。
因为你们 PPT 也写了场景二运行过滤是本地 Docker，实验测评也参考 SWE-Bench / RepoTransBench 的方式。

#### 3. pass2pass

原先就通过的测试。

#### 4. fail2pass

专门验证迁移目标的新测试，或者从 PR 中识别出的新增测试。

---

### 第六步：做评测闭环

最后一条样本不是“看起来像”，而是必须能进入统一评测：

* 输入：issue
* 模型改 repo
* 在 Docker 中运行
* 跑 P2P + F2P
* 输出 resolved / unresolved

这也是 PPT 里整个 Porta-Bench 的基本思路。

---

## 五、你现在最该学会的“判断题”

下面这些是你以后每天都要判断的。

### 这个 PR 算不算语言迁移？

看“根因”是不是语言或版本变化。

### 这是版本迁移还是跨语言迁移？

这个决定后面环境和统计方式。

### 这个样本能不能做 benchmark？

看能不能复现、能不能测试、能不能改写成 issue。

### 这个 PR 有没有泄露答案？

如果有，rewrite issue 时就要去掉 patch 线索。

### 这个样本的成功标准是什么？

不是“代码看起来差不多”，而是“全部测试通过”。

---

## 六、我对你们第二部分的具体建议

这个是最重要的。

### 建议 1：先缩范围，不要一开始就做太大

你现在最容易踩坑的地方，就是把 `py2-py3` 和 `cpp-python` 放在同一篮子里同时推进。

我的建议是：

**第一阶段只做 Python 版本迁移。**

因为它最符合 benchmark 构造需求：

* PR 更容易找
* issue 更容易改写
* 测试更容易复用
* Docker 更容易做
* 统计更稳定

等这一套流程跑通以后，再加跨语言迁移。

---

### 建议 2：先做“标注规范”，再做“搜集”

很多学生组最容易反过来做：先搜一堆 PR，后面才发现标准不统一。

你们第二部分现在最该先写出来的文档不是实验，而是：

**《语言迁移样本标注规范 v1》**

里面至少写清：

* 什么算语言迁移
* 什么不算
* 如何区分 version / cross-language
* source/target 怎么标
* 何时判定可复现
* 何时淘汰样本

这个文档一旦有了，你和同学之间筛样本的一致性会高很多。

---

### 建议 3：你个人先拿 20 条 PR 做试标

不要一上来追 150 条。

先做一个小样本：

* 搜 50 条候选
* 人工筛到 20 条
* 再跑运行过滤
* 最后看看能剩几条

你会立刻知道：

* query 是否太宽
* 哪类 PR 噪声最大
* Docker 最常卡在哪里
* rewrite issue 最难写的是什么

这个小试跑，比空想有用得多。

---

## 七、你这周可以直接照着做的任务清单

### 第 1 天

把“语言迁移”写成一页规范：

* 定义
* 边界
* 两个子类
* 纳入 / 排除标准

### 第 2 天

写第一版 query 清单：

* Python 2 -> 3
* Python 版本兼容
* 跨语言迁移

### 第 3 天

人工试搜 30 到 50 条 PR，建立标注表。

### 第 4 天

筛出 10 到 20 条高质量候选，给每条填：

* source / target
* 是否可复现
* 是否有 tests
* 是否可 rewrite issue

### 第 5 天

尝试对其中 3 到 5 条做运行过滤：

* checkout 前后 commit
* 配 Docker
* 跑 tests
* 记录问题

这一轮做完，你就不再是“听懂 PPT”，而是真正开始做这部分了。

---

## 八、你可以先这样向学长汇报

你可以直接这样说：

> 我理解第二部分的核心不是泛泛搜语言相关 PR，而是构造“语言变化导致的真实迁移任务”。我建议先把语言迁移细分成版本迁移和跨语言迁移两类，并优先从 Python 2 到 3 的版本迁移开始，因为这类样本更容易统一筛选、运行和评测。接下来我会先写标注规范和 query 清单，再做一轮小规模试标和运行过滤，确认流程跑通后再扩到 150 条以上。

这段话会显得你已经进入“做 benchmark”的状态了。

---

如果你愿意，我下一条可以直接帮你写出一份 **《语言变化迁移样本标注规范 v1》**，你可以几乎原样发给组里。

[1]: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests?utm_source=chatgpt.com "Filtering and searching issues and pull requests"

