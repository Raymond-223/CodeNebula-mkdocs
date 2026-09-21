# Task Allocation & Distributed Decision Making

> **Section:** Multi-Agent Systems

## Why it matters

多智能体协作最终要落到两个问题：**谁负责什么**，以及**每个 agent 在只掌握局部信息时怎样继续做决定**。把任务分配和分布式决策放在一起，更接近真实系统的工作链。

## Core ideas

- **Task / resource**：需要执行的工作与时间、能量、车辆、带宽等有限资源。
- **Assignment**：任务到 agent 的映射。
- **Cost / utility**：评估分配质量。
- **Local information**：每个 agent 只能访问部分状态。
- **Decentralized decision**：执行时不依赖中心节点实时给出每一步动作。
- **Consensus / coordination**：节点通过必要的信息交换减少冲突。

## Key theory

典型分配问题可以写成

$$
\min_x \sum_{i,j} c_{ij}x_{ij},
$$

再加上“一个任务只能分给允许的 agent”“资源不能超限”等约束。真正部署后，即使初始分配来自中心节点，每个 agent 仍要面对延迟、局部观测和任务变化，因此需要本地决策和有限通信。

主线原则是：**中心化便于使用全局信息，分布式执行提高扩展性与故障隔离；二者可以组合，而不是二选一。**

## Representative methods

- Centralized assignment：信息充分、规模较小时最直接。
- Auction / bidding：用局部成本或效用做分配。
- Local policy + shared state：分配后由各 agent 本地执行并共享必要状态。

## Minimal code

这个贪心例子只帮助理解“任务—资源—代价”的结构，不代表真实系统的最优算法。

```python
tasks = {"T1": 4, "T2": 7, "T3": 2}
agents = {"A1": 0, "A2": 0}

for task, load in sorted(tasks.items(), key=lambda x: -x[1]):
    agent = min(agents, key=agents.get)
    agents[agent] += load
    print(task, "->", agent)
```

## Worked example

三台机器人抢占多个目标点时，可先根据距离、剩余电量和能力分配任务；执行过程中，每台车只交换目标占用状态和邻车位置，局部重规划即可，不必持续上传全部原始传感器。

## Connections

- → Optimization：分配问题通常是约束组合优化。
- → Distributed Systems：消息延迟、一致性和故障会改变可执行策略。
- → Robotics：分配完成后进入单车规划与控制。
- → MARL：学习方法可以替代部分人工规则，但不会消除通信与执行约束。

## Further Reading

- Hungarian algorithm、DCOP、CBBA、distributed MPC。

> 主学习路径只要求分清“全局分配”和“局部执行”两个层次。

## Learning path

[← Section overview](index.md) · [← Communication & Information Sharing](03-communication.md) · [Multi-Agent Learning & CTDE →](05-multi-agent-learning.md)
