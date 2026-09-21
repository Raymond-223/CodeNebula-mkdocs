# Distributed Systems & Networking

> **定位：** 系统部分不深入完整网络协议栈，只保留多机器人/多节点最常用的通信模型、时间与并发、共享状态、容错和 DDS/ROS2 中间件。

<figure markdown="span">
  ![Distributed Systems & Networking learning map](../assets/diagrams/distributed-map.svg)
  <figcaption>Distributed Systems & Networking 的最小主学习路径；箭头表示认知依赖，不代表必须掌握所有高级分支。</figcaption>
</figure>

## What to master

学完本 Section，只要求做到三件事：

1. 能用自己的话解释本领域的核心问题；
2. 能读懂最关键的公式、流程或系统结构；
3. 能把概念连接到一个简单实现或真实系统。

## Core chapters

| No. | Chapter | Why it stays in the core path |
|---:|---|---|
| 01 | [Networks & Message Passing](01-network-messaging.md) | 先理解 TCP/UDP 等传输差异，再理解请求-响应和发布-订阅等消息模式，才能正确设计节点之间的接口。 |
| 02 | [Distributed Systems, Time & Asynchrony](02-distributed-time.md) | 分布式系统的根本难点不是“机器多”，而是没有统一时钟、消息有延迟、节点可能独立失败。 |
| 03 | [Consistency & Distributed State](03-consistency-state.md) | 多个节点拥有同一对象的副本后，必须定义更新顺序、冲突处理和“何时算一致”。 |
| 04 | [Fault Tolerance](04-fault-tolerance.md) | 容错不是让故障消失，而是提前规定检测、隔离、降级、重试和恢复后的系统行为。 |
| 05 | [Middleware: DDS & ROS2](05-middleware-ros2-dds.md) | 中间件把发现、序列化、传输、QoS 和接口抽象封装起来，让应用代码聚焦于数据和任务。 |

## Stop rule

当你能够解释上述主线并完成每章的 Worked example，就可以进入下一个 Section。高级证明、算法变体和工具细节统一放在 **Further Reading**，不阻塞主线。
