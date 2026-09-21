# Distributed Systems, Time & Asynchrony

> **Section:** Distributed Systems & Networking

## Why it matters

分布式系统的根本难点不是“机器多”，而是没有统一时钟、消息有延迟、节点可能独立失败。

<figure markdown="span">
  ![多源数据通常依靠时间戳和缓冲区近似对齐，而不是等待所有消息严格同时到达。](../assets/diagrams/time-alignment.svg)
  <figcaption>工程上更常见的是“按时间戳对齐一个窗口”，而不是假设存在完美全局时钟。</figcaption>
</figure>

## Core ideas

- **Partial failure**：某些节点或链路异常时，其他部分仍可能继续运行。
- **No global clock**：不同节点的时间不能假设完全一致。
- **Concurrency / ordering**：事件可能并发发生，观察到的顺序不唯一。
- **Synchronous vs asynchronous**：等待统一节奏更易推理，独立推进更符合真实网络。
- **Timeout**：只是“等待超过阈值”的工程信号，不等价于对方确定失效。

## Key theory

### Distributed Systems

单机失败通常是“程序停了”；分布式系统更麻烦的是**一部分正常、一部分超时、一部分消息还在路上**。因此超时不能简单等于“对方一定死了”。

### Synchronization & Asynchrony

异步系统更符合真实网络，但需要显式处理消息晚到、重复和乱序。同步结构更容易推理，但可能被最慢节点拖住。

## Representative methods

- Idempotency：重复请求不应产生重复副作用。
- Sequence number：识别旧消息。
- Timestamp + buffer：对齐异步数据。

## Worked example

**Distributed Systems：**给机器人发送“增加速度 0.1”若因重试执行两次会出错；改为“将速度设为 0.5”更容易设计成幂等命令。

**Synchronization & Asynchrony：**相机 30 Hz、LiDAR 10 Hz、IMU 200 Hz，不可能要求所有传感器每次严格同时到达；通常用时间戳和缓冲区近似对齐。

## Connections

- → Fault Tolerance。
- → Software Engineering / APIs。
- → Perception / Multi-Modal：时间同步是融合前提。
- → Control：控制环对延迟尤其敏感。

## Further Reading

- Replication/partitioning、logical clocks、backpressure、real-time scheduling。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Networks & Message Passing](01-network-messaging.md) · [Consistency & Distributed State →](03-consistency-state.md)
