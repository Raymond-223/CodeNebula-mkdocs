# Robustness, Risk & Reliability

> **Section:** Robustness & Safety

## Why it matters

鲁棒性关心性能对扰动是否敏感，风险关心坏结果的概率和代价，可靠性关心系统在时间尺度上的可持续工作能力。

## Core ideas

- **Perturbation / sensitivity**：系统对输入、参数和环境变化有多敏感。
- **Margin / worst case**：离失效边界还有多少余量，以及规定范围内最差会怎样。
- **Hazard / risk**：什么会造成伤害，以及发生概率与后果。
- **Reliability**：系统在规定条件下持续完成任务的能力。

## Key theory

### Robustness

鲁棒性必须绑定**扰动集合 + 性能指标**。说“模型很鲁棒”没有可验证含义；说“定位偏差 ±0.2 m、通信延迟 ≤100 ms 时仍保持安全距离 ≥0.5 m”才可测试。

### Risk & Reliability

平均性能高不等于风险低。风险评估需要同时看**频率与后果**，并对关键危险设置独立约束或保护层。

## Representative methods

- Stress / scenario testing：主动覆盖边界场景。
- Robust optimization：对规定扰动集合保留性能。
- Risk matrix / failure metrics：把风险和可靠性量化到可跟踪指标。

## Worked example

**Robustness：**控制器在标称质量 20 kg 下稳定，不代表负载增加到 30 kg 仍稳定；应显式扫质量范围和稳定裕度。

**Risk & Reliability：**路线 A 平均快 5%，但偶尔进入无法恢复的危险区域；安全系统不能只根据平均完成时间选择 A。

## Connections

- ← Stochastic & Robust Optimization。
- → Safety Constraints。
- → Human-AI Interaction：高风险状态需要明确告警与接管。
- → Runtime Safety。

## Further Reading

- CVaR、H-infinity / certified robustness、FMEA / fault-tree analysis。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Uncertainty & Distribution Shift](01-uncertainty-shift.md) · [Safety Constraints →](03-safety-constraints.md)
