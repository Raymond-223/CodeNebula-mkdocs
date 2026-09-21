# Trust & Explainability

> **Section:** Human–AI Interaction

## Why it matters

可解释性的目标不是让所有模型完全透明，而是给用户足够的信息来理解限制、判断置信度并做正确干预。

## Core ideas

- **Trust calibration**：人的信任应与系统真实能力匹配。
- **Uncertainty display**：显示系统是否不确定。
- **Rationale**：解释关键决策依据。
- **Limitations**：明确系统不能做什么。

## Key theory

目标不是最大化信任，而是避免**过度信任**与**完全不信任**。解释应优先回答用户行动所需的问题：现在发生了什么？为什么？风险是什么？我能做什么？

## Representative methods

- Confidence/context display：告诉人系统知道什么、不确定什么。
- Failure reason + next action：解释必须能支持下一步操作。

## Worked example

“规划失败”不够；界面显示“目标被动态禁区覆盖，已停止；可选择新目标或人工接管”才是可操作解释。

## Connections

- → Runtime Safety / alerts。
- → Software Engineering / observability。

## Further Reading

- XAI methods、trust measurement studies。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Shared Autonomy](03-shared-autonomy.md) · [Intervention & Takeover →](05-intervention-takeover.md)
