# Multi-Modal Perception

> **Section:** Perception

## Why it matters

不同传感器在量程、精度、频率和失效模式上互补，多模态感知的重点是时间、空间和不确定性的对齐。

## Core ideas

- **Complementarity**：不同模态擅长不同信息。
- **Calibration**：空间对齐。
- **Synchronization**：时间对齐。
- **Fusion level**：原始数据、特征或决策层融合。

## Key theory

融合前先解决两个基础问题：**同一时间**和**同一坐标系**。如果时空对齐错误，再复杂的网络也会学习错误对应。

融合可以发生在 early、middle 或 late stage，选择取决于数据同步程度和下游任务。

## Representative methods

- Camera + LiDAR：语义与几何互补。
- Camera + IMU：低频绝对几何与高频惯性互补。
- Late fusion：工程上更易隔离故障。

## Worked example

相机看到“这是行人”，LiDAR 给出“目标在 12.4 m”；二者标定正确后才能形成可供规划使用的带距离语义目标。

## Connections

- → Robotics / State Estimation。
- → Robustness：单模态失效时需要检测与降级。

## Further Reading

- BEV fusion、cross-modal transformers。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Depth, 3D Vision & Point Clouds](04-depth-point-cloud.md)
