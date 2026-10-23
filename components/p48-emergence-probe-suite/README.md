# P48 · emergence-probe-suite

> 机制簇：**涌现能力度量/探针** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
用几个小测试探一探：这个系统到底'长出'了什么本事。

**L1 · 机制本质**
每个探针 pass=1，汇总成能力得分。

**L2 · 怎么用上**
probe(results) → {probe: pass, score}。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P48] ({'plan': True, 'verify': False, 'reuse': True}, 0.67)
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 换模型/升版本/改 prompt 前后的能力对比，尤其要抓「意外退化」。 |
| **不该用** | 单一固定任务的验收（用任务指标即可，不必上探针）。 |
| **常见误用** | 只看通过率——涌现常伴随旧能力退化，必须同时测「原本会做的现在还会吗」。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P49` capability-drift-meter · `P50` surprise-bench
- 本仓是 **P48 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P48-emergence-probe-suite/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P48 · emergence-probe-suite © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
