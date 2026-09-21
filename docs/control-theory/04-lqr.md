# Optimal Control: LQR

> **Section:** Control Theory

## Why it matters

LQR 是“模型 + 代价函数 → 最优反馈增益”的最简代表，让你第一次看到控制器可以由优化问题系统地产生。

## Visual intuition

<figure markdown="span">
  ![LQR 提供最简最优反馈直觉，MPC 则进一步显式处理有限时域和约束。](../assets/diagrams/lqr-vs-mpc.svg)
  <figcaption>LQR 提供最简最优反馈直觉，MPC 则进一步显式处理有限时域和约束。</figcaption>
</figure>

## Core ideas

- **Cost**：量化状态偏差与控制能量。
- **LQR**：线性系统 + 二次代价的经典最优控制。
- **Riccati equation**：求最优反馈增益的核心方程。
- **Trade-off**：Q/R 决定“追踪更紧”还是“动作更温和”。

## Key theory

离散 LQR 常优化

$$
J=\sum_t (x_t^TQx_t+u_t^TRu_t),
$$

得到线性反馈 $u_t=-Kx_t$。LQR 的价值在于把“调多个增益”变成结构化优化。

## Representative methods

- LQR design：通过 $Q/R$ 权衡状态误差和控制代价。

## Worked example

平衡小车若把姿态误差权重设得很大，控制器会优先保持直立；若控制输入权重过大，动作会更温和但恢复更慢。

## Connections

- ← Optimization Basics。
- → MPC：从无约束二次最优推广到滚动约束优化。

## Further Reading

- LQG、iLQR。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← PID Control](03-pid.md) · [Model Predictive Control →](05-mpc.md)
