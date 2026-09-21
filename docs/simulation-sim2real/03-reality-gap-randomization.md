# Reality Gap & Domain Randomization

> **Section:** Simulation & Sim2Real

## Why it matters

Reality Gap 是仿真假设与真实世界的系统性差异；校准减少已知偏差，随机化降低对未知变化的敏感性。

## Visual intuition

<figure markdown="span">
  ![校准减少已知误差，随机化让策略对剩余不确定性更不敏感。](../assets/diagrams/domain-rand.svg)
  <figcaption>校准减少已知误差，随机化让策略对剩余不确定性更不敏感。</figcaption>
</figure>

## Core ideas

- **Dynamics gap**：质量、摩擦和执行器响应不同。
- **Perception gap**：纹理、光照、噪声和传感器模型不同。
- **Timing gap**：延迟、频率和异步行为不同。
- **Domain randomization**：训练时主动覆盖可能的参数变化。
- **Calibration / adaptation**：利用真实数据修正已知系统性偏差。
- **Coverage**：随机化必须覆盖真实变化，但不能无限放大范围。

## Key theory

### Reality Gap

Reality gap 不是一个单一误差。应按**动力学、感知、时间、环境和交互主体**拆分，再通过真实数据定位最主要差异。

### Domain Randomization & Adaptation

随机化不是“参数越乱越鲁棒”。合理做法是根据真实误差来源定义分布，并验证真实参数是否处于训练覆盖范围内。

## Representative methods

- Real-vs-sim trajectory / sensor comparison：先量化差距。
- Dynamics / visual randomization：覆盖主要变化来源。
- Calibration / adaptation：对已知系统性偏差做修正。

## Worked example

**Reality Gap：**仿真路径跟踪很好，实车转弯总过冲：先比较转向执行器延迟和最大角速度，而不是立刻重训策略。

**Domain Randomization & Adaptation：**实车轮胎摩擦在 0.6–0.9 间变化，则围绕该范围随机化比从 0.01 到 3.0 无依据乱采样更合理。

## Connections

- → Robustness：跨域误差就是分布偏移。
- → Real2Sim：用真实数据反向校准。
- ← Stochastic & Robust Optimization。
- → Robustness & Safety。

## Further Reading

- Adversarial randomization、representation/domain adaptation。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Robot & Sensor Simulation](02-robot-sensor-simulation.md) · [Sim2Real & Real2Sim →](04-sim2real-real2sim.md)
