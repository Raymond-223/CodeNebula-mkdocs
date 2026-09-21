# Robot Models, Kinematics & Dynamics

> **Section:** Robotics

## Why it matters

坐标系解决“在哪里”，运动学解决“怎么动”，动力学解决“为什么这样动”。三者合起来才构成机器人物理模型。

## Core ideas

- **Frame & pose**：定义“相对哪个坐标系，机器人在哪里、朝哪”。
- **Transform**：在不同坐标系之间变换位置和姿态。
- **Kinematics**：描述执行变量与机器人运动之间的几何关系。
- **Jacobian**：描述小的执行变化如何映射成速度变化。
- **Dynamics**：进一步考虑质量、惯量和力/力矩。

## Key theory

### Robot Models & Coordinate Systems

三维刚体变换常写为

$$
T=\begin{bmatrix}R&t\\0&1\end{bmatrix},
$$

并按链式关系组合：$T^A_C=T^A_BT^B_C$。机器人中最常见错误不是公式不会，而是**坐标系方向和时间戳不一致**。

### Kinematics & Dynamics

运动学不考虑力，只讨论几何与速度关系；动力学进一步写成

$$
M(q)\ddot q+C(q,\dot q)\dot q+g(q)=\tau.
$$

移动底盘入门阶段只需掌握差速/阿克曼等运动学模型。

## Representative methods

- 2D/3D pose 与坐标变换。
- Differential-drive kinematics：移动机器人最小代表。
- Jacobian：理解“执行变量变化如何映射到末端/车体运动”。

## Minimal code

齐次变换把旋转和平移放进一个矩阵，是 TF、定位、运动学链条最常见的坐标表达。

```python
import numpy as np

def transform_2d(x, y, yaw):
    c, s = np.cos(yaw), np.sin(yaw)
    return np.array([[c, -s, x],
                     [s,  c, y],
                     [0,  0, 1]])

T_world_robot = transform_2d(2.0, 1.0, 0.5)
```

## Worked example

**Robot Models & Coordinate Systems：**相机检测到目标在 camera frame 前方 2 m；要让底盘导航过去，必须通过外参把点变换到 base/map frame。

**Kinematics & Dynamics：**差速车左右轮同速则直行，速度不同则产生角速度；这属于运动学，不需要先计算轮胎受力。

## Connections

- → Perception：视觉输出必须落到统一坐标系。
- → ROS2/DDS：TF 负责传播坐标变换关系。
- → Control Theory：模型进入控制器。
- → Simulation：仿真器实现更完整动力学。

## Further Reading

- Ackermann / manipulator kinematics、SE(2)/SE(3)、完整刚体动力学。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Sensors & State Estimation →](02-sensing-estimation.md)
