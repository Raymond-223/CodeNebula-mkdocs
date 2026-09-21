# Game Models & Classification

> **Section:** Game Theory

## Why it matters

先学会把问题写成“谁参与、能做什么、得到什么”，再区分合作/非合作、零和/一般和、静态/动态等结构。

## Core ideas

- **Player / action / strategy**：谁做决策，以及一次选择和完整决策规则分别是什么。
- **Payoff**：玩家如何评价联合结果。
- **Interest structure**：合作/非合作、零和/一般和描述目标关系。
- **Timing structure**：静态或动态决定是否存在行动顺序与历史。
- **Information structure**：完全/不完全信息决定玩家知道哪些关键参数。

## Key theory

### Games, Strategies & Payoffs

有限正则型博弈可写为

$$
G=(\mathcal N,\{\mathcal A_i\},\{u_i\}).
$$

其中 $u_i(\mathbf a)$ 取决于所有玩家的联合动作。博弈论的关键变化是：**你的最优动作取决于别人怎么做**。

### Game Classification

分类不是标签游戏，而是决定解法。零和博弈可用 minimax；一般和博弈往往需要 Nash 等稳定概念；动态博弈必须考虑历史与未来反应；不完全信息需要对未知类型建模。

## Representative methods

- Payoff matrix：两人有限博弈最直观表示。
- Mixed strategy：当确定动作不足以描述策略时，对动作分配概率。

## Worked example

**Games, Strategies & Payoffs：**剪刀石头布中不存在一个永远最好的纯动作；“最佳选择”取决于对手策略，因此需要混合策略。

**Game Classification：**两个机器人争同一资源且一方收益就是另一方损失，可近似零和；若两者既竞争资源又共享完成任务奖励，则是一般和。

## Connections

- → Multi-Agent Systems：把收益结构放进动态环境。
- → Reinforcement Learning：学习可以作为求策略的一种方式。
- → Game Theory 后续各章。
- → MAS：合作/竞争/混合任务的组织方式不同。

## Further Reading

- 严格支配、混合策略存在性证明。
- Potential games、congestion games。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Best Response & Nash Equilibrium →](02-best-response-nash.md)
