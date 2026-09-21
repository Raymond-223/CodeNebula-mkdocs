# Modeling & Physics Simulation

> **Section:** Simulation & Sim2Real

## Why it matters

仿真首先是选择抽象层级：哪些物理必须保留，哪些可以忽略；数值积分和接触模型只是这种抽象的实现。

## Visual intuition

<figure markdown="span">
  ![Sim2Real 不是一次“从仿真导出模型”，而是现实数据不断反向校准仿真的循环。](../assets/diagrams/sim2real-loop.svg)
  <figcaption>Sim2Real 不是一次“从仿真导出模型”，而是现实数据不断反向校准仿真的循环。</figcaption>
</figure>

## Core ideas

- **Model / simulator**：模型定义规律，仿真器按模型推进状态并生成观测。
- **Fidelity & validation**：只要求对当前任务足够准确，并用真实数据验证。
- **Integrator / timestep**：连续动力学如何在离散时间中推进。
- **Contact**：碰撞、摩擦和约束会显著改变机器人行为。
- **Numerical stability**：时间步和参数不能让数值误差不断放大。

## Key theory

### Modeling & Simulation

仿真建模的原则是**按用途决定精度**。用于路径规划的底盘模型不一定需要轮胎有限元；用于抓取接触稳定性时，接触参数又可能非常关键。

### Physics Simulation

更小 timestep 通常提高数值精度但增加计算量；接触刚度、摩擦和求解器设置会显著影响移动/抓取行为。仿真“看起来不卡”不代表动力学正确。

## Representative methods

- Start simple：先建立最小可用模型。
- Validate against measurements：用真实数据检查模型是否够用。
- Timestep / contact tuning：只调整会影响任务结果的关键仿真参数。

## Minimal code

数值积分把连续动力学变成离散更新。时间步过大时，速度和接触过程都会产生明显数值误差。

```python
def euler_step(x, v, force, mass, dt):
    a = force / mass
    v_next = v + a * dt
    x_next = x + v_next * dt
    return x_next, v_next
```

## Worked example

**Modeling & Simulation：**如果目标是验证三车任务分配，先准确建模速度、转向、通信延迟即可；螺丝位置和外壳纹理通常不是首要误差源。

**Physics Simulation：**轮子在仿真中不断打滑，可能不是控制器问题，而是摩擦系数、接触几何或积分步长设置不合理。

## Connections

- → Robotics / Dynamics。
- → Robustness：模型误差必须显式考虑。
- → Control：控制频率必须与仿真时间尺度匹配。
- → Sim2Real：接触参数误差是典型 reality gap。

## Further Reading

- High-fidelity multiphysics、advanced contact / soft-body simulation。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Robot & Sensor Simulation →](02-robot-sensor-simulation.md)
