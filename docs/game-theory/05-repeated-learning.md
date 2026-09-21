# Repeated Games & Learning in Games

> **Section:** Game Theory

## Why it matters

当博弈反复发生，策略不仅取决于当前收益，也取决于历史、信誉和对其他参与者的学习。

## Core ideas

- **Repeated game**：同一类交互多次发生。
- **History-dependent strategy**：当前动作依赖过去行为。
- **Reputation**：历史行为影响未来对手反应。
- **Learning dynamics**：玩家不知道最优策略时通过互动调整。

## Key theory

重复交互让“今天的收益”与“未来后果”绑定。长期收益常写为

$$
\sum_{t=0}^{\infty}\delta^t u_i(a_t),\quad \delta\in[0,1).
$$

当未来足够重要时，合作可能比一次性背叛更有吸引力，但具体结论依赖博弈和策略空间。

## Representative methods

- Tit-for-Tat：直观的条件合作策略。
- Fictitious play / no-regret learning：根据历史对手行为调整。

## Worked example

若两车每天都要共享狭窄通道，一次强抢虽然获利，但可能导致对方以后拒绝让行；重复关系改变了短期最优。

## Connections

- → MARL：学习算法会产生动态博弈过程。
- → MAS Coordination：声誉与长期互动可支持协作。

## Further Reading

- Folk theorem、PSRO、evolutionary games。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Sequential & Bayesian Games](04-sequential-bayesian.md)
