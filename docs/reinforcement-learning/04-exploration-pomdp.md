# Exploration & Partial Observability

> **Section:** Reinforcement Learning

## Why it matters

探索解决“没试过”，部分可观测解决“看不全”。两者都表现为不确定，但处理方式完全不同。

## Core ideas

- **Exploration**：为获得信息而尝试当前不确定的动作。
- **Exploitation**：使用当前认为最优的动作。
- **POMDP**：真实状态不可完全观测。
- **Belief / memory**：用历史信息补偿当前观测不足。

## Key theory

探索处理的是知识不足；部分可观测处理的是信息本身不完整。二者不能混为一谈。

在 POMDP 中，策略通常写成

$$
\pi(a_t\mid \tau_t),
$$

其中 $\tau_t$ 是观测—动作历史，实际可用 RNN/Transformer 压缩历史。

## Representative methods

- $\varepsilon$-greedy：简单随机探索。
- Entropy bonus：鼓励随机策略。
- Recurrent policy：用记忆处理部分可观测。

## Worked example

门后目标不可见：随机尝试不同门属于探索；传感器被墙遮挡导致当前看不到目标属于部分可观测。

## Connections

- → Perception：更好的观测降低 POMDP 难度。
- → Multi-Agent Systems：其他 agent 的行为也会造成部分可观测。

## Further Reading

- UCB/Thompson Sampling、intrinsic motivation、belief-state planning。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Policy Gradient & Actor-Critic](03-policy-actor-critic.md) · [Model-Based vs Model-Free RL →](05-model-based-vs-model-free.md)
