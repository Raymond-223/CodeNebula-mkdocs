# Fault Tolerance

> **Section:** Distributed Systems & Networking

## Why it matters

容错不是让故障消失，而是提前规定检测、隔离、降级、重试和恢复后的系统行为。

## Core ideas

- **Fault**：部件出现异常。
- **Failure**：系统无法提供预期服务。
- **Redundancy**：通过副本/备份提高容错能力。
- **Graceful degradation**：失败后降低能力，而不是完全崩溃。

## Key theory

容错的基本链是

**Detect → Isolate → Recover / Reconfigure → Verify**。

心跳只能说明“最近是否收到消息”，不能区分节点宕机、网络分区或严重拥塞。

## Representative methods

- Heartbeat + timeout。
- Retry with idempotency。
- Failover / fallback mode。

## Minimal code

幂等命令让网络重试更安全：同一个 `command_id` 重复到达时，不重复产生副作用。

```python
executed = set()

def handle(command_id, action):
    if command_id in executed:
        return "duplicate ignored"
    action()
    executed.add(command_id)
    return "done"
```

## Worked example

高层规划节点失联时，底盘不应继续执行无限期旧指令；本地控制器可进入限速、停车或返航等预定义安全模式。

## Connections

- → Robustness & Safety / Fault Detection。
- → Human-AI Interaction / takeover。

## Further Reading

- Raft/Paxos、Byzantine fault tolerance。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Consistency & Distributed State](03-consistency-state.md) · [Middleware: DDS & ROS2 →](05-middleware-ros2-dds.md)
