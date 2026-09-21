# Sequential & Bayesian Games

> **Section:** Game Theory

## Why it matters

同时行动、完全信息是最简单情形；一旦行动有先后或信息不完整，就必须把时间顺序和信念纳入策略。

## Visual intuition

<figure markdown="span">
  ![顺序博弈需要把先后关系和可观察信息显式放进决策结构。](../assets/diagrams/game-tree.svg)
  <figcaption>顺序博弈需要把先后关系和可观察信息显式放进决策结构。</figcaption>
</figure>

## Core ideas

- **Extensive form / information set**：表示行动顺序以及玩家当时知道什么。
- **Backward induction**：在完全信息有限树上从终局倒推。
- **Stackelberg game**：领导者先承诺，跟随者随后回应。
- **Type & prior**：用私有类型和先验表示不完全信息。
- **Bayes-Nash equilibrium**：策略依赖类型时的最佳回应稳定点。

## Key theory

### Sequential Games

顺序改变策略空间：先行动者需要预测后行动者的最佳回应。Stackelberg 问题可写成

$$
\max_{a_L}u_L(a_L,BR_F(a_L)).
$$

它与同时行动 Nash 的解概念不同。

### Incomplete Information & Bayesian Games

Bayesian game 把收益写成 $u_i(a,\theta)$，玩家对未知类型按信念取期望。核心不是“猜对别人”，而是在给定信息结构下选择期望最优策略。

## Representative methods

- Backward induction：完全信息有限树。
- Leader-follower optimization：Stackelberg。
- Bayesian best response。

## Worked example

**Sequential Games：**两台机器人抢充电桩：若 A 先公布预约时间，B 再避开冲突，这是领导者—跟随者结构；若同时选时段，则是静态博弈。

**Incomplete Information & Bayesian Games：**车辆不知道对方是“激进”还是“保守”，只能根据先验和已观察行为更新判断，再决定是否让行。

## Connections

- → Control / planning：决策顺序也会形成树搜索。
- → Human-AI Interaction：人机协作中常出现 leader/follower 角色。
- ← Conditional Probability & Bayes。
- → MAS Communication：消息可能传递私有信息，也可能被策略性操纵。

## Further Reading

- Subgame perfect equilibrium、signaling games、mechanism design。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Zero-Sum & Minimax](03-zero-sum-minimax.md) · [Repeated Games & Learning in Games →](05-repeated-learning.md)
