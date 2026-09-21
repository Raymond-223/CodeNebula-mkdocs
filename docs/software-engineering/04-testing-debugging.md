# Testing & Debugging

> **Section:** Software Engineering

## Why it matters

测试提供可重复证据，调试则通过复现、观测和假设逐步定位根因；二者应形成闭环。

## Visual intuition

<figure markdown="span">
  ![调试闭环从复现开始，以回归测试结束。](../assets/diagrams/debugging-loop.svg)
  <figcaption>不要边猜边改；先稳定复现，再缩小范围、验证假设，并留下回归测试。</figcaption>
</figure>

## Core ideas

- **Unit test**：验证小模块。
- **Integration test**：验证模块之间的真实接口。
- **Regression test**：防止修过的问题再次出现。
- **Observability**：日志、指标、追踪帮助解释系统行为。

## Key theory

调试主线应是

**Reproduce → Minimize → Observe → Hypothesize → Verify → Add regression test**。

测试覆盖率不是质量本身；关键路径、边界条件和失败模式比追求一个百分比更重要。

## Representative methods

- Unit tests：纯函数/算法。
- Integration tests：数据库、ROS topic、网络接口。
- Fault injection：验证超时、断连、异常输入。

## Minimal code

好的测试应针对可观察行为和边界条件，而不是把内部实现细节写死。

```python
def stopping_distance(v, decel):
    return v * v / (2 * decel)

def test_stopping_distance():
    assert stopping_distance(10.0, 5.0) == 10.0
```

## Worked example

机器人偶发不动时，先固定输入和日志复现，再判断是规划没输出、消息没到、还是控制器拒绝执行；不要同时改三个模块。

## Connections

- → Robustness & Safety：故障注入与安全验证。
- → Distributed Systems：超时和重试必须测试。

## Further Reading

- Property-based testing、fuzzing。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Version Control](03-version-control.md) · [Containers, Deployment & Reliability →](05-deployment-reliability.md)
