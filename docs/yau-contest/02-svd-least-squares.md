# SVD & Least Squares

本章从正交投影开始，推导最小二乘问题（least-squares problem）、奇异值分解（Singular Value Decomposition，SVD）、摩尔－彭若斯伪逆（Moore–Penrose pseudoinverse）以及全部最小二乘解。每个矩阵的尺寸都会明确写出。

## 正交性与投影

向量 $u,v\in\mathbb R^m$ 正交，记为 $u\perp v$，当且仅当 $u^Tv=0$。若 $u$ 是单位向量，则 $b$ 在 $u$ 方向的正交投影为

$$
\operatorname{proj}_u(b)=(u^Tb)u.
$$

若 $U\in\mathbb R^{m\times r}$ 的列标准正交，即 $U^TU=I_r$，则

$$
P=UU^T
$$

是到 $\operatorname{Col}(U)$ 的正交投影算子（orthogonal projector）。它满足

$$
P^T=P,
\qquad
P^2=P.
$$

第二式的计算为

$$
P^2=UU^TUU^T=U(U^TU)U^T=UU^T=P.
$$

对任意 $b$，$Pb\in\operatorname{Col}(U)$，且

$$
U^T(b-Pb)=U^Tb-U^TUU^Tb=0,
$$

所以残差 $b-Pb$ 与整个列空间正交。

### 最佳逼近性质

任取 $y\in\operatorname{Col}(U)$，有正交分解

$$
b-y=(b-Pb)+(Pb-y).
$$

两项互相正交，故 Pythagorean theorem 给出

$$
\|b-y\|_2^2
=\|b-Pb\|_2^2+\|Pb-y\|_2^2
\ge\|b-Pb\|_2^2.
$$

因此 $Pb$ 是列空间中距离 $b$ 最近的唯一向量。

## 最小二乘问题（Least-Squares Problem）

给定 $A\in\mathbb R^{m\times n}$ 与 $b\in\mathbb R^m$，最小二乘问题为

$$
\min_{x\in\mathbb R^n}\|Ax-b\|_2^2.
$$

目标不是让 $x$ 接近 $b$，而是让可达到的向量 $Ax\in\operatorname{Col}(A)$ 接近 $b$。

令 $f(x)=\|Ax-b\|_2^2$，展开得

$$
f(x)=x^TA^TAx-2b^TAx+b^Tb.
$$

因此

$$
\nabla f(x)=2A^T(Ax-b).
$$

驻点满足正规方程（normal equations）：

$$
A^TAx=A^Tb.
$$

### 必要性与充分性

正规方程不仅必要，而且充分。若 $A^T(Ax_*-b)=0$，则对任意 $h$，

$$
\begin{aligned}
\|A(x_*+h)-b\|_2^2
&=\|Ax_*-b+Ah\|_2^2\\
&=\|Ax_*-b\|_2^2
+2h^TA^T(Ax_*-b)+\|Ah\|_2^2\\
&=\|Ax_*-b\|_2^2+\|Ah\|_2^2\\
&\ge\|Ax_*-b\|_2^2.
\end{aligned}
$$

所以 $x_*$ 是全局最小点。反过来，可微函数的无约束局部最小点必须满足梯度为零，因此正规方程也是必要条件。

最小二乘解唯一当且仅当 $\ker(A)=\{0\}$。如果存在 $0\ne h\in\ker(A)$，则 $x_*+h$ 与 $x_*$ 有同一个拟合值；若零空间平凡，目标差中的 $\|Ah\|^2$ 对 $h\ne0$ 严格为正。

## 奇异值分解（Singular Value Decomposition）

**奇异值分解定理（SVD Theorem）。** 对任意 $A\in\mathbb R^{m\times n}$，存在正交矩阵

$$
U\in\mathbb R^{m\times m},
\qquad
V\in\mathbb R^{n\times n},
$$

以及矩形对角矩阵 $\Sigma\in\mathbb R^{m\times n}$，使

$$
A=U\Sigma V^T.
$$

$\Sigma$ 的非零对角元为

$$
\sigma_1\ge\sigma_2\ge\cdots\ge\sigma_r>0,
\qquad r=\operatorname{rank}(A),
$$

称为奇异值（singular values）。

### 从谱定理构造奇异值分解

$A^TA$ 是实对称半正定矩阵，因此存在正交矩阵 $V$ 使

$$
A^TA=V\Lambda V^T,
\qquad
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
\quad \lambda_i\ge0.
$$

定义 $\sigma_i=\sqrt{\lambda_i}$。对每个 $\sigma_i>0$，令

$$
u_i=\frac{Av_i}{\sigma_i}.
$$

则

$$
u_i^Tu_j
=\frac{v_i^TA^TAv_j}{\sigma_i\sigma_j}
=\frac{\lambda_jv_i^Tv_j}{\sigma_i\sigma_j}
=\delta_{ij}.
$$

所以这些 $u_i$ 标准正交。再把它们补成 $\mathbb R^m$ 的标准正交基，即得到 $U$。同时

$$
Av_i=\sigma_i u_i,
\qquad
A^Tu_i=\sigma_i v_i
$$

对正奇异值成立，从而 $A=U\Sigma V^T$。

还需检查零特征值对应的方向。若 $\lambda_i=0$，则

$$
\|Av_i\|_2^2
=v_i^TA^TAv_i
=\lambda_i\|v_i\|_2^2
=0,
$$

所以 $Av_i=0$。因此 $V$ 中所有列——包括零奇异值对应的列——都满足 $Av_i=\sigma_i u_i$ 的矩阵形式，这才完整得到 $AV=U\Sigma$，即 $A=U\Sigma V^T$。

### 紧致奇异值分解（Compact SVD）

只保留正奇异值对应的向量，得到紧致奇异值分解：

$$
A=U_r\Sigma_rV_r^T,
$$

其中

$$
U_r\in\mathbb R^{m\times r},
\quad
\Sigma_r\in\mathbb R^{r\times r},
\quad
V_r\in\mathbb R^{n\times r}.
$$

这里 $\operatorname{Col}(A)=\operatorname{Col}(U_r)$，而 $\ker(A)=\operatorname{Col}(V_0)$，其中 $V=[V_r\ V_0]$。

## 奇异值分解的手工计算

取

$$
A=\begin{pmatrix}1&1\\1&-1\\0&0\end{pmatrix}.
$$

第一步计算

$$
A^TA
=\begin{pmatrix}2&0\\0&2\end{pmatrix}.
$$

特征值均为 $2$，故奇异值 $\sigma_1=\sigma_2=\sqrt2$。可取

$$
v_1=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
v_2=\begin{pmatrix}0\\1\end{pmatrix}.
$$

然后

$$
u_1=\frac{Av_1}{\sqrt2}
=\frac1{\sqrt2}\begin{pmatrix}1\\1\\0\end{pmatrix},
\qquad
u_2=\frac{Av_2}{\sqrt2}
=\frac1{\sqrt2}\begin{pmatrix}1\\-1\\0\end{pmatrix}.
$$

补上 $u_3=(0,0,1)^T$，得到

$$
U=\begin{pmatrix}
1/\sqrt2&1/\sqrt2&0\\
1/\sqrt2&-1/\sqrt2&0\\
0&0&1
\end{pmatrix},
\quad
\Sigma=\begin{pmatrix}
\sqrt2&0\\0&\sqrt2\\0&0
\end{pmatrix},
\quad V=I_2.
$$

直接相乘可验证 $U\Sigma V^T=A$。

## 摩尔－彭若斯伪逆（Moore–Penrose Pseudoinverse）

若 $A=U\Sigma V^T$，定义 $\Sigma^+$：将每个正奇异值 $\sigma_i$ 换成 $1/\sigma_i$，再转置矩形形状。摩尔－彭若斯伪逆为

$$
A^+=V\Sigma^+U^T
=V_r\Sigma_r^{-1}U_r^T.
$$

它满足四个彭若斯方程（Penrose equations）：

$$
AA^+A=A,
\qquad
A^+AA^+=A^+,
$$

$$
(AA^+)^T=AA^+,
\qquad
(A^+A)^T=A^+A.
$$

由紧致奇异值分解可直接算出

$$
AA^+=U_rU_r^T,
\qquad
A^+A=V_rV_r^T.
$$

例如，

$$
AA^+A
=U_r\Sigma_rV_r^TV_r\Sigma_r^{-1}U_r^TU_r\Sigma_rV_r^T
=U_r\Sigma_rV_r^T
=A.
$$

同理 $A^+AA^+=A^+$。而 $U_rU_r^T$ 与 $V_rV_r^T$ 都是对称矩阵，所以另外两个彭若斯方程也成立。

前者是到 $\operatorname{Col}(A)$ 的正交投影，后者是到 $\operatorname{Col}(A^T)$ 的正交投影。

### 满秩公式

若 $A$ 满列秩，$A^TA$ 可逆。由紧致奇异值分解，

$$
A^TA=V\Sigma^2V^T,
$$

所以

$$
(A^TA)^{-1}A^T
=V\Sigma^{-2}V^TV\Sigma U^T
=V\Sigma^{-1}U^T
=A^+.
$$

因此满列秩时

$$
\boxed{A^+=(A^TA)^{-1}A^T.}
$$

若 $A$ 满行秩，则 $AA^T$ 可逆，同理得到

$$
\boxed{A^+=A^T(AA^T)^{-1}.}
$$

这两个公式只在相应的满秩条件下成立；一般情形必须回到奇异值分解的定义。

## 全部最小二乘解

将 $V=[V_r\ V_0]$。任意 $x\in\mathbb R^n$ 可唯一写成

$$
x=V_ry+V_0z.
$$

因为 $AV_0=0$，

$$
Ax=U_r\Sigma_ry.
$$

再将 $b$ 分解为列空间部分与正交补：

$$
b=U_rU_r^Tb+(I-U_rU_r^T)b.
$$

于是

$$
\|Ax-b\|_2^2
=\|\Sigma_ry-U_r^Tb\|_2^2
+\|(I-U_rU_r^T)b\|_2^2.
$$

第二项与 $y,z$ 无关，第一项在

$$
y=\Sigma_r^{-1}U_r^Tb
$$

时为零。因此全部最小二乘解为

$$
\boxed{x=A^+b+V_0z,qquad z\in\mathbb R^{n-r}.}
$$

等价地，也可写成

$$
x=A^+b+(I-A^+A)w,
\qquad w\in\mathbb R^n.
$$

### 最小范数解

两部分 $A^+b\in\operatorname{Col}(V_r)$ 与 $V_0z\in\operatorname{Col}(V_0)$ 正交，所以

$$
\|A^+b+V_0z\|_2^2
=\|A^+b\|_2^2+\|z\|_2^2.
$$

最小值唯一在 $z=0$ 取得。因此

$$
\boxed{x_{\min}=A^+b}
$$

是唯一的最小范数最小二乘解（minimum-norm least-squares solution）。

## 秩亏情形的完整示例

设

$$
A=\begin{pmatrix}1&1\\0&0\end{pmatrix},
\qquad
b=\begin{pmatrix}2\\1\end{pmatrix}.
$$

目标为

$$
\|Ax-b\|_2^2=(x_1+x_2-2)^2+1.
$$

所以全部最小二乘解满足 $x_1+x_2=2$，可写成

$$
x=\begin{pmatrix}t\\2-t\end{pmatrix}.
$$

其范数平方为

$$
t^2+(2-t)^2=2(t-1)^2+2,
$$

故最小范数解为 $(1,1)^T$。

从奇异值分解计算：正奇异值是 $\sqrt2$，

$$
u_1=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
v_1=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}.
$$

于是

$$
A^+
=v_1\frac1{\sqrt2}u_1^T
=\begin{pmatrix}1/2&0\\1/2&0\end{pmatrix},
$$

从而 $A^+b=(1,1)^T$，与直接计算一致。

## 正规方程的稳定性

若 $A$ 满列秩，则

$$
\kappa_2(A^TA)=\kappa_2(A)^2.
$$

因为 $A^TA$ 的特征值是 $\sigma_i(A)^2$，所以

$$
\kappa_2(A^TA)
=\frac{\sigma_{\max}^2}{\sigma_{\min}^2}
=\kappa_2(A)^2.
$$

因此正规方程适合理论推导，但数值计算中可能放大病态性。本专题使用奇异值分解分析秩亏、敏感性和最小范数解。

## 低秩逼近（Low-Rank Approximation）

秩 $k$ 逼近（rank-$k$ approximation）要在所有秩不超过 $k$ 的矩阵中寻找最接近 $A$ 的矩阵。设


$$
A=\sum_{i=1}^r\sigma_i u_iv_i^T,
\qquad
\sigma_1\ge\cdots\ge\sigma_r>0.
$$

截断奇异值分解（truncated SVD）定义为

$$
A_k=\sum_{i=1}^k\sigma_i u_iv_i^T.
$$

它保留最大的 $k$ 个伸缩方向，且 $\operatorname{rank}(A_k)=k$（当 $k\le r$）。

### 算子范数下的埃卡特－杨定理（Eckart–Young Theorem）

**定理。** 对 $0\le k<r$，

$$
\min_{\operatorname{rank}(B)\le k}\|A-B\|_2
=\sigma_{k+1},
$$

且 $A_k$ 取得最小值。

**下界证明。** 任取 $\operatorname{rank}(B)\le k$。考虑维数为 $k+1$ 的子空间

$$
S=\operatorname{span}\{v_1,\ldots,v_{k+1}\}.
$$

线性映射 $B|_S:S\to\mathbb R^m$ 的秩至多为 $k$，所以其零空间在 $S$ 中至少一维。故存在单位向量

$$
x=\sum_{i=1}^{k+1}c_iv_i\in S,
\qquad Bx=0.
$$

于是

$$
\begin{aligned}
\|A-B\|_2
&\ge\|(A-B)x\|_2\\
&=\|Ax\|_2\\
&=\sqrt{\sum_{i=1}^{k+1}\sigma_i^2c_i^2}\\
&\ge\sigma_{k+1}
\sqrt{\sum_{i=1}^{k+1}c_i^2}\\
&=\sigma_{k+1}.
\end{aligned}
$$

**达到下界。** 因为

$$
A-A_k=\sum_{i=k+1}^r\sigma_i u_iv_i^T,
$$

其最大奇异值正是 $\sigma_{k+1}$，所以

$$
\|A-A_k\|_2=\sigma_{k+1}.
$$

上下界相同，定理得证。$\square$

### 弗罗贝尼乌斯范数下的埃卡特－杨定理

同一个 $A_k$ 也满足

$$
\min_{\operatorname{rank}(B)\le k}\|A-B\|_F
=\sqrt{\sum_{i=k+1}^r\sigma_i^2}.
$$

先看达到值：奇异值分解的秩一项在弗罗贝尼乌斯内积（Frobenius inner product）下互相正交，因此

$$
\|A-A_k\|_F^2
=\sum_{i=k+1}^r\sigma_i^2.
$$

再证下界。令 $P$ 是到 $\operatorname{Col}(B)$ 的正交投影，则 $PB=B$，且

$$
A-B=(I-P)A+(PA-B).
$$

两项的每一列分别落在正交子空间中，所以

$$
\|A-B\|_F^2
=\|(I-P)A\|_F^2+\|PA-B\|_F^2
\ge\|(I-P)A\|_F^2.
$$

把 $P$ 写到左奇异向量基中。令 $p_i=u_i^TPu_i$，则 $0\le p_i\le1$，并且

$$
\sum_i p_i=\operatorname{tr}(P)=\operatorname{rank}(P)\le k.
$$

于是

$$
\|PA\|_F^2
=\sum_{i=1}^r\sigma_i^2p_i
\le\sum_{i=1}^k\sigma_i^2.
$$

因此

$$
\|(I-P)A\|_F^2
=\|A\|_F^2-\|PA\|_F^2
\ge\sum_{i=k+1}^r\sigma_i^2.
$$

这给出所需下界。

### 数值示例

设

$$
A=\begin{pmatrix}5&0&0\\0&2&0\\0&0&1\end{pmatrix}.
$$

最佳秩一逼近为

$$
A_1=\begin{pmatrix}5&0&0\\0&0&0\\0&0&0\end{pmatrix}.
$$

误差为

$$
\|A-A_1\|_2=2,
\qquad
\|A-A_1\|_F=\sqrt{2^2+1^2}=\sqrt5.
$$

最佳秩二逼近保留 $5,2$ 两个奇异值，对应误差分别为 $1$ 与 $1$。

## 练习

1. 证明 $P=UU^T$ 对称且幂等，并证明 $I-P$ 也是正交投影。
2. 对 $A=\operatorname{diag}(3,2,0)$ 写出完整奇异值分解（full SVD）与紧致奇异值分解。
3. 对 $A=(1\ 1)$、$b=2$，写出全部精确解及最小范数解。
4. 证明 $\|A^+b\|_2\le\|b\|_2/\sigma_r$，其中 $\sigma_r$ 是最小正奇异值。
5. 证明最小二乘残差（least-squares residual）$r=b-AA^+b$ 与 $\operatorname{Col}(A)$ 正交。
6. 对奇异值为 $8,3,1$ 的矩阵，计算最佳秩一逼近（rank-one approximation）在算子范数与弗罗贝尼乌斯范数下的误差。

**答案。** 第 3 题为 $(t,2-t)^T$，最小范数解 $(1,1)^T$。第 4 题由 $A^+b=\sum_{i=1}^r(u_i^Tb)v_i/\sigma_i$ 与正交性得到。第 6 题分别为 $3$ 与 $\sqrt{10}$。

**上一章：** [矩阵范数与谱理论](01-matrix-norms-spectral.md)  
**下一章：** [线性迭代与幂法](03-linear-iterations-power.md)
