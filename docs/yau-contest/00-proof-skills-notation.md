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

??? proof "证明"

    存在整数 $m,n$ 使 $a=2m$、$b=2n$，于是 $a+b=2(m+n)$。由于 $m+n\in\mathbb Z$，故结论成立。

### 反证法

**命题。** $\sqrt2$ 不是有理数。

??? proof "证明"

    假设 $\sqrt2=p/q$，其中 $p,q$ 是互素正整数。则 $p^2=2q^2$，所以 $p$ 为偶数，记 $p=2r$。代回得 $q^2=2r^2$，故 $q$ 也为偶数，与互素矛盾。

### 反例

“特征值全为正的实矩阵一定对称”是错误命题。

??? proof "反例验证"

    取

    $$
    A=\begin{pmatrix}1&1\\0&2\end{pmatrix}.
    $$

    上三角矩阵的特征值是对角元，所以其特征值为 $1,2$，但直接转置可见 $A^T\ne A$。

## 数学归纳法

数学归纳法包含基础步骤、归纳假设和归纳步骤。以

$$
1+2+\cdots+n=\frac{n(n+1)}2
$$

为例，其完整论证如下。

??? proof "证明"

    $n=1$ 时，等式左边为 $1$，右边为 $1(1+1)/2=1$，基础步骤成立。

    假设等式在 $n=k$ 时成立，即

    $$
    1+2+\cdots+k=\frac{k(k+1)}2.
    $$

    那么

    $$
    1+\cdots+k+(k+1)
    =\frac{k(k+1)}2+(k+1)
    =\frac{(k+1)(k+2)}2.
    $$

    因此“对 $k$ 成立”推出“对 $k+1$ 成立”。由数学归纳法，等式对所有正整数成立。

## 绝对值与范数

本手册把绝对值三角不等式等高中结论作为已知。欧几里得范数（Euclidean norm）定义为

$$
\|x\|_2=\sqrt{x_1^2+\cdots+x_n^2}.
$$

柯西－施瓦茨不等式（Cauchy–Schwarz inequality）为

$$
|x^Ty|\le \|x\|_2\|y\|_2.
$$

??? proof "证明"

    若 $y=0$，结论成立。若 $y\ne0$，对任意 $t\in\mathbb R$，

    $$
    0\le\|x-ty\|_2^2
    =\|x\|_2^2-2t x^Ty+t^2\|y\|_2^2.
    $$

    右侧二次多项式恒非负，故判别式不大于零，从而

    $$
    (x^Ty)^2\le\|x\|_2^2\|y\|_2^2.
    $$

    等号成立当且仅当某个 $t$ 使 $x-ty=0$，也就是 $x,y$ 线性相关。

**欧几里得范数的三角不等式。** 对任意 $x,y\in\mathbb R^n$，

$$
\|x+y\|_2\le\|x\|_2+\|y\|_2.
$$

??? proof "证明"

    两边都非负。展开左边平方并使用柯西－施瓦茨不等式：

    $$
    \begin{aligned}
    \|x+y\|_2^2
    &=\|x\|_2^2+2x^Ty+\|y\|_2^2\\
    &\le\|x\|_2^2+2\|x\|_2\|y\|_2+\|y\|_2^2\\
    &=(\|x\|_2+\|y\|_2)^2.
    \end{aligned}
    $$

    对非负数取平方根保持不等号方向，得到结论。这一步说明：标量绝对值的三角不等式不能直接替代向量范数的三角不等式，后者依赖内积与柯西－施瓦茨不等式。

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

若集合 $E\subset\mathbb R$ 满足存在 $M$ 使每个 $x\in E$ 都有 $x\le M$，就称 $E$ 有上界，$M$ 是一个上界。所有上界中最小的一个叫上确界（supremum），记为 $\sup E$。下界和下确界（infimum）反向定义。

实数空间 $\mathbb R$ 是完备的（complete）：每个柯西数列（Cauchy sequence）都收敛到某个实数。等价地，每个非空有上界的实数集合都有上确界。后面的巴拿赫不动点定理（Banach fixed-point theorem）正是用完备性把“迭代项彼此靠近”转化成“存在极限”。

本手册把实数完备性及上述两个标准表述的等价性作为实数系统的基础公理，而不是从有理数的代数公理中推出。若从有理数构造实数，可以用戴德金分割或柯西列等价类证明完备性；那属于实分析的基础构造，不在后续数值算法中重复使用。

**单调有界收敛定理。** 单调递增且有上界的实数数列收敛；单调递减且有下界的情形同理。

??? proof "证明"

    设 $x_n$ 单调递增且集合 $E=\{x_n:n\in\mathbb N\}$ 有上界。由完备性，$L=\sup E$ 存在。给定 $\varepsilon>0$，$L-\varepsilon$ 不可能仍是 $E$ 的上界，所以存在 $N$ 使 $x_N>L-\varepsilon$。当 $n\ge N$ 时，由单调性

    $$
    L-\varepsilon<x_N\le x_n\le L.
    $$

    因而 $|x_n-L|<\varepsilon$，即 $x_n\to L$。递减情形对 $-x_n$ 应用同一结论。

**Bolzano–Weierstrass 定理。** 每个有界实数数列都有收敛子列。

??? proof "证明"

    设全部数列项位于闭区间 $[a,b]$。把区间二等分，至少有一半包含无穷多个数列项；保留这样的半区间并继续二分，得到闭区间套

    $$
    I_1\supset I_2\supset\cdots,
    \qquad |I_k|=2^{-k}(b-a).
    $$

    设 $I_k=[a_k,b_k]$。$a_k$ 单调递增且有上界，故收敛；$b_k$ 单调递减且有下界，也收敛。又因 $b_k-a_k\to0$，两者极限相同，记为 $x^*$。依次从 $I_k$ 中选取下标严格递增的数列项 $x_{n_k}$，则 $|x_{n_k}-x^*|\le|I_k|\to0$，所以该子列收敛到 $x^*$。

## 连续性与介值定理

函数 $f$ 在 $a$ 连续，表示 $\lim_{x\to a}f(x)=f(a)$。其 $\varepsilon$–$\delta$ 形式为

$$
\forall\varepsilon>0,
\ \exists\delta>0,
\quad |x-a|<\delta
\Rightarrow |f(x)-f(a)|<\varepsilon.
$$

**闭区间极值定理。** 连续函数 $f:[a,b]\to\mathbb R$ 在 $[a,b]$ 上取得最大值和最小值。

??? proof "证明"

    先说明闭区间中的任意数列都有收敛子列。把 $[a,b]$ 二等分，至少有一半包含数列的无穷多项；继续对这一半二等分并保留含无穷多项的一半。得到套区间

    $$
    I_1\supset I_2\supset\cdots,
    \qquad |I_k|=2^{-k}(b-a).
    $$

    依次在 $I_k$ 中选择一个下标严格递增的数列项 $x_{n_k}$。套区间端点由实数完备性收敛到同一点 $x^*$，且 $|x_{n_k}-x^*|\le|I_k|\to0$，所以 $x_{n_k}\to x^*$。

    现在证明最大值存在。令

    $$
    M=\sup\{f(x):x\in[a,b]\}.
    $$

    连续函数在闭区间上有界可用同样的二分反证法证明：若无界，就能构造 $x_n\to x^*$ 但 $|f(x_n)|\to\infty$，与 $f(x_n)\to f(x^*)$ 矛盾。

    按上确界定义，对每个 $n$ 选择 $x_n$ 使 $M-1/n<f(x_n)\le M$。取收敛子列 $x_{n_k}\to x^*$。连续性给出

    $$
    f(x^*)=\lim_{k\to\infty}f(x_{n_k})=M.
    $$

    所以最大值能够取得。对 $-f$ 应用同一结论，就得到最小值。

**介值定理（Intermediate Value Theorem）。** 若 $f$ 在 $[a,b]$ 连续，且 $f(a)f(b)<0$，则存在 $c\in(a,b)$ 使 $f(c)=0$。

??? proof "证明"

    不妨设 $f(a)<0<f(b)$。用二分法构造闭区间 $[a_n,b_n]$。初始取 $[a_0,b_0]=[a,b]$。令中点 $m_n=(a_n+b_n)/2$：若 $f(m_n)=0$，证明结束；否则保留端点函数值异号的那一半。

    因此对每个 $n$，

    $$
    f(a_n)<0<f(b_n),
    \qquad
    b_n-a_n=2^{-n}(b-a).
    $$

    数列 $(a_n)$ 单调递增且有上界，$(b_n)$ 单调递减且有下界。由实数完备性，二者分别收敛。又因为 $b_n-a_n\to0$，它们具有同一极限 $c\in[a,b]$。

    连续性给出

    $$
    f(c)=\lim_{n\to\infty}f(a_n)\le0,
    \qquad
    f(c)=\lim_{n\to\infty}f(b_n)\ge0.
    $$

    所以 $f(c)=0$。由于端点函数值非零，$c\in(a,b)$。

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

??? proof "证明"

    先证明罗尔定理。若连续函数 $h$ 满足 $h(a)=h(b)$，它在闭区间上取得最大值和最小值。若两者相等，则 $h$ 为常数，任取内部点都有 $h'=0$。否则至少一个非端点极值在 $(a,b)$ 内取得。设 $\xi$ 是内部极值点。对足够小的正负 $t$，差商

    $$
    \frac{h(\xi+t)-h(\xi)}{t}
    $$

    在 $t>0$ 与 $t<0$ 时符号相反；两侧极限若相等，只能等于零，所以 $h'(\xi)=0$。

    现在定义

    $$
    h(x)=f(x)-f(a)-\frac{f(b)-f(a)}{b-a}(x-a).
    $$

    有 $h(a)=h(b)=0$。由罗尔定理，存在 $\xi\in(a,b)$ 使 $h'(\xi)=0$，即

    $$
    f'(\xi)=\frac{f(b)-f(a)}{b-a}.
    $$

    整理后得到中值定理。

因此若 $|f'(x)|\le M$ 在区间内成立，就有

$$
|f(b)-f(a)|\le M|b-a|.
$$

## 梯度、雅可比矩阵（Jacobian）与海森矩阵（Hessian）

### 偏导数

多元函数的偏导数（partial derivative）仍是单变量导数，只是在求某个变量的导数时把其他变量暂时当作常数。例如

$$
f(x_1,x_2)=x_1^2+3x_1x_2+2x_2^2.
$$

计算 $\partial f/\partial x_1$ 时固定 $x_2$：

$$
\frac{\partial f}{\partial x_1}
=2x_1+3x_2+0.
$$

计算 $\partial f/\partial x_2$ 时固定 $x_1$：

$$
\frac{\partial f}{\partial x_2}
=0+3x_1+4x_2.
$$

在点 $(1,2)$，梯度为 $(8,11)^T$。这个计算顺序比直接背矩阵公式更重要：先确认输出是标量还是向量，再逐个输入变量求导，最后按约定排列。

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

标量函数的海森矩阵（Hessian matrix）是 $\nabla^2 f(x)$。对上面的例子，

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

??? proof "二阶拉格朗日余项的证明"

    设

    $$
    R=f(x+h)-f(x)-f'(x)h.
    $$

    需要证明 $R=f''(\xi)h^2/2$。定义辅助函数

    $$
    \Phi(t)=f(t)-f(x)-f'(x)(t-x)-R\frac{(t-x)^2}{h^2}.
    $$

    可直接验证 $\Phi(x)=\Phi(x+h)=0$，且 $\Phi'(x)=0$。在 $[x,x+h]$ 上对 $\Phi$ 使用罗尔定理，存在 $\eta$ 使 $\Phi'(\eta)=0$；再在 $x$ 与 $\eta$ 之间对 $\Phi'$ 使用罗尔定理，存在 $\xi$ 使 $\Phi''(\xi)=0$。

    由于

    $$
    \Phi''(t)=f''(t)-\frac{2R}{h^2},
    $$

    代入 $t=\xi$ 得

    $$
    R=\frac12f''(\xi)h^2.
    $$

    若 $h<0$，只需交换区间端点，论证完全相同。

**三阶泰勒余项。** 若 $f$ 在相应区间上三次连续可微，则存在位于 $x$ 与 $x+h$ 之间的 $\xi$，使

$$
f(x+h)=f(x)+f'(x)h+\frac12f''(x)h^2+\frac16f'''(\xi)h^3.
$$

??? proof "证明"

    记

    $$
    R=f(x+h)-f(x)-f'(x)h-\frac12f''(x)h^2
    $$

    并定义

    $$
    \Phi(t)=f(t)-f(x)-f'(x)(t-x)
    -\frac12f''(x)(t-x)^2-R\frac{(t-x)^3}{h^3}.
    $$

    有 $\Phi(x)=\Phi(x+h)=0$，同时 $\Phi'(x)=\Phi''(x)=0$。先后对 $\Phi$、$\Phi'$、$\Phi''$ 使用罗尔定理，得到两端之间某个 $\xi$ 满足 $\Phi'''(\xi)=0$。由于

    $$
    \Phi'''(t)=f'''(t)-\frac{6R}{h^3},
    $$

    故 $R=f'''(\xi)h^3/6$。$h<0$ 时交换区间端点即可。

三阶导数在局部闭区间上连续，因而有界，所以也可简写成

$$
f(x+h)=f(x)+f'(x)h+\frac12f''(x)h^2+O(h^3).
$$

$r(h)=O(h^p)$ 表示存在 $C,\delta>0$，当 $|h|<\delta$ 时 $|r(h)|\le C|h|^p$。而 $r(h)=o(h^p)$ 表示 $r(h)/h^p\to0$。

对 $e^x$ 在 $0$ 展开：

$$
e^h=1+h+\frac{h^2}{2}+O(h^3).
$$

把公式用于一个可核对的数值。取 $h=0.1$，二阶近似为

$$
e^{0.1}\approx1+0.1+\frac{0.1^2}{2}=1.105.
$$

因为三阶余项中的 $\xi\in(0,0.1)$，所以 $e^\xi\le e^{0.1}$，从而

$$
\left|e^{0.1}-1.105\right|
\le\frac{e^{0.1}}6(0.1)^3
<1.85\times10^{-4}.
$$

实际值约为 $1.105170$，确实落在误差界内。使用泰勒公式时应同时写出展开点、保留阶数和余项界，而不只是背多项式。

## 复数的几何表示

复数 $z=x+iy$ 可看成平面上的点 $(x,y)$，其中 $i^2=-1$。它的模为

$$
|z|=\sqrt{x^2+y^2}.
$$

当 $z\ne0$ 时，可以写成极坐标形式

$$
z=r(\cos\theta+i\sin\theta)=re^{i\theta},
\qquad r=|z|>0.
$$

复数相乘时模相乘、辐角相加：$r_1e^{i\theta_1}r_2e^{i\theta_2}=r_1r_2e^{i(\theta_1+\theta_2)}$。因此任意非零复数 $c=|c|e^{i\phi}$ 都有 $k$ 次根，例如

$$
u=|c|^{1/k}e^{i\phi/k},
\qquad u^k=c.
$$

下一节证明中选择复数方向、讨论闭圆盘和最小模，使用的就是这套平面几何。

## 复多项式的根

后面的矩阵三角化需要知道复特征多项式一定有根。这里先给出所需结果。

**代数基本定理（Fundamental Theorem of Algebra）。** 每个次数至少为一的复系数多项式都至少有一个复根。

??? proof "证明"

    设

    $$
    p(z)=a_nz^n+\cdots+a_0,
    \qquad a_n\ne0,\quad n\ge1.
    $$

    当 $|z|\to\infty$ 时，$|p(z)|\to\infty$。因此可取 $R>0$，使 $|z|>R$ 时 $|p(z)|>|p(0)|$。令 $m$ 是 $|p|$ 在闭圆盘 $|z|\le R$ 上的下确界，并选取点列 $(z_j)$ 使 $|p(z_j)|\to m$。把复数看成 $\mathbb R^2$ 中的点：先从有界的实部抽取收敛子列，再从该子列的有界虚部抽取收敛子列，便得到 $z_{j_\ell}\to z_0$，且闭圆盘保证 $|z_0|\le R$。由连续性，$|p(z_0)|=m$。圆盘外的函数值又大于 $|p(0)|\ge m$，所以 $z_0$ 实际上是全平面的最小点。

    反设 $p(z_0)\ne0$。把 $p(z_0+w)/p(z_0)$ 按 $w$ 的幂展开，并令 $k\ge1$ 是第一个非零的非常数项次数：

    $$
    \frac{p(z_0+w)}{p(z_0)}
    =1+c_kw^k+c_{k+1}w^{k+1}+\cdots+c_nw^n,
    \qquad c_k\ne0.
    $$

    选取单位复数 $u$，使 $c_ku^k=-|c_k|$；这样的 $u$ 可由复数的极坐标表示直接取出。令 $w=ru$，其中 $r>0$。余项满足

    $$
    \left|\sum_{j=k+1}^nc_jr^ju^j\right|
    \le Cr^{k+1}
    $$

    对某个常数 $C$ 成立。取 $r$ 足够小，使 $Cr\le |c_k|/2$ 且 $|c_k|r^k<1$。于是

    $$
    \left|\frac{p(z_0+ru)}{p(z_0)}\right|
    \le 1-|c_k|r^k+Cr^{k+1}
    \le 1-\frac{|c_k|}{2}r^k<1.
    $$

    这说明 $|p(z_0+ru)|<|p(z_0)|$，与 $z_0$ 的最小性矛盾。因此 $p(z_0)=0$。

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

??? proof "证明"

    $$
    e_{k+1}=\frac12e_k,
    \qquad
    e_k=2^{-k}e_0.
    $$

    因为 $2^{-k}\to0$，故任意初值都收敛到 $2$。要保证 $|e_k|\le\varepsilon$，只需

    $$
    k\ge \frac{\log(|e_0|/\varepsilon)}{\log2}.
    $$

    这同时给出了候选极限、误差方程、极限和步数界。

## 练习

1. 写出“每个实对称矩阵都有实特征值”的量词结构及否定。
2. 使用柯西－施瓦茨不等式证明欧几里得范数的三角不等式。
3. 用 $\varepsilon$–$N$ 定义证明 $3^{-k}\to0$。
4. 对 $f(x)=\log x$ 写出以 $x=1$ 为中心的二阶泰勒展开（Taylor expansion）。
5. 对 $x_{k+1}=x_k/3+2/3$ 求固定点、精确误差式及达到 $10^{-6}$ 误差所需的充分步数。

??? tip "第一步提示"

    第 2 题先把 $\|x+y\|_2^2$ 展开；第 3 题从 $3^{-k}<\varepsilon$ 反解 $k$；第 5 题先解 $x=x/3+2/3$，再令 $e_k=x_k-x^*$。

**答案。** 第 3 题可取 $N>\log(1/\varepsilon)/\log3$。第 4 题为 $\log(1+h)=h-h^2/2+O(h^3)$。第 5 题固定点为 $1$，且 $e_k=3^{-k}e_0$。

**下一章：** [矩阵范数与谱理论](01-matrix-norms-spectral.md)
