# Zero-Sum & Minimax

> **Section:** Game Theory

## Why it matters

零和博弈把竞争压缩成一个共同价值，minimax 则给出面对最强对手时的保守决策原则。

## Core ideas

- **Zero-sum**：$u_1=-u_2$。
- **Maximin**：选择能保证最低收益最高的策略。
- **Minimax**：对手最小化你的最大收益。
- **Saddle point**：双方都没有单边改进空间的对抗平衡。

## Key theory

有限两人零和博弈满足 minimax 定理：

$$
\max_{\sigma_1}\min_{\sigma_2}u(\sigma_1,\sigma_2)
=
\min_{\sigma_2}\max_{\sigma_1}u(\sigma_1,\sigma_2).
$$

这个结论依赖零和结构，不能直接推广到一般和博弈。

## Representative methods

- Maximin / minimax reasoning：先理解最坏情况下的保证。
- Self-play：用对抗数据逐步改进策略。

## Worked example

守门员与点球手可以近似零和：一方希望扑到，另一方希望进球。双方随机化方向可以防止被对手利用固定模式。

## Connections

- → Robust Optimization：minimax 形式与最坏情况优化相似。
- → MARL：self-play 常用于竞争学习。

## Further Reading

- Linear-programming solution、exploitability、fictitious play。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Best Response & Nash Equilibrium](02-best-response-nash.md) · [Sequential & Bayesian Games →](04-sequential-bayesian.md)
