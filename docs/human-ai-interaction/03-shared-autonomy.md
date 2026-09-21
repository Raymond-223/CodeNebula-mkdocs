# Shared Autonomy

> **Section:** Human–AI Interaction

## Why it matters

共享自治不是人和机器人同时抢控制权，而是根据任务阶段、风险和置信度在意图与自动控制之间仲裁。

## Visual intuition

<figure markdown="span">
  ![共享自治的核心是控制权仲裁，而不是简单把人的输入和机器指令相加。](../assets/diagrams/shared-autonomy.svg)
  <figcaption>共享自治的核心是控制权仲裁，而不是简单把人的输入和机器指令相加。</figcaption>
</figure>

## Core ideas

- **Human intent**：操作者想完成的目标。
- **Autonomy assistance**：系统补足稳定、避障或精细控制。
- **Blending**：组合人和自动控制输入。
- **Conflict**：人和系统意图不一致时的处理规则。

## Key theory

共享自主的目标不是简单做加权平均，而是在**保留人类目标控制权**的同时，让自动系统承担高频、精细或安全相关的部分。

## Representative methods

- Assistive / constraint-based control：人给目标或方向，系统负责稳定与安全。
- Goal inference：当人只给部分意图时估计其目标。

## Minimal code

最简单的共享控制可以先理解为“仲裁权重”，但真实系统的权重必须受安全约束和置信度控制。

```python
def shared_command(human, autonomy, alpha):
    alpha = max(0.0, min(1.0, alpha))
    return alpha * human + (1 - alpha) * autonomy
```

## Worked example

人用摇杆指向大致方向，系统自动保持安全距离并绕过小障碍；人仍决定去哪，AI 决定如何安全到达。

## Connections

- → Control Theory / feedback。
- → Robotics / navigation。

## Further Reading

- POMDP-based shared autonomy、intent inference。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Human-in-the-Loop](02-human-in-loop.md) · [Trust & Explainability →](04-trust-explainability.md)
