# Uncertainty & Distribution Shift

> **Section:** Robustness & Safety

## Why it matters

噪声是观测的随机波动，分布偏移是数据生成机制发生变化；二者都影响可靠性，但诊断与处理方式不同。

## Core ideas

- **Aleatoric / epistemic uncertainty**：分别来自数据随机性与模型知识不足。
- **Bias**：具有方向性的系统误差。
- **Distribution shift / OOD**：运行输入或任务关系超出训练覆盖。
- **Coverage**：测试是否覆盖预期运行条件。

## Key theory

### Uncertainty & Noise

安全分析首先要问“不确定来自哪里”。随机噪声可用概率描述；模型未知需要更多数据或保守边界；系统 bias 则不能靠简单平均消除。

### Distribution Shift

模型在 IID 测试集上的性能不能自动外推到雨天、夜间、传感器老化或新地图。安全验证需要按场景切分表现，而不是只看一个平均指标。

## Representative methods

- Noise / bias modeling。
- Calibration + residual analysis。
- Scenario / OOD evaluation：发现训练覆盖之外的情况。

## Worked example

**Uncertainty & Noise：**IMU 白噪声多测几次可平均降低；固定安装角误差属于 bias，不会因为采样更多自动消失。

**Distribution Shift：**白天训练的视觉模型夜间漏检增加，属于分布变化；应单独统计夜间性能并决定降级策略。

## Connections

- ← Probability & Random Variables。
- → Sim2Real / Reality Gap。
- → Risk & Reliability。

## Further Reading

- Ensemble/Bayesian uncertainty、test-time adaptation。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Robustness, Risk & Reliability →](02-robustness-risk.md)
