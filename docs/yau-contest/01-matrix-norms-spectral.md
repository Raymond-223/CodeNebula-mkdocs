# Matrix Norms & Spectral Theory

矩阵既可以看成数字表，也可以看成线性映射（linear map）。后一个观点解释了范数、特征值、正定性和迭代收敛之间的关系。

## 线性映射与矩阵维数

$A\in\mathbb R^{m\times n}$ 定义映射

$$
A:\mathbb R^n\to\mathbb R^m,
\qquad x\mapsto Ax.
$$

矩阵的 $n$ 列是标准基向量 $e_1,\ldots,e_n$ 的像。若

$$
A=\begin{pmatrix}1&2\\3&4\end{pmatrix},
$$

则 $Ae_1=(1,3)^T$、$Ae_2=(2,4)^T$。矩阵乘法 $AB$ 表示先施加 $B$，再施加 $A$，所以一般 $AB\ne BA$。

### 矩阵乘法

矩阵乘向量按“行乘列”计算。以上面的 $A$ 和 $x=(5,-1)^T$ 为例，

$$
Ax=
\begin{pmatrix}
1\cdot5+2\cdot(-1)\\
3\cdot5+4\cdot(-1)
\end{pmatrix}
=\begin{pmatrix}3\\11\end{pmatrix}.
$$

若 $A$ 是 $m\times n$、$B$ 是 $n\times p$，那么 $AB$ 是 $m\times p$，其第 $(i,j)$ 个元素为

$$
(AB)_{ij}=\sum_{k=1}^na_{ik}b_{kj}.
$$

内侧维数 $n$ 必须相同；结果保留外侧维数 $m\times p$。

### 张成、线性无关、基与维数

给定向量 $v_1,\ldots,v_k$，所有形如

$$
c_1v_1+\cdots+c_kv_k
$$

的向量组成它们的张成空间（span），记作 $\operatorname{span}\{v_1,\ldots,v_k\}$。这里的 $c_i$ 可以取任意实数。例如 $(1,0)^T$ 与 $(0,1)^T$ 能张成整个 $\mathbb R^2$，因为任意 $(a,b)^T$ 都能写成 $a(1,0)^T+b(0,1)^T$。

若等式

$$
c_1v_1+\cdots+c_kv_k=0
$$

只有全部 $c_i=0$ 这一组解，就称这些向量线性无关（linearly independent）；如果存在不全为零的系数使等式成立，就称线性相关（linearly dependent）。例如 $(1,0)^T$ 与 $(2,0)^T$ 线性相关，因为 $2(1,0)^T-(2,0)^T=0$。这意味着第二个向量没有增加新方向。

一个向量组若既线性无关又张成空间，就叫这个空间的一组基（basis）。向量在一组基下的表示是唯一的：若同一个向量有两组系数，把两种表示相减就得到基向量的一组非平凡线性关系，与线性无关矛盾。有限维空间任意一组基所含向量个数相同，这个数叫维数（dimension）。因此 $\mathbb R^n$ 的标准基有 $n$ 个向量，维数就是 $n$。

这些词之间的计算联系是：把 $v_1,\ldots,v_k$ 作为矩阵的列，对齐次方程

$$
\begin{pmatrix}v_1&\cdots&v_k\end{pmatrix}c=0
$$

做高斯消元。若只有零解，则列向量线性无关；若出现自由变量，则它们线性相关。主元列对应真正新增的方向。

### 消元与行列式

高斯消元（Gaussian elimination）通过交换两行、把一行乘非零常数、把一行的倍数加到另一行，把线性方程组化成阶梯形。主元个数就是矩阵的秩。对二阶方阵

先完整算一个三元方程组：

$$
\begin{cases}
x+y+z=6,\\
2x-y+z=3,\\
x+2y-z=2.
\end{cases}
$$

写成增广矩阵并进行行变换：

$$
\begin{aligned}
\left[
\begin{array}{ccc|c}
1&1&1&6\\
2&-1&1&3\\
1&2&-1&2
\end{array}
\right]
&\xrightarrow{R_2\leftarrow R_2-2R_1,\;R_3\leftarrow R_3-R_1}
\left[
\begin{array}{ccc|c}
1&1&1&6\\
0&-3&-1&-9\\
0&1&-2&-4
\end{array}
\right]\\
&\xrightarrow{R_2\leftrightarrow R_3}
\left[
\begin{array}{ccc|c}
1&1&1&6\\
0&1&-2&-4\\
0&-3&-1&-9
\end{array}
\right]\\
&\xrightarrow{R_3\leftarrow R_3+3R_2}
\left[
\begin{array}{ccc|c}
1&1&1&6\\
0&1&-2&-4\\
0&0&-7&-21
\end{array}
\right].
\end{aligned}
$$

从最后一行回代：$z=3$，第二行给 $y-2z=-4$，所以 $y=2$；第一行再给 $x=1$。三个未知量所在列都有主元，因此没有自由变量，系数矩阵的秩为 $3$。如果最后一行变成 $0=0$，就会出现自由变量；若变成 $0=1$，方程组则无解。

**立即练习。** 用消元解 $2x+y=5$、$x-y=1$，并判断系数矩阵的秩。

??? tip "第一步提示"

    把第二行的两倍从第一行减去，先消去 $x$。

??? tip "关键转化"

    增广矩阵可化为

    $$
    \left[\begin{array}{cc|c}1&-1&1\\0&3&3\end{array}\right].
    $$

??? proof "完整解答"

    第二行给 $y=1$，回代得到 $x=2$。两个未知量列都有主元，故系数矩阵的秩为 $2$；方程组有唯一解 $(2,1)^T$。

对二阶方阵

$$
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
\det(A)=ad-bc.
$$

若 $\det(A)\ne0$，两行不会在消元后产生零行，方程 $Ax=y$ 对每个 $y$ 有唯一解；若 $\det(A)=0$，则存在非零方向被 $A$ 压到零。后面的特征值计算会把 $A-\lambda I$ 的行列式设为零，本质上就是寻找这种非零零空间。

### 秩、核与列空间

零空间（kernel）与列空间（column space）定义为

$$
\ker(A)=\{x:Ax=0\},
\qquad
\operatorname{Col}(A)=\{Ax:x\in\mathbb R^n\}.
$$

**基扩充引理。** 有限维向量空间中的任意线性无关向量组，都可以扩充为这个空间的一组基。

??? proof "证明"

    设空间维数为 $n$，已有线性无关向量 $u_1,\ldots,u_k$。若它们已经张成整个空间，证明结束。否则可选取一个不在其张成空间中的向量 $u_{k+1}$；加入它以后向量组仍线性无关。若仍未张成全空间，就重复这一步。

    线性无关向量的个数不可能超过 $n$，所以这个过程至多进行 $n-k$ 次就必须停止。停止时所得向量组既线性无关又张成整个空间，因此是一组基。

**秩－零化度定理（rank–nullity theorem）。** 对线性映射 $A:\mathbb R^n\to\mathbb R^m$，

$$
\operatorname{rank}(A)+\dim\ker(A)=n.
$$

这里 $n$ 是定义域的维数，而不是矩阵的行数。定理说明：定义域中的自由方向分成两类，一类被 $A$ 压到零，另一类在像空间中贡献独立方向。

??? proof "证明"

    设 $\ker(A)$ 的一组基为

    $$
    u_1,\ldots,u_k.
    $$

    根据基扩充原理，可添加向量 $v_1,\ldots,v_{n-k}$，使

    $$
    u_1,\ldots,u_k,v_1,\ldots,v_{n-k}
    $$

    成为 $\mathbb R^n$ 的一组基。下面证明 $Av_1,\ldots,Av_{n-k}$ 是 $\operatorname{Col}(A)$ 的一组基。

    先证线性无关。若

    $$
    c_1Av_1+\cdots+c_{n-k}Av_{n-k}=0,
    $$

    则

    $$
    A(c_1v_1+\cdots+c_{n-k}v_{n-k})=0.
    $$

    因而 $c_1v_1+\cdots+c_{n-k}v_{n-k}\in\ker(A)$，可写成 $u_1,\ldots,u_k$ 的线性组合。把等式两边移到同一侧，就得到上述定义域基的一组线性关系，所以全部 $c_j=0$。

    再证张成性。任取 $y\in\operatorname{Col}(A)$，存在 $x\in\mathbb R^n$ 使 $y=Ax$。把 $x$ 按上述基展开：

    $$
    x=\sum_{i=1}^ka_iu_i+\sum_{j=1}^{n-k}b_jv_j.
    $$

    因为 $Au_i=0$，所以

    $$
    y=Ax=\sum_{j=1}^{n-k}b_jAv_j.
    $$

    因此 $Av_1,\ldots,Av_{n-k}$ 确实构成列空间的一组基，于是

    $$
    \operatorname{rank}(A)=n-k,
    \qquad \dim\ker(A)=k.
    $$

    两式相加即得结论。

**推论。** $A$ 的列线性无关当且仅当 $\ker(A)=\{0\}$。

??? proof "证明"

    $A$ 的列线性无关等价于 $\operatorname{rank}(A)=n$。由秩－零化度定理，这又等价于 $\dim\ker(A)=0$，也就是 $\ker(A)=\{0\}$。

## 特征值与特征向量

非零向量 $v$ 若满足

$$
Av=\lambda v,
$$

则 $v$ 是特征向量（eigenvector），$\lambda$ 是特征值（eigenvalue）。它表示 $A$ 在方向 $v$ 上只做伸缩或反向。

**命题。** 数 $\lambda$ 是方阵 $A$ 的特征值，当且仅当

$$
\det(A-\lambda I)=0.
$$

??? proof "证明"

    方程 $Av=\lambda v$ 等价于 $(A-\lambda I)v=0$。由秩－零化度定理，它存在非零解，当且仅当 $A-\lambda I$ 不满秩。

    下面补出所用的行列式判据。高斯消元的三种初等行变换分别使行列式保持不变、乘以非零常数或改变符号，因此不会改变“行列式是否为零”。任意方阵经高斯消元得到行阶梯形矩阵；它满秩时有 $n$ 个非零主元，行列式是非零主元之积（再乘一个非零因子）；不满秩时至少有一行全零，行列式为零。因此方阵满秩当且仅当行列式非零。应用于 $A-\lambda I$ 即得结论。

**手算例子。** 设

$$
A=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$

特征多项式为

$$
\det(A-\lambda I)
=(2-\lambda)^2-1
=(\lambda-1)(\lambda-3).
$$

对应 $\lambda_1=3$ 可取 $v_1=(1,1)^T$；对应 $\lambda_2=1$ 可取 $v_2=(1,-1)^T$。

## 向量范数

向量范数（vector norm）$\|\cdot\|$ 必须满足：

1. 正定性：$\|x\|\ge0$，且 $\|x\|=0\iff x=0$；
2. 齐次性：$\|\alpha x\|=|\alpha|\|x\|$；
3. 三角不等式：$\|x+y\|\le\|x\|+\|y\|$。

常见范数为

$$
\|x\|_1=\sum_i|x_i|,
\qquad
\|x\|_2=\sqrt{\sum_i x_i^2},
\qquad
\|x\|_\infty=\max_i|x_i|.
$$

对 $x=(1,-2,2)^T$，三者分别为 $5,3,2$。

**有限维范数等价定理。** 在有限维向量空间中，任意两个范数 $\|\cdot\|_a,\|\cdot\|_b$ 之间都存在与 $x$ 无关的常数 $c,C>0$，使

$$
c\|x\|_a\le\|x\|_b\le C\|x\|_a.
$$

??? proof "证明"

    先把任意范数 $N(x)$ 与欧几里得范数比较。设 $e_1,\ldots,e_n$ 是标准基，$x=\sum_i x_ie_i$。由三角不等式和柯西－施瓦茨不等式，

    $$
    N(x)
    \le\sum_{i=1}^n|x_i|N(e_i)
    \le\left(\sum_{i=1}^nx_i^2\right)^{1/2}
       \left(\sum_{i=1}^nN(e_i)^2\right)^{1/2}.
    $$

    记 $M=\bigl(\sum_iN(e_i)^2\bigr)^{1/2}$，则

    $$
    N(x)\le M\|x\|_2.
    $$

    反三角不等式给出

    $$
    |N(x)-N(y)|\le N(x-y)\le M\|x-y\|_2,
    $$

    所以 $N$ 关于欧几里得距离连续。欧几里得单位球面

    $$
    S=\{x\in\mathbb R^n:\|x\|_2=1\}
    $$

    是闭且有界的有限维集合，因此是紧集。连续函数 $N$ 在 $S$ 上取得最小值 $m$。由于 $S$ 不含零向量且范数只在零点取零，故 $m>0$。

    对任意 $x\ne0$，令 $u=x/\|x\|_2\in S$。由齐次性，

    $$
    N(x)=\|x\|_2N(u),
    $$

    从而

    $$
    m\|x\|_2\le N(x)\le M\|x\|_2.
    $$

    分别把 $\|\cdot\|_a$ 和 $\|\cdot\|_b$ 与 $\|\cdot\|_2$ 比较，再消去 $\|x\|_2$，便得到两个任意范数之间的上下界。

证明中“单位球面是紧集”正是有限维条件发挥作用的位置。有限维有界序列可以逐坐标抽取收敛子列；无限维空间的单位球通常不具备这种性质。

### 无限维空间中的不等价范数

**命题。** 无限维向量空间中的两个范数不一定等价。

??? proof "反例证明"

    考虑无限维向量空间 $C[0,1]$，即 $[0,1]$ 上的实连续函数。定义

    $$
    \|f\|_\infty=\max_{0\le x\le1}|f(x)|,
    \qquad
    \|f\|_1=\int_0^1|f(x)|\,dx.
    $$

    总有 $\|f\|_1\le\|f\|_\infty$。若两范数等价，还应存在与 $f$ 无关的常数 $c>0$，使

    $$
    c\|f\|_\infty\le\|f\|_1
    $$

    对全部连续函数成立。取 $f_n(x)=x^n$，则

    $$
    \|f_n\|_\infty=1,
    \qquad
    \|f_n\|_1=\int_0^1x^n\,dx=\frac1{n+1}.
    $$

    代入假设得到 $c\le1/(n+1)$ 对所有 $n$ 成立，这是不可能的。几何上，$f_n$ 的高度一直为 $1$，但非零部分越来越集中在 $x=1$ 附近，积分面积趋于零。因此无限维中不能仅凭“都是范数”就断言它们等价。

因此有限维中的“是否收敛”不依赖所选范数，但数值界的常数会依赖范数。

## 对称矩阵与谱定理

实矩阵 $A$ 若满足 $A^T=A$，称为实对称矩阵（real symmetric matrix）。

**谱定理（Spectral Theorem）。** 每个实对称矩阵都存在正交矩阵 $Q$ 和实对角矩阵 $\Lambda$，使

$$
A=Q\Lambda Q^T,
\qquad Q^TQ=I.
$$

$Q$ 的列是标准正交特征向量，$\Lambda$ 的对角元是对应特征值。

??? proof "证明"

    对矩阵阶数 $n$ 使用归纳法。$n=1$ 时，矩阵只有一个实数元素 $a$，可直接取 $Q=(1)$、$\Lambda=(a)$，所以结论成立。设结论对 $(n-1)\times(n-1)$ 实对称矩阵成立。

    在单位球面 $S=\{x:\|x\|_2=1\}$ 上考虑连续函数

    $$
    R_A(x)=x^TAx.
    $$

    单位球面紧，所以 $R_A$ 在某个单位向量 $q_1$ 处取得最大值。任取满足 $y^Tq_1=0$ 的向量 $y$，考察

    $$
    \phi(t)=R_A\!\left(\frac{q_1+ty}{\|q_1+ty\|_2}\right).
    $$

    $t=0$ 是极大点，因此 $\phi'(0)=0$。直接求导，并使用 $y^Tq_1=0$，得到

    $$
    \phi'(0)=2y^TAq_1=0.
    $$

    这对每个 $y\perp q_1$ 都成立，所以 $Aq_1$ 与 $q_1$ 平行。存在实数 $\lambda_1$ 使

    $$
    Aq_1=\lambda_1q_1.
    $$

    现在看正交补空间 $q_1^\perp$。若 $z\in q_1^\perp$，则利用 $A^T=A$，

    $$
    q_1^TAz=(Aq_1)^Tz=\lambda_1q_1^Tz=0.
    $$

    因此 $Az\in q_1^\perp$，即该正交补空间在 $A$ 下不变。$A$ 在这个 $(n-1)$ 维空间上的限制仍是实对称线性映射。由归纳假设，$q_1^\perp$ 有一组标准正交特征向量 $q_2,\ldots,q_n$。

    于是 $q_1,\ldots,q_n$ 是 $\mathbb R^n$ 的标准正交特征向量基。令 $Q=(q_1,\ldots,q_n)$，并把相应特征值放入 $\Lambda$，便有

    $$
    AQ=Q\Lambda,
    \qquad A=Q\Lambda Q^T.
    $$

### 瑞利商（Rayleigh Quotient）

对 $x\ne0$，瑞利商定义为

$$
R_A(x)=\frac{x^TAx}{x^Tx}.
$$

若 $A$ 对称，设 $A=Q\Lambda Q^T$ 且 $y=Q^Tx$。由于 $Q$ 正交，$x^Tx=y^Ty$，于是

$$
R_A(x)
=\frac{\sum_i\lambda_i y_i^2}{\sum_i y_i^2}.
$$

令 $w_i=y_i^2/\sum_jy_j^2$，则 $w_i\ge0$ 且 $\sum_iw_i=1$。因此瑞利商是特征值的加权平均：

$$
\lambda_{\min}(A)
\le R_A(x)
\le\lambda_{\max}(A).
$$

上下界分别在最小、最大特征值的特征向量方向取得。

??? proof "瑞利商界的证明"

    因为 $y=Q^Tx\ne0$，令

    $$
    w_i=\frac{y_i^2}{\sum_jy_j^2}.
    $$

    每个 $w_i\ge0$ 且 $\sum_iw_i=1$，所以

    $$
    R_A(x)=\sum_iw_i\lambda_i
    $$

    是全部特征值的凸组合。任何凸组合都不小于最小分量且不大于最大分量，故得到所写上下界。取 $x$ 为对应的单位特征向量时，只有一个权重等于 $1$，所以上下界都能达到。

## 正定性

实对称矩阵 $A$ 称为正定矩阵（positive definite matrix），若对所有 $x\ne0$，

$$
x^TAx>0.
$$

利用谱定理，

$$
x^TAx
=y^T\Lambda y
=\sum_i\lambda_i y_i^2.
$$

因此

$$
A\succ0
\quad\Longleftrightarrow\quad
\lambda_i(A)>0\ \text{for all }i.
$$

??? proof "证明"

    若全部特征值为正，则对任意 $x\ne0$，$y=Q^Tx\ne0$，从而

    $$
    x^TAx=\sum_i\lambda_i y_i^2>0.
    $$

    反过来，若 $A$ 正定，取任意单位特征向量 $q_i$，便有

    $$
    0<q_i^TAq_i=q_i^T(\lambda_iq_i)=\lambda_i.
    $$

    因此每个特征值都为正。

非对称矩阵即使特征值全正，也不能直接称作正定矩阵；二次型只依赖其对称部分 $(A+A^T)/2$。

## 格拉姆矩阵（Gram Matrix）

对任意 $A\in\mathbb R^{m\times n}$，

$$
(A^TA)^T=A^TA,
$$

且

$$
x^TA^TAx=\|Ax\|_2^2\ge0.
$$

所以 $A^TA$ 总是对称半正定矩阵（symmetric positive semidefinite matrix）。并且

$$
A^TA\succ0
\quad\Longleftrightarrow\quad
\ker(A)=\{0\}
\quad\Longleftrightarrow\quad
A\text{ has full column rank}.
$$

这条结论解释了满列秩时正规方程具有唯一解，也构成奇异值分解的入口。

??? proof "证明"

    已经由 $x^TA^TAx=\|Ax\|_2^2\ge0$ 得到半正定性。进一步，

    $$
    A^TA\succ0
    $$

    等价于对每个 $x\ne0$ 都有 $\|Ax\|_2^2>0$，也就是不存在非零 $x$ 满足 $Ax=0$。这正是

    $$
    \ker(A)=\{0\}.
    $$

    根据秩－零化度定理，$\ker(A)=\{0\}$ 等价于 $\operatorname{rank}(A)=n$，即 $A$ 的 $n$ 列线性无关，也就是满列秩。

## 诱导矩阵范数

由向量范数诱导的算子范数（operator norm）定义为

$$
\|A\|=\sup_{x\ne0}\frac{\|Ax\|}{\|x\|}
=\sup_{\|x\|=1}\|Ax\|.
$$

它表示 $A$ 对单位向量的最大放大倍数。由定义立即得到相容性（compatibility）：

$$
\|Ax\|\le\|A\|\|x\|.
$$

三个常用诱导范数有显式公式：

$$
\|A\|_1=\max_j\sum_i|a_{ij}|,
$$

即最大绝对列和；

$$
\|A\|_\infty=\max_i\sum_j|a_{ij}|,
$$

即最大绝对行和；

$$
\|A\|_2=\sqrt{\lambda_{\max}(A^TA)}.
$$

??? proof "三个诱导范数公式的证明"

    对 $1$-范数，记第 $j$ 列绝对值之和为 $c_j=\sum_i|a_{ij}|$。任意 $x$ 满足

    $$
    \begin{aligned}
    \|Ax\|_1
    &=\sum_i\left|\sum_j a_{ij}x_j\right|\\
    &\le\sum_j\left(\sum_i|a_{ij}|\right)|x_j|\\
    &\le\left(\max_jc_j\right)\|x\|_1.
    \end{aligned}
    $$

    因而 $\|A\|_1\le\max_jc_j$。若 $j_*$ 是达到最大列和的列，取 $x=e_{j_*}$，则 $\|x\|_1=1$ 且 $\|Ax\|_1=c_{j_*}$，所以上界可以达到。

    对 $\infty$-范数，令 $r_i=\sum_j|a_{ij}|$。有

    $$
    |(Ax)_i|
    \le\sum_j|a_{ij}|\,|x_j|
    \le r_i\|x\|_\infty,
    $$

    所以 $\|A\|_\infty\le\max_i r_i$。若第 $i_*$ 行达到最大行和，选择 $x_j=\operatorname{sgn}(a_{i_*j})$；零元素对应的符号可任取。此时 $\|x\|_\infty=1$，且第 $i_*$ 个输出分量的绝对值等于 $r_{i_*}$，故上界也能达到。

    对 $2$-范数，矩阵 $A^TA$ 对称半正定。由谱定理，任意单位向量 $x$ 都满足

    $$
    \|Ax\|_2^2=x^TA^TAx\le\lambda_{\max}(A^TA).
    $$

    取 $x$ 为最大特征值对应的单位特征向量时等号成立。因此

    $$
    \|A\|_2=\sqrt{\lambda_{\max}(A^TA)}.
    $$

    下一章定义奇异值后，会把这个平方根记为最大奇异值 $\sigma_{\max}(A)$；这里的证明只使用本章已经证明的谱定理。

### 弗罗贝尼乌斯范数（Frobenius Norm）

弗罗贝尼乌斯范数定义为

$$
\|A\|_F=\sqrt{\sum_{i,j}a_{ij}^2}
=\sqrt{\operatorname{tr}(A^TA)}.
$$

它是矩阵元素构成向量后的欧几里得范数（Euclidean norm），但对 $n>1$ 并不是由同一个 $n$ 维向量范数诱导的算子范数。仍有

$$
\|AB\|_F\le\|A\|_2\|B\|_F.
$$

??? proof "证明"

    把 $B$ 的列记为 $b_1,\ldots,b_p$。矩阵 $AB$ 的列就是 $Ab_1,\ldots,Ab_p$，因此

    $$
    \|AB\|_F^2
    =\sum_{j=1}^p\|Ab_j\|_2^2
    \le\sum_{j=1}^p\|A\|_2^2\|b_j\|_2^2
    =\|A\|_2^2\|B\|_F^2.
    $$

    两边开平方即得结论。

## 次乘性

**定理。** 任意诱导矩阵范数满足

$$
\|AB\|\le\|A\|\|B\|.
$$

??? proof "证明"

    对任意 $x\ne0$，

    $$
    \|ABx\|
    \le\|A\|\|Bx\|
    \le\|A\|\|B\|\|x\|.
    $$

    两边除以 $\|x\|$，再对所有 $x\ne0$ 取上确界，即得结论。

这个证明说明“诱导”不是装饰：正是定义中的最大放大倍数带来了乘法相容性。

## 谱半径

谱半径（spectral radius）定义为

$$
\rho(A)=\max_{\lambda\in\sigma(A)}|\lambda|,
$$

其中 $\sigma(A)$ 是全部特征值的集合。特征值可以是负数或复数，所以必须取模。

**定理。** 对任意诱导矩阵范数，

$$
\rho(A)\le\|A\|.
$$

??? proof "证明"

    若 $Av=\lambda v$ 且 $v\ne0$，则

    $$
    |\lambda|\|v\|
    =\|\lambda v\|
    =\|Av\|
    \le\|A\|\|v\|.
    $$

    约去 $\|v\|$ 得 $|\lambda|\le\|A\|$，再对全部特征值取最大值。对于复特征值，在 $\mathbb C^n$ 上使用同一诱导范数。

反向不成立。矩阵

$$
A=\begin{pmatrix}0&10\\0&0\end{pmatrix}
$$

满足 $A^2=0$，故全部特征值为零，$\rho(A)=0$；但 $\|A\|_2=10$。

## 格什戈林圆盘定理（Gershgorin Circle Theorem）

对方阵 $A=(a_{ij})$，定义第 $i$ 个格什戈林圆盘（Gershgorin disc）：

$$
D_i=\left\{z\in\mathbb C:
|z-a_{ii}|\le\sum_{j\ne i}|a_{ij}|
\right\}.
$$

**定理。** $A$ 的每个特征值至少落在一个 $D_i$ 中。

??? proof "证明"

    设 $Av=\lambda v$，选择满足 $|v_i|=\|v\|_\infty>0$ 的指标 $i$。第 $i$ 行给出

    $$
    (\lambda-a_{ii})v_i=\sum_{j\ne i}a_{ij}v_j.
    $$

    取绝对值并用 $|v_j|\le|v_i|$：

    $$
    |\lambda-a_{ii}|\,|v_i|
    \le\sum_{j\ne i}|a_{ij}|\,|v_j|
    \le\left(\sum_{j\ne i}|a_{ij}|\right)|v_i|.
    $$

    约去 $|v_i|$ 即得 $\lambda\in D_i$。

**推论。** 若 $|a_{ii}|>\sum_{j\ne i}|a_{ij}|$ 对每行成立，则 $A$ 可逆。

??? proof "证明"

    严格行对角占优说明每个格什戈林圆盘都不含零。由格什戈林圆盘定理，$0$ 不是 $A$ 的特征值，所以 $\ker(A)=\{0\}$。方阵定义的线性映射从 $\mathbb R^n$ 到自身；由秩－零化度定理，它满秩，因而可逆。

## 练习

1. 计算 $A=\begin{pmatrix}2&-1\\1&3\end{pmatrix}$ 的 $1$-范数、$\infty$-范数与弗罗贝尼乌斯范数。
2. 证明 $\|A^k\|\le\|A\|^k$。
3. 对 $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ 计算瑞利商的最小值和最大值。
4. 证明严格行对角占优矩阵可逆，不使用格什戈林圆盘定理，而从 $Ax=0$ 选取最大模分量证明。
5. 给出 $\rho(A)<1$ 但 $\|A\|_2>1$ 的矩阵，并直接计算验证。

??? tip "第一步提示"

    第 1 题按列和、行和、元素平方和分别计算。第 2 题重复使用次乘性。第 4 题从 $Ax=0$ 出发，选取绝对值最大的分量。第 5 题尝试非零的严格上三角矩阵。

**答案。** 第 1 题为 $4,4,\sqrt{15}$。第 3 题为 $1,3$。第 5 题可用本章的幂零矩阵例子。

**上一章：** [证明语言与微积分](00-proof-skills-notation.md)  
**下一章：** [奇异值分解与最小二乘](02-svd-least-squares.md)

