# Numerical Computation Essentials

> **Section:** Mathematics for Intelligent Systems

## Why it matters

连续公式最终都要落到有限精度的计算机上。控制、SLAM、仿真和优化真正运行时，都会遇到离散化、线性方程、数值积分和迭代误差；因此这里需要一章“够用的数值计算”，但不扩展成完整数值分析课程。

## Visual intuition

<figure markdown="span">
  ![数值计算把连续模型离散化，再用有限精度算法求近似结果，并检查误差是否可接受。](../assets/diagrams/numerical-computation.svg)
  <figcaption>主线只有四步：离散化 → 求解 → 检查误差 → 必要时调整步长或算法。</figcaption>
</figure>

## Core ideas

- **Floating-point error**：计算机只能近似表示实数，比较数值时通常使用容差而不是直接判断完全相等。
- **Discretization**：把连续时间、连续空间或导数转成离散近似。
- **Linear solve**：求 $Ax=b$；工程中通常直接求解，不显式计算 $A^{-1}$。
- **Least squares**：方程无精确解或观测有噪声时，寻找残差最小的近似解。
- **Numerical integration**：用有限时间步推进动态系统。
- **Iteration & convergence**：迭代算法要同时看误差、步长和停止条件。

## Key theory

导数可以用有限差分近似：

$$
f'(x)\approx\frac{f(x+h)-f(x)}{h}.
$$

连续动力学 $\dot x=f(x,u)$ 最简单的 Euler 离散化是

$$
x_{k+1}=x_k+\Delta t\,f(x_k,u_k).
$$

$\Delta t$ 太大时误差会明显增大；太小时计算量又会上升。数值计算的核心不是“永远取更小步长”，而是让**精度、稳定性和计算代价**与任务匹配。

对于 $Ax=b$，优先使用线性求解器；对超定方程 $Ax\approx b$，最小二乘求

$$
\min_x \|Ax-b\|_2^2.
$$

## Representative methods

- Finite difference：理解导数和 Jacobian 的数值近似。
- Euler：理解连续动力学如何离散推进；更高阶积分器按需要再学。
- `solve` / least squares：状态估计、标定、优化里反复出现。
- Tolerance-based stopping：根据残差或参数变化停止迭代。

## Minimal code

下面只展示两个最常见动作：解线性方程与用有限差分检查导数。

```python
import numpy as np

A = np.array([[2.0, 1.0], [1.0, 3.0]])
b = np.array([1.0, 2.0])
x = np.linalg.solve(A, b)          # 不需要显式求 inv(A)

f = lambda z: z**2
h = 1e-5
df = (f(3.0 + h) - f(3.0)) / h
print(x, df)                       # df 约等于 6
```

## Worked example

机器人仿真中把控制周期从 $20\,\mathrm{ms}$ 改成 $200\,\mathrm{ms}$ 后轨迹明显发散，首先应怀疑离散积分和控制更新过粗，而不是立即把问题归因于控制算法本身。

## Connections

- → Control Theory：离散状态更新、MPC 求解。
- → Robotics：标定、最小二乘、状态估计。
- → Simulation：时间步和积分器直接决定数值行为。
- → Optimization：梯度、迭代停止条件和线性子问题。

## Further Reading

- Numerical conditioning、higher-order integration、sparse linear algebra。

> 主线只要求知道“计算得到的是近似值”，并会判断步长、残差和数值稳定性是否合理。

## Learning path

[← Section overview](index.md) · [← Linear Algebra & Calculus Essentials](01-linear-algebra-calculus.md) · [Probability & Random Variables →](03-probability-random-variables.md)
