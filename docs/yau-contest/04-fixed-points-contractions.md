# Fixed Points & Contractions

不动点迭代（fixed-point iteration）把方程求解写成反复应用一个映射。本章严格区分不动点的存在性、唯一性和算法收敛性，并完整证明巴拿赫不动点定理（Banach fixed-point theorem）。

## 不动点与皮卡迭代（Picard Iteration）

若映射 $g:X\to X$ 满足

$$
g(x^*)=x^*,
$$

则 $x^*$ 称为不动点（fixed point）。皮卡迭代为

$$
x_{k+1}=g(x_k).
$$

方程 $f(x)=0$ 可通过 $g(x)=x-\eta f(x)$ 改写为不动点方程（fixed-point equation），但不同 $\eta$ 会产生不同的收敛行为。

存在性、唯一性和迭代收敛性是三个不同命题。$g(x)=x^2$ 有两个不动点 $0,1$；从 $x_0=1/2$ 出发趋于 $0$，从 $x_0=3/2$ 出发发散。

## 度量空间与完备性

度量（metric）$d:X\times X\to[0,\infty)$ 满足：

1. $d(x,y)=0\iff x=y$；
2. $d(x,y)=d(y,x)$；
3. $d(x,z)\le d(x,y)+d(y,z)$。

在 $\mathbb R^n$ 中，$d(x,y)=\|x-y\|_2$ 是常用距离。

度量空间（metric space）$(X,d)$ 称为完备的（complete），如果每个柯西数列（Cauchy sequence）都收敛到 $X$ 中的点。$\mathbb R^n$ 完备；闭子集仍完备；开区间 $(0,1)$ 不完备，因为 $x_k=1/k$ 是其中的柯西数列，但极限 $0$ 不在该区间。

## 自映射与压缩映射

$g:X\to X$ 是自映射（self-map），表示迭代不会离开 $X$。若存在 $q\in[0,1)$ 使对所有 $x,y\in X$，

$$
d(g(x),g(y))\le q,d(x,y),
$$

则 $g$ 是压缩映射（contraction mapping），$q$ 是压缩因子（contraction factor）。

在实区间上，若 $g$ 可微且

$$
\sup_{x\in I}|g'(x)|\le q<1,
$$

由中值定理（Mean Value Theorem）可得压缩不等式。仅有导数界还不够，必须同时验证 $g(I)\subseteq I$。

## 巴拿赫不动点定理（Banach Fixed-Point Theorem）

**定理。** 设 $(X,d)$ 是非空完备度量空间，$g:X\to X$ 是压缩映射，压缩因子为 $q<1$。则：

1. $g$ 在 $X$ 中存在唯一不动点 $x^*$；
2. 对任意 $x_0\in X$，皮卡迭代 $x_{k+1}=g(x_k)$ 收敛到 $x^*$；
3. 具有可计算的先验与后验误差界。

### 第一步：相邻迭代点之差

由压缩性，

$$
d(x_{k+1},x_k)
\le q,d(x_k,x_{k-1})
\le\cdots\le q^k d(x_1,x_0).
$$

### 第二步：柯西性质

对 $m>n$，由三角不等式，

$$
\begin{aligned}
d(x_m,x_n)
&\le\sum_{j=n}^{m-1}d(x_{j+1},x_j)\\
&\le\sum_{j=n}^{m-1}q^j d(x_1,x_0)\\
&\le\frac{q^n}{1-q}d(x_1,x_0).
\end{aligned}
$$

右侧随 $n\to\infty$ 趋于零，因此 $(x_n)$ 是柯西数列。

### 第三步：存在性

$X$ 完备，所以存在 $x^*\in X$ 使 $x_n\to x^*$。压缩映射自动连续，因为

$$
d(g(x),g(y))\le qd(x,y).
$$

故

$$
x^*=\lim_{n\to\infty}x_{n+1}
=\lim_{n\to\infty}g(x_n)
=g(x^*).
$$

### 第四步：唯一性

若 $x^*,y^*$ 都是不动点，则

$$
d(x^*,y^*)
=d(g(x^*),g(y^*))
\le qd(x^*,y^*).
$$

由于 $q<1$，只能有 $d(x^*,y^*)=0$，即 $x^*=y^*$。$\square$

## 误差上界

令 $m\to\infty$，由证明中的估计得到先验误差界（a priori bound）：

$$
\boxed{
d(x_n,x^*)
\le\frac{q^n}{1-q}d(x_1,x_0)
}.
$$

把迭代从 $x_{n-1}$ 重新编号，也得到后验误差界（a posteriori bound）：

$$
\boxed{
d(x_n,x^*)
\le\frac{q}{1-q}d(x_n,x_{n-1})
}.
$$

第一式适合预估迭代次数，第二式适合根据已经观察到的相邻差决定停止。

若要求先验误差界不超过 $\varepsilon$，需要

$$
\frac{q^n}{1-q}d(x_1,x_0)\le\varepsilon.
$$

当 $0<q<1$ 时，$\log q<0$，故

$$
n\ge
\frac{\log\left(\varepsilon(1-q)/d(x_1,x_0)\right)}{\log q}.
$$

最后向上取整。$q=0$ 时 $g$ 是常值映射，一步到达不动点，应单独处理。

## 一维完整示例

设

$$
g(x)=\frac12\cos x,
\qquad I=[-1,1].
$$

**自映射（Self-map）。** 对 $x\in I$，$|g(x)|\le1/2$，所以 $g(I)\subseteq I$。

**压缩性（Contraction）。** $g'(x)=-(1/2)\sin x$，所以 $|g'(x)|\le1/2$。可取 $q=1/2$。

**完备性（Completeness）。** $I$ 是 $\mathbb R$ 的非空闭子集，因此完备。

巴拿赫定理保证 $I$ 中存在唯一不动点，且从任意 $x_0\in I$ 出发收敛。若 $x_0=0$，则 $x_1=1/2$，先验误差界为

$$
|x_n-x^*|
\le\frac{(1/2)^n}{1-1/2}\cdot\frac12
=2^{-n}.
$$

要保证误差严格小于 $10^{-8}$，取 $n=27$ 即可，因为 $2^{-27}<10^{-8}$。

## 不满足压缩条件时的存在性

若 $g:[a,b]\to[a,b]$ 连续，则至少存在一个不动点。定义

$$
h(x)=g(x)-x.
$$

由于 $g(a)\ge a$ 与 $g(b)\le b$，有 $h(a)\ge0$、$h(b)\le0$。介值定理给出 $c\in[a,b]$ 使 $h(c)=0$。

这个结论只保证存在，不保证唯一，也不保证皮卡迭代收敛。例如 $g(x)=1-x$ 将 $[0,1]$ 映回自身且连续，唯一不动点为 $1/2$；但除非 $x_0=1/2$，迭代会在 $x_0$ 与 $1-x_0$ 之间振荡。

## 不动点迭代的局部收敛性

设 $g(x^*)=x^*$、$g'$ 在 $x^*$ 附近连续且 $|g'(x^*)|<1$。可取 $q$ 满足

$$
|g'(x^*)|<q<1.
$$

由连续性，存在半径 $r>0$，使 $|x-x^*|\le r$ 时 $|g'(x)|\le q$。于是

$$
|g(x)-x^*|
=|g(x)-g(x^*)|
\le q|x-x^*|
\le qr<r.
$$

因此闭区间 $[x^*-r,x^*+r]$ 是不变集（invariant set），巴拿赫定理给出局部收敛。

若 $|g'(x^*)|>1$，不动点通常是排斥的（repelling）。若 $|g'(x^*)|=1$，一阶判据没有结论，必须检查更高阶项。

## 向量压缩映射

设 $D\subset\mathbb R^n$ 非空、闭且凸，$g:D\to D$ 连续可微（continuously differentiable）。若某个诱导范数下

$$
\sup_{x\in D}\|J_g(x)\|\le q<1,
$$

则 $g$ 是压缩映射。

对 $x,y\in D$，凸性保证线段 $y+t(x-y)$ 留在 $D$。由微积分基本定理，

$$
g(x)-g(y)
=\int_0^1J_g(y+t(x-y))(x-y)\,dt.
$$

取范数得

$$
\|g(x)-g(y)\|
\le\int_0^1q\|x-y\|\,dt
=q\|x-y\|.
$$

只知道 $\rho(J_g(x^*))<1$ 是局部线性化信息，不能直接推出整个区域上的一致压缩性。

## 二维完整示例

在闭方形 $D=[0,1]^2$ 上定义

$$
g(x,y)
=\left(\frac{x+y}{4},\frac{x-y}{4}+\frac12\right).
$$

先验证自映射条件。对 $(x,y)\in D$，

$$
0\le \frac{x+y}{4}\le\frac12,
\qquad
\frac14\le\frac{x-y}{4}+\frac12\le\frac34,
$$

故 $g(D)\subset D$。它的雅可比矩阵（Jacobian）是常矩阵

$$
J_g=
\begin{pmatrix}
1/4&1/4\\
1/4&-1/4
\end{pmatrix},
\qquad
J_g^TJ_g=\frac18I.
$$

因此欧几里得算子范数（Euclidean operator norm）为

$$
\|J_g\|_2=\sqrt{\lambda_{\max}(J_g^TJ_g)}
=\frac1{2\sqrt2}=:q<1.
$$

$D$ 是 $\mathbb R^2$ 的闭子集，所以在欧几里得度量（Euclidean metric）下完备。巴拿赫定理因而保证 $g$ 在 $D$ 内有唯一不动点，且从 $D$ 内任意初值出发的皮卡迭代都收敛。

固定点方程等价于

$$
3x-y=0,
\qquad
5y-x=2.
$$

解得

$$
(x^*,y^*)=\left(\frac17,\frac37\right).
$$

若取 $z_0=(0,0)^T$，则 $z_1=(0,1/2)^T$，所以 $\|z_1-z_0\|_2=1/2$。先验误差界为

$$
\|z_n-z^*\|_2
\le \frac{q^n}{1-q}\,\frac12.
$$

要保证该上界不超过 $\varepsilon$，只需

$$
n\ge
\frac{\log\!\bigl(2\varepsilon(1-q)\bigr)}{\log q}.
$$

取 $\varepsilon=10^{-4}$ 与 $q=1/(2\sqrt2)$，右端约为 $8.61$，故 $n=9$ 次迭代足够。这一例子完整展示了二维情形中的自映射、雅可比矩阵范数（Jacobian norm）、存在唯一性、误差上界和迭代次数。

## 不动点迭代格式的设计

同一方程可以产生不同迭代。对 $f(x)=x^2-2=0$，取

$$
g_\eta(x)=x-\eta(x^2-2).
$$

在正根 $\alpha=\sqrt2$，

$$
g_\eta'(\alpha)=1-2\eta\sqrt2.
$$

局部吸引的必要条件是

$$
|1-2\eta\sqrt2|<1,
$$

即 $0<\eta<1/\sqrt2$。当 $\eta=1/(2\sqrt2)$ 时导数为零，线性误差项消失，局部速度可能提高。算法设计的核心正是调整误差映射，而不只是保持相同不动点。

## 精确误差与定理上界

考虑

$$
g(x)=\frac{x+1}{4},
\qquad x_0=0.
$$

固定点为 $x^*=1/3$，且

$$
e_{n+1}=\frac14e_n,
\qquad
|e_n|=\frac13\,4^{-n}.
$$

要使 $|e_n|<10^{-5}$，需 $4^n>1/(3\times10^{-5})$，所以 $n=8$ 足够。

巴拿赫先验界使用 $q=1/4$、$|x_1-x_0|=1/4$：

$$
|e_n|
\le\frac{(1/4)^n}{1-1/4}\cdot\frac14
=\frac13\,4^{-n}.
$$

在这个线性例子中，通用界恰好等于精确误差。

## 练习

1. 证明 $g(x)=x/4+3$ 在 $\mathbb R$ 上是压缩映射，并求唯一不动点。
2. 说明 $g(x)=\cos x$ 为什么不能直接在整个 $\mathbb R$ 上使用统一 $q<1$ 的导数界。
3. 已知 $q=1/3$、$|x_1-x_0|=2$，计算 $|x_4-x^*|$ 的先验上界。
4. 给出有唯一不动点但皮卡迭代不收敛的连续自映射。
5. 设 $g:\mathbb R^2\to\mathbb R^2$ 为 $g(x)=Bx+c$。证明它在某诱导范数下为压缩映射时，结论与线性迭代章节一致。

**答案。** 第 1 题压缩因子 $1/4$，固定点 $4$。第 3 题上界为 $1/27$。第 4 题可取 $g(x)=1-x$ 于 $[0,1]$。

**上一章：** [线性迭代与幂法](03-linear-iterations-power.md)  
**下一章：** [牛顿法与收敛阶](05-newton-convergence.md)
