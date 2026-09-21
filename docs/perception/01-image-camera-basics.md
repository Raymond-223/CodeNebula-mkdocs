# Image & Camera Basics

> **Section:** Perception

## Why it matters

理解相机投影、内外参和图像采样，是后续所有视觉几何和视觉学习方法的共同基础。

## Visual intuition

<figure markdown="span">
  ![视觉系统先经历物理投影与采样，再进入特征、学习和几何推理。](../assets/diagrams/camera-pipeline.svg)
  <figcaption>视觉系统先经历物理投影与采样，再进入特征、学习和几何推理。</figcaption>
</figure>

## Core ideas

- **Pixel**：图像离散采样位置。
- **Intrinsics**：焦距、主点等相机内部参数。
- **Extrinsics**：相机与其他坐标系之间的位姿。
- **Projection**：3D 点如何映射到 2D 图像。

## Key theory

针孔模型核心关系为

$$
s\begin{bmatrix}u\\v\\1\end{bmatrix}=K[R\mid t]
\begin{bmatrix}X\\Y\\Z\\1\end{bmatrix}.
$$

标定的目的就是让像素、相机坐标和机器人坐标能够互相对应。

## Representative methods

- Intrinsic calibration。
- Extrinsic calibration。
- Undistortion。

## Minimal code

这就是针孔相机模型的计算核心：三维点经过内参矩阵后除以深度得到像素坐标。

```python
import numpy as np

def project(K, point_xyz):
    x = K @ point_xyz
    return x[:2] / x[2]

K = np.array([[500, 0, 320], [0, 500, 240], [0, 0, 1]])
uv = project(K, np.array([1.0, 0.2, 4.0]))
print(uv)
```

## Worked example

检测框中心只是一个像素点 $(u,v)$；没有深度与标定，它不能直接变成“目标距离机器人 2 m”。

## Connections

- → Robotics / Coordinate Systems。
- → Depth & 3D Vision。

## Further Reading

- Lens models、rolling shutter。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [Feature-Based Vision →](02-feature-vision.md)
