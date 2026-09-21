# PID Control

> **Section:** Control Theory

## Why it matters

PID 是最值得掌握的经典控制器，因为它把当前误差、累计误差和变化趋势分别映射成三种控制作用。

## Core ideas

- **P**：按当前误差纠正。
- **I**：积累历史误差，消除稳态偏差。
- **D**：看误差变化趋势，增加阻尼。
- **Saturation**：执行器有物理上限。

## Key theory

PID 控制律为

$$
u(t)=K_Pe(t)+K_I\int e(t)dt+K_D\dot e(t).
$$

P 太大可能振荡；I 太强会 windup；D 对噪声敏感。理解这三个现象比死记调参口诀重要。

## Representative methods

- Manual tuning：先 P，再 I，最后少量 D。
- Anti-windup：执行器饱和时限制积分累积。

## Minimal code

实现时还要考虑积分饱和、微分滤波和输出限幅；这段代码只保留 P/I/D 三项的结构。

```python
class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.integral = 0.0
        self.prev_error = 0.0

    def step(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        return self.kp*error + self.ki*self.integral + self.kd*derivative
```

## Worked example

温控器只用 P 时可能长期差 1°C；加入 I 后可以逐渐消除这个稳态偏差。

## Connections

- → Robot Control：底盘速度、关节位置常用 PID。
- → Filtering：D 项通常需要滤波。

## Further Reading

- Derivative filtering、2-DOF PID、系统化整定方法。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Feedback & Stability](02-feedback-stability.md) · [Optimal Control: LQR →](04-lqr.md)
