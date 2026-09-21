# Depth, 3D Vision & Point Clouds

> **Section:** Perception

## Why it matters

深度把二维像素恢复为空间距离，点云则把这些空间测量组织成可直接用于几何推理的三维表示。

## Visual intuition

<figure markdown="span">
  ![深度既可以来自几何，也可以来自主动传感或学习；不同来源的误差结构不同。](../assets/diagrams/depth-modalities.svg)
  <figcaption>深度既可以来自几何，也可以来自主动传感或学习；不同来源的误差结构不同。</figcaption>
</figure>

## Core ideas

- **Depth**：相机射线方向上的距离。
- **Stereo disparity**：左右图像匹配位移。
- **Triangulation**：由多视角几何恢复 3D。
- **RGB-D**：每像素同时有颜色和深度。
- **Point cloud**：3D 离散点集合。

## Key theory

### Depth & 3D Vision

双目中在理想针孔模型下，深度与视差近似满足

$$
Z=\frac{fB}{d},
$$

其中 $f$ 是焦距，$B$ 是基线，$d$ 是视差。视差越小，远距离深度越敏感。

### Point Cloud Perception

点云没有规则像素网格，处理方法通常围绕**邻域、体素、投影或稀疏卷积**构造结构。机器人基础阶段最重要的是坐标变换、滤波和几何分割。

## Representative methods

- Stereo / RGB-D：两种直接获得深度的代表。
- Voxel/downsample：降低点云计算量。
- Geometric clustering：把邻近 3D 点形成障碍候选。

## Minimal code

把每个像素的深度反投影到三维坐标，就能形成点云；后续再做滤波、分割和几何拟合。

```python
def backproject(u, v, depth, fx, fy, cx, cy):
    x = (u - cx) * depth / fx
    y = (v - cy) * depth / fy
    z = depth
    return x, y, z
```

## Worked example

**Depth & 3D Vision：**同样 1 像素视差误差，在远处对应的米制深度误差通常比近处大，因此远距离几何要更谨慎。

**Point Cloud Perception：**室外 LiDAR 每帧数十万点，先体素降采样再去地面，可显著减少后续障碍聚类计算量。

## Connections

- ← Camera Basics。
- → Point Cloud Perception / SLAM。
- → Robotics / Mapping。
- → Multi-Modal Perception：点云与相机互补。

## Further Reading

- Monocular depth、3D detection、PointNet/sparse convolution、BEV perception。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Detection & Segmentation](03-detection-segmentation.md) · [Multi-Modal Perception →](05-multimodal.md)
