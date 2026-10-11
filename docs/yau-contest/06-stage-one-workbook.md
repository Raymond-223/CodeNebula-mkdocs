# Worked Problems

本章把前六章的定义和定理用于完整证明。每道题都明确条件、目标和逻辑方向；所有题目均为教学重写。

## 问题一：诱导范数与谱半径

设

$$
B=\begin{pmatrix}0&3\\0&1/2\end{pmatrix}.
$$

计算 $\rho(B)$ 与 $\|B\|_\infty$，并判断 $B^k$ 是否趋于零。

### 解答

$B$ 是上三角矩阵，特征值为对角元 $0$ 与 $1/2$，所以

$$
\rho(B)=\frac12.
$$

最大绝对行和为

$$
\|B\|_\infty=\max\{3,1/2\}=3.
$$

虽然 $\|B\|_\infty>1$，但 $\rho(B)<1$，因此由谱半径收敛判据（spectral radius criterion），$B^k\to0$。

还可直接计算。设

$$
B^k=\begin{pmatrix}0&a_k\\0&2^{-k}\end{pmatrix}.
$$

由 $B^{k+1}=B^kB$ 得 $a_{k+1}=a_k/2$，且 $a_1=3$，所以

$$
B^k=\begin{pmatrix}0&3\cdot2^{-(k-1)}\\0&2^{-k}\end{pmatrix}\to0.
$$

这个例子说明 $\|B\|<1$ 是方便的充分条件，不是收敛的必要条件。

## 问题二：严格对角占优

设 $A=(a_{ij})\in\mathbb C^{n\times n}$ 满足

$$
|a_{ii}|>\sum_{j\ne i}|a_{ij}|
\qquad(i=1,\ldots,n).
$$

证明 $A$ 可逆。

### 最大模分量解法

只需证明 $Ax=0$ 只有零解。反设存在 $x\ne0$ 满足 $Ax=0$。选择指标 $i$ 使

$$
|x_i|=\max_j|x_j|>0.
$$

第 $i$ 行给出

$$
a_{ii}x_i=-\sum_{j\ne i}a_{ij}x_j.
$$

取绝对值：

$$
|a_{ii}|,|x_i|
\le\sum_{j\ne i}|a_{ij}|,|x_j|
\le\left(\sum_{j\ne i}|a_{ij}|\right)|x_i|.
$$

由于 $|x_i|>0$，约去它得到

$$
|a_{ii}|\le\sum_{j\ne i}|a_{ij}|,
$$

与严格对角占优矛盾。因此 $\ker(A)=\{0\}$。方阵上的单射等价于可逆，故 $A$ 可逆。$\square$

## 问题三：最小二乘解的刻画

设 $A\in\mathbb R^{m\times n}$、$b\in\mathbb R^m$。证明 $x_*$ 是最小二乘解（least-squares solution）当且仅当

$$
A^T(Ax_*-b)=0.
$$

### 必要性

目标函数

$$
f(x)=\|Ax-b\|_2^2
$$

在整个 $\mathbb R^n$ 可微。若 $x_*$ 是全局最小点，也是局部最小点，因此

$$
\nabla f(x_*)=2A^T(Ax_*-b)=0.
$$

### 充分性

若 $A^T(Ax_*-b)=0$，则任取 $h\in\mathbb R^n$，

$$
\begin{aligned}
f(x_*+h)-f(x_*)
&=2h^TA^T(Ax_*-b)+\|Ah\|_2^2\\
&=\|Ah\|_2^2\ge0.
\end{aligned}
$$

故 $x_*$ 是全局最小点。两个方向均已证明。$\square$

注意：这里不要求 $A$ 满列秩。满列秩只决定解是否唯一。

## 问题四：全部最小二乘解

设

$$
A=\begin{pmatrix}
1&0&1\\
0&1&1
\end{pmatrix},
\qquad
b=\begin{pmatrix}1\\1\end{pmatrix}.
$$

求全部最小二乘解与最小范数解（minimum-norm solution）。

### 精确解集

这里 $Ax=b$ 本身相容：

$$
x_1+x_3=1,
\qquad
x_2+x_3=1.
$$

令 $x_3=t$，则全部解为

$$
x(t)=\begin{pmatrix}1-t\\1-t\\t\end{pmatrix}.
$$

因为残差能达到零，这些也正是全部最小二乘解。

### 最小范数解

计算

$$
\|x(t)\|_2^2
=2(1-t)^2+t^2
=3t^2-4t+2.
$$

求导得 $6t-4=0$，所以 $t=2/3$。因此

$$
x_{\min}=\begin{pmatrix}1/3\\1/3\\2/3\end{pmatrix}.
$$

也可用满行秩公式

$$
A^+=A^T(AA^T)^{-1}.
$$

先算

$$
AA^T=\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad
(AA^T)^{-1}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
$$

于是 $A^+b=(1/3,1/3,2/3)^T$，与直接最小化一致。

## 问题五：理查森迭代的最优参数

设 $A=\operatorname{diag}(2,4)$，使用

$$
x_{k+1}=x_k+\eta(b-Ax_k),
\qquad \eta>0.
$$

求对任意初值收敛的 $\eta$ 范围及最优收敛因子。

### 误差矩阵

精确解 $x^*$ 满足 $Ax^*=b$。相减得

$$
e_{k+1}=(I-\eta A)e_k.
$$

迭代矩阵为

$$
B_\eta=\operatorname{diag}(1-2\eta,1-4\eta).
$$

### 收敛区间

需要

$$
|1-2\eta|<1,
\qquad
|1-4\eta|<1.
$$

第一式给出 $0<\eta<1$，第二式给出 $0<\eta<1/2$，所以

$$
\boxed{0<\eta<1/2}.
$$

### 最优参数

收敛因子为

$$
q(\eta)=\max\{|1-2\eta|,|1-4\eta|\}.
$$

最优点使区间两端等模异号：

$$
1-2\eta=-(1-4\eta).
$$

所以 $\eta_*=1/3$，且 $q(\eta_*)=1/3$。

## 问题六：幂零矩阵的有限步收敛

设 $B\in\mathbb C^{n\times n}$ 且 $\rho(B)=0$。证明迭代

$$
x_{k+1}=Bx_k+c
$$

至多 $n$ 步到达固定点。

### 解答

$\rho(B)=0$ 意味着全部特征值为零，因此特征多项式为

$$
p_B(t)=t^n.
$$

由 Cayley–Hamilton theorem，

$$
p_B(B)=B^n=0.
$$

因为 $1$ 不是特征值，$I-B$ 可逆，固定点 $x^*=(I-B)^{-1}c$ 唯一。误差满足

$$
e_n=B^ne_0=0.
$$

故 $x_n=x^*$。注意这不是渐近收敛，而是有限步精确到达。

## 问题七：压缩映射与迭代次数

设

$$
g(x)=\frac{x+2}{4},
\qquad x_0=0.
$$

证明存在唯一不动点，并求保证 $|x_n-x^*|<10^{-6}$ 的最小整数 $n$。

### 巴拿赫定理的条件

$g:\mathbb R\to\mathbb R$，而 $\mathbb R$ 完备。并且

$$
|g(x)-g(y)|=\frac14|x-y|,
$$

故 $q=1/4$。巴拿赫定理给出唯一不动点和任意初值的收敛性。

固定点满足

$$
x^*=\frac{x^*+2}{4},
$$

所以 $x^*=2/3$。

### 精确误差与次数

误差精确满足

$$
e_n=4^{-n}e_0,
\qquad
|e_n|=\frac23,4^{-n}.
$$

要求

$$
\frac23,4^{-n}<10^{-6}.
$$

等价于

$$
n>\frac{\log((2/3)10^6)}{\log4}\approx9.67.
$$

所以最小整数为 $n=10$。

## 问题八：牛顿法的局部误差界

设 $f(\alpha)=0$，并且在 $I=[\alpha-r,\alpha+r]$ 上

$$
|f'(x)|\ge2,
\qquad
|f''(x)|\le6.
$$

证明牛顿法误差（Newton error）满足

$$
|e_{k+1}|\le\frac32|e_k|^2
$$

并给出保证 $I$ 不变的一个半径条件。

### 解答

泰勒余项给出

$$
e_{k+1}=\frac{f''(\xi_k)}{2f'(x_k)}e_k^2.
$$

因此

$$
|e_{k+1}|
\le\frac6{2\cdot2}|e_k|^2
=\frac32|e_k|^2.
$$

若希望 $|e_k|\le r$ 推出 $|e_{k+1}|\le r$，充分条件是

$$
\frac32r^2\le r.
$$

对 $r>0$，等价于 $r\le2/3$。因此只要给定导数界确实在该区间成立，并取 $r\le2/3$，牛顿映射（Newton map）将区间送回自身。

## 问题九：幂法的收敛速度

设

$$
A=\begin{pmatrix}5&0\\0&2\end{pmatrix},
\qquad
x_0=\begin{pmatrix}1\\3\end{pmatrix}.
$$

求归一化迭代方向与主特征向量的误差比例，并估计达到 $10^{-4}$ 所需步数。

### 解答

$$
A^kx_0
=\begin{pmatrix}5^k\\3\cdot2^k\end{pmatrix}
=5^k\begin{pmatrix}1\\3(2/5)^k\end{pmatrix}.
$$

相对第二分量为 $3(2/5)^k$。要求

$$
3(2/5)^k\le10^{-4},
$$

所以

$$
k\ge
\frac{\log(10^{-4}/3)}{\log(2/5)}
\approx11.25.
$$

取 $k=12$ 足够。

## 问题十：证明辨析

下面的“证明”试图说明 $\rho(B)<1$：

> 从 $x_0=0$ 开始计算，观察到 $x_k$ 收敛，所以迭代对任意初值收敛，因此 $\rho(B)<1$。

指出错误并给出反例。

### 解答

谱半径判据的必要性要求“对任意初始误差 $e_0$，$B^ke_0\to0$”。单个初值可能恰好没有不稳定特征方向分量。

取

$$
B=\begin{pmatrix}2&0\\0&1/2\end{pmatrix},
\qquad c=0,
\qquad x_0=0.
$$

该初值产生恒零数列，当然收敛；但 $\rho(B)=2>1$。即使取非零初值 $(0,1)^T$，也会收敛，而含第一坐标分量的初值会发散。

## 问题十一：最佳秩一逼近

设

$$
A=\operatorname{diag}(4,2,1).
$$

求 $A$ 在算子范数（operator norm）和弗罗贝尼乌斯范数（Frobenius norm）下的最佳秩一逼近（rank-one approximation），并计算两种最小误差。

### 奇异值分解

$A$ 已经是非负对角矩阵，因此可取

$$
U=V=I_3,
\qquad
\Sigma=\operatorname{diag}(4,2,1).
$$

三个奇异值（singular values）为 $\sigma_1=4$、$\sigma_2=2$、$\sigma_3=1$。截断到第一项得到

$$
A_1=\sigma_1u_1v_1^T
=\begin{pmatrix}
4&0&0\\
0&0&0\\
0&0&0
\end{pmatrix}.
$$

### 最优性与误差

由埃卡特－杨定理（Eckart–Young theorem），$A_1$ 同时在两种范数下达到最佳秩一逼近。残差为

$$
A-A_1=\operatorname{diag}(0,2,1).
$$

因此算子范数误差（operator-norm error）是下一奇异值：

$$
\min_{\operatorname{rank}(B)\le1}\|A-B\|_2
=\|A-A_1\|_2
=\sigma_2
=2.
$$

弗罗贝尼乌斯范数误差（Frobenius-norm error）是被舍弃奇异值平方和的平方根：

$$
\min_{\operatorname{rank}(B)\le1}\|A-B\|_F
=\|A-A_1\|_F
=\sqrt{\sigma_2^2+\sigma_3^2}
=\sqrt5.
$$

两种误差不同，因为算子范数只测量残差最强的伸缩方向，而弗罗贝尼乌斯范数累计所有被舍弃方向的平方能量。

## 进一步练习

1. 对一个 $3\times2$ 矩阵完整计算紧致奇异值分解（compact SVD），并核对所有矩阵尺寸。
2. 构造一个连续自映射，使其具有唯一不动点，但皮卡迭代形成二周期。
3. 对重数为 $m$ 的根，推导牛顿法的线性误差因子 $(m-1)/m$。
4. 证明当 $A$ 对称正定时，$\|I-\eta A\|_2=\max_i|1-\eta\lambda_i|$。
5. 从斯特芬森展开（Steffensen expansion）重新计算二次误差系数，检查 $g'(\alpha)=0$ 与 $g''(\alpha)=0$ 的特殊情况。
6. 对 $A=\operatorname{diag}(1,4,9)$、位移（shift）$\mu=3.8$，写出带位移的反幂迭代（shifted inverse iteration）对三个特征方向的放大因子，并判断最终提取哪个特征向量。

这些练习的目标是独立重建证明。若某一步只能写“显然”，应补出所用的定义、不等式或定理。

**上一章：** [牛顿法与收敛阶](05-newton-convergence.md)  
**专题概览：** [丘成桐竞赛专题](index.md)
