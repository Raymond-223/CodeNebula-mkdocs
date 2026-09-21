# Control Theory

> **定位：** 控制部分围绕唯一主线展开：建立动态模型，形成反馈，判断稳定性，再选择 PID、LQR 或 MPC 等代表控制器。

<figure markdown="span">
  ![Control Theory learning map](../assets/diagrams/control-map.svg)
  <figcaption>Control Theory 的最小主学习路径；箭头表示认知依赖，不代表必须掌握所有高级分支。</figcaption>
</figure>

## What to master

学完本 Section，只要求做到三件事：

1. 能用自己的话解释本领域的核心问题；
2. 能读懂最关键的公式、流程或系统结构；
3. 能把概念连接到一个简单实现或真实系统。

## Core chapters

| No. | Chapter | Why it stays in the core path |
|---:|---|---|
| 01 | [Dynamic Models & State Space](01-modeling-state-space.md) | 动态系统描述“状态如何随输入和时间变化”；状态空间只是把这种动态关系写成适合分析和计算的统一形式。 |
| 02 | [Feedback & Stability](02-feedback-stability.md) | 反馈的意义是利用误差纠偏，而稳定性决定这种纠偏会收敛、振荡还是发散，两者必须连着理解。 |
| 03 | [PID Control](03-pid.md) | PID 是最值得掌握的经典控制器，因为它把当前误差、累计误差和变化趋势分别映射成三种控制作用。 |
| 04 | [Optimal Control: LQR](04-lqr.md) | LQR 是“模型 + 代价函数 → 最优反馈增益”的最简代表，让你第一次看到控制器可以由优化问题系统地产生。 |
| 05 | [Model Predictive Control](05-mpc.md) | MPC 每个时刻都在有限预测窗口内求解优化问题，因此能自然处理输入、状态和安全约束。 |

## Stop rule

当你能够解释上述主线并完成每章的 Worked example，就可以进入下一个 Section。高级证明、算法变体和工具细节统一放在 **Further Reading**，不阻塞主线。
