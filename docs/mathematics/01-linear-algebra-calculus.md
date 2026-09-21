# Linear Algebra & Calculus Essentials

> **Section:** Mathematics for Intelligent Systems

## Why it matters

向量和矩阵负责表示状态、坐标、特征和线性模型；导数、梯度和 Jacobian 负责描述“输出对输入如何变化”。后续的优化、控制、机器人坐标变换和深度学习都反复使用这两套语言。

## Visual intuition

<figure markdown="span">
  ![线性代数负责表示与变换，微积分负责描述变化与更新。](../assets/diagrams/linear-algebra-calculus.svg)
  <figcaption>线性代数负责表示与变换，微积分负责描述变化与更新。</figcaption>
</figure>

## Core ideas

- **Vector / matrix**：表示状态、特征、线性模型和坐标变换。
- **Dot product / norm**：分别描述方向关系与向量大小。
- **Derivative / gradient**：描述标量输出对输入变化的敏感方向。
- **Jacobian**：描述向量输出对向量输入的一阶变化。
- **Chain rule**：把多层函数的局部变化连接起来。

## Key theory

线性模型最基本的形式是

$$
y=Ax+b.
$$

它既可以表示神经网络的一层，也可以表示局部线性系统。对标量目标 $J(\theta)$，梯度

$$
\nabla_\theta J=
\begin{bmatrix}
\partial J/\partial \theta_1 & \cdots & \partial J/\partial \theta_n
\end{bmatrix}^T
$$

给出局部变化最快的方向，因此梯度下降沿 $-\nabla J$ 更新。

对机器人运动学中 $y=f(x)$ 这类向量映射，Jacobian 近似描述小变化：

$$
\Delta y \approx J_f(x)\,\Delta x.
$$

主线只要求会读这些对象的**维度、输入输出和几何意义**，不要求做完整矩阵分析证明。

## Representative methods

- 矩阵乘法：组合多个线性/坐标变换。
- Gradient：优化标量目标。
- Jacobian：机器人运动学、状态估计与非线性模型局部线性化。
- Chain rule：多层模型与 backpropagation 的核心规则。

## Minimal code

```python
import numpy as np

A = np.array([[2.0, 0.0],
              [0.0, 0.5]])
x = np.array([1.0, 4.0])
y = A @ x
print(y)  # [2. 2.]
```

这里不需要记 NumPy API；重点是看懂“矩阵把一个向量映射成另一个向量”。

## Worked example

二维机器人状态 $x=[p_x,p_y]^T$ 经过旋转矩阵 $R$ 后得到另一个坐标系中的表示 $x'=Rx$。若损失函数衡量预测位置与真实位置的距离，则梯度告诉优化器应该怎样修改模型参数来减小该距离。

## Connections

- → Optimization：梯度和 Hessian 描述目标函数局部形状。
- → Control Theory：状态空间模型直接使用矩阵 $A,B,C,D$。
- → Robotics：旋转、齐次变换和 Jacobian 都建立在线性代数上。
- → Perception：相机投影、特征向量与深度网络都大量使用矩阵运算。

## Further Reading

- Eigenvalue / eigenvector、SVD、positive definite matrix。
- Hessian、matrix calculus、automatic differentiation。

> 这些内容需要时再补；第一次学习只要求会操作向量/矩阵、读懂梯度与 Jacobian。

## Learning path

[← Section overview](index.md) · [Numerical Computation Essentials →](02-numerical-computation.md)
