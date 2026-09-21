# Detection & Segmentation

> **Section:** Perception

## Why it matters

检测回答“目标在哪里”，分割回答“哪些像素属于它”；具体 CNN/Transformer 只是实现这种映射的模型。

## Core ideas

- **Classification**：整图类别。
- **Detection**：类别 + 边界框。
- **Semantic segmentation**：每像素类别，不区分同类实例。
- **Instance segmentation**：每个实例独立掩膜。

## Key theory

任务选择由下游需求决定：只需要“前方有人”可用检测；需要精确可行驶区域边界时，分割通常更合适。不要围绕某个网络名字组织知识，而应围绕输出表示组织。

## Representative methods

- Object detector：输出类别和位置。
- Segmentation model：输出像素级区域。

## Worked example

导航系统只需知道障碍物大致框时，检测足够；机械臂抓取需要目标精确轮廓时，实例分割更有用。

## Connections

- → Robotics / Planning：感知输出最终要转为障碍/语义约束。
- → Robustness：检测置信度不等于安全概率。

## Further Reading

- YOLO、DETR、SAM 等具体模型家族。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Feature-Based Vision](02-feature-vision.md) · [Depth, 3D Vision & Point Clouds →](04-depth-point-cloud.md)
