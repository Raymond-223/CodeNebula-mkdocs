# Mapping & SLAM

> **Section:** Robotics

## Why it matters

建图回答“环境长什么样”，定位回答“我在哪里”；SLAM 把两者耦合起来共同估计。

## Visual intuition

<figure markdown="span">
  ![SLAM 中位姿与地图互相依赖，回环检测用于纠正长期累计漂移。](../assets/diagrams/slam-loop.svg)
  <figcaption>SLAM 中位姿与地图互相依赖，回环检测用于纠正长期累计漂移。</figcaption>
</figure>

## Core ideas

- **Map**：环境的几何或语义表示。
- **Mapping**：已知/估计轨迹下构建地图。
- **SLAM**：轨迹和地图相互依赖，需要联合估计。
- **Loop closure**：再次到达旧地点时纠正累计漂移。

## Key theory

SLAM 的循环依赖是：位姿更准才能建好地图，地图更准又能反过来修正位姿。因此核心是数据关联与全局一致性，而不是“把传感器点画出来”。

## Representative methods

- Occupancy grid：最常用的二维环境表示。
- Odometry：提供局部运动约束。
- Pose graph optimization：利用回环等约束修正全局漂移。

## Worked example

机器人绕一圈回到起点，如果估计位置没有闭合，loop closure 会增加约束并调整整条历史轨迹。

## Connections

- ← Perception / Feature-Based Vision：视觉匹配可提供运动约束。
- → Planning：地图是规划的环境模型。

## Further Reading

- ORB-SLAM、LIO-SAM 等具体系统实现。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Sensors & State Estimation](02-sensing-estimation.md) · [Path & Motion Planning →](04-path-motion-planning.md)
