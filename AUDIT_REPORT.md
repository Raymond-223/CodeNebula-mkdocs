# CodeNebula V6 — Theory-to-System Content Audit

## 1. 本轮修正目标

V6 的目标重新定义为“面向智能系统研究与工程实践的知识地图”，而不是 AI 编程入门网站。内容依赖链为：

```text
数学 → 理论方法 → 算法理解 → 工程实现 → 真实系统
```

代码归属执行以下约束：

- Mathematics、Game Theory、Reinforcement Learning、Multi-Agent Systems 与 Control Theory 不含可执行代码；
- RL 使用公式级更新规则，明确当前估计、目标值与更新方向；
- Robotics、Perception、Distributed Systems、Software Engineering 与 Simulation 承担工程示例；
- 图片用于几何关系、状态空间、概率/优化关系、架构、数据流和系统连接，不使用代码或软件界面截图。

## 2. 当前规模

- **12 Sections** / 5 learning domains
- **61 core chapters**
- **74 Markdown pages**
- **47 local SVG teaching diagrams**
- 理论层可执行代码块为 **0**
- 顶部与左侧导航全部使用英文，正文保持中文；五个领域为 Foundations、Decision & Learning、Robotics & Perception、Systems & Simulation、Safety & Human Factors

## 3. 逐 Section 复核结果

### Mathematics for Intelligent Systems

保留线性代数/微积分、数值计算、概率、Bayes、Markov、优化六个节点。重点解释负梯度、局部/全局最优、Lagrange multiplier、离散化、误差来源和稳定性，不再出现 NumPy 或工具调用。

### Reinforcement Learning

保留 MDP/Bellman、Value-Based、Policy/Actor-Critic、探索与部分可观测、Model-Based vs Model-Free、安全/鲁棒/离线 RL。实现片段已改为数学更新式与算法关系，不依赖 PyTorch 或训练框架。

### Game Theory

围绕参与者、策略、收益、信息、行动顺序与重复交互展开。收益矩阵改为数学表示，不包含求解器代码。

### Multi-Agent Systems

保留 Agent 架构、协调、通信、任务分配/分布式决策、MARL/CTDE。理论消息、任务触发和反应式策略均改为形式化描述，网络实现移到 Distributed Systems。

### Control Theory

保持建模与状态空间 → 反馈与稳定性 → PID → LQR → MPC 的连续逻辑。离散更新和 PID 的可执行实现移到 Robotics，理论页只解释机制与成立条件。

### Robotics

保留坐标变换、差速运动、状态估计、A*、PID 控制循环等小型工程例子，并明确坐标系、单位、时间戳与执行器边界。

### Perception

保留图像读取与预处理、投影/反投影、点云处理流程和模型推理接口。代码围绕稳定的数据契约，不扩展为框架教程。

### Distributed Systems & Networking

保留 TCP/UDP、Pub/Sub、版本更新、退避容错、ROS2 Topic/Service 与 DDS QoS。实现服务于通信语义，不扩展 Raft/Paxos/CRDT。

### Software Engineering

只保留需求/架构、模块/API、Git、pytest、Docker、CI 与必要调试示例，不继续扩展企业级工具清单。

### Simulation & Sim2Real

保留物理推进、MuJoCo/Gazebo 抽象交互循环、传感器模拟接口、Reality Gap/随机化和 Sim2Real/Real2Sim 闭环。

### Robustness & Safety

按不确定性/分布偏移 → 风险/可靠性 → 安全约束 → 故障处理 → Runtime Safety 展开，强调条件、指标和退化模式。

### Human–AI Interaction

只保留自动化权限、人机在环、共享自治、信任/解释、干预/接管，重点解释控制权与安全交接。

## 4. 图片与代码策略

图片总量控制在 47 张，主要用于闭环、数据流、几何关系、系统架构和算法结构。Section 首页保留概念总图，正文只在可视化确实降低理解成本时使用。

工程代码覆盖坐标变换、PID 循环、ROS2 Topic/Service、A*、图像预处理、点云流程、推理接口、TCP/UDP、Pub/Sub、容错、API、pytest、Docker、CI、MuJoCo/Gazebo 抽象循环和传感器模拟。理论层不再使用可执行代码。

## 5. 最终静态验收

- 所有导航目标均存在且无孤立 Markdown 页面；
- 无失效旧交叉引用或同页重复图片；
- 无 LaTeX 控制字符损坏；
- 所有本地图片和页面链接均可解析；
- Python 示例通过语法解析；
- `mkdocs build --strict` 已在本机完整通过。
