# Cooperation, Competition & Coordination

> **Section:** Multi-Agent Systems

## Why it matters

多主体的核心困难是彼此行为会改变环境。先区分合作、竞争与混合关系，再讨论协调目标。

## Core ideas

- **Cooperation**：主体目标高度一致。
- **Competition**：主体收益相反或存在资源冲突。
- **Mixed motives**：既合作又竞争。
- **Coordination**：让行动在时间、空间或资源上相容。

## Key theory

合作不等于自动协调。即使所有 agent 奖励相同，如果各自观测不同、通信受限、行动存在耦合，也可能发生冲突。

协调的核心是减少联合行动中的不一致，而不是强行追求完全相同的动作。

## Representative methods

- Role assignment：不同 agent 承担不同角色。
- Convention：预先约定冲突解决规则。
- Coordination signal：共享少量关键信息。

## Worked example

两台车都想帮助团队，但如果同时去搬同一个已经被拿走的物资，就会重复劳动；问题是协调，不是“缺乏合作意愿”。

## Connections

- ← Game Theory / classification。
- → Communication、Task Allocation。

## Further Reading

- Coalition formation、mechanism design。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Agents & Architectures](01-agents-architectures.md) · [Communication & Information Sharing →](03-communication.md)
