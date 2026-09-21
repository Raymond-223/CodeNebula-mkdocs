# Navigation & Robot Control

> **Section:** Robotics

## Why it matters

导航不是某一个算法，而是定位、地图、规划、局部避障和控制形成的闭环系统。

## Core ideas

- **Global planning**：较低频生成到目标的大方向。
- **Local planning**：根据局部障碍和动力学实时修正。
- **Tracking controller**：让真实机器人跟随参考轨迹。
- **Recovery / fallback**：局部失败时安全退化。

## Key theory

导航不是一个算法，而是一条闭环：

**Localization → Global Plan → Local Trajectory → Controller → Robot → Sensors → Localization**。

任何一环的坐标、时间戳或频率出错，都可能表现成“规划算法不好”。

## Representative methods

- Pure Pursuit / PID：简单轨迹跟踪。
- MPC：带动力学与约束的跟踪。

## Worked example

机器人发现动态障碍时，通常不需要每次重算整张全局图；局部规划先绕行，只有路线真正不可达时再触发全局重规划。

## Connections

- → Distributed Systems：ROS2/DDS 连接各导航节点。
- → Human-AI Interaction：人可以监督目标和接管边界。

## Further Reading

- Behavior tree、Nav2 internals、whole-body control。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Path & Motion Planning](04-path-motion-planning.md)
