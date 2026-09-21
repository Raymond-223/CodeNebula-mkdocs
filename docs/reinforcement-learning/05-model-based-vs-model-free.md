# Model-Based vs Model-Free RL

> **Section:** Reinforcement Learning

## Why it matters

是否显式学习或使用环境模型，是 RL 最重要的结构分界之一：模型换来规划能力，也引入模型偏差。

## Visual intuition

<figure markdown="span">
  ![是否显式使用环境模型决定了规划能力、样本效率与模型偏差之间的权衡。](../assets/diagrams/model-based-vs-free.svg)
  <figcaption>是否显式使用环境模型决定了规划能力、样本效率与模型偏差之间的权衡。</figcaption>
</figure>

## Core ideas

- **Model-free**：直接学价值或策略，不显式预测下一状态。
- **Model-based**：使用 $P(s'\mid s,a)$、奖励模型或 learned dynamics。
- **Planning**：利用模型在真实交互之外进行搜索/优化。
- **Model bias**：模型误差会在多步 rollout 中累积。

## Key theory

Model-free 把真实交互直接变成参数更新；Model-based 则多了一层

$$
(s_t,a_t)\rightarrow \hat s_{t+1},\hat r_{t+1}\rightarrow \text{planning / synthetic data}.
$$

前者结构简单，后者通常更节省真实交互，但必须管理模型误差。

## Representative methods

- Learned dynamics + MPC：用预测模型滚动规划。
- Model-generated rollouts：用模型补充真实交互数据。

## Worked example

真实机器人试错昂贵时，可先用少量轨迹拟合动力学，再在模型中筛掉明显差的动作，只把候选动作放到实车。

## Connections

- → Simulation & Sim2Real：模拟器可以作为已知或近似模型。
- → Control Theory / MPC：model-based 决策的经典形式。

## Further Reading

- Dyna、MuZero、Dreamer、MBPO。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Exploration & Partial Observability](04-exploration-pomdp.md) · [Safe, Robust & Offline RL →](06-safe-robust-offline.md)
