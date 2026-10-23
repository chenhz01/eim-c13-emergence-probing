# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P48 emergence-probe-suite — 涌现能力度量/探针

L0: 用几个小测试探一探：这个系统到底'长出'了什么本事。
L1: 每个探针 pass=1，汇总成能力得分。
L2: probe(results) → {probe: pass, score}。
"""

def probe(results):
    passed = {k: bool(v) for k, v in results.items()}
    score = sum(passed.values()) / max(1, len(passed))
    return passed, round(score, 2)

def demo():
    print("[P48]", probe({"plan":1,"verify":0,"reuse":1}))


if __name__ == "__main__":
    demo()
