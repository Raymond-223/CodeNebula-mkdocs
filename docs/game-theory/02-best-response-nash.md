# Best Response & Nash Equilibrium

> **Section:** Game Theory

## Why it matters

最佳响应回答“别人不变时我怎么选”，Nash 均衡则要求所有人的策略同时互为最佳响应。

## Visual intuition

<figure markdown="span">
  ![Nash 面向一般策略相互依赖，minimax 则利用零和结构讨论最坏对手。](../assets/diagrams/nash-minimax.svg)
  <figcaption>Nash 面向一般策略相互依赖，minimax 则利用零和结构讨论最坏对手。</figcaption>
</figure>

## Core ideas

- **Best response $BR_i$**：对给定对手策略的最优回应集合。
- **Nash equilibrium**：所有玩家同时处于彼此最佳回应。
- **Pure vs mixed Nash**：均衡可以是确定动作，也可以是概率分布。
- **Stability**：Nash 是单边偏离稳定，不等于社会最优。

## Key theory

策略组合 $\sigma^*$ 是 Nash equilibrium，当且仅当

$$
u_i(\sigma_i^*,\sigma_{-i}^*)\ge u_i(\sigma_i,\sigma_{-i}^*)
$$

对每个玩家 $i$ 和任意单边替代策略 $\sigma_i$ 都成立。

## Representative methods

- Best-response iteration：简单但不总收敛。

## Minimal code

最佳响应就是在对方策略固定后最大化自己的收益；Nash 均衡要求所有参与者同时满足这一条件。

```python
import numpy as np

payoff = np.array([[3, 0],
                   [5, 1]])
opponent_action = 0
best_action = int(np.argmax(payoff[:, opponent_action]))
print(best_action)
```

## Worked example

囚徒困境中双方背叛是 Nash：任何一方单独改成合作都会更差；但双方合作的总收益更高，所以 Nash 不等于社会最优。

## Connections

- → Mechanism design（仅拓展）：可通过修改激励结构改变均衡。
- → MARL：学习动态常尝试逼近某类稳定策略。

## Further Reading

- Correlated equilibrium、混合策略均衡求解。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Game Models & Classification](01-game-models.md) · [Zero-Sum & Minimax →](03-zero-sum-minimax.md)
