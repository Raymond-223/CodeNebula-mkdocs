# 机器人模型、运动学与动力学

机器人要在真实世界运动，至少要解决三件事：**它在哪里、它会怎样运动、要产生这种运动需要什么力或力矩。** 坐标系、运动学和动力学分别对应这三个层次。

## 一、坐标系先解决“相对谁来描述”

同一个点可以在相机坐标系、机器人底盘坐标系和地图坐标系下得到完全不同的数值。机器人系统因此不会只说“目标在 $(2,1)$”，而要说明“目标在 camera frame 还是 map frame”。

刚体位姿通常由旋转 $R$ 和平移 $t$ 表示，齐次变换写成

$$
T=\begin{bmatrix}R&t\\0&1\end{bmatrix}.
$$

若已知 $T^A_B$ 和 $T^B_C$，则

$$T^A_C=T^A_BT^B_C.$$

这条链式关系就是机器人 TF 系统的数学基础。

在工程层，一个二维坐标变换的小例子可以把“先旋转、再平移”的顺序固定下来：

```python
import math

def transform_point(px, py, tx, ty, yaw):
    c, s = math.cos(yaw), math.sin(yaw)
    return c * px - s * py + tx, s * px + c * py + ty
```

这里输入点位于局部坐标系，`tx, ty, yaw` 描述该坐标系相对目标坐标系的位姿。实际系统还要同时传递 frame 名称和时间戳。

## 二、运动学只关心“动作变量怎样变成运动”

运动学不考虑质量和受力，只研究几何关系。对差速小车，左右轮线速度为 $v_l,v_r$，轮距为 $L$，车体线速度和角速度近似为

$$
v=\frac{v_r+v_l}{2},\qquad \omega=\frac{v_r-v_l}{L}.
$$

因此两轮同速时直行，速度不同则转弯。对机械臂，关节变量 $q$ 通过正运动学映射到末端位姿；Jacobian 则描述关节速度和末端速度的局部关系

$$\dot x=J(q)\dot q.$$

运动学回答的是“怎么动”，不是“为什么能这样动”。

## 三、动力学把质量、惯性和力加入模型

当控制任务需要考虑加速度、负载或高速运动时，只靠运动学就不够。机械系统常写成

$$
M(q)\ddot q+C(q,\dot q)\dot q+g(q)=\tau,
$$

其中 $M$ 表示惯性，$C$ 表示速度相关项，$g$ 表示重力，$\tau$ 是执行器力矩。

移动机器人低速导航时，简单运动学模型往往已经够用；机械臂高速轨迹控制、无人机姿态控制则更依赖动力学。**模型复杂度要由任务决定。**

## 四、差速车的位姿怎样随速度更新

二维差速车位姿为 $(x,y,\theta)$，在短时间 $\Delta t$ 内可近似更新为

$$
\begin{aligned}
x_{k+1}&=x_k+v\cos\theta_k\Delta t,\\
y_{k+1}&=y_k+v\sin\theta_k\Delta t,\\
\theta_{k+1}&=\theta_k+\omega\Delta t.
\end{aligned}
$$

```python
import math

def diff_drive_step(x, y, yaw, vl, vr, wheel_base, dt):
    v = 0.5 * (vl + vr)
    w = (vr - vl) / wheel_base
    return (x + v * math.cos(yaw) * dt,
            y + v * math.sin(yaw) * dt,
            yaw + w * dt)
```

这段代码没有考虑轮胎打滑、执行器动态和地形，因此适合低速平面运动，不应被当成真实车辆的完整物理模型。

## 五、模型使用时最容易错的是坐标、单位和时间

很多“算法错误”其实来自模型接口不一致：角度一处用 degree、一处用 radian；位置来自旧时间戳；相机外参方向写反；把 `map → base` 当成 `base → map` 使用。

因此机器人模型落地时应明确三个约定：**坐标系方向、单位、时间戳**。公式本身往往比这些工程约定更简单。
