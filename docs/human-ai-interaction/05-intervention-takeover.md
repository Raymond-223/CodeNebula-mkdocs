# Intervention & Takeover

> **Section:** Human–AI Interaction

## Why it matters

接管流程必须设计上下文传递、权限切换和失败回退，否则“有人可以接管”并不等于“可以安全接管”。

## Visual intuition

<figure markdown="span">
  ![安全接管必须传递当前状态、意图和风险，并明确何时完成权限切换。](../assets/diagrams/takeover.svg)
  <figcaption>安全接管必须传递当前状态、意图和风险，并明确何时完成权限切换。</figcaption>
</figure>

## Core ideas

- **Trigger**：触发接管的风险/能力边界。
- **Handover**：控制权转移过程。
- **Reaction time**：人需要时间理解状态并行动。
- **Fallback**：人未响应时系统的保底行为。

## Key theory

接管不是一个按钮，而是一段过程：**Detect boundary → Alert → Provide context → Transfer authority → Confirm control → Recover**。高风险系统还必须定义“人没有及时接管”时的安全动作。

## Representative methods

- Clear alert + control-ownership indicator。
- Minimal-risk fallback：人未及时接管时系统先保底。

## Worked example

机器人检测到定位置信度持续下降：先提示操作者；若跌破安全阈值则减速并请求接管；超时无人响应则停车，而不是继续盲走。

## Connections

- → Fault Detection。
- → Levels of Automation。

## Further Reading

- Takeover time modeling、adaptive autonomy。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Trust & Explainability](04-trust-explainability.md)
