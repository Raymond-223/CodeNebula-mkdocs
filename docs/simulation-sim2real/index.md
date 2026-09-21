# Simulation & Sim2Real

> **定位：** 仿真部分不按 MuJoCo/Gazebo/Isaac Sim 分章节，而是按“模型—仿真—差距—适应—真实验证”的闭环组织。

<figure markdown="span">
  ![Simulation & Sim2Real learning map](../assets/diagrams/sim2real-map.svg)
  <figcaption>Simulation & Sim2Real 的最小主学习路径；箭头表示认知依赖，不代表必须掌握所有高级分支。</figcaption>
</figure>

## What to master

学完本 Section，只要求做到三件事：

1. 能用自己的话解释本领域的核心问题；
2. 能读懂最关键的公式、流程或系统结构；
3. 能把概念连接到一个简单实现或真实系统。

## Core chapters

| No. | Chapter | Why it stays in the core path |
|---:|---|---|
| 01 | [Modeling & Physics Simulation](01-modeling-physics.md) | 仿真首先是选择抽象层级：哪些物理必须保留，哪些可以忽略；数值积分和接触模型只是这种抽象的实现。 |
| 02 | [Robot & Sensor Simulation](02-robot-sensor-simulation.md) | 机器人仿真不仅要模拟刚体运动，还要模拟控制周期、传感器噪声、延迟和观测接口。 |
| 03 | [Reality Gap & Domain Randomization](03-reality-gap-randomization.md) | Reality Gap 是仿真假设与真实世界的系统性差异；校准减少已知偏差，随机化降低对未知变化的敏感性。 |
| 04 | [Sim2Real & Real2Sim](04-sim2real-real2sim.md) | Sim2Real 把策略或模型带到真实系统；Real2Sim 用真实数据反过来校准模型，形成迭代闭环。 |

## Stop rule

当你能够解释上述主线并完成每章的 Worked example，就可以进入下一个 Section。高级证明、算法变体和工具细节统一放在 **Further Reading**，不阻塞主线。
