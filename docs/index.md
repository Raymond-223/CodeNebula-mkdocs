# CodeNebula — 技术知识体系

> 一个面向专业开发者与自学者的系统性技术知识库。覆盖从底层原理到工程实践的完整技术栈。
> 目前包含三大板块：**软件开发** · **强化学习** · **多智能体系统**。

---

## 章节目录

### 软件开发

| 章节 | 核心内容 |
|------|---------|
| [**概览**](./assets/software-development/index.md) | 软件工程全景、SDLC、技术栈选型、学习路径 |
| [**前端开发**](./assets/software-development/01-frontend.md) | HTML5/CSS3/JavaScript/TypeScript, React/Vue/Angular, 构建工具 |
| [**后端开发**](./assets/software-development/02-backend.md) | Python/Node.js/Java/Go/Rust 生态, 框架对比, API 设计 |
| [**数据库与存储**](./assets/software-development/03-database.md) | 关系型/非关系型数据库, SQL 进阶, ORM, 缓存, 存储引擎 |
| [**版本控制**](./assets/software-development/04-version-control.md) | Git 原理与工作流, 分支策略, 协作规范 |
| [**DevOps 与部署**](./assets/software-development/05-devops.md) | Docker/K8s, CI/CD 流水线, 云服务, 监控告警 |
| [**软件架构**](./assets/software-development/06-architecture.md) | 架构风格, 设计模式, 系统设计原则, 微服务 |
| [**测试与质量**](./assets/software-development/07-testing.md) | 测试金字塔, TDD/BDD, 代码审查, 重构 |
| [**安全基础**](./assets/software-development/08-security.md) | 认证授权, 加密体系, Web 安全, 安全编码 |

### 强化学习

| 章节 | 核心内容 |
|------|---------|
| [**概览**](./assets/reinforcement-learning/index.md) | 奖励假设、三大范式、探索与利用、技术全景、学习路径 |
| [**多臂老虎机**](./assets/reinforcement-learning/00-bandit.md) | 探索-利用、ε-greedy/UCB/Thompson 采样、遗憾界 |
| [**MDP 与数学基础**](./assets/reinforcement-learning/01-mdp-foundations.md) | 马尔可夫决策过程、贝尔曼方程、压缩映射与不动点 |
| [**动态规划**](./assets/reinforcement-learning/02-dynamic-programming.md) | 策略迭代、价值迭代、策略改进定理 |
| [**蒙特卡洛方法**](./assets/reinforcement-learning/03-monte-carlo-methods.md) | MC 预测与控制、重要性采样、MCTS |
| [**时序差分学习**](./assets/reinforcement-learning/04-temporal-difference.md) | TD 预测/控制、SARSA/Q-Learning、TD(λ) 与资格迹 |
| [**值函数逼近与 DQN**](./assets/reinforcement-learning/05-value-approximation.md) | 半梯度、死亡三角、经验回放、DQN 家族 |
| [**策略梯度与 Actor-Critic**](./assets/reinforcement-learning/06-policy-gradient.md) | 策略梯度定理、REINFORCE、A2C/PPO、TRPO |
| [**连续控制**](./assets/reinforcement-learning/07-continuous-control.md) | DDPG/TD3/SAC、最大熵框架 |
| [**环境与工具链**](./assets/reinforcement-learning/08-tools-environments.md) | Gymnasium、MuJoCo、训练框架与实验评估 |
| [**进阶专题**](./assets/reinforcement-learning/09-advanced-topics.md) | 模仿学习、Model-based、MARL、RLHF、离线 RL、探索机制 |
| [**工程实践**](./assets/reinforcement-learning/10-engineering-practice.md) | 环境设计、调试、训练稳定性、部署与收敛判据 |

### 多智能体系统

| 章节 | 核心内容 |
|------|---------|
| [**概览**](./assets/multi-agent-systems/index.md) | 设计哲学、五条研究路线、技术全景、学习路径 |
| [**系统基础**](./assets/multi-agent-systems/01-foundations.md) | MAS 定义与分类、与单智能体的本质差别、信息结构、解概念地图 |
| [**智能体架构**](./assets/multi-agent-systems/02-agent-architectures.md) | 反应式/慎思式/BDI、经典架构、现代 LLM Agent 架构 |
| [**博弈论基础**](./assets/multi-agent-systems/03-game-theory.md) | 正则型/扩展型/随机博弈、各类均衡、均衡求解算法 |
| [**机制设计与社会选择**](./assets/multi-agent-systems/04-mechanism-design.md) | 投票、拍卖与 VCG、稳定匹配、Shapley 值、声誉与信任 |
| [**多智能体强化学习**](./assets/multi-agent-systems/05-marl.md) | Markov Game、非平稳性、值分解、COMA、MADDPG/MAPPO、自博弈 |
| [**通信与协同**](./assets/multi-agent-systems/06-communication.md) | 通信协议、涌现语言、通信受限、MCP/A2A/FIPA-ACL |
| [**协调与协商**](./assets/multi-agent-systems/07-coordination-negotiation.md) | DCOP、任务分配、协商协议、分布式一致性、群体智能 |
| [**LLM 多智能体**](./assets/multi-agent-systems/08-llm-multi-agent.md) | 编排范式、框架对比、社会仿真、失败模式、何时该用 |
| [**工具与环境**](./assets/multi-agent-systems/09-tools-environments.md) | PettingZoo/MARLlib/SMAC、训练框架、评估指标与复现 |
| [**应用与前沿**](./assets/multi-agent-systems/10-applications-frontier.md) | 应用地图、异构群体智能、可扩展性、多智能体安全与开放问题 |

---

## 目标读者

- **初学者**：想系统学习软件开发、构建完整知识体系
- **中级开发者**：需要查漏补缺、深入原理
- **算法与 AI 方向学习者**：想系统掌握强化学习、多智能体系统的理论与工程
- **转行者**：从零开始、需要清晰的学习路径

---

## 如何使用

按顺序阅读，或有针对性地选择章节。每章末尾有"下一章"链接。代码示例均为**可运行**的真实代码。

> 🚧 持续更新中。欢迎贡献内容。
