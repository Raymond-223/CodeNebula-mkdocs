# Human–AI Interaction & Automation Levels

> **Section:** Human–AI Interaction

## Why it matters

先明确人与系统各自负责什么，再讨论自动化程度；“自动化更高”并不天然意味着系统更好。

## Core ideas

- **Human role**：人负责目标、监督、价值判断或必要接管。
- **System state & feedback**：界面必须让人知道系统在做什么，并能施加修正。
- **Manual / assisted**：人直接控制，或由系统提供建议与辅助。
- **Supervised autonomy**：系统自主执行，人负责监督和边界决策。
- **Authority boundary**：明确哪些动作系统可自行完成，哪些必须升级给人。

## Key theory

### Human-AI Interaction

HCI/HRI 的核心不是“界面好看”，而是让人能够在正确时间**理解系统状态、预测下一步、施加有效控制**。信息太少会失去态势感知，信息太多也会造成认知负荷。

### Levels of Automation

自动化等级应与任务风险、系统能力和人的响应能力共同设计。更高自动化并不天然更好；如果系统能力边界不清晰，反而可能让人失去准备。

## Representative methods

- Status + alert prioritization：让人先看到任务状态和关键风险。
- Function / authority allocation：明确人和系统各自负责什么、何时升级给人。

## Worked example

**Human-AI Interaction：**地面站不需要持续展示每个 ROS topic；更有价值的是任务状态、车辆健康、关键风险、当前计划和可接管入口。

**Levels of Automation：**远程机器人可以自主导航，但“进入未知高风险区域”必须等待操作者授权，这属于分层自动化。

## Connections

- → Software Engineering / observability。
- → Runtime Safety。
- → Human-in-the-Loop。
- → Safety Constraints。

## Further Reading

- Human factors、workload measurement、领域自动化分级。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Human-in-the-Loop →](02-human-in-loop.md)
