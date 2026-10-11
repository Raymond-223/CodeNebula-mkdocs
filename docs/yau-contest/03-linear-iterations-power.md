# Linear Iterations & Power Method

线性迭代的核心不是“多算几步”，而是从更新式提取误差传播矩阵（error propagation matrix），并判断它的幂是否趋于零。本章给出完整充要条件，然后推导雅可比方法（Jacobi）、高斯－赛德尔方法（Gauss–Seidel）、理查森迭代（Richardson）与幂法（power method）。

## 标量线性迭代

先考虑

$$
x_{k+1}=ax_k+c.
$$

若 $a\ne1$，固定点为 $x^*=c/(1-a)$。令 $e_k=x_k-x^*$，则

$$
e_{k+1}=ae_k,
\qquad
e_k=a^ke_0.
$$

因此对任意初值收敛当且仅当 $|a|<1$。$a<0$ 时误差会交替变号，但只要 $|a|<1$ 仍然收敛。

## 定常矩阵迭代

考虑

$$
x_{k+1}=Bx_k+c,
\qquad B\in\mathbb C^{n\times n}.
$$

若存在固定点 $x^*$，则 $(I-B)x^*=c$。相减得到

$$
e_{k+1}=Be_k,
\qquad
e_k=B^ke_0.
$$

所以“对任意初值收敛到同一个固定点”等价于 $B^k\to0$。

## 谱半径收敛判据

**定理。** 对方阵 $B$，以下命题等价：

1. $B^k\to0$；
2. $\rho(B)<1$；
3. 对每个初值，$x_{k+1}=Bx_k+c$ 收敛到唯一固定点 $(I-B)^{-1}c$。

### 必要性

若 $B^k\to0$，任取特征对 $Bv=\lambda v$，$v\ne0$，则

$$
B^kv=\lambda^kv\to0.
$$

因此 $|\lambda|<1$。对所有特征值成立，所以 $\rho(B)<1$。

### 可对角化矩阵情形的充分性

若 $B=V\Lambda V^{-1}$，则

$$
B^k=V\Lambda^kV^{-1}.
$$

$\rho(B)<1$ 意味着每个 $|\lambda_i|<1$，故 $\Lambda^k\to0$，从而 $B^k\to0$。

### 一般矩阵情形的充分性

一般矩阵在复数域可写为 Jordan form $B=PJP^{-1}$。一个大小为 $s$ 的 Jordan block 为

$$
J_\lambda=\lambda I+N,
\qquad N^s=0.
$$

由二项式公式，

$$
J_\lambda^k
=\sum_{j=0}^{s-1}\binom{k}{j}\lambda^{k-j}N^j.
$$

当 $|\lambda|<1$ 时，每项都是“至多 $k^j$ 的多项式”乘“指数衰减 $|\lambda|^k$”，因此趋于零。全部 Jordan blocks 都趋于零，所以 $J^k\to0$，进而 $B^k=PJ^kP^{-1}\to0$。

### 不动点的存在性与唯一性

$\rho(B)<1$ 时，$1$ 不是 $B$ 的特征值，故 $I-B$ 可逆，固定点唯一。还可使用 Neumann series：

$$
(I-B)^{-1}=\sum_{j=0}^{\infty}B^j.
$$

因为部分和满足

$$
(I-B)\sum_{j=0}^{N}B^j=I-B^{N+1}\to I.
$$

## 矩阵分裂

线性系统 $Ax=b$ 可通过 splitting

$$
A=M-N
$$

改写为

$$
Mx_{k+1}=Nx_k+b,
$$

即

$$
x_{k+1}=M^{-1}Nx_k+M^{-1}b.
$$

迭代矩阵是 $B=M^{-1}N$，对任意初值收敛当且仅当

$$
\rho(M^{-1}N)<1.
$$

分析时不需要先知道精确解，只需识别迭代矩阵。

## 雅可比方法（Jacobi Method）

写

$$
A=D+L+U,
$$

其中 $D$ 是对角部分，$L,U$ 分别是严格下三角和上三角部分。雅可比方法为

$$
Dx_{k+1}=b-(L+U)x_k,
$$

故

$$
B_J=-D^{-1}(L+U)=I-D^{-1}A.
$$

**例子。** 对

$$
A=\begin{pmatrix}4&1\\1&3\end{pmatrix},
$$

有

$$
B_J=\begin{pmatrix}0&-1/4\\-1/3&0\end{pmatrix}.
$$

特征值为 $\pm1/\sqrt{12}$，所以 $\rho(B_J)<1$，雅可比迭代对任意初值收敛。

## 高斯－赛德尔方法（Gauss–Seidel Method）

高斯－赛德尔方法使用当前轮已经更新的分量：

$$
(D+L)x_{k+1}=b-Ux_k,
$$

所以

$$
B_{GS}=-(D+L)^{-1}U.
$$

对二维系统

$$
\begin{cases}
4x+y=1,\\
x+3y=2,
\end{cases}
$$

雅可比方法同时使用旧值：

$$
x_{k+1}=\frac{1-y_k}{4},
\qquad
y_{k+1}=\frac{2-x_k}{3}.
$$

高斯－赛德尔方法的第二式使用刚得到的 $x_{k+1}$：

$$
x_{k+1}=\frac{1-y_k}{4},
\qquad
y_{k+1}=\frac{2-x_{k+1}}{3}.
$$

二者不能仅凭名称比较速度，应比较各自迭代矩阵的谱半径。

## 理查森迭代（Richardson Iteration）

理查森迭代为

$$
x_{k+1}=x_k+\omega(b-Ax_k),
$$

其迭代矩阵为

$$
B_\omega=I-\omega A.
$$

若 $A$ 是对称正定矩阵（symmetric positive definite matrix），特征值满足

$$
0<\lambda_{\min}\le\lambda_i\le\lambda_{\max},
$$

则收敛条件为

$$
|1-\omega\lambda_i|<1
\quad\text{for all }i,
$$

等价于

$$
0<\omega<\frac{2}{\lambda_{\max}}.
$$

最优固定步长使区间两端的误差因子等模：

$$
1-\omega\lambda_{\min}
=-(1-\omega\lambda_{\max}),
$$

所以

$$
\omega_*=\frac{2}{\lambda_{\min}+\lambda_{\max}},
$$

对应收敛因子

$$
q_*=\frac{\kappa_2(A)-1}{\kappa_2(A)+1}.
$$

条件数越大，$q_*$ 越接近 $1$，迭代越慢。

## 范数界与瞬态增长

若某个诱导范数下 $\|B\|=q<1$，则

$$
\|e_k\|\le q^k\|e_0\|.
$$

这是简单的非渐近误差界。但 $\rho(B)<1$ 不保证预先指定的 $\|B\|_2<1$。非正规矩阵可能先放大误差再最终衰减，例如

$$
B=\begin{pmatrix}0&10\\0&0\end{pmatrix}.
$$

$B^2=0$，所以两步后误差归零；但某些向量第一步会被放大十倍。

## 幂零迭代

若 $\rho(B)=0$，则所有特征值为零，特征多项式为 $p_B(t)=t^n$。Cayley–Hamilton theorem 说明 $p_B(B)=0$，故

$$
B^n=0.
$$

所以误差至多经过 $n$ 步精确归零。注意 $\rho(B)=0$ 不意味着 $B=0$，只意味着 $B$ 是 nilpotent。

## 幂法（Power Method）

幂法用于求模最大的特征值及其特征向量。先假设 $A$ 可对角化，有特征向量基 $v_1,\ldots,v_n$，并且

$$
|\lambda_1|>|\lambda_2|\ge\cdots\ge|\lambda_n|.
$$

若初值

$$
x_0=\sum_{i=1}^nc_iv_i,
\qquad c_1\ne0,
$$

则

$$
A^kx_0
=\lambda_1^k
\left(
c_1v_1+
\sum_{i=2}^nc_i
\left(\frac{\lambda_i}{\lambda_1}\right)^k v_i
\right).
$$

归一化后方向趋向 $v_1$，渐近方向误差由 $|\lambda_2/\lambda_1|^k$ 控制。

这里“方向趋向”允许相差一个符号：若主特征值 $\lambda_1<0$，归一化向量可能在 $v_1$ 与 $-v_1$ 之间交替，但它所张成的一维 eigenspace 仍然收敛。

实际算法为

$$
y_{k+1}=Ax_k,
\qquad
x_{k+1}=\frac{y_{k+1}}{\|y_{k+1}\|_2}.
$$

瑞利商（Rayleigh quotient）

$$
\mu_k=\frac{x_k^TAx_k}{x_k^Tx_k}
$$

可用于估计特征值，特别是 $A$ 对称时。

### 失效条件

幂法可能失败或不能给出唯一方向：

- $c_1=0$，初值没有主特征向量分量；
- 最大模特征值不唯一；
- 最大模特征值形成复共轭对，实迭代可能旋转；
- 谱隙很小，$|\lambda_2/\lambda_1|$ 接近 $1$，收敛很慢。

## 反幂法与位移

若 $A$ 可逆，则 $A^{-1}$ 的特征值为 $1/\lambda_i$。对 $(A-\mu I)^{-1}$ 使用幂法，会突出最接近位移（shift）$\mu$ 的特征值，因为

$$
(A-\mu I)^{-1}v_i
=\frac1{\lambda_i-\mu}v_i.
$$

数值实现每步求解

$$
(A-\mu I)y_{k+1}=x_k
$$

而不是显式计算逆矩阵。

## 完整示例

设

$$
A=\begin{pmatrix}5&0\\0&2\end{pmatrix},
\qquad x_0=\begin{pmatrix}1\\1\end{pmatrix}.
$$

则

$$
A^kx_0
=\begin{pmatrix}5^k\\2^k\end{pmatrix}
=5^k\begin{pmatrix}1\\(2/5)^k\end{pmatrix}.
$$

第二坐标相对第一坐标的比例是 $(2/5)^k$。要使比例不超过 $10^{-3}$，需要

$$
k\ge\frac{\log(10^{-3})}{\log(2/5)}\approx7.54,
$$

因此 $k=8$ 足够。

## 练习

1. 对 $B=\operatorname{diag}(0.8,-0.6)$ 证明任意初值收敛，并给出误差界。
2. 对 $B=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ 计算 $B^k$，说明误差几步归零。
3. 对 $A=\operatorname{diag}(6,1)$、$x_0=(1,1)^T$，给出幂法的方向误差。
4. 推导 $2\times2$ 对称正定矩阵的最优理查森参数。
5. 说明“某一个特殊初值收敛”为什么不能推出 $\rho(B)<1$。

**Answer to 5.** 可取 $B=\operatorname{diag}(2,1/2)$ 与 $e_0=(0,1)^T$；该初值误差收敛，但 $\rho(B)=2$。

**上一章：** [奇异值分解与最小二乘](02-svd-least-squares.md)  
**下一章：** [不动点与压缩映射](04-fixed-points-contractions.md)
