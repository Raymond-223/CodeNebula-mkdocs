# Software Engineering

> **定位：** 软件工程部分只保留科研/机器人项目真正需要的能力：把需求变成架构，用稳定接口拆模块，用版本与测试管理变化，最后可靠交付。

<figure markdown="span">
  ![Software Engineering learning map](../assets/diagrams/software-map.svg)
  <figcaption>Software Engineering 的最小主学习路径；箭头表示认知依赖，不代表必须掌握所有高级分支。</figcaption>
</figure>

## What to master

学完本 Section，只要求做到三件事：

1. 能用自己的话解释本领域的核心问题；
2. 能读懂最关键的公式、流程或系统结构；
3. 能把概念连接到一个简单实现或真实系统。

## Core chapters

| No. | Chapter | Why it stays in the core path |
|---:|---|---|
| 01 | [Requirements & Architecture](01-requirements-architecture.md) | 需求定义“系统必须做到什么”，架构定义“由哪些边界清晰的部分共同做到”；这两个阶段不应割裂。 |
| 02 | [Modular Design & APIs](02-modular-apis.md) | 模块化的重点不是文件夹整齐，而是让职责、依赖和数据契约可以单独理解、测试和替换。 |
| 03 | [Version Control](03-version-control.md) | 版本控制不是备份工具，而是让变更可追踪、可评审、可回滚，并为并行协作提供共同历史。 |
| 04 | [Testing & Debugging](04-testing-debugging.md) | 测试提供可重复证据，调试则通过复现、观测和假设逐步定位根因；二者应形成闭环。 |
| 05 | [Containers, Deployment & Reliability](05-deployment-reliability.md) | 交付不仅是“能启动”，还包括依赖隔离、配置管理、健康检查、日志监控和故障后的恢复能力。 |

## Stop rule

当你能够解释上述主线并完成每章的 Worked example，就可以进入下一个 Section。高级证明、算法变体和工具细节统一放在 **Further Reading**，不阻塞主线。
