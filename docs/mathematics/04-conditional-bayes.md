# Conditional Probability & Bayes

> **Section:** Mathematics for Intelligent Systems

## Why it matters

条件概率解决“已知新信息后如何更新判断”，Bayes 则把这种更新写成统一规则。

## Visual intuition

<figure markdown="span">
  ![Bayes 规则把先验和新证据组合成后验，是状态估计和概率推断的共同直觉。](../assets/diagrams/bayes-update.svg)
  <figcaption>Bayes 规则把先验和新证据组合成后验，是状态估计和概率推断的共同直觉。</figcaption>
</figure>

## Core ideas

- **条件概率**：已知 $B$ 发生后 $A$ 的概率。
- **独立性**：知道一个事件不会改变另一个事件的概率。
- **Bayes 公式**：由先验和证据得到后验。
- **似然**：在给定假设下看到数据的可能性。

## Key theory

条件概率为

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
$$

Bayes 公式把推断方向反过来：

$$
P(H\mid D)=\frac{P(D\mid H)P(H)}{P(D)}.
$$

核心不是背公式，而是区分**先验、证据、似然、后验**。

## Representative methods

- Bayesian update：持续融合新观测。

## Worked example

假设传感器报警在“真的有障碍”时有 95% 概率触发，但障碍本身很少出现。即使报警，也不能直接说“95% 一定有障碍”；还必须乘上障碍的先验概率。

## Connections

- → Perception：观测是证据，不等于真实状态。
- → Game Theory：Bayesian Game 用类型概率描述不完全信息。

## Further Reading

- 共轭先验、变分推断。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Probability & Random Variables](03-probability-random-variables.md) · [Markov Processes →](05-markov-processes.md)
