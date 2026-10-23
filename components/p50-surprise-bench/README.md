# P50 · surprise-bench

> 机制簇：**涌现能力度量/探针** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
系统遇到意外的程度，也是一种'聪明'的指标。

**L1 · 机制本质**
用简化 KL 散度衡量预期与实际的意外度。

**L2 · 怎么用上**
surprise(expected, actual) → float。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P50] 0.3681
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 换模型/升版本/改 prompt 前后的能力对比，尤其要抓「意外退化」。 |
| **不该用** | 单一固定任务的验收（用任务指标即可，不必上探针）。 |
| **常见误用** | 只看通过率——涌现常伴随旧能力退化，必须同时测「原本会做的现在还会吗」。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P48` emergence-probe-suite · `P49` capability-drift-meter
- 本仓是 **P50 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P50-surprise-bench/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](../../LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](../../LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P50 · surprise-bench © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](../../NOTICE)。
