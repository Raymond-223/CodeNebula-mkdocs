# Model Predictive Control

> **Section:** Control Theory

## Why it matters

MPC 每个时刻都在有限预测窗口内求解优化问题，因此能自然处理输入、状态和安全约束。

## Core ideas

- **Prediction horizon**：向未来预测有限步。
- **Receding horizon**：每次只执行当前最优序列的第一步。
- **Constraints**：速度、加速度、碰撞等直接进入优化。
- **Model mismatch**：预测模型与真实系统永远有差异。

## Key theory

MPC 每个时刻求解

$$
\min_{u_{0:H-1}}\sum_{k=0}^{H-1}\ell(x_k,u_k)
$$

并满足动力学与约束，然后只执行 $u_0$，下一时刻重新测量和优化。

## Representative methods

- Linear MPC：最适合作为“预测 + 约束 + 滚动优化”的入门代表。

## Worked example

自动驾驶车辆规划未来 2 秒转向/加速度，加入道路边界和最大横向加速度约束；执行 0.1 秒后重新规划。

## Connections

- → Robotics / Navigation & Control。
- → Safe Learning：MPC 可作为安全过滤器的一部分。

## Further Reading

- Nonlinear MPC、robust/tube MPC。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Optimal Control: LQR](04-lqr.md)
