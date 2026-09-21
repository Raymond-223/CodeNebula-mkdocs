# Robustness & Safety

> **定位：** 安全部分从不确定性出发，区分鲁棒性、风险与硬安全约束，再学习故障处理和运行时保护。目标是知道“什么时候性能问题会变成安全问题”。

<figure markdown="span">
  ![Robustness & Safety learning map](../assets/diagrams/safety-map.svg)
  <figcaption>Robustness & Safety 的最小主学习路径；箭头表示认知依赖，不代表必须掌握所有高级分支。</figcaption>
</figure>

## What to master

学完本 Section，只要求做到三件事：

1. 能用自己的话解释本领域的核心问题；
2. 能读懂最关键的公式、流程或系统结构；
3. 能把概念连接到一个简单实现或真实系统。

## Core chapters

| No. | Chapter | Why it stays in the core path |
|---:|---|---|
| 01 | [Uncertainty & Distribution Shift](01-uncertainty-shift.md) | 噪声是观测的随机波动，分布偏移是数据生成机制发生变化；二者都影响可靠性，但诊断与处理方式不同。 |
| 02 | [Robustness, Risk & Reliability](02-robustness-risk.md) | 鲁棒性关心性能对扰动是否敏感，风险关心坏结果的概率和代价，可靠性关心系统在时间尺度上的可持续工作能力。 |
| 03 | [Safety Constraints](03-safety-constraints.md) | 安全约束不是“希望系统表现好”，而是明确哪些状态、动作或风险水平不可越过。 |
| 04 | [Fault Detection & Fault Tolerance](04-fault-tolerance.md) | 故障处理至少包含检测、隔离、诊断和恢复，真正的系统设计还要明确降级模式和安全状态。 |
| 05 | [Safe Learning & Runtime Safety](05-safe-learning-runtime.md) | 训练阶段的安全约束不能替代运行时保护。 |

## Stop rule

当你能够解释上述主线并完成每章的 Worked example，就可以进入下一个 Section。高级证明、算法变体和工具细节统一放在 **Further Reading**，不阻塞主线。
