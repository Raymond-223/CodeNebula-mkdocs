# Modular Design & APIs

> **Section:** Software Engineering

## Why it matters

模块化的重点不是文件夹整齐，而是让职责、依赖和数据契约可以单独理解、测试和替换。

## Visual intuition

<figure markdown="span">
  ![API contract 要同时定义数据、单位、语义和失败行为。](../assets/diagrams/api-contract.svg)
  <figcaption>接口不是函数名；完整契约至少包含输入、输出、单位/坐标系以及错误语义。</figcaption>
</figure>

## Core ideas

- **Module**：对外暴露有限能力、内部隐藏实现。
- **API contract**：输入、输出、错误与语义约定。
- **Coupling**：模块间相互依赖程度。
- **Compatibility**：接口升级后旧调用方是否还能工作。

## Key theory

模块化的重点不是“文件拆得多”，而是让调用方只依赖必要抽象。API 应明确：类型、单位、坐标系、时间戳、错误码和幂等语义。

## Representative methods

- Function/class API：进程内接口。
- Message/service API：跨进程接口。
- Schema/versioning：消息格式演进。

## Minimal code

工程代码可以先用简单的数据结构把单位和约束写进接口，而不是依赖调用者“默认知道”。

```python
from dataclasses import dataclass

@dataclass
class VelocityCommand:
    speed_mps: float
    timeout_ms: int = 100

    def validate(self):
        if not 0.0 <= self.speed_mps <= 2.0:
            raise ValueError("speed out of range")
```

## Worked example

`set_velocity(0.5)` 如果没有说明单位、坐标系和持续时间，就不是一个完整契约；`0.5 m/s in base frame until 100 ms timeout` 才更可执行。

## Connections

- → ROS2/DDS：消息类型也是 API。
- → Testing：接口契约直接生成测试边界。

## Further Reading

- API governance、semantic versioning details。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Requirements & Architecture](01-requirements-architecture.md) · [Version Control →](03-version-control.md)
