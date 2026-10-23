# C13 · Emergence Probing

> **机制簇**：涌现能力度量/探针 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：3
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
你怎么知道系统「突然会了新东西」？用一组固定探针定期测，记下能力跳变的时刻。

**L1 · 机制本质**
设计能力探针电池 + 意外度指标，把「涌现」从传说变成可测量、可复现的曲线。

**L2 · 怎么用上**
probe-battery 跑固定任务集；surprise-scorer 算跳变；capability-ledger 记时间线。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c13-emergence-probing.git && cd eim-c13-emergence-probing
python run_all.py        # 跑全簇 3 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p48-emergence-probe-suite/impl.py        # 看 demo 输出
python components/p48-emergence-probe-suite/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P48` | emergence-probe-suite | 每个探针 pass=1，汇总成能力得分。 | `components/p48-emergence-probe-suite/` |
| `P49` | capability-drift-meter | 最小二乘斜率作为漂移率。 | `components/p49-capability-drift-meter/` |
| `P50` | surprise-bench | 用简化 KL 散度衡量预期与实际的意外度。 | `components/p50-surprise-bench/` |

## 该用 / 不该用 / 常见误用

**该用**
模型/系统升级前后对比；自进化系统运行期监控。

**不该用**
单次静态评估（探针的价值在时间序列，不在单点分数）。

**常见误用（这条最重要）**
一次跑分就宣称「涌现」。须重复测量并给出置信区间。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C13 · Emergence Probing © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
