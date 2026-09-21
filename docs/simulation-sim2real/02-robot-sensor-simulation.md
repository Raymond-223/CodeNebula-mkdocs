# Robot & Sensor Simulation

> **Section:** Simulation & Sim2Real

## Why it matters

机器人仿真不仅要模拟刚体运动，还要模拟控制周期、传感器噪声、延迟和观测接口。

## Visual intuition

<figure markdown="span">
  ![传感器仿真应从真实量经过采样、噪声、偏置和延迟后再交给算法。](../assets/diagrams/sensor-simulation.svg)
  <figcaption>算法看到的应是“模拟观测”，而不是直接读取仿真器里的真值。</figcaption>
</figure>

## Core ideas

- **Sensor model**：真实量到模拟观测的映射。
- **Noise**：随机测量误差。
- **Bias/drift**：随时间累积的系统误差。
- **Latency**：采样与使用之间的时间延迟。

## Key theory

理想传感器会让算法在仿真中“作弊”。有效仿真至少应考虑分辨率、频率、视场、量化、噪声和延迟；对 IMU 还需关注 bias/drift。

## Representative methods

- Camera rendering。
- LiDAR ray casting。
- IMU/encoder noise model。

## Minimal code

噪声模型不需要一开始就很复杂；先显式区分真值、偏置和随机噪声即可。

```python
import random

def measure(true_value, bias=0.05, sigma=0.02):
    return true_value + bias + random.gauss(0.0, sigma)

print(measure(1.0))
```

## Worked example

若仿真里 LiDAR 永远无遮挡、零噪声，SLAM 在仿真中的成功率对实车几乎没有解释力。

## Connections

- → Perception / State Estimation。
- → Domain Randomization。

## Further Reading

- Photorealistic rendering、sensor-specific calibration。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Modeling & Physics Simulation](01-modeling-physics.md) · [Reality Gap & Domain Randomization →](03-reality-gap-randomization.md)
