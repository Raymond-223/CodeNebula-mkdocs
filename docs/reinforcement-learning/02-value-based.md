# Value-Based Methods

> **Section:** Reinforcement Learning

## Why it matters

价值方法先回答“这个状态/动作有多好”，再根据价值选择动作；Q-Learning 和 DQN 只是这一思想的代表。

## Core ideas

- **Q-value**：$Q(s,a)$ 评价在状态 $s$ 采取动作 $a$ 的长期价值。
- **TD target**：用一步奖励和下一状态估计构造学习目标。
- **Off-policy**：行为策略与目标策略可以不同。
- **Function approximation**：用神经网络近似大规模 $Q$。

## Key theory

表格 Q-Learning 更新为

$$
Q(s_t,a_t)\leftarrow Q(s_t,a_t)+\alpha\left[r_{t+1}+\gamma\max_a Q(s_{t+1},a)-Q(s_t,a_t)\right].
$$

DQN 只是把表格 $Q$ 换成神经网络，并加入经验回放与目标网络来降低训练相关性和目标漂移。

## Representative methods

- Q-Learning：离散小状态空间。
- DQN：用神经网络把 Q-Learning 扩展到高维状态。

## Minimal code

这一行更新就是 tabular Q-Learning 的核心；DQN 只是用神经网络近似 Q，并加入 replay buffer、target network 等稳定化机制。

```python
def q_update(q, s, a, r, s_next, alpha=0.1, gamma=0.99):
    target = r + gamma * max(q[s_next])
    q[s][a] += alpha * (target - q[s][a])
```

## Worked example

在网格世界中，Q 表可以直接存储“每个格子 × 每个动作”的价值；换成图像输入后无法列出所有状态，需要 DQN 由像素预测每个离散动作的 Q 值。

## Connections

- → Exploration：value-based 方法仍需要探索策略。
- → Actor-Critic：连续动作时不方便对所有动作取 $\max$。

## Further Reading

- Double DQN、Dueling DQN、Prioritized Replay、Rainbow。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← MDP & Bellman Equation](01-mdp-bellman.md) · [Policy Gradient & Actor-Critic →](03-policy-actor-critic.md)
