# Sensors & State Estimation

> **Section:** Robotics

## Why it matters

传感器给出带噪测量，状态估计把多源测量和运动模型融合成可用于控制的位姿与速度估计。

## Visual intuition

<figure markdown="span">
  ![机器人闭环不是感知、规划、控制的三个孤立模块，而是持续交换状态和约束。](../assets/diagrams/robot-stack.svg)
  <figcaption>机器人闭环不是感知、规划、控制的三个孤立模块，而是持续交换状态和约束。</figcaption>
</figure>

<figure markdown="span">
  ![状态估计在运动预测和传感器修正之间循环。](../assets/diagrams/state-estimation-loop.svg)
  <figcaption>状态估计的核心不是某个滤波器名字，而是 prediction 与 measurement update 的循环。</figcaption>
</figure>

## Core ideas

- **Exteroceptive sensors**：Camera/LiDAR 观察外部环境，各有语义、几何和失效特性。
- **Proprioceptive sensors**：IMU/Encoder 高频描述自身运动，但会漂移或受打滑影响。
- **Prediction → update**：状态估计先用模型预测，再用新观测修正。
- **Uncertainty**：估计必须同时表达可信程度。
- **Localization**：在给定地图或参考系中估计自身位姿。

## Key theory

### Robot Sensors

传感器没有“谁最好”，只有互补信息。设计时同时关注**量测物理意义、频率、延迟、噪声、外参和失效模式**。

### Localization & State Estimation

状态估计的一般循环是

$$
\text{prior} \xrightarrow{\text{motion}} \text{prediction}
\xrightarrow{\text{measurement}} \text{posterior}.
$$

Kalman Filter、EKF、Particle Filter 都是在实现这条逻辑，只是模型和分布假设不同。

## Representative methods

- Camera/LiDAR：提供外部语义与几何约束。
- IMU/Encoder：提供高频自身运动信息。
- Kalman Filter：线性高斯估计的代表。
- EKF：非线性机器人状态估计中最常见的扩展。

## Minimal code

下面是一维 Kalman update 的最小形式，只用于理解“预测不确定性越大，就越相信新观测”。

```python
x_pred, p_pred = 10.0, 4.0
z, r = 12.0, 1.0

k = p_pred / (p_pred + r)
x = x_pred + k * (z - x_pred)
p = (1 - k) * p_pred
print(x, p)
```

## Worked example

**Robot Sensors：**轮编码器说“走了 1 m”，但地面打滑时真实位移可能小于 1 m；IMU 能感知加速度变化，LiDAR/视觉可提供外部几何约束。

**Localization & State Estimation：**车轮里程计高频但会累计漂移；地图匹配低频但能提供全局修正。融合后既平滑又不容易长期跑偏。

## Connections

- → Perception：原始传感器变成可用特征。
- ← Conditional Probability & Bayes。
- → Mapping & SLAM。

## Further Reading

- Particle Filter、factor graph、UKF/smoothing、传感器标定。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Robot Models, Kinematics & Dynamics](01-models-kinematics-dynamics.md) · [Mapping & SLAM →](03-mapping-slam.md)
