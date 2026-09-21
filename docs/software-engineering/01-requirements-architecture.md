# Requirements & Architecture

> **Section:** Software Engineering

## Why it matters

需求定义“系统必须做到什么”，架构定义“由哪些边界清晰的部分共同做到”；这两个阶段不应割裂。

## Visual intuition

<figure markdown="span">
  ![从需求到模块边界，再到接口、实现和测试，是软件设计最短闭环。](../assets/diagrams/software-architecture.svg)
  <figcaption>从需求到模块边界，再到接口、实现和测试，是软件设计最短闭环。</figcaption>
</figure>

## Core ideas

- **Requirement**：可验证地说明系统要做什么以及有哪些约束。
- **Acceptance criteria**：明确怎样判断需求已经完成。
- **Component**：把系统拆成职责清晰的模块。
- **Dependency / boundary**：明确模块依赖、数据接口和故障传播边界。
- **Trade-off**：架构选择需要在复杂度、性能与可靠性之间权衡。

## Key theory

### Requirements & System Design

需求不是愿望清单。一个可执行需求应尽量包含**输入、输出、边界条件、失败行为和验收方式**。系统设计则把需求映射为组件、数据流和接口。

先定义契约，再选择框架；否则很容易把技术栈当成需求本身。

### Software Architecture

好架构的核心是**高内聚、低耦合、清晰边界、可替换依赖**。单体、分层、事件驱动、微服务都只是结构选择，不存在天然“更先进”的形式。

## Representative methods

- Acceptance criteria：把需求写成可验证条件。
- Architecture sketch：画组件、数据流和故障边界。
- Layered / event-driven：两种常见组织方式，按依赖和消息流选择。

## Worked example

**Requirements & System Design：**“系统要实时”不可验收；“控制指令端到端 P95 延迟 < 100 ms，超时进入停车模式”才是可测试的工程要求。

**Software Architecture：**一个科研系统若只有三名开发者、单机部署，却拆成 20 个微服务，通常增加的是部署和调试成本，而不是可维护性。

## Connections

- → Deployment & Reliability：架构决定系统能否被稳定部署、观测和恢复。
- → Distributed Systems：跨进程边界会引入网络、时延与一致性约束。
- → MAS：agent 架构与软件架构是不同层次。

## Further Reading

- Formal specification、DDD、hexagonal architecture。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Modular Design & APIs →](02-modular-apis.md)
