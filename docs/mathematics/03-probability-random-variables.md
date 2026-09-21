# Probability & Random Variables

> **Section:** Mathematics for Intelligent Systems

## Why it matters

概率描述事件的可能性，随机变量把随机结果变成可以计算的数值；两者放在一起学习，才能自然进入期望、方差和分布。

## Core ideas

- **Event & probability**：事件是可能结果的集合，$P(A)$ 描述其发生可能性。
- **Random variable**：把随机结果映射为可以计算的数值。
- **PMF / PDF**：描述离散或连续随机变量的分布。
- **Expectation**：描述平均行为。
- **Variance / covariance**：描述单变量波动和多变量共同变化。

## Key theory

### Probability Basics

概率论解决的不是“预测每一次随机结果”，而是描述长期规律。最常用的三条规则是

$$
P(A^c)=1-P(A),\qquad P(A\cup B)=P(A)+P(B)-P(A\cap B),
$$

以及线性期望

$$
\mathbb E[aX+bY]=a\mathbb E[X]+b\mathbb E[Y].
$$

后续 RL 中的“期望回报”、控制中的“噪声均值”、可靠性中的“失效概率”都从这里出发。

### Random Variables & Distributions

常见分布只需掌握“什么时候用”：Bernoulli 描述一次成败，Gaussian 常用于连续噪声近似，Categorical 描述有限动作选择。

$$
\mathrm{Var}(X)=\mathbb E[(X-\mathbb E[X])^2].
$$

向量随机变量进一步使用协方差矩阵 $\Sigma$ 表示不同维度的不确定性。

## Representative methods

- 用频率估计概率：大量独立重复试验中，频率趋近真实概率。
- 用期望描述平均收益，用方差描述波动大小。
- Categorical：离散动作或类别。
- Gaussian：连续噪声与状态估计中最常见。

## Minimal code

代码只用于建立“大数下频率接近概率”的直觉，不需要把统计模拟当成概率定义。

```python
import random

# 用频率理解概率：Bernoulli(0.3) 的样本均值会逐渐接近 0.3
samples = [1 if random.random() < 0.3 else 0 for _ in range(10_000)]
print(sum(samples) / len(samples))
```

## Worked example

**Probability Basics：**机器人传感器一次测距可能偏大也可能偏小。若误差 $\varepsilon$ 满足 $\mathbb E[\varepsilon]=0$，多次独立测量取平均可降低随机误差；但系统性偏差不会靠平均消失。

**Random Variables & Distributions：**若二维定位误差近似高斯，均值给出“最可能中心”，协方差椭圆给出“不确定性朝哪个方向更大”。这比只报一个误差标量更有信息。

## Connections

- → Robustness & Safety：概率用于描述风险而不是消除风险。
- → Robotics：Kalman Filter 直接传播均值与协方差。
- → RL：随机策略本质上是条件分布。

## Further Reading

- 大数定律与中心极限定理的严格证明。
- 指数族、矩母函数、重尾分布。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Numerical Computation Essentials](02-numerical-computation.md) · [Conditional Probability & Bayes →](04-conditional-bayes.md)
