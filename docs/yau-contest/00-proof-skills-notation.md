# Proof Language & Calculus

本章建立后续证明所需的语言和微积分工具。内容按依赖顺序排列，不假设读者记得量词、极限、导数或泰勒定理（Taylor theorem）。

## 集合、函数与量词

集合是对象的总体。$x\in S$ 表示 $x$ 属于集合 $S$，$A\subseteq B$ 表示 $A$ 的每个元素也属于 $B$。常见数集为

$$
\mathbb N\subset\mathbb Z\subset\mathbb Q\subset\mathbb R\subset\mathbb C.
$$

函数 $f:X\to Y$ 把定义域 $X$ 中每个元素映到陪域 $Y$ 中唯一元素。两个量词决定命题的逻辑结构：

- 全称量词（universal quantifier）：$\forall x\in X$，对所有 $x$；
- 存在量词（existential quantifier）：$\exists x\in X$，存在至少一个 $x$。

量词顺序不能交换。例如

$$
\forall x\in\mathbb R\;\exists y\in\mathbb R:\ y>x
$$

为真；但 $\exists y\in\mathbb R\;\forall x\in\mathbb R:\ y>x$ 为假。

### 量词命题的否定

$$
\neg(\forall x\in X, P(x))\iff \exists x\in X, \neg P(x),
$$

$$
\neg(\exists x\in X, P(x))\iff \forall x\in X, \neg P(x).
$$

一个反例足以推翻全称命题，却不能证明另一个全称命题。

## 蕴含与等价

$P\Rightarrow Q$ 表示 $P$ 是 $Q$ 的充分条件，$Q$ 是 $P$ 的必要条件。$P\Longleftrightarrow Q$ 表示两边等价，必须分别证明两个方向。

逆否命题

$$
P\Rightarrow Q
\quad\Longleftrightarrow\quad
\neg Q\Rightarrow\neg P
$$

与原命题等价。逆命题 $Q\Rightarrow P$ 一般不等价。

## 直接证明、反证法与反例

### 直接证明

**命题。** 若 $a,b$ 为偶数，则 $a+b$ 为偶数。

**证明。** 存在整数 $m,n$ 使 $a=2m$、$b=2n$，于是 $a+b=2(m+n)$。由于 $m+n\in\mathbb Z$，故结论成立。$\square$

### 反证法

**命题。** $\sqrt2$ 不是有理数。

**证明。** 假设 $\sqrt2=p/q$，其中 $p,q$ 是互素正整数。则 $p^2=2q^2$，所以 $p$ 为偶数，记 $p=2r$。代回得 $q^2=2r^2$，故 $q$ 也为偶数，与互素矛盾。$\square$

### 反例

“特征值全为正的实矩阵一定对称”是错误命题，因为

$$
A=\begin{pmatrix}1&1\\0&2\end{pmatrix}
$$

的特征值为 $1,2$，但 $A^T\ne A$。

## 数学归纳法

数学归纳法包含基础步骤、归纳假设和归纳步骤。以

$$
1+2+\cdots+n=\frac{n(n+1)}2
$$

为例，$n=1$ 时成立。若 $n=k$ 时成立，则

$$
1+\cdots+k+(k+1)
=\frac{k(k+1)}2+(k+1)
=\frac{(k+1)(k+2)}2.
$$

因此命题对所有正整数成立。

## 绝对值与范数

绝对值满足三角不等式 $|a+b|\le |a|+|b|$。欧几里得范数（Euclidean norm）为

$$
\|x\|_2=\sqrt{x_1^2+\cdots+x_n^2}.
$$

柯西－施瓦茨不等式（Cauchy–Schwarz inequality）为

$$
|x^Ty|\le \|x\|_2\|y\|_2.
$$

**证明。** 若 $y=0$，结论成立。若 $y\ne0$，对任意 $t\in\mathbb R$，

$$
0\le\|x-ty\|_2^2
=\|x\|_2^2-2t x^Ty+t^2\|y\|_2^2.
$$

右侧二次多项式恒非负，故判别式不大于零，从而

$$
(x^Ty)^2\le\|x\|_2^2\|y\|_2^2.
$$

等号成立当且仅当 $x,y$ 线性相关。

## 数列与极限

数列 $(x_k)$ 收敛到 $L$ 的精确定义是

$$
\forall\varepsilon>0,
\ \exists N\in\mathbb N,
\ \forall k\ge N,
\quad |x_k-L|<\varepsilon.
$$

**例子。** 对 $x_k=1/k$，给定 $\varepsilon>0$，取整数 $N>1/\varepsilon$。当 $k\ge N$ 时，$|x_k|\le1/N<\varepsilon$，故 $x_k\to0$。

### 柯西数列与完备性

数列 $(x_k)$ 是柯西数列，如果

$$
\forall\varepsilon>0,
\ \exists N,
\ \forall m,n\ge N,
\quad |x_m-x_n|<\varepsilon.
$$

实数空间 $\mathbb R$ 是完备的（complete）：每个柯西数列（Cauchy sequence）都收敛到某个实数。后面的巴拿赫不动点定理（Banach fixed-point theorem）正是用完备性把“迭代项彼此靠近”转化成“存在极限”。

## 连续性与介值定理

函数 $f$ 在 $a$ 连续，表示 $\lim_{x\to a}f(x)=f(a)$。其 $\varepsilon$–$\delta$ 形式为

$$
\forall\varepsilon>0,
\ \exists\delta>0,
\quad |x-a|<\delta
\Rightarrow |f(x)-f(a)|<\varepsilon.
$$

**介值定理（Intermediate Value Theorem）。** 若 $f$ 在 $[a,b]$ 连续，且 $f(a)f(b)<0$，则存在 $c\in(a,b)$ 使 $f(c)=0$。

这个定理给出存在性，但不给唯一性。

## 导数与中值定理

导数定义为

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h.
$$

对 $f(x)=x^2$，差商为 $2x+h$，所以 $f'(x)=2x$。

**中值定理（Mean Value Theorem）。** 若 $f$ 在 $[a,b]$ 连续、在 $(a,b)$ 可微，则存在 $\xi\in(a,b)$ 使

$$
f(b)-f(a)=f'(\xi)(b-a).
$$

因此若 $|f'(x)|\le M$ 在区间内成立，就有

$$
|f(b)-f(a)|\le M|b-a|.
$$

## 梯度、雅可比矩阵（Jacobian）与海森矩阵（Hessian）

对 $f:\mathbb R^n\to\mathbb R$，梯度（gradient）是

$$
\nabla f(x)=
\begin{pmatrix}
\partial f/\partial x_1\\
\vdots\\
\partial f/\partial x_n
\end{pmatrix}.
$$

对 $g:\mathbb R^n\to\mathbb R^m$，雅可比矩阵（Jacobian matrix）为

$$
J_g(x)=
\left(\frac{\partial g_i}{\partial x_j}\right)_{m\times n}.
$$

标量函数的海森矩阵（Hessian matrix）是 $\nabla^2 f(x)$。例如

$$
f(x_1,x_2)=x_1^2+3x_1x_2+2x_2^2
$$

满足

$$
\nabla f=
\begin{pmatrix}2x_1+3x_2\\3x_1+4x_2\end{pmatrix},
\qquad
\nabla^2 f=
\begin{pmatrix}2&3\\3&4\end{pmatrix}.
$$

## 泰勒定理（Taylor Theorem）

若 $f$ 在包含 $x$ 与 $x+h$ 的区间上二次连续可微，则存在两点之间的 $\xi$ 使

$$
f(x+h)=f(x)+f'(x)h+\frac12 f''(\xi)h^2.
$$

若 $f$ 三次连续可微，也可写成

$$
f(x+h)=f(x)+f'(x)h+\frac12f''(x)h^2+O(h^3).
$$

$r(h)=O(h^p)$ 表示存在 $C,\delta>0$，当 $|h|<\delta$ 时 $|r(h)|\le C|h|^p$。而 $r(h)=o(h^p)$ 表示 $r(h)/h^p\to0$。

对 $e^x$ 在 $0$ 展开：

$$
e^h=1+h+\frac{h^2}{2}+O(h^3).
$$

## 误差序列与收敛阶

定义误差（error）$e_k=x_k-x^*$。若存在 $p\ge1$ 与 $C\in(0,\infty)$ 使

$$
\lim_{k\to\infty}\frac{|e_{k+1}|}{|e_k|^p}=C,
$$

则称迭代具有 $p$ 阶收敛。$p=1$ 且 $C<1$ 为线性收敛（linear convergence）；$p=2$ 为二次收敛（quadratic convergence）。

只证明 $e_{k+1}=O(e_k^2)$ 通常只能说明至少二阶；要断言恰为二阶，还须证明二次项系数非零。

## 完整证明示例

考虑

$$
x_{k+1}=\frac12x_k+1.
$$

固定点为 $x^*=2$。令 $e_k=x_k-2$，则

$$
e_{k+1}=\frac12e_k,
\qquad
e_k=2^{-k}e_0.
$$

因为 $2^{-k}\to0$，故任意初值都收敛到 $2$。要保证 $|e_k|\le\varepsilon$，只需

$$
k\ge \frac{\log(|e_0|/\varepsilon)}{\log2}.
$$

这个证明包含候选极限、误差方程、极限和步数界，逻辑闭合。

## 练习

1. 写出“每个实对称矩阵都有实特征值”的量词结构及否定。
2. 使用柯西－施瓦茨不等式证明欧几里得范数的三角不等式。
3. 用 $\varepsilon$–$N$ 定义证明 $3^{-k}\to0$。
4. 对 $f(x)=\log x$ 写出以 $x=1$ 为中心的二阶泰勒展开（Taylor expansion）。
5. 对 $x_{k+1}=x_k/3+2/3$ 求固定点、精确误差式及达到 $10^{-6}$ 误差所需的充分步数。

**答案。** 第 3 题可取 $N>\log(1/\varepsilon)/\log3$。第 4 题为 $\log(1+h)=h-h^2/2+O(h^3)$。第 5 题固定点为 $1$，且 $e_k=3^{-k}e_0$。

**下一章：** [矩阵范数与谱理论](01-matrix-norms-spectral.md)
