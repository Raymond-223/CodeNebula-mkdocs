# Pseudoinverse & Low-Rank Approximation

本章接续上一章已经构造好的奇异值分解（Singular Value Decomposition，SVD），依次定义伪逆、求出全部最小二乘解和唯一最小范数解，再讨论条件数与最佳低秩逼近。若还不能手算一个小矩阵的 SVD，请先返回上一章。
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

??? proof "四个彭若斯方程的证明"

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

??? proof "满足四个方程的矩阵唯一"

    设 $X$ 是任意满足四式的矩阵，令 $Y=V^TXU$，并按秩 $r$ 分块。把 $A=U\Sigma V^T$ 代入四式，相当于让 $Y$ 与

    $$
    \Sigma=\begin{pmatrix}D&0\\0&0\end{pmatrix},
    \qquad D=\operatorname{diag}(\sigma_1,\ldots,\sigma_r)
    $$

    满足同样四式。由 $\Sigma Y\Sigma=\Sigma$ 得 $DY_{11}D=D$，所以 $Y_{11}=D^{-1}$。由 $\Sigma Y$ 对称，右上块 $DY_{12}$ 必为零，故 $Y_{12}=0$；由 $Y\Sigma$ 对称，同理 $Y_{21}=0$。最后 $Y\Sigma Y=Y$ 的右下块给出 $Y_{22}=0$。因此 $Y=\Sigma^+$，从而 $X=V\Sigma^+U^T=A^+$。四个方程唯一刻画伪逆。

前者是到 $\operatorname{Col}(A)$ 的正交投影，后者是到 $\operatorname{Col}(A^T)$ 的正交投影。

### 满秩公式

**命题。** 若 $A$ 满列秩，则 $A^+=(A^TA)^{-1}A^T$；若 $A$ 满行秩，则 $A^+=A^T(AA^T)^{-1}$。

??? proof "证明"

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

    若 $A$ 满行秩，则 $AA^T$ 可逆，对 $AA^T=U\Sigma^2U^T$ 作相同计算，得到

    $$
    \boxed{A^+=A^T(AA^T)^{-1}.}
    $$

这两个公式只在相应的满秩条件下成立；一般情形必须回到奇异值分解的定义。

## 全部最小二乘解

**定理。** 全部最小二乘解为

$$
x=A^+b+V_0z,
\qquad z\in\mathbb R^{n-r},
$$

其中 $V_0$ 的列构成 $\ker(A)$ 的标准正交基。唯一的最小范数解是 $A^+b$。

??? proof "证明"

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
    \boxed{x=A^+b+V_0z,\qquad z\in\mathbb R^{n-r}.}
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

## 条件数

若 $A$ 满列秩，二范数条件数（condition number）定义为

$$
\kappa_2(A)
=\frac{\sigma_{\max}(A)}{\sigma_{\min}(A)}.
$$

当 $A$ 是可逆方阵时，这也等于 $\|A\|_2\|A^{-1}\|_2$。

**命题。** 对可逆方阵的线性系统 $Ax=b$，设 $b\ne0$。若矩阵 $A$ 不变、只有右端发生扰动 $\delta b$，则下式专指二范数：

$$
\frac{\|\delta x\|_2}{\|x\|_2}
\le
\kappa_2(A)
\frac{\|\delta b\|_2}{\|b\|_2}.
$$

??? proof "扰动界的证明"

    由 $A=U\Sigma V^T$ 可知 $A^{-1}=V\Sigma^{-1}U^T$，所以

    $$
    \|A^{-1}\|_2=\frac1{\sigma_{\min}(A)},
    \qquad
    \|A\|_2\|A^{-1}\|_2=\kappa_2(A).
    $$

    原方程和扰动后的方程分别为

    $$
    Ax=b,
    \qquad A(x+\delta x)=b+\delta b.
    $$

    两式相减得到 $A\delta x=\delta b$，所以

    $$
    \|\delta x\|_2
    =\|A^{-1}\delta b\|_2
    \le\|A^{-1}\|_2\,\|\delta b\|_2.
    $$

    同时 $b=Ax$ 给出

    $$
    \|b\|_2\le\|A\|_2\,\|x\|_2,
    \qquad
    \frac1{\|x\|_2}\le\frac{\|A\|_2}{\|b\|_2}.
    $$

    将两个不等式相乘：

    $$
    \frac{\|\delta x\|_2}{\|x\|_2}
    \le\|A^{-1}\|_2\,\|A\|_2
    \frac{\|\delta b\|_2}{\|b\|_2}
    =\kappa_2(A)\frac{\|\delta b\|_2}{\|b\|_2}.
    $$

条件数描述问题对输入扰动的敏感性，不等于某个算法的舍入误差。

## 正规方程的稳定性

**命题。** 若 $A$ 满列秩，则

$$
\kappa_2(A^TA)=\kappa_2(A)^2.
$$

??? proof "证明"

    $A^TA$ 的特征值是 $\sigma_i(A)^2$，满列秩保证最小奇异值为正。因此

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

??? proof "证明"
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

**定理。** 同一个 $A_k$ 也满足

$$
\min_{\operatorname{rank}(B)\le k}\|A-B\|_F
=\sqrt{\sum_{i=k+1}^r\sigma_i^2}.
$$

??? proof "证明"
    先看达到值：奇异值分解的秩一项在弗罗贝尼乌斯内积（Frobenius inner product）下互相正交，因此

    $$
    \|A-A_k\|_F^2
    =\left\|\sum_{i=k+1}^r\sigma_i u_iv_i^T\right\|_F^2.
    $$

    这里的秩一项在 Frobenius 内积下正交。按定义 $\langle R,S\rangle_F=\operatorname{tr}(R^TS)$，并且

    $$
    \langle u_iv_i^T,u_jv_j^T\rangle_F
    =\operatorname{tr}(v_i u_i^T u_j v_j^T)
    =(u_i^Tu_j)(v_j^Tv_i)=\delta_{ij};
    $$

    同时 $\|u_iv_i^T\|_F^2=1$。展开平方和后交叉项全为零，故

    $$\|A-A_k\|_F^2=\sum_{i=k+1}^r\sigma_i^2.$$

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

    把 $P$ 写到一组完整的左奇异向量标准正交基 $u_1,\ldots,u_m$ 中，其中 $u_1,\ldots,u_r$ 对应非零奇异值，并令 $p_i=u_i^TPu_i$。因为 $P^T=P=P^2$，有 $p_i=u_i^TP^TPu_i=\|Pu_i\|_2^2$，所以 $0\le p_i\le1$。在完整正交基下求和，$\sum_{i=1}^m p_i=\operatorname{tr}(P)$。又由谱定理，投影矩阵 $P$ 的特征值只可能是 $0$ 或 $1$，故 $\operatorname{tr}(P)=\operatorname{rank}(P)\le k$。

    若 $k=0$，条件 $\operatorname{rank}(B)\le0$ 强迫 $B=0$。此时唯一候选 $A_0=0$ 的误差为 $\|A\|_F=\sqrt{\sum_{i=1}^r\sigma_i^2}$，所以结论成立。以下只需考虑 $1\le k<r$，从而 $\sigma_k$ 有定义。因为 $\sigma_i^2\le\sigma_k^2$ 对 $i>k$，且前 $k$ 个奇异值不小于 $\sigma_k$，

    $$
    \sum_{i=1}^r\sigma_i^2p_i
    \le\sum_{i=1}^k\sigma_i^2p_i+\sigma_k^2\sum_{i=k+1}^m p_i
    \le\sum_{i=1}^k\sigma_i^2p_i+\sigma_k^2\left(k-\sum_{i=1}^k p_i\right)
    \le\sum_{i=1}^k\sigma_i^2.
    $$

    第二个不等号来自完整和 $\sum_{i=1}^m p_i\le k$；最后一个不等号逐项来自 $p_i\le1$ 与 $\sigma_i^2\ge\sigma_k^2$（$i\le k$）。因此

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

1. 对 $A=(1\ 1)$、$b=2$，写出全部精确解及最小范数解。
2. 证明 $\|A^+b\|_2\le\|b\|_2/\sigma_r$，其中 $\sigma_r$ 是最小正奇异值。
3. 证明最小二乘残差 $r=b-AA^+b$ 与 $\operatorname{Col}(A)$ 正交。
4. 对奇异值为 $8,3,1$ 的矩阵，计算最佳秩一逼近在算子范数与弗罗贝尼乌斯范数下的误差。

??? tip "第一步提示"

    第 1 题先写出约束 $x_1+x_2=2$，再最小化 $x_1^2+x_2^2$。第 2、3 题把 $A^+$ 写成紧致 SVD 的求和形式。第 4 题直接识别被截去的奇异值。

**答案。** 第 1 题为 $(t,2-t)^T$，最小范数解为 $(1,1)^T$。第 2 题使用正交性。第 4 题分别为 $3$ 与 $\sqrt{10}$。

**上一章：** [奇异值分解与最小二乘](02-svd-least-squares.md)  
**下一章：** [线性迭代与幂法](03-linear-iterations-power.md)
