# Consistency & Distributed State

> **Section:** Distributed Systems & Networking

## Why it matters

多个节点拥有同一对象的副本后，必须定义更新顺序、冲突处理和“何时算一致”。

## Visual intuition

<figure markdown="span">
  ![副本越多，状态同步就越需要明确顺序、延迟与冲突解决规则。](../assets/diagrams/consistency-flow.svg)
  <figcaption>副本越多，状态同步就越需要明确顺序、延迟与冲突解决规则。</figcaption>
</figure>

## Core ideas

- **Strong consistency**：读操作看到满足严格一致语义的状态。
- **Eventual consistency**：没有新更新时副本最终趋于一致。
- **Conflict**：并发更新可能互相覆盖。
- **CAP context**：网络分区期间无法同时保证强一致语义与所有请求都可用。

## Key theory

一致性是**对读写行为的语义保证**，不是“数据有没有同步”。机器人任务状态、地图版本、资源所有权对一致性需求不同，不能统一用一种协议。

## Representative methods

- Single writer：最简单的冲突规避方式。
- Version / CAS：检测并发更新。

## Worked example

“当前急停状态”必须快速且明确；“累计统计日志”可以稍后最终一致。二者不应使用同一一致性要求。

## Connections

- → MAS Task Allocation：共享资源冲突必须有一致语义。
- → Fault Tolerance。

## Further Reading

- Linearizability、serializability、CRDT。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Distributed Systems, Time & Asynchrony](02-distributed-time.md) · [Fault Tolerance →](04-fault-tolerance.md)
