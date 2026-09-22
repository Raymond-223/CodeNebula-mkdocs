# Linear Algebra & Calculus

后面的控制、机器人、SLAM、优化和强化学习都会反复出现向量、矩阵、梯度和 Jacobian。这里不展开完整数学课程，只保留这些工具怎样描述状态、变换和局部变化。

<figure markdown="span">
  ![线性代数描述空间关系，微积分描述局部变化。](../assets/diagrams/linear-algebra-calculus.svg)
  <figcaption>矩阵负责“怎样变换”，导数负责“改变一点会发生什么”。</figcaption>
</figure>

## 向量与系统状态

机器人状态可以写成

$$
x=\begin{bmatrix}p_x&p_y&v&\theta\end{bmatrix}^\top.
$$

向量不只是把数字排成一列，而是让一组量可以统一做加法、内积、范数和线性变换。

常用的二范数

$$\|x\|_2=\sqrt{x^\top x}$$

可以表示误差大小或距离。

## 矩阵、映射与坐标变换

若

$$y=Ax,$$

矩阵 $A$ 把输入空间中的向量映射到输出空间。旋转矩阵、状态转移矩阵、神经网络线性层都属于这种结构。

矩阵乘法的顺序不能随意交换：通常 $AB\ne BA$。机器人坐标变换里，这一点尤其重要。

## 线性方程与最小二乘

很多估计和优化问题最后会变成

$$Ax=b.$$

数值计算时通常直接求解线性方程组，而不是先构造 $A^{-1}$。显式求逆不仅引入多余计算，也可能放大数值误差。

如果方程数量多于未知量、数据又有噪声，就会进入最小二乘问题。

## 导数与局部敏感度

一元函数中

$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.$$

多变量函数 $f(x_1,\ldots,x_n)$ 的梯度

$$
\nabla f=\begin{bmatrix}
\partial f/\partial x_1\\
\vdots\\
\partial f/\partial x_n
\end{bmatrix}
$$

指出函数增长最快的局部方向。这正是梯度下降和策略梯度等方法的核心几何含义。

## Jacobian 与多变量映射

若 $y=f(x)$ 为向量函数，Jacobian 为

$$J_{ij}=\frac{\partial y_i}{\partial x_j}.$$

机械臂中

$$\dot x=J(q)\dot q$$

把关节速度映射为末端速度；EKF 也用 Jacobian 在当前估计附近线性化非线性模型。

从几何上看，Jacobian 在当前构型附近把关节空间中的一个小位移映射为任务空间中的切向位移：

$$
\Delta x\approx J(q)\Delta q.
$$

它不是一段实现技巧，而是非线性映射在局部的线性近似；当构型变化时，Jacobian 也随之变化。

## 链式法则与复合系统

如果 $z=g(y)$、$y=f(x)$，则

$$\frac{dz}{dx}=\frac{dz}{dy}\frac{dy}{dx}.$$

神经网络反向传播、复合坐标变换的敏感度分析，本质上都在反复使用链式法则。理解这一点，比记住某个自动微分框架的 API 更重要。

## 从局部线性化看统一性

向量、矩阵、Jacobian 与梯度并不是彼此独立的工具。线性模型负责描述整体映射，Jacobian 把非线性模型在当前点附近变成线性映射，梯度则是标量输出对输入方向的特殊 Jacobian。读后续章节时，先判断对象是标量、向量还是映射，可以避免大量维度错误。
