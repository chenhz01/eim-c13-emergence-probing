# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P49 capability-drift-meter — 涌现能力度量/探针

L0: 能力会不会悄悄退化？画条线看趋势。
L1: 最小二乘斜率作为漂移率。
L2: drift(series) → slope。
"""

def drift(series):
    n = len(series)
    if n < 2: return 0.0
    xs = list(range(n)); mx = sum(xs)/n; my = sum(series)/n
    num = sum((x-mx)*(y-my) for x, y in zip(xs, series))
    den = sum((x-mx)**2 for x in xs) or 1
    return round(num/den, 4)

def demo():
    print("[P49]", drift([.9,.88,.86,.85]), drift([.8,.82,.85]))


if __name__ == "__main__":
    demo()
