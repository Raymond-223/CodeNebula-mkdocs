# Rotations, $SO(3)$ & Rigid Transforms

> 这一章专门补机器人、视觉和 SLAM 的几何前置。读完后，后文中的 $SO(3)$、$SE(3)$、齐次变换、流形与 $\boxplus$ 都不应该再是“突然出现的符号”。

## 一、从普通矩阵到旋转矩阵

到这里我们只说过“矩阵是一条线性规则”，但机器人、相机和 SLAM 后面会不断出现一种很特殊的矩阵：**旋转矩阵**。它不能随便填 9 个数，因为它代表的是“只改变朝向，不拉伸、不压缩、不镜像”。如果这一层不先讲清，后面看到 $R\in SO(3)$、$T\in SE(3)$ 就会像突然多出一套新数学。

先从二维开始。把平面向量 $(x,y)$ 绕原点逆时针旋转角度 $\theta$，新坐标是

$$
\begin{bmatrix}x'\\y'\end{bmatrix}
=
\underbrace{
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}}_{R(\theta)}
\begin{bmatrix}x\\y\end{bmatrix}.
$$

取 $\theta=90^\circ$、$p=(1,0)^\top$，就有

$$
R(90^\circ)p=
\begin{bmatrix}0&-1\\1&0\end{bmatrix}
\begin{bmatrix}1\\0\end{bmatrix}
=
\begin{bmatrix}0\\1\end{bmatrix}.
$$

这个例子先给出一个最重要的直觉：**旋转仍然可以用矩阵表示，但不是任意矩阵都能表示旋转。**

### 1.1 为什么旋转矩阵必须满足 $R^\top R=I$

纯旋转不能改变向量长度。对任意向量 $x$，旋转前后都应满足

$$
\|Rx\|_2^2=\|x\|_2^2.
$$

把左边展开：

$$
\|Rx\|_2^2=(Rx)^\top(Rx)=x^\top R^\top R x.
$$

要让它对任意 $x$ 都等于 $x^\top x$，只能有

$$
R^\top R=I.
$$

这意味着 $R$ 的列向量彼此正交且长度为 1。再加上

$$
\det R=1,
$$

就排除了镜像反射。这里的 $\det R$ 是**行列式（determinant）**：入门时可以把它理解成“这个线性变换把体积放大多少倍，并用正负号记录朝向是否被翻转”。纯旋转既不改变体积，也不能把右手坐标系镜像成左手坐标系，所以必须是 $+1$。于是三维所有“合法旋转矩阵”的集合记为

$$
\boxed{SO(3)=\{R\in\mathbb R^{3\times3}\mid R^\top R=I,\ \det R=1\}}.
$$

名字也可以直接拆开：

- **O** = Orthogonal，正交，来自 $R^\top R=I$；
- **S** = Special，特殊，表示再加一条 $\det R=1$；
- **3** = 在三维空间里作用。

二维同理得到 $SO(2)$。因此以后看到 $R\in SO(3)$，不要把它读成“一个神秘新变量”，只要读成：**$R$ 是一个三维合法旋转矩阵。**

### 1.2 为什么 3 个自由度却写成 9 个数

这里的**自由度（DoF）**就是“可以独立调节的参数个数”。三维朝向只需要 3 个自由度，但 $3\times3$ 矩阵有 9 个元素。多出来的数不是额外自由，而是被约束住了：$R^\top R=I$ 提供 6 个独立约束，因此

$$
9-6=3.
$$

这就是“旋转矩阵有 9 个数，但只描述 3 个自由度”的来源。后面机器人章节会再比较欧拉角和四元数：它们只是**同一个三维旋转的不同参数化方式**，不是三套不同的几何。

### 1.3 为什么说 $SO(3)$ 是一个“群”

入门阶段不需要抽象代数，只要检查四件事：

1. 两个旋转连续执行仍然是旋转：$R_1R_2\in SO(3)$；
2. 什么都不转的 $I$ 也是旋转；
3. 每个旋转都能撤销：$R^{-1}=R^\top$；
4. 矩阵乘法满足结合律。

满足这些规则的集合叫**群（group）**。所以 $SO(3)$ 的“群”只是在说：旋转可以连续组合、可以撤销、组合后仍然合法。

注意矩阵乘法通常不交换：$R_xR_y\neq R_yR_x$。三维里“先绕 $x$ 轴转，再绕 $y$ 轴转”和反过来，最终朝向一般不同。这就是后面欧拉角顺序、TF 变换链顺序必须写清的根源。

## 二、从旋转到刚体位姿：$SE(3)$

### 2.1 只有旋转还不够：平移加入后得到 $SE(3)$

机器人位姿不仅有朝向，还有位置。若一个点在局部坐标系中的坐标为 $p$，先旋转再平移得到

$$
p'=Rp+t,
$$

其中 $R\in SO(3)$、$t\in\mathbb R^3$。为了把“旋转 + 平移”也变成一次矩阵乘法，把点补成齐次坐标 $\bar p=(p^\top,1)^\top$，再定义

$$
T=
\begin{bmatrix}
R&t\\
0&1
\end{bmatrix}.
$$

于是

$$
\bar p'=T\bar p.
$$

所有这样的三维刚体变换组成

$$
\boxed{SE(3)=\left\{
\begin{bmatrix}R&t\\0&1\end{bmatrix}
\ \middle|\ R\in SO(3),\ t\in\mathbb R^3
\right\}}.
$$

同理，平面机器人使用 $SE(2)$。以后看到

$$
T_{world\leftarrow base}\in SE(3)
$$

就把它读成：**这个 $4\times4$ 矩阵把 base 坐标系里的点变换到 world 坐标系，它内部同时包含旋转和平移。**

### 2.2 连乘和求逆：TF 变换链为什么天然是矩阵链

若

$$
T_{A\leftarrow B}
$$

表示“把 B 系坐标变成 A 系坐标”，而 $T_{B\leftarrow C}$ 把 C 系变成 B 系，则

$$
T_{A\leftarrow C}=T_{A\leftarrow B}T_{B\leftarrow C}.
$$

中间的 B 正好首尾相接，这就是最安全的记法。逆变换则是

$$
T^{-1}=
\begin{bmatrix}
R^\top&-R^\top t\\
0&1
\end{bmatrix}.
$$

最常见的错误是把逆平移直接写成 $-t$。正确答案必须是 $-R^\top t$，因为平移向量本身也要换坐标系。

### 2.3 一个数字例子：先转 $90^\circ$，再平移

取

$$
R=
\begin{bmatrix}
0&-1&0\\
1&0&0\\
0&0&1
\end{bmatrix},\qquad
 t=\begin{bmatrix}1\\2\\0\end{bmatrix},\qquad
 p=\begin{bmatrix}1\\0\\0\end{bmatrix}.
$$

先旋转得到 $Rp=(0,1,0)^\top$，再平移得到

$$
p'=Rp+t=(1,3,0)^\top.
$$

写成齐次形式，完全是同一个结果：

$$
\begin{bmatrix}p'\\1\end{bmatrix}
=
\begin{bmatrix}
0&-1&0&1\\
1&0&0&2\\
0&0&1&0\\
0&0&0&1
\end{bmatrix}
\begin{bmatrix}1\\0\\0\\1\end{bmatrix}
=
\begin{bmatrix}1\\3\\0\\1\end{bmatrix}.
$$

如果你能手算出这个例子，后面机器人坐标变换已经有了最小前置。

## 三、为什么 SLAM 还需要局部增量

### 3.1 流形、李群和 $\boxplus$ 为什么会出现

还有一个容易突然跳出来的词：**流形（manifold）**。它只是在提醒你，旋转矩阵虽然写在 $\mathbb R^9$ 里，却不能在 9 个元素上随便加减，因为加完通常不再满足 $R^\top R=I$。

例如两个合法旋转 $R_1,R_2$，一般不能把“平均朝向”直接写成 $(R_1+R_2)/2$；这个矩阵通常已经不是合法旋转。也就是说，$SO(3)$ 像一个嵌在普通欧氏空间中的弯曲集合。

优化时仍然希望使用普通的小向量增量，所以在当前姿态附近，用一个三维小量

$$
\delta\theta=(\delta\theta_x,\delta\theta_y,\delta\theta_z)^\top\in\mathbb R^3
$$

表示“绕三个轴分别再转一点”。它对应的**反对称矩阵**满足 $A^\top=-A$，具体写成

$$
[\delta\theta]_\times=
\begin{bmatrix}
0&-\delta\theta_z&\delta\theta_y\\
\delta\theta_z&0&-\delta\theta_x\\
-\delta\theta_y&\delta\theta_x&0
\end{bmatrix}.
$$

所有这种反对称矩阵组成 $\mathfrak{so}(3)$，可以把它理解成 **$SO(3)$ 在当前位置附近的线性“小平面”**。指数映射 $\operatorname{Exp}$ 把这个小增量送回一个合法旋转：

$$
R_{new}=R\,\operatorname{Exp}([\delta\theta]_\times).
$$

三维位姿同理用六维小量 $\delta\xi=(\delta t,\delta\theta)\in\mathbb R^6$ 更新 $SE(3)$。SLAM 里常写

$$
T_{new}=T\boxplus\delta\xi,
$$

$\boxplus$ 就是“先在局部六维空间里加一个小增量，再映射回合法位姿”的简写。**入门阶段不需要推指数映射公式，只要知道为什么不能直接写 $T+\Delta T$。**

这时“李群 / 李代数”也不再神秘：$SO(3),SE(3)$ 是可以连续变化的群，叫李群；$\mathfrak{so}(3),\mathfrak{se}(3)$ 是它们在局部用于微小增量计算的线性空间，叫李代数。

## 四、记忆表：这些符号分别是什么

| 记号 | 一句话含义 | 自由度 | 后面第一次大量使用 |
| --- | --- | ---: | --- |
| $SO(2)$ | 二维合法旋转 | 1 | 平面机器人运动学 |
| $SO(3)$ | 三维合法旋转，$R^\top R=I,\det R=1$ | 3 | 相机外参、3D SLAM |
| $SE(2)$ | 二维旋转 + 二维平移 | 3 | 移动机器人位姿 |
| $SE(3)$ | 三维旋转 + 三维平移 | 6 | TF、点云、3D SLAM |
| $\mathfrak{so}(3)$ | 三维旋转的局部小增量空间 | 3 | 姿态优化 |
| $\mathfrak{se}(3)$ | 三维位姿的局部小增量空间 | 6 | 位姿图优化、Bundle Adjustment |

读到后面时只做两步判断：**这是旋转还是刚体位姿？这是全局合法状态还是局部小增量？** 前者决定用 $SO/SE$，后者决定是否会看到李代数、$\operatorname{Exp}$ 或 $\boxplus$。


## 五、向后接口：这些符号会在哪里再次出现

| 这里的概念 | 后文位置 | 后文拿它做什么 |
| --- | --- | --- |
| $SO(2),SE(2)$ | [机器人模型、运动学与动力学](../../robotics-perception/robotics/01-models-kinematics-dynamics.md) | 平面移动机器人位姿与运动 |
| $SO(3),SE(3)$ | [图像与相机基础](../../robotics-perception/perception/01-image-camera-basics.md) | 相机外参、world ↔ camera 变换 |
| 齐次变换链 | [机器人模型、运动学与动力学](../../robotics-perception/robotics/01-models-kinematics-dynamics.md) | TF、传感器外参、连杆变换 |
| $SE(3)$ | [深度、3D 视觉与点云](../../robotics-perception/perception/04-depth-point-cloud.md) | 点云配准、ICP |
| $\mathfrak{so}(3),\mathfrak{se}(3),\boxplus$ | [地图构建与 SLAM](../../robotics-perception/robotics/03-mapping-slam.md) | 在局部六维增量上优化，再回到合法位姿 |

### 自检

进入 Robotics 前，至少能回答四个问题：

1. 为什么任意 $3\times3$ 矩阵都不能叫旋转矩阵？
2. $SO(3)$ 与 $SE(3)$ 相差的是什么？
3. 为什么 $T^{-1}$ 的平移不是简单写成 $-t$？
4. 为什么 SLAM 优化姿态时不能直接做 $R+\Delta R$？

四个问题都能用一句话解释，就足以继续后面的机器人与感知章节。
