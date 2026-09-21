# Safety Constraints

> **Section:** Robustness & Safety

## Why it matters

安全约束不是“希望系统表现好”，而是明确哪些状态、动作或风险水平不可越过。

## Core ideas

- **Hard constraint**：原则上不可违反。
- **Soft constraint**：可在代价中权衡。
- **Safe set**：允许系统状态所在的集合。
- **Safety margin**：与危险边界的余量。

## Key theory

仅给危险行为一个大负奖励，并不能保证学习策略永不违反安全条件。更清晰的建模是

$$
\max_\pi J(\pi)\quad\text{s.t.}\quad C(\pi)\le d,
$$

或直接定义状态/控制可行集。

## Representative methods

- Hard limits：速度、区域、温度等直接工程约束。
- Safety filter / constrained optimization：在执行前过滤不安全动作。

## Worked example

移动机器人可以允许规划器自由优化时间，但最终速度命令必须通过速度上限和碰撞距离检查。

## Connections

- → Control / MPC。
- → Safe RL。

## Further Reading

- Control barrier functions、formal reachability。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Robustness, Risk & Reliability](02-robustness-risk.md) · [Fault Detection & Fault Tolerance →](04-fault-tolerance.md)
