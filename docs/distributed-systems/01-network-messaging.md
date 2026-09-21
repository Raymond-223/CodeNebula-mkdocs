# Networks & Message Passing

> **Section:** Distributed Systems & Networking

## Why it matters

先理解 TCP/UDP 等传输差异，再理解请求-响应和发布-订阅等消息模式，才能正确设计节点之间的接口。

## Visual intuition

<figure markdown="span">
  ![请求—响应适合明确服务调用，发布—订阅适合松耦合的数据流。](../assets/diagrams/pubsub.svg)
  <figcaption>请求—响应适合明确服务调用，发布—订阅适合松耦合的数据流。</figcaption>
</figure>

## Core ideas

- **Latency / bandwidth / loss**：网络有时延、容量上限和丢包，不应被当成理想总线。
- **TCP vs UDP**：理解可靠有序字节流与低开销数据报的基本差异。
- **Request-response**：适合明确的一次调用。
- **Publish-subscribe**：适合连续数据流和松耦合广播。
- **Topic / message contract**：消息需要按语义和数据契约组织。

## Key theory

### Network Communication Basics

分布式程序必须默认存在延迟、重传、乱序和断连。TCP 提供可靠有序字节流，但不保证应用消息边界；UDP 保留数据报边界但不保证交付。

### Message Passing & Publish-Subscribe

机器人系统常用 pub-sub 处理连续状态流，用 request/service 处理一次性查询，用 action/task 处理有进度和可取消的长任务。接口语义应跟交互模式一致。

## Representative methods

- TCP / UDP：理解可靠性、时延和丢包之间的基本取舍。
- Pub-sub：传感器和状态流。
- Service / action：一次性查询与长时间任务。

## Worked example

**Network Communication Basics：**激光雷达 10 Hz 流偶尔丢一帧通常比“等待重传导致整条链路阻塞”更可接受；任务指令则通常不能静默丢失。

**Message Passing & Publish-Subscribe：**相机图像适合 topic；“保存地图”适合 service；“导航到目标点”需要进度、取消和最终结果，更适合 action。

## Connections

- → Middleware / DDS / ROS2：把消息模式落实成可配置的数据接口。
- → MAS Communication：传输机制与协作协议是不同层次，协议选择要服务于信息需求。

## Further Reading

- QUIC、拥塞控制、message broker internals。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Distributed Systems, Time & Asynchrony →](02-distributed-time.md)
