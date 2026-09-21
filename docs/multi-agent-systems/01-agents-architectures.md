# Agents & Architectures

> **Section:** Multi-Agent Systems

## Why it matters

“Agent 是什么”和“Agent 内部怎么组织决策”本质上是同一个入口问题，因此合并为一章。

## Visual intuition

<figure markdown="span">
  ![Agent 之间的边可以代表通信、共同观测或任务依赖；MAS 的难点来自这些耦合。](../assets/diagrams/mas-network.svg)
  <figcaption>Agent 之间的边可以代表通信、共同观测或任务依赖；MAS 的难点来自这些耦合。</figcaption>
</figure>

## Core ideas

- **Agent & environment**：主体感知环境并通过动作实现目标。
- **Interaction / joint action**：多个主体的结果依赖彼此行为。
- **Reactive**：观测直接映射到动作，响应快。
- **Deliberative**：维护模型/目标并规划。
- **Hybrid**：低层快速反应 + 高层规划，是常见工程结构。
- **State / memory**：在需要历史信息时保留内部状态。

## Key theory

### Agents & Multi-Agent Systems

单智能体中环境动力学常被视为固定；多智能体中，其他 agent 也在决策和学习，因此同一动作的结果会依赖联合策略。

动态多智能体决策常用 Markov Game：

$$
(\mathcal N,\mathcal S,\{\mathcal A_i\},P,\{\mathcal R_i\},\gamma).
$$

### Agent Architectures

架构选择本质上是**响应速度、模型复杂度与规划深度**之间的权衡。没有一种架构对所有 agent 都最好。

机器人系统中常见混合结构：安全避障在低层快速执行，高层负责目标分解和路径规划。

## Representative methods

- Reactive：直接从观测到动作，适合低延迟响应。
- Deliberative：显式维护目标/模型并规划。
- Hybrid：低层快速响应，高层负责规划与任务。

## Worked example

**Agents & Multi-Agent Systems：**三个机器人搬箱子：单个机器人能否移动并不只取决于自己的动作，还取决于另外两台是否同步施力。问题已经不是“单体规划复制三份”。

**Agent Architectures：**遇到突然出现的人时，机器人不应等待高层规划器重新搜索整条路线；低层先刹停，高层再重新规划。

## Connections

- ← Game Theory：提供收益与稳定性语言。
- → Control Theory：低层控制负责快速稳定。
- → Software Engineering：模块边界与接口影响 agent 可维护性。

## Further Reading

- BDI、Dec-POMDP、LLM-agent orchestration。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Cooperation, Competition & Coordination →](02-coordination.md)
