# Optimization, Constraints & Uncertainty

> **Section:** Mathematics for Intelligent Systems

## Why it matters

智能系统里的优化通常同时面对三件事：**目标要变好、约束不能违反、数据和模型又不完全确定**。这三类问题放在同一章理解，比把每个优化分支拆成独立课程更适合主学习路径。

## Visual intuition

<figure markdown="span">
  ![优化先明确变量、目标和可行域，再决定如何处理不确定性。](../assets/diagrams/optimization-constraints.svg)
  <figcaption>先问“优化什么、允许什么”，再问“随机性和最坏情况要怎样处理”。</figcaption>
</figure>

## Core ideas

- **Objective & gradient**：定义要优化什么，以及局部往哪个方向改。
- **Constraint & feasible set**：定义哪些解允许被选择。
- **Stochastic objective**：目标依赖随机样本或环境变化。
- **Risk**：不仅看平均值，也关注坏结果。
- **Robust objective**：要求在给定扰动范围内仍保持可接受表现。

## Key theory

无约束的一阶更新常写为

$$
\theta_{k+1}=\theta_k-\alpha_k\nabla J(\theta_k).
$$

带约束的问题可写为

$$
\min_x f(x)\quad \text{s.t.}\quad g_i(x)\le 0.
$$

当问题含随机性时，常见目标是期望性能：

$$
\min_x \mathbb E_\xi[f(x,\xi)].
$$

若更关注最坏情况，则可能采用

$$
\min_x \max_{\xi\in\mathcal U} f(x,\xi).
$$

主线只需理解这些目标在“平均表现、约束、安全余量”之间的区别，不要求推导完整对偶理论。

## Representative methods

- Gradient descent / SGD：一阶优化代表。
- Projection / penalty / Lagrangian：处理约束的代表思路。
- Sample average：用有限样本近似期望目标。

## Minimal code

```python
def projected_gradient(x, grad, lr=0.1, low=-1.0, high=1.0):
    x = x - lr * grad(x)
    return min(high, max(low, x))

x = 0.0
for _ in range(50):
    x = projected_gradient(x, lambda z: 2 * (z - 3))
print(x)  # 无约束最优是 3，但约束把结果限制在 1
```

## Worked example

移动机器人希望路径短，但速度和障碍距离必须满足安全约束；如果定位误差还存在，则只优化“名义情况下最短”并不足够，还需要为误差保留安全余量。

## Connections

- → RL：策略梯度优化期望回报。
- → Control：LQR/MPC 都是结构化优化问题。
- → Robustness & Safety：chance constraint、CVaR 和鲁棒集合在这里复用。
- → Sim2Real：域随机化可以看作对模型不确定性的采样覆盖。

## Further Reading

- KKT / duality、chance constraints、CVaR、distributionally robust optimization。

> 主线目标是会“写出问题”，不是熟练掌握所有优化求解器。

## Learning path

[← Section overview](index.md) · [← Markov Processes](05-markov-processes.md)
