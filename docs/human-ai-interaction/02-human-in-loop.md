# Human-in-the-Loop

> **Section:** Human–AI Interaction

## Why it matters

人在环必须明确介入点、频率和权限：人适合处理目标、异常和价值判断，不适合逐毫秒审批低层控制量。

## Core ideas

- **Training feedback**：人在训练阶段标注、偏好或纠正。
- **Decision approval**：关键决策执行前由人确认。
- **Runtime correction**：运行中人修改目标/约束。
- **Escalation**：系统不确定时主动请求帮助。

## Key theory

“人在环”必须说明人在哪个环节、以什么频率、拥有何种权限。让人每 50 ms 审批控制量不现实；让人审批高层目标则可行。

## Representative methods

- Human approval gate：高风险决策前确认。
- Exception handling / escalation：系统不确定时主动交给人。

## Minimal code

HITL 的关键是把需要人的条件写成可执行策略，而不是简单增加一个“确认”按钮。

```python
def execute(plan, risk_score, approved=False):
    if risk_score < 0.3:
        return "auto_execute"
    if approved:
        return "human_approved_execute"
    return "pause_and_request_review"
```

## Worked example

任务规划器自动分配车辆；当需要进入禁区附近时，系统暂停并请求人确认，而低层避障仍自动运行。

## Connections

- → MAS / task allocation。
- → Software Engineering / requirements。

## Further Reading

- Preference feedback、RLHF、interactive imitation learning。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Human–AI Interaction & Automation Levels](01-human-ai-automation.md) · [Shared Autonomy →](03-shared-autonomy.md)
