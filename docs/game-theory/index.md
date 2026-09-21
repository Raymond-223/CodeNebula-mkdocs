# Game Theory

> **定位：** 博弈论只保留一条完整主线：先定义参与者、策略和收益，再学习均衡，之后看零和、顺序/信息结构以及重复交互。

<figure markdown="span">
  ![Game Theory learning map](../assets/diagrams/game-map.svg)
  <figcaption>Game Theory 的最小主学习路径；箭头表示认知依赖，不代表必须掌握所有高级分支。</figcaption>
</figure>

## What to master

学完本 Section，只要求做到三件事：

1. 能用自己的话解释本领域的核心问题；
2. 能读懂最关键的公式、流程或系统结构；
3. 能把概念连接到一个简单实现或真实系统。

## Core chapters

| No. | Chapter | Why it stays in the core path |
|---:|---|---|
| 01 | [Game Models & Classification](01-game-models.md) | 先学会把问题写成“谁参与、能做什么、得到什么”，再区分合作/非合作、零和/一般和、静态/动态等结构。 |
| 02 | [Best Response & Nash Equilibrium](02-best-response-nash.md) | 最佳响应回答“别人不变时我怎么选”，Nash 均衡则要求所有人的策略同时互为最佳响应。 |
| 03 | [Zero-Sum & Minimax](03-zero-sum-minimax.md) | 零和博弈把竞争压缩成一个共同价值，minimax 则给出面对最强对手时的保守决策原则。 |
| 04 | [Sequential & Bayesian Games](04-sequential-bayesian.md) | 同时行动、完全信息是最简单情形；一旦行动有先后或信息不完整，就必须把时间顺序和信念纳入策略。 |
| 05 | [Repeated Games & Learning in Games](05-repeated-learning.md) | 当博弈反复发生，策略不仅取决于当前收益，也取决于历史、信誉和对其他参与者的学习。 |

## Stop rule

当你能够解释上述主线并完成每章的 Worked example，就可以进入下一个 Section。高级证明、算法变体和工具细节统一放在 **Further Reading**，不阻塞主线。
