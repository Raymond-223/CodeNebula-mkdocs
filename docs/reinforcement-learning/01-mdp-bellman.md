# MDP & Bellman Equation

> **Section:** Reinforcement Learning

## Why it matters

MDP 给出序列决策的最小数学模型；Bellman 方程则把长期回报压缩成一步递推，是几乎所有经典 RL 方法的共同骨架。

## Visual intuition

<figure markdown="span">
  ![状态、动作、奖励和下一状态构成 RL 最基本的交互闭环。](../assets/diagrams/mdp-loop.svg)
  <figcaption>状态、动作、奖励和下一状态构成 RL 最基本的交互闭环。</figcaption>
</figure>

## Core ideas

- **MDP**：$(\mathcal S,\mathcal A,P,\mathcal R,\gamma)$。
- **Return $G_t$**：从时刻 $t$ 开始的折扣累积奖励。
- **Value function**：$V^\pi,Q^\pi$ 衡量未来回报。
- **Bellman equation**：把长期价值拆成一步奖励 + 下一状态价值。

## Key theory

核心递推是

$$
V^\pi(s)=\mathbb E_\pi[r_{t+1}+\gamma V^\pi(s_{t+1})\mid s_t=s].
$$

最优价值则满足 Bellman optimality equation。Bellman 的意义不是某个具体算法，而是把“无限长未来”转成可以反复更新的一步关系。

## Representative methods

- Policy evaluation：给定策略估价值。
- Policy improvement：根据价值改策略。
- Dynamic programming：模型已知时直接用 Bellman 递推。

## Worked example

两状态任务中，若动作“前进”立即得到 1 分并转到终止状态，则 $Q(s,\text{forward})=1$；若“等待”得到 0 分并留在原地，则价值取决于未来是否还会前进。

## Connections

- ← Mathematics / Markov Processes。
- → Value-Based Methods：直接学习 Bellman 目标。

## Further Reading

- Bellman contraction proof、occupation measure。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Value-Based Methods →](02-value-based.md)
