# CodeNebula — AI & Robotics Knowledge Map

> 目标不是收录最多，而是用尽可能少的核心知识建立完整的 AI、机器人与自主系统认知框架。

<figure markdown="span">
  ![CodeNebula minimum sufficient knowledge map](assets/diagrams/knowledge-map.svg)
  <figcaption>全站只保留五个知识域和十二个 Section；高级分支不进入主路径。</figcaption>
</figure>

## Learning philosophy

这版不再强制每个 Section 都有相同章节数，而遵循四个判断：

- **能合并就合并**：如果两个主题只有放在一起才能形成完整逻辑，就不拆成两个页面。
- **必须独立才独立**：状态估计、SLAM、规划这类会在后续反复被引用的能力节点保留独立章节。
- **代表方法只服务于理解**：Q-Learning、PPO、PID、LQR、A*、EKF 等用于建立方法直觉，不扩展成算法百科。
- **工程知识必须能落地**：涉及控制、机器人、网络、软件、仿真的地方保留少量短代码；数学则加入够用的数值计算，帮助理解公式如何真正运行。

## Knowledge map

| Domain | Section | Core question |
|---|---|---|
| **Foundations** | [Mathematics for Intelligent Systems](mathematics/index.md) | 如何描述不确定性、动态过程与优化？ |
| **Intelligent Systems** | [Reinforcement Learning](reinforcement-learning/index.md) | 智能体如何通过交互学习决策？ |
|  | [Game Theory](game-theory/index.md) | 多个策略主体相互影响时如何分析行为？ |
|  | [Multi-Agent Systems](multi-agent-systems/index.md) | 多个 Agent 如何组织、通信、分工与学习？ |
| **Robotics** | [Control Theory](control-theory/index.md) | 如何让动态系统稳定地达到目标？ |
|  | [Robotics](robotics/index.md) | 如何把建模、定位、规划和控制串成实体闭环？ |
|  | [Perception](perception/index.md) | 如何把图像和点云变成可用于决策的环境表示？ |
| **Systems** | [Distributed Systems & Networking](distributed-systems/index.md) | 多节点如何可靠通信、同步与容错？ |
|  | [Software Engineering](software-engineering/index.md) | 如何把算法变成可维护、可部署、可验证的软件？ |
| **Advanced Autonomous Systems** | [Simulation & Sim2Real](simulation-sim2real/index.md) | 如何让仿真与真实系统形成迭代闭环？ |
|  | [Robustness & Safety](robustness-safety/index.md) | 不确定、故障和风险下如何维持安全行为？ |
|  | [Human–AI Interaction](human-ai-interaction/index.md) | 人如何监督、共享控制并在必要时接管？ |

## Recommended order

**Mathematics → Reinforcement Learning / Game Theory → Multi-Agent Systems → Control / Robotics / Perception → Distributed Systems / Software Engineering → Simulation / Safety / Human–AI Interaction**

这不是严格先修图。第一次学习时只沿主线前进；遇到项目需求再从 Further Reading 回补。

## How to use the website

每章只保留必要模块：**Why it matters → Core ideas → Key theory → Representative methods → Worked example**。

数学基础额外保留一章 **Numerical Computation Essentials**，只覆盖有限精度、差分、线性求解、最小二乘、积分和迭代停止条件；不进入完整数值分析。

只有当代码能明显帮助理解“公式如何变成实现”时才加入 **Minimal code**；只有当空间结构、数据流或闭环关系用文字难以表达时才加入图。这样图片和代码都服务于理解，而不是装饰页面。
