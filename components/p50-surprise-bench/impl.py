# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P50 surprise-bench — 涌现能力度量/探针

L0: 系统遇到意外的程度，也是一种'聪明'的指标。
L1: 用简化 KL 散度衡量预期与实际的意外度。
L2: surprise(expected, actual) → float。
"""

import math
def surprise(expected, actual):
    s = 0.0
    for e, a in zip(expected, actual):
        if a > 0 and e > 0: s += a * math.log(a / e)
    return round(s, 4)

def demo():
    print("[P50]", surprise([.5,.5], [.9,.1]))


if __name__ == "__main__":
    demo()
