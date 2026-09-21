# Robotics

> **定位：** 机器人部分只保留实体系统闭环：坐标与运动、传感与状态估计、地图、规划、导航控制。具体传感器和算法都挂在这条链上。

<figure markdown="span">
  ![Robotics learning map](../assets/diagrams/robotics-map.svg)
  <figcaption>Robotics 的最小主学习路径；箭头表示认知依赖，不代表必须掌握所有高级分支。</figcaption>
</figure>

## What to master

学完本 Section，只要求做到三件事：

1. 能用自己的话解释本领域的核心问题；
2. 能读懂最关键的公式、流程或系统结构；
3. 能把概念连接到一个简单实现或真实系统。

## Core chapters

| No. | Chapter | Why it stays in the core path |
|---:|---|---|
| 01 | [Robot Models, Kinematics & Dynamics](01-models-kinematics-dynamics.md) | 坐标系解决“在哪里”，运动学解决“怎么动”，动力学解决“为什么这样动”。 |
| 02 | [Sensors & State Estimation](02-sensing-estimation.md) | 传感器给出带噪测量，状态估计把多源测量和运动模型融合成可用于控制的位姿与速度估计。 |
| 03 | [Mapping & SLAM](03-mapping-slam.md) | 建图回答“环境长什么样”，定位回答“我在哪里”；SLAM 把两者耦合起来共同估计。 |
| 04 | [Path & Motion Planning](04-path-motion-planning.md) | 规划的最小区分是：路径只关心几何可达，运动规划还要考虑机器人动力学、时间和碰撞约束。 |
| 05 | [Navigation & Robot Control](05-navigation-control.md) | 导航不是某一个算法，而是定位、地图、规划、局部避障和控制形成的闭环系统。 |

## Stop rule

当你能够解释上述主线并完成每章的 Worked example，就可以进入下一个 Section。高级证明、算法变体和工具细节统一放在 **Further Reading**，不阻塞主线。
