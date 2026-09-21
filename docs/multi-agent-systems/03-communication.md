# Communication & Information Sharing

> **Section:** Multi-Agent Systems

## Why it matters

通信的价值不是“越多越好”，而是在成本、时延和信息增益之间找到足够的共享机制。

## Core ideas

- **Message**：agent 间显式传递的信息。
- **Shared observation**：多个 agent 直接获得相同环境信息。
- **Bandwidth/latency**：通信不是免费且即时的。
- **Common knowledge**：大家知道且知道别人也知道的信息。

## Key theory

通信的作用通常是弥补局部观测、共享意图或同步状态，但**不是协调的唯一来源**：共享观测、公共信号、预先约定也可以支持协调。

工程设计先问三件事：消息是否必要？频率多高？延迟/丢包后系统是否还能退化运行？

## Representative methods

- Event-driven messaging：有变化再发。
- Publish-subscribe：解耦发送者与接收者。

## Worked example

多车共享“我正在去目标 X”比持续广播完整传感器流便宜得多，却可能已经足够避免重复分配。

## Connections

- → Distributed Systems：提供网络、pub-sub、容错机制。
- → MARL：通信可以作为策略网络的一部分。

## Further Reading

- Learned / emergent communication、information bottleneck。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Cooperation, Competition & Coordination](02-coordination.md) · [Task Allocation & Distributed Decision Making →](04-allocation-distributed-decision.md)
