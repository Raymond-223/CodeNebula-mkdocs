# Markov Processes

> **Section:** Mathematics for Intelligent Systems

## Why it matters

Markov 过程是从静态概率走向序列决策的最短桥梁：只保留状态、转移和稳态等后续会用到的核心概念。

## Core ideas

- **Markov property**：给定当前状态后，未来与更早历史条件独立。
- **Transition matrix $P$**：离散 Markov Chain 的一步转移。
- **State**：必须包含做未来预测所需的信息。

## Key theory

Markov 性写作

$$
P(S_{t+1}\mid S_t,S_{t-1},\ldots)=P(S_{t+1}\mid S_t).
$$

它并不等于“系统没有记忆”，而是说明**记忆已经被压缩进当前状态**。如果当前状态缺少速度、历史观测等信息，模型可能就不是 Markov 的。

## Representative methods

- Markov Chain：没有控制动作。
- MDP：在 Markov 状态上加入动作与奖励。
- POMDP：真实状态不可直接观测。

## Worked example

只用机器人的当前位置描述运动通常不够，因为下一位置还取决于速度。把“位置 + 速度”一起作为状态后，模型更接近 Markov。

## Connections

- → Reinforcement Learning：MDP 是 RL 的基础模型。
- → Control Theory：状态空间模型同样依赖“状态足够性”。

## Further Reading

- Stationary distribution、遍历性、Markov Chain Monte Carlo。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Conditional Probability & Bayes](04-conditional-bayes.md) · [Optimization, Constraints & Uncertainty →](06-optimization-under-uncertainty.md)
