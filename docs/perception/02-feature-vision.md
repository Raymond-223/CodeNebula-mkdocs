# Feature-Based Vision

> **Section:** Perception

## Why it matters

特征方法提供最直接的“图像对应关系”直觉：先找稳定局部结构，再匹配，再估计几何。

## Core ideas

- **Keypoint**：图像中重复可检测的位置。
- **Descriptor**：描述关键点邻域的向量。
- **Matching**：在两帧/两图间寻找同一物理点。
- **RANSAC**：在含外点匹配中估计几何模型。

## Key theory

特征法主链是

**Detect → Describe → Match → Geometric verification**。

它的优势是几何解释清楚，缺点是弱纹理、强光照变化等情况下特征可能不足。

## Representative methods

- ORB：快速二进制特征。
- SIFT-like pipeline：更经典的尺度不变思路。
- RANSAC：剔除错误匹配。

## Worked example

两张走廊照片可能有 200 个初始匹配，其中 40 个错配；用 RANSAC 估计几何关系并删除不一致点后，剩余匹配才适合定位。

## Connections

- → Robotics / Mapping & SLAM：特征匹配可用于视觉运动估计。
- → Deep perception：深度模型替代部分手工特征。

## Further Reading

- SIFT derivation、epipolar geometry details。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Image & Camera Basics](01-image-camera-basics.md) · [Detection & Segmentation →](03-detection-segmentation.md)
