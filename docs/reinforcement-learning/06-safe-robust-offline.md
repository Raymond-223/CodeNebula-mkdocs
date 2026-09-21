# Safe, Robust & Offline RL

> **Section:** Reinforcement Learning

## Why it matters

当在线自由试错不可接受时，需要从数据来源、约束和分布偏移三个方向重新定义学习问题。

## Core ideas

- **Safe RL**：决策过程必须满足成本或安全约束。
- **Robust RL**：面对模型、观测或动力学扰动仍保持性能。
- **Offline RL**：只使用固定数据集训练，不能继续探索环境。
- **Distribution shift**：策略选择的数据外动作可能导致估计失真。

## Key theory

三类问题关注不同限制：Safe RL 关心**不能违反什么**，Robust RL 关心**环境变化后是否还能工作**，Offline RL 关心**只能从历史数据学什么**。

约束 MDP 常写为

$$
\max_\pi J_R(\pi)\quad \text{s.t.}\quad J_C(\pi)\le d.
$$

## Representative methods

- Constrained objective：把性能目标与成本/安全约束分开建模。
- Conservative offline learning：避免对数据外动作过度乐观。

## Worked example

自动驾驶日志很多，但不能为了探索让车辆在线随机尝试危险动作，因此“离线数据 + 安全约束 + 上线前鲁棒验证”往往同时出现。

## Connections

- → Robustness & Safety：提供不确定性、风险和运行时安全框架。
- → Simulation & Sim2Real：先在仿真中扩展覆盖，再谨慎迁移。

## Further Reading

- CQL、IQL、CMDP theory；更系统的鲁棒性见 Robustness & Safety。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Model-Based vs Model-Free RL](05-model-based-vs-model-free.md)
