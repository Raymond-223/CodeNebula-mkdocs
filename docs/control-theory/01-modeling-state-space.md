# Dynamic Models & State Space

> **Section:** Control Theory

## Why it matters

动态系统描述“状态如何随输入和时间变化”；状态空间只是把这种动态关系写成适合分析和计算的统一形式。

## Core ideas

- **State & dynamics**：状态必须足以描述系统未来如何演化。
- **Input / output**：控制器施加什么，以及系统测量什么。
- **State-space equations**：用 $x_{t+1}=Ax_t+Bu_t$、$y_t=Cx_t+Du_t$ 统一表示线性动态。
- **Controllability**：输入是否有能力影响需要控制的状态。
- **Observability**：测量是否包含足够信息估计内部状态。

## Key theory

### Dynamic Systems & Modeling

连续系统常写为

$$
\dot x=f(x,u),\qquad y=h(x,u),
$$

线性系统写为 $\dot x=Ax+Bu$。模型不是越复杂越好，而是要保留与控制目标有关的动态。

### State-Space Methods

线性状态空间模型统一了多变量动力学。可控性矩阵

$$
\mathcal C=[B,AB,\ldots,A^{n-1}B]
$$

满秩时，线性系统在经典条件下可控。观测性有对偶结构。

## Representative methods

- First-principles modeling：由力学、电路等规律建立。
- System identification：由输入输出数据估计模型。
- State feedback：直接使用 $u=-Kx$。

## Minimal code

离散状态空间最小实现就是一次矩阵更新。代码的价值在于把 $x_{k+1}=Ax_k+Bu_k$ 从符号变成“输入什么、输出什么”。

```python
import numpy as np

A = np.array([[1.0, 0.1], [0.0, 1.0]])
B = np.array([[0.005], [0.1]])
x = np.array([0.0, 1.0])          # position, velocity
u = np.array([0.5])               # acceleration command
x_next = A @ x + (B @ u).ravel()
print(x_next)
```

## Worked example

**Dynamic Systems & Modeling：**小车一维运动若只关心低速，可用 $\dot p=v,\ \dot v=u$ 近似；若研究轮胎极限，就需要更复杂模型。

**State-Space Methods：**两轮车的“位置、速度、姿态”相互耦合，仅根据一个位置误差调 PID 往往不够，状态反馈可以同时考虑多个变量。

## Connections

- → Robotics / Kinematics & Dynamics。
- → Simulation：仿真器本质上也是动态模型。
- → Robotics / State Estimation。
- → LQR：在状态空间中系统化选择反馈矩阵。

## Further Reading

- Nonlinear system identification、hybrid systems。
- Canonical forms、observer design。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Feedback & Stability →](02-feedback-stability.md)
