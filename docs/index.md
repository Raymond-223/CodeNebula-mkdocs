# CodeNebula — 智能系统研究与工程实践知识地图

CodeNebula 不是 AI 编程入门站，也不试图成为包罗万象的百科全书。它是一套面向智能系统研究与工程实践的**最小充分知识地图**：先回答方法为什么成立，再说明算法如何组织，最后进入工程接口与真实系统。

<figure markdown="span">
  ![CodeNebula minimum sufficient knowledge map](assets/diagrams/knowledge-map.svg)
  <figcaption>学习路径从数学解释出发，经过理论与算法，最终落到工程实现和真实系统。</figcaption>
</figure>

## 阅读主线

$$
\text{数学}\longrightarrow\text{理论方法}\longrightarrow\text{算法理解}
\longrightarrow\text{工程实现}\longrightarrow\text{真实系统}
$$

### 数学：为什么这些方法成立

线性代数、微积分、数值计算、概率、Bayes、Markov 过程和优化用于解释空间、变化、不确定性、递推与最优性。这里不提供 Python 数值库或调参教程。

### 理论方法：问题应该怎样被描述

博弈论、多智能体系统和控制理论定义收益、信息、反馈、稳定性与约束。理论页使用公式、关系图和模型边界，不承担工程实现教学。

### 算法理解：更新规则怎样连接概念

强化学习用 Bellman 关系、TD error、策略梯度等公式级伪代码解释“当前估计、目标值和更新方向”，避免把算法章节变成某个框架的使用手册。

### 工程实现：代码只解决接口与系统问题

Robotics、Perception、Distributed Systems 和 Software Engineering 保留必要代码：坐标变换、PID 循环、路径规划、图像与点云处理、推理接口、TCP/UDP、Pub/Sub、ROS2、API、pytest、Docker 与 CI。

### 真实系统：面对误差、故障和现实差距

Simulation & Sim2Real、Robustness & Safety、Human–AI Interaction 处理部署后才会暴露的问题：仿真和现实不一致、环境分布变化、组件故障、安全边界，以及人类如何监督、共享控制并在必要时接管。

!!! note "内容边界"
    每个 Section 只保留能连接上下游的核心概念。代码只出现在工程实现与真实系统；图片优先使用几何解释图、状态空间图、概率关系图、优化曲面图、架构图、数据流图、系统连接图和实验结果图。
