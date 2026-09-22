# 中间件、DDS 与 ROS2

机器人软件通常包含定位、感知、规划、控制和硬件驱动等多个进程。中间件的作用是让这些模块能够交换数据，而不要求每个模块自己重新实现发现、序列化、网络传输和通信质量控制。

<figure markdown="span">
  ![DDS/ROS2 的 QoS 需要根据数据语义选择。](../assets/diagrams/qos-choice.svg)
  <figcaption>高速传感器流和关键状态事件对可靠性、历史深度和时延的要求不同。</figcaption>
</figure>

## ROS2 把模块间通信抽象成几个基本原语

**Topic** 适合持续数据流，例如 `/odom`、`/scan`；**Service** 适合一次请求、一次响应；**Action** 适合耗时任务，需要反馈、取消和最终结果。

这三种接口反映的是交互时序差异，而不是“哪个更高级”。

## DDS 让通信语义可以被显式配置

ROS2 默认依赖 DDS/RTPS 体系。DDS 不只是传输数据，还提供 reliability、history、durability、deadline 等 QoS 语义。

高频 LiDAR 数据偶尔丢一帧通常可以接受，重点是最新数据尽快到达；任务模式切换则可能要求可靠送达。不同 Topic 使用同一 QoS 并不一定合理。

## QoS 兼容性检查

发布者和订阅者即使名字完全一致，如果 reliability 或 durability 等策略不兼容，也可能无法通信。这是 ROS2 实机调试中非常常见的问题。

因此排查顺序应包含：节点是否存在、Topic 名称/类型是否一致、QoS 是否兼容、网络发现是否正常。

## ROS2 消息仍然需要好的数据契约

中间件解决“怎么传”，不解决“字段语义是否合理”。一个状态消息应明确单位、坐标系、时间戳和有效范围。

```python
# Topic：持续发布带明确单位的速度命令
cmd = Twist()
cmd.linear.x = 0.4       # m/s
cmd.angular.z = -0.2     # rad/s
velocity_publisher.publish(cmd)

# Service：一次请求、一次响应
future = reset_client.call_async(Trigger.Request())
future.add_done_callback(handle_reset_result)
```

若单位和 frame 没有统一，即使通信 100% 可靠，系统仍然会产生错误动作。

Topic 回调应快速处理持续数据；Service 适合有明确完成结果的短操作。耗时导航任务应使用 Action，以便反馈进度和取消，而不是让 Service 长时间阻塞。

## ROS2/DDS 的解耦边界

定位节点不需要知道规划器运行在哪台机器，规划器只需要订阅符合契约的位姿数据。但网络延迟、带宽和节点故障仍然存在，不能因为用了 ROS2 就假设通信等同于本地函数调用。

真正稳定的机器人系统会同时设计接口语义、QoS、超时和失联后的退化行为。

## QoS 要沿通信两端检查

ROS2 通信是否建立取决于发布端与订阅端策略是否兼容，而不是单边配置是否看起来合理。排查时应把消息类型、Topic 名称、reliability、durability、history 和 deadline 放在同一张表中比较，避免只在某个节点上反复改参数。
