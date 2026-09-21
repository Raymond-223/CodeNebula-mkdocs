# Sim2Real & Real2Sim

> **Section:** Simulation & Sim2Real

## Why it matters

Sim2Real 把策略或模型带到真实系统；Real2Sim 则用真实数据反过来修正仿真，两者组合才形成长期迭代闭环。

## Core ideas

- **Sim2Real**：把仿真中开发/训练结果迁移到真实系统。
- **Real2Sim**：用真实数据校准模型或构造更真实仿真。
- **Staged validation**：从纯仿真逐步增加真实硬件。
- **Safety gate**：每一步迁移都有明确验收条件。

## Key theory

更可靠的路线是闭环：

**Sim → Limited Real Test → Measure Gap → Real2Sim Calibration → Retrain/Retune → Wider Real Test**。

一次从仿真直接跳到开放实车测试，通常把所有误差源混在一起。

## Representative methods

- Software-in-the-loop → hardware-in-the-loop：逐级增加真实组件。
- Shadow / constrained rollout：真实环境中先限制策略权限。

## Worked example

先在仿真跑 1000 个场景，再用低速封闭场地验证控制和通信，随后扩大环境范围；每阶段只增加少量新风险。

## Connections

- → Robustness & Safety：迁移必须配合风险边界。
- → Software Engineering：仿真和实车配置都要版本化。

## Further Reading

- Digital twin、online adaptation、system-identification loops。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Reality Gap & Domain Randomization](03-reality-gap-randomization.md)
