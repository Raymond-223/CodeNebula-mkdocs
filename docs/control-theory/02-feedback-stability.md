# Feedback & Stability

> **Section:** Control Theory

## Why it matters

反馈的意义是利用误差纠偏，而稳定性决定这种纠偏会收敛、振荡还是发散，两者必须连着理解。

## Visual intuition

<figure markdown="span">
  ![反馈控制把测量结果送回控制器，用实际输出与目标之间的误差持续修正输入。](../assets/diagrams/feedback-loop.svg)
  <figcaption>反馈控制把测量结果送回控制器，用实际输出与目标之间的误差持续修正输入。</figcaption>
</figure>

## Core ideas

- **Reference & error**：用 $e=r-y$ 表示目标与实际之间的偏差。
- **Feedback**：根据测量结果持续修正控制输入。
- **Disturbance**：模型之外影响系统的因素。
- **Equilibrium**：系统希望维持或回到的平衡状态。
- **Stability / asymptotic stability**：受小扰动后不发散，并在更强条件下回到平衡。
- **Lyapunov function**：判断一般系统稳定性的代表工具。

## Key theory

### Feedback Control

闭环结构是

$$
r\rightarrow \text{controller}\rightarrow \text{plant}\rightarrow y,
\qquad e=r-y.
$$

反馈的价值是根据真实结果修正模型误差和扰动，但高增益也可能放大噪声或造成振荡。

### Stability

线性连续系统 $\dot x=Ax$ 若所有特征值实部都小于 0，则原点渐近稳定。Lyapunov 方法则寻找 $V(x)>0$ 且沿轨迹 $\dot V(x)<0$ 的函数。

## Representative methods

- Negative feedback：闭环纠偏的基本结构。
- Eigenvalue test：判断线性系统局部稳定性。
- Lyapunov method：理解一般稳定性证明的代表工具。

## Worked example

**Feedback Control：**恒速巡航遇到上坡会减速；闭环控制检测到速度低于目标后自动增加驱动力。

**Stability：**弹簧阻尼系统受推后逐渐回到平衡位置，是渐近稳定；如果振幅越来越大，就是不稳定。

## Connections

- → State Estimation：反馈依赖可靠状态/输出。
- → Robustness：反馈要面对模型误差。
- → PID / State-Space：控制器设计必须首先保证闭环稳定。
- → Safety：稳定性是运行安全的一部分，但不是全部。

## Further Reading

- Loop shaping、frequency response。
- Input-to-state stability、LaSalle invariance。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Dynamic Models & State Space](01-modeling-state-space.md) · [PID Control →](03-pid.md)
