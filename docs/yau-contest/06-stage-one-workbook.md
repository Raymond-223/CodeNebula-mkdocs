# Yau Contest Problems

## Singular Value Decomposition and Best Low-Rank Approximation

*2010 Written Contest · Individual · Problem 6(1)、(2) · [Original paper (PDF)](../assets/yau-papers/2010-written-individual.pdf)*

(1) 对 $A\in\mathbb R^{m\times n}$，证明存在正交 $U,V$，使 $U^TAV$ 为矩形非负对角矩阵，奇异值递减排列。

(2) 若 $\operatorname{rank}(A)=r$，$0<k<r$，证明 $\min_{\operatorname{rank}(B)=k}\|A-B\|_2=\sigma_{k+1}$。

??? proof "答案"

    (1) 令 $A^TA=V\operatorname{diag}(\sigma_1^2,\ldots,\sigma_n^2)V^T$，其中 $V$ 正交，且 $\sigma_1\ge\cdots\ge\sigma_n\ge0$。对 $\sigma_i>0$ 定义 $u_i=Av_i/\sigma_i$。逐项计算

    $$
    u_i^Tu_j=\frac{v_i^TA^TAv_j}{\sigma_i\sigma_j}
    =\frac{\sigma_j^2v_i^Tv_j}{\sigma_i\sigma_j}=\delta_{ij}.
    $$

    所以正奇异值对应的 $u_i$ 是正交单位向量；把它们补成 $\mathbb R^m$ 的正交基 $U$。若 $\sigma_i=0$，则 $\|Av_i\|_2^2=v_i^TA^TAv_i=0$，故 $Av_i=0$。因此正奇异值对应列满足 $U^TAv_i=\sigma_i e_i$，零奇异值对应列为零。将这些列合并即 $U^TAV=\Sigma$，也就是 $A=U\Sigma V^T$。

    (2) 先证明上界。取 $A_k=\sum_{i=1}^k\sigma_i u_iv_i^T$。对 $j=1,\ldots,k$，有 $A_kv_j=\sigma_ju_j$。因为每个 $\sigma_j>0$ 且 $u_1,\ldots,u_k$ 线性无关，像空间至少含 $k$ 个线性无关向量，故 $\operatorname{rank}(A_k)\ge k$；另一方面 $A_k$ 是 $k$ 个秩一矩阵之和，秩至多 $k$，所以 $\operatorname{rank}(A_k)=k$。由 SVD，

    $$
    A-A_k=\sum_{i=k+1}^r\sigma_i u_iv_i^T,
    \quad \|(A-A_k)x\|_2^2=\sum_{i=k+1}^r\sigma_i^2(v_i^Tx)^2\le\sigma_{k+1}^2\|x\|_2^2.
    $$

    取 $x=v_{k+1}$ 达到等号，故 $\|A-A_k\|_2=\sigma_{k+1}$。

    再证下界。令 $W=\operatorname{span}(v_1,\ldots,v_{k+1})$，则 $\dim W=k+1$。任给秩至多 $k$ 的 $B$，限制映射 $B|_W$ 的像维数至多 $k$，所以它有非零核；取核中单位向量 $z=\sum_{i=1}^{k+1}c_iv_i$。于是 $Bz=0$、$\sum c_i^2=1$，并且

    $$
    \|A-B\|_2\ge\|(A-B)z\|_2=\|Az\|_2
    =\left(\sum_{i=1}^{k+1}\sigma_i^2c_i^2\right)^{1/2}\ge\sigma_{k+1}.
    $$

    上下界相同，最小值就是 $\sigma_{k+1}$。

## Polynomial Interpolation from Prescribed Values

*2011 Written Contest · Individual · Problem 2 · [Original paper (PDF)](../assets/yau-papers/2011-written-individual.pdf)*

**Scope: foundational supplement.** This problem uses the polynomial factor theorem and the fact that a nonzero degree-$d$ polynomial has at most $d$ roots.

五次多项式 $p,q$ 满足 $p(i)=q(i)=1/i$（$i=2,3,4,5,6$），且 $p(1)=1,q(1)=2$。求 $p(0)-q(0)$。

??? proof "答案"

    令 $r(x)=p(x)-q(x)$。它的次数至多为 $5$，并且 $r(j)=0$ 对 $j=2,3,4,5,6$。多项式因子定理逐个给出

    $$
    r(x)=C(x-2)(x-3)(x-4)(x-5)(x-6)
    $$

    （若 $r\equiv0$，则 $r(1)=0$，与已知 $r(1)=-1$ 矛盾，所以 $C\ne0$）。在 $x=1$ 处，$r(1)=p(1)-q(1)=-1$，而乘积为 $(-1)(-2)(-3)(-4)(-5)=-120$，所以 $C=1/120$。在 $x=0$ 处，乘积为 $(-2)(-3)(-4)(-5)(-6)=720$，故

    $$
    p(0)-q(0)=r(0)=\frac{720}{120}=6.
    $$

## Fibonacci Numbers via Matrix Powers

*2013 Written Contest · Individual · Problem 6 · [Original paper (PDF)](../assets/yau-papers/2013-written-individual.pdf)*

**Extension — arithmetic-operation model.** The $O(\log n)$ bound below counts scalar additions and multiplications as unit-cost operations. Since $F_n$ has $\Theta(n)$ bits, this is not a bit-complexity bound; the cost of operating on growing integers must also be counted.

$F_0=0,F_1=1,F_{n+2}=F_{n+1}+F_n$。求 $\begin{pmatrix}0&1\\1&1\end{pmatrix}^n$ 与 Fibonacci 数的关系，并设计比逐项递推更快的算法，估计运算次数。

??? proof "答案"

    记 $M=\begin{pmatrix}0&1\\1&1\end{pmatrix}$。对 $n\ge1$，归纳证明

    $$
    M^n=\begin{pmatrix}F_{n-1}&F_n\\F_n&F_{n+1}\end{pmatrix}.
    $$

    $n=1$ 时两边都是 $M$（$F_0=0,F_1=1,F_2=1$）。若公式对 $n$ 成立，右乘 $M$ 得

    $$
    \begin{pmatrix}F_{n-1}&F_n\\F_n&F_{n+1}\end{pmatrix}M
    =\begin{pmatrix}F_n&F_{n-1}+F_n\\F_{n+1}&F_n+F_{n+1}\end{pmatrix}
    =\begin{pmatrix}F_n&F_{n+1}\\F_{n+1}&F_{n+2}\end{pmatrix},
    $$

    这就是 $n+1$ 的公式。快速幂初始化 $R=I$、$B=M$、$t=n$；当 $t>0$ 时，若 $t$ 为奇数就令 $R\leftarrow RB$，再令 $B\leftarrow B^2$、$t\leftarrow\lfloor t/2\rfloor$。循环不变式是 $RB^t=M^n$，其中右边的 $n$ 始终指原始指数。若 $t=2h$，更新 $B\leftarrow B^2,t\leftarrow h$ 后有 $R(B^2)^h=RB^t$；若 $t=2h+1$，先令 $R\leftarrow RB$，再平方并令 $t\leftarrow h$，则新乘积 $R_{旧}B_{旧}^{2h+1}$ 仍等于旧的 $RB^t$。故不变式保持。每轮 $t$ 变为 $\lfloor t/2\rfloor$，至多 $\lfloor\log_2n\rfloor+1$ 轮后 $t=0$，所以 $R=M^n$。每轮至多做两次 $2\times2$ 矩阵乘法，总计不超过 $2(\lfloor\log_2n\rfloor+1)$ 次；按通常算法，每次矩阵乘法用 8 次标量乘法、4 次加法，因此标量运算也是 $O(\log n)$。逐项递推需 $O(n)$ 次。团体赛同题答案相同。

## Fibonacci Numbers via Matrix Powers

*2013 Written Contest · Team · Problem 6 · [Original paper (PDF)](../assets/yau-papers/2013-written-team.pdf)*

**Extension — arithmetic-operation model.** The $O(\log n)$ bound below counts scalar additions and multiplications as unit-cost operations. Since $F_n$ has $\Theta(n)$ bits, this is not a bit-complexity bound; the cost of operating on growing integers must also be counted.

$F_0=0,F_1=1,F_{n+2}=F_{n+1}+F_n$。求 $\begin{pmatrix}0&1\\1&1\end{pmatrix}^n$ 与 Fibonacci 数的关系，并设计比逐项递推更快的算法，估计运算次数。

??? proof "答案"

    The team problem is identical to the individual problem above. Its matrix identity, fast-power invariant, and operation count have the same proof; see the complete derivation above. This entry retains the original-paper reference without duplicating the solution.

## Rank-One Updates and the Sherman–Morrison Formula

*2013 Final Contest · Individual · Problem 1(a)、(b) · [Original paper (PDF)](../assets/yau-papers/2013-final-individual.pdf)*

**Extension — prerequisite.** Rank-one updates and the Sherman–Morrison formula require invertibility of A and direct verification of the proposed inverse; these are matrix-algebra applications beyond the core SVD and iteration techniques.

$A$ 可逆。(a) 求 $A+uv^T$ 可逆的条件及逆矩阵；(b) 将 $A$ 第一列替换为 $b$，求新矩阵的逆。

??? proof "答案"

    (a) 令 $w=A^{-1}u$，则 $A+uv^T=A(I+wv^T)$。记 $d=1+v^Tw$。若 $d\ne0$，直接相乘：

    $$
    (I+wv^T)\left(I-\frac{wv^T}{d}\right)
    =I+w v^T-\frac{wv^T}{d}-\frac{w(v^Tw)v^T}{d}=I,
    $$

    因为 $1-1/d-(d-1)/d=0$。因此逆矩阵为 $A^{-1}-A^{-1}uv^TA^{-1}/d$。若 $d=0$ 且 $w\ne0$，则 $(I+wv^T)w=w(1+v^Tw)=0$，矩阵奇异。若 $w=0$，则 $d=1$，不属于 $d=0$ 情况。故条件充要。

    (b) 令 $p=A^{-1}b$，$e_1=(1,0,\ldots,0)^T$。替换第一列得到 $\widehat A=A+(b-Ae_1)e_1^T=A[I+(p-e_1)e_1^T]$。内层秩一矩阵的标量条件为 $1+e_1^T(p-e_1)=p_1$。所以它可逆当且仅当 $p_1\ne0$；把 (a) 的公式代入即

    $$
    \widehat A^{-1}=A^{-1}-\frac{(p-e_1)e_1^TA^{-1}}{p_1}.
    $$

    代回 $\widehat A\widehat A^{-1}$ 也可按 (a) 的乘法逐项得到单位矩阵。

## Triangular Systems and Matrix Condition Numbers

*2014 Written Contest · Team · Problem 5(i)、(ii) · [Original paper (PDF)](../assets/yau-papers/2014-written-team.pdf)*

$x_0=0,x_k=2x_{k-1}+b_k$。(i) 写成 $Ax=b$，并对 $b_1=-1/3,b_k=(-1)^k$（$k\ge2$）验证 $x_k=(-1)^k/3$；(ii) 求 $A^{-1}$ 和 $1$-范数条件数。

??? proof "答案"

    (i) 递推 $x_k-2x_{k-1}=b_k$ 且 $x_0=0$。所以 $A$ 是对角元为 $1$、次对角元为 $-2$ 的下双对角矩阵。给定 $b_1=-1/3$ 时 $x_1=-1/3$；若 $k\ge2$ 且 $x_{k-1}=(-1)^{k-1}/3$，则

    $$
    x_k=2\frac{(-1)^{k-1}}3+(-1)^k
    =(-1)^k\left(1-\frac23\right)=\frac{(-1)^k}{3}.
    $$

    故由归纳法，所有 $k$ 都满足题给公式。

    (ii) 设 $B_{ij}=2^{i-j}$（$i\ge j$），$B_{ij}=0$（$i<j$）。对 $i=j$，$(AB)_{ii}=1$；对 $i>j$，$(AB)_{ij}=B_{ij}-2B_{i-1,j}=2^{i-j}-2\cdot2^{i-1-j}=0$；对 $i<j$ 两项均为零。因此 $AB=I$，即 $A^{-1}=B$。矩阵 $1$-范数为最大列绝对值和。若 $n\ge2$，$A$ 第一列绝对值和为 $3$，其余列不超过 $3$，故 $\|A\|_1=3$。$A^{-1}$ 第 $j$ 列和为 $1+2+\cdots+2^{n-j}=2^{n-j+1}-1$，最大在 $j=1$，得 $\|A^{-1}\|_1=2^n-1$。所以 $\kappa_1(A)=3(2^n-1)$；$n=1$ 时 $A=[1]$，条件数为 $1$。

## Eigenvalues of a Tridiagonal Matrix

*2014 Final Contest · Individual and Overall · Problem 1 · [Original paper (PDF)](../assets/yau-papers/2014-final-individual.pdf)*

**Extension — prerequisite.** The eigenvector formula comes from a second-order difference equation with endpoint conditions; derive this recurrence before using the sine-vector eigenbasis.

$A$ 为 $N$ 阶三对角矩阵，下对角 $a$、对角 $b$、上对角 $c$，$ac>0$。求其特征值和特征向量。

??? proof "答案"

    令 $d=\sqrt{a/c}>0$，$D=\operatorname{diag}(1,d,\ldots,d^{N-1})$，并设 $B=D^{-1}AD$。$B$ 的上、下对角元分别为 $cd$ 与 $a/d$，由 $d^2=a/c$ 二者相等，记其值为 $\tau=\operatorname{sgn}(a)\sqrt{ac}$；故 $B$ 是对角元 $b$、相邻对角元 $\tau$ 的对称三对角矩阵。

    设 $Bw=\lambda w$。第 $i$ 行方程为

    $$\tau w_{i-1}+(b-\lambda)w_i+\tau w_{i+1}=0,\qquad i=1,\ldots,N,$$

    其边界条件可写成 $w_0=w_{N+1}=0$。为了满足相邻项的二阶递推，试取 $w_i=\sin(i\theta)$。由和角公式

    $$\sin((i-1)\theta)+\sin((i+1)\theta)=2\cos\theta\sin(i\theta),$$

    可知递推左边为 $[b+2\tau\cos\theta-\lambda]\sin(i\theta)$，故 $\lambda=b+2\tau\cos\theta$。$w_0=0$ 自动成立；右端条件要求 $\sin((N+1)\theta)=0$。取 $\theta_j=j\pi/(N+1)$，$j=1,\ldots,N$，得到 $N$ 个非零向量 $w_i^{(j)}=\sin(i\theta_j)$。

    其特征值 $\lambda_j=b+2\tau\cos\theta_j$ 两两不同，因为 $\cos\theta$ 在 $(0,\pi)$ 严格递减，而 $\tau\ne0$。因此这些向量线性无关，构成 $N$ 维空间的一组基，已列出全部特征值。又 $A=DBD^{-1}$，所以 $A$ 的特征向量为 $Dw^{(j)}$，其第 $i$ 个分量是 $d^{i-1}\sin(i\theta_j)$，且 $A$ 与 $B$ 有相同特征值。

## Singular Values and Best Rank-k Approximation

*2015 Written Contest · Team · Problem 5(a)–(c) · [Original paper (PDF)](../assets/yau-papers/2015-written-team.pdf)*

$A=U\Sigma V^T\in\mathbb R^{n\times m}$，秩 $r$。(a) $r<\min(m,n)$ 时，证明任意 $\epsilon>0$ 都有满秩 $A_\epsilon$ 且 $\|A-A_\epsilon\|_2=\epsilon$；(b) 证明截断 SVD $A_k$ 是最佳秩不超过 $k$ 的算子范数逼近；(c) $r=\min(m,n)$ 时，证明 $\|A-B\|_2<\sigma_r$ 推出 $B$ 满秩。

??? proof "答案"

    记奇异值为 $\sigma_1\ge\cdots\ge\sigma_r>0$，并将 $\Sigma$ 补零到矩形尺寸。

    (a) 因 $r<\min(m,n)$，$\Sigma$ 的前 $\min(m,n)$ 个对角位置中至少有一个零。把其中每一个零都改成 $\epsilon$，其余奇异值保持不变，得到 $\Sigma_\epsilon$。这样所有 $\min(m,n)$ 个奇异值都非零，所以 $A_\epsilon=U\Sigma_\epsilon V^T$ 满秩；并且 $\|\Sigma-\Sigma_\epsilon\|_2=\epsilon$，因为差矩阵的非零奇异值全等于 $\epsilon$。左乘正交矩阵不改变向量长度；右乘 $V^T$ 也不改变算子范数，因为 $V^T$ 将单位球面一一映到自身。因此

    $$\|A-A_\epsilon\|_2=\|U(\Sigma-\Sigma_\epsilon)V^T\|_2=\|\Sigma-\Sigma_\epsilon\|_2=\epsilon.$$

    (b) $A_k=\sum_{i=1}^k\sigma_i u_iv_i^T$。对 $j=1,\ldots,k$ 有 $A_kv_j=\sigma_ju_j$；因 $\sigma_j>0$ 且 $u_1,\ldots,u_k$ 线性无关，$\operatorname{rank}(A_k)\ge k$。另一方面 $A_k$ 是 $k$ 个秩一矩阵之和，故秩至多为 $k$，于是秩恰为 $k$。且对任意单位向量 $x$，

    $$
    \|(A-A_k)x\|_2^2=\sum_{i>k}\sigma_i^2(v_i^Tx)^2\le\sigma_{k+1}^2.
    $$

    取 $x=v_{k+1}$ 达到等号，所以误差为 $\sigma_{k+1}$。任给秩至多 $k$ 的 $B$，在 $W=\operatorname{span}(v_1,\ldots,v_{k+1})$ 上，限制映射 $B|_W$ 的像维数至多 $k$，而 $\dim W=k+1$；由秩－零度定理，它有非零核向量。将其归一为 $z=\sum_{i=1}^{k+1}c_iv_i$，则 $Bz=0$ 且 $\sum_i c_i^2=1$，所以

    $$\|Az\|_2^2=\sum_{i=1}^{k+1}\sigma_i^2c_i^2\ge\sigma_{k+1}^2\sum_i c_i^2=\sigma_{k+1}^2.$$

    故 $\|A-B\|_2\ge\|(A-B)z\|_2=\|Az\|_2\ge\sigma_{k+1}$，$A_k$ 达到最小值。

    (c) 这里 $r=\min(m,n)$。若 $\operatorname{rank}B<r$，则 $B$ 在 $A$ 的 $r$ 维右奇异向量空间 $W=\operatorname{span}(v_1,\ldots,v_r)$ 上有非零核向量。取单位 $z\in W$ 且 $Bz=0$，得到 $\|(A-B)z\|_2=\|Az\|_2\ge\sigma_r$。因此 $\|A-B\|_2<\sigma_r$ 与 $\operatorname{rank}B<r$ 矛盾，必有 $\operatorname{rank}B=r$。

## Convergence of Newton’s Method for a Positive Root

*2015 Final Contest · Individual · Problem 3 · [Original paper (PDF)](../assets/yau-papers/2015-final-individual.pdf)*

$C>0,k\ge2$，Newton 迭代 $x_{n+1}=x_n-(x_n^k-C)/(kx_n^{k-1})$。证明任意 $x_0>0$ 都收敛。

??? proof "答案"

    令 $r=C^{1/k}>0$，并写 Newton 更新为

    $$
    N(x)=x-\frac{x^k-r^k}{kx^{k-1}}=\frac{(k-1)x+r^k/x^{k-1}}k.
    $$

    对每个 $x>0$，加权算术几何平均不等式给 $(k-1)x+r^k/x^{k-1}\ge kr$（$k-1$ 个因子为 $x$、一个因子为 $r^k/x^{k-1}$，其几何平均是 $r$），故 $N(x)\ge r$。若 $x\ge r$，则 $r^k/x^{k-1}\le x$，所以 $N(x)\le x$。因此无论 $x_0>0$ 在根哪侧，$x_1\ge r$；从第 1 步起 $r\le x_{n+1}\le x_n$。单调有界数列收敛到某个 $L\ge r>0$。在更新式取极限（分母趋于非零数）得 $L=L-(L^k-r^k)/(kL^{k-1})$，所以 $L^k=r^k$。正数范围内唯一解为 $L=r=C^{1/k}$。

## Convergence Criteria for Stationary Iterations

*2017 Written Contest · Individual · Problem 4(a)、(c)、(d) · [Original paper (PDF)](../assets/yau-papers/2017-written-individual.pdf)*

设 $A$ 可逆。(a) 给出迭代 $Ax_{k+1}=b-Bx_k$ 对任意初值收敛到唯一解的充要条件。(c) 对称正定 $M$ 及权重 $\omega_1>1,\omega_i>0$，分析 $x^{(r+1)}=\omega_1x^{(r)}+\sum_{i=2}^s\omega_i(c_{i-1}-Mx^{(r)})$。(d) 比较同时更新与先后更新的两块迭代的收敛条件和渐近谱因子：

$$
\begin{aligned}
(&*)\quad Ax_1^{(r+1)}=b_1-Bx_2^{(r)},\quad Ax_2^{(r+1)}=b_2-Bx_1^{(r)},\\
(&**)\quad Ax_1^{(r+1)}=b_1-Bx_2^{(r)},\quad Ax_2^{(r+1)}=b_2-Bx_1^{(r+1)}.
\end{aligned}
$$

??? proof "答案"

    (a) 令 $C=A^{-1}B$、$d=A^{-1}b$。迭代等价于 $x_{k+1}=d-Cx_k$。若 $\rho(C)<1$，则 $I+C$ 可逆，唯一固定点为 $x_*=(I+C)^{-1}d$；误差满足 $e_{k+1}=-Ce_k$，故 $e_k=(-C)^ke_0\to0$（这是 Stage 1 的谱半径判据）。反过来，若对任意初值都收敛到同一固定点，任意两条轨道之差给出 $(-C)^k(x_0-y_0)\to0$。令 $x_0-y_0$ 逐一取标准基向量，即 $(-C)^k\to0$；若 $C$ 有特征值 $\lambda$ 且 $|\lambda|\ge1$，相应复特征向量 $v$ 满足 $\|(-C)^kv\|=|\lambda|^k\|v\|$ 不趋零，矛盾。因此 $\rho(C)<1$。

    (c) 令 $S=\sum_{i=2}^s\omega_i$、$c=\sum_{i=2}^s\omega_ic_{i-1}$。迭代是 $x^{(r+1)}=(\omega_1I-SM)x^{(r)}+c$，误差矩阵 $G=\omega_1I-SM$。因 $M$ 对称正定，存在正交特征基，特征值 $\mu_j>0$；同一基下 $G$ 的特征值是 $\omega_1-S\mu_j$。故任意初值收敛到唯一固定点当且仅当

    $$-1<\omega_1-S\mu_j<1\quad\text{对所有 }j,$$

    即 $(\omega_1-1)/S<\mu_j<(\omega_1+1)/S$。这由每个特征坐标的误差递推 $e_{j,r+1}=(\omega_1-S\mu_j)e_{j,r}$ 直接得到。

    (d) 令 $C=A^{-1}B$、$d_i=A^{-1}b_i$。两种格式有相同固定方程 $x_1+Cx_2=d_1$、$Cx_1+x_2=d_2$。减去固定点后，同时更新的误差矩阵为 $T_* =\begin{pmatrix}0&-C\\-C&0\end{pmatrix}$。令 $u=e_1+e_2$、$v=e_1-e_2$，则 $u'=-Cu$、$v'=Cv$；变量变换 $(e_1,e_2)\mapsto(u,v)$ 可逆，所以 $T_*$ 与 $\operatorname{diag}(-C,C)$ 相似，故 $\rho(T_*)=\rho(C)$。

    先后更新满足 $e_1'=-Ce_2$、$e_2'=-Ce_1'=C^2e_2$，所以误差矩阵是 $T_{GS}=\begin{pmatrix}0&-C\\0&C^2\end{pmatrix}$。对块上三角矩阵，行列式按对角块相乘，故

    $$\det(\lambda I-T_{GS})=\det(\lambda I)\det(\lambda I-C^2).$$

    因此 $T_{GS}$ 的特征值由 $0$ 和 $C^2$ 的特征值组成，谱半径为 $\rho(C^2)=\rho(C)^2$。由定常迭代判据，两者对任意初值收敛的充要条件都是 $\rho(C)<1$；当 $0<\rho(C)<1$ 时，先后更新每完整轮的渐近谱因子 $\rho(C)^2$ 小于同时更新的 $\rho(C)$。

## Block Matrix Eigenvalues and Gradient Iteration

*2019 Written Contest · Team · Problem 3(i)–(iii) · [Original paper (PDF)](../assets/yau-papers/2019-written-team.pdf)*

$X\in\mathbb R^{n\times m}$ 满列秩、$m\le n$，$A=\begin{pmatrix}I&X\\X^T&0\end{pmatrix}$。(i) 证明可逆；(ii) 用 $X$ 的奇异值给出全部特征值；(iii) 判断迭代 $z_{k+1}=z_k-(Az_k-b)$ 能否对任意初值收敛。

??? proof "答案"

    取 $X=U\Sigma V^T$ 为紧致 SVD，$U$ 的列为 $u_i$，$V$ 的列为 $v_i$，奇异值 $\sigma_i>0$。对每个 $i$，在二维子空间 $\operatorname{span}\{(u_i,0),(0,v_i)\}$ 上，$A$ 的矩阵是

    $$K_i=\begin{pmatrix}1&\sigma_i\\\sigma_i&0\end{pmatrix}.$$

    $u_i\in\mathbb R^n$，且 $u_1,\ldots,u_m$ 是 $\operatorname{Col}(X)$ 的标准正交基；$v_i\in\mathbb R^m$，且 $v_1,\ldots,v_m$ 是 $\mathbb R^m$ 的标准正交基。若 $n>m$，取 $\operatorname{Col}(X)^\perp$ 的标准正交基 $w_1,\ldots,w_{n-m}$。对每个 $w$，有 $X^Tw=0$，故 $A(w,0)=(w,0)$，特征值为 $1$。由 $\mathbb R^n=\operatorname{Col}(X)\oplus\operatorname{Col}(X)^\perp$，$u_1,\ldots,u_m,w_1,\ldots,w_{n-m}$ 是 $\mathbb R^n$ 的标准正交基；与 $v_1,\ldots,v_m$ 一起，所列 $m$ 个二维子空间及 $n-m$ 个一维子空间两两正交，维数总和 $2m+n-m=n+m$，所以它们张成 $\mathbb R^n\times\mathbb R^m$。解 $\det(K_i-\lambda I)=\lambda^2-\lambda-\sigma_i^2=0$，得到

    $$\lambda_{i,\pm}=\frac{1\pm\sqrt{1+4\sigma_i^2}}2,$$

    另有 $n-m$ 个 $1$。每个二维块的行列式为 $-\sigma_i^2\ne0$，其余特征值 $1$ 也非零，所以 $A$ 可逆。

    (iii) 误差满足 $e_{r+1}=(I-A)e_r$。每个 $K_i$ 有负特征值 $\lambda_{i,-}<0$，故 $I-A$ 有特征值 $1-\lambda_{i,-}>1$。取对应特征向量为初始误差，误差范数按 $(1-\lambda_{i,-})^r$ 增长。因此只要 $m\ge1$，这个步长为 $1$ 的迭代不可能对任意初值收敛。

## Diagonalization of a Companion Matrix

*2019 Final Contest · Individual · Problem 1 · [Original paper (PDF)](../assets/yau-papers/2019-final-individual.pdf)*

**Terminology.** Here *companion matrix* is translated as “友矩阵”. It is constructed from polynomial coefficients and is distinct from the *adjugate matrix* $\operatorname{adj}(A)$ (“伴随矩阵”), which is constructed from cofactors.

友矩阵 $C$ 的最后一列为 $(-c_0,\ldots,-c_{n-1})^T$、下对角为 $1$，特征值 $\lambda_i$ 互异。令 $V_{ij}=\lambda_i^{j-1}$。证明 $VCV^{-1}=\operatorname{diag}(\lambda_i)$。

??? proof "答案"

    设特征多项式 $p(t)=t^n+c_{n-1}t^{n-1}+\cdots+c_0$。第 $i$ 行 $w_i^T=(1,\lambda_i,\ldots,\lambda_i^{n-1})$ 与友矩阵 $C$ 相乘：前 $n-1$ 个分量依次为 $\lambda_i,\ldots,\lambda_i^{n-1}$；最后一个分量为

    $$-c_0-c_1\lambda_i-\cdots-c_{n-1}\lambda_i^{n-1}=\lambda_i^n,$$

    因为 $p(\lambda_i)=0$。所以 $w_i^TC=\lambda_iw_i^T$。将所有行叠起来得 $VC=\operatorname{diag}(\lambda_i)V$。还需说明 $V$ 可逆：若 $Vc=0$，则多项式 $q(t)=\sum_{j=1}^n c_jt^{j-1}$ 在互异的 $n$ 个点 $\lambda_1,\ldots,\lambda_n$ 都为零；而 $\deg q\le n-1$，因子定理迫使 $q$ 恒为零，所以每个 $c_j=0$。因此 $V$ 的核只有零向量，作为方阵可逆。右乘 $V^{-1}$ 得 $VCV^{-1}=\operatorname{diag}(\lambda_i)$。

## Fixed-Point Convergence by Contraction

*2019 Final Contest · Individual · Problem 3(a) · [Original paper (PDF)](../assets/yau-papers/2019-final-individual.pdf)*

考虑用不动点迭代 $x_{n+1}=g(x_n)$ 求解非线性方程。 (a) 陈述迭代存在唯一不动点 $x=\alpha$ 的必要条件，并推导判定收敛阶的准则。

??? proof "答案"

    在区间 $[a,b]$ 上，$\alpha$ 是唯一固定点的充要条件是 $\alpha\in[a,b]$、$g(\alpha)=\alpha$，且对每个 $x\in[a,b]$ 且 $x\ne\alpha$ 都有 $g(x)\ne x$。连续映射 $g:[a,b]\to[a,b]$ 且 $|g'(x)|\le q<1$ 是保证存在唯一固定点并使迭代收敛的一个充分条件，不是唯一性的必要条件。

    先证收敛。任取 $x_0\in[a,b]$，令 $x_{n+1}=g(x_n)$。由中值定理，

    $$|x_{n+1}-x_n|\le q|x_n-x_{n-1}|\le\cdots\le q^n|x_1-x_0|.$$

    若 $m>n$，逐项相加并用等比数列求和：

    $$|x_m-x_n|\le\sum_{j=n}^{m-1}|x_{j+1}-x_j|\le |x_1-x_0|\sum_{j=n}^{m-1}q^j\le\frac{|x_1-x_0|q^n}{1-q}\longrightarrow0.$$

    所以 $(x_n)$ 是 Cauchy 列。闭区间 $[a,b]$ 完备，故 $x_n\to\alpha\in[a,b]$。连续性给出 $g(\alpha)=\lim g(x_n)=\lim x_{n+1}=\alpha$，因此固定点存在。若 $\alpha,\beta$ 都是固定点，则

    $$|\alpha-\beta|=|g(\alpha)-g(\beta)|\le q|\alpha-\beta|,$$

    而 $q<1$，只能有 $\alpha=\beta$，故固定点唯一。

    说明导数收缩条件并非必要：令 $g(x)=x-x^3$，区间为 $[-1/2,1/2]$。因 $|g(x)|=|x|(1-x^2)\le|x|\le1/2$，它映区间到自身；固定点方程 $g(x)=x$ 等价于 $x^3=0$，所以唯一固定点是 $0$。但 $g'(0)=1$，任何含 $0$ 的区间上都不可能有统一的 $|g'(x)|\le q<1$。因此“区间映入自身且导数一致小于 $1$”是方便的充分条件，不能称为必要条件。

    最后说明局部收敛阶，并区分“误差关系”和“迭代收敛”。设 $p\ge1$，$g$ 在 $\alpha$ 附近有 $p$ 阶连续导数，且

    $$g(\alpha)=\alpha,\qquad g'(\alpha)=\cdots=g^{(p-1)}(\alpha)=0,\qquad g^{(p)}(\alpha)\ne0.$$

    令 $c=g^{(p)}(\alpha)/p!\ne0$。Taylor 公式给出对 $e_n=x_n-\alpha$，

    $$e_{n+1}=g(\alpha+e_n)-g(\alpha)=c e_n^p+o(e_n^p).$$

    这条展开本身不保证从任意初值收敛。若题设已知 $x_n\to\alpha$，并且误差最终不为零，则除以 $e_n^p$ 可得 $e_{n+1}/e_n^p\to c$，故该收敛序列的局部阶为 $p$。若 $p\ge2$，则 $|e_{n+1}|/|e_n|=|c+o(1)|\,|e_n|^{p-1}\to0$；选取 $q<1$ 后，误差充分小时有 $|e_{n+1}|\le q|e_n|$，所以足够靠近且不恰好落到固定点的初值会局部收敛。若 $p=1$ 且 $|g'(\alpha)|<1$，同样由误差比趋于 $|g'(\alpha)|$ 可得局部收敛；若 $|g'(\alpha)|>1$，非零误差在充分靠近时反而增大；当 $|g'(\alpha)|=1$ 时，仅凭一阶项不能判定，例如 $g(x)=x-x^3$ 在 $[-1/2,1/2]$ 上迭代会收敛到 $0$。

## Convergence of a Two-Block Iteration

*2019 Final Contest · Individual · Problem 5 · [Original paper (PDF)](../assets/yau-papers/2019-final-individual.pdf)*

$A$ 可逆，求解 $Ax_1+Bx_2=b_1$、$Bx_1+Ax_2=b_2$，并考虑同步迭代 $Ax_1^{k+1}=b_1-Bx_2^k$、$Ax_2^{k+1}=b_2-Bx_1^k$。原卷问该迭代对“某个初值”收敛的充要条件。先按这句话的字面含义作答，再给出对任意初值收敛到唯一解的充要条件。

??? proof "答案"

    置 $C=A^{-1}B$、$d_i=A^{-1}b_i$。乘以 $A^{-1}$ 后，固定点方程为

    $$x_1+Cx_2=d_1,\qquad Cx_1+x_2=d_2.$$

    令 $u=x_1+x_2$、$v=x_1-x_2$。将两式相加、相减，分别得到

    $$(I+C)u=d_1+d_2,\qquad (I-C)v=d_1-d_2.$$

    反过来，若这两式有解，则 $x_1=(u+v)/2$、$x_2=(u-v)/2$ 解原方程组。因此原系统有解，当且仅当 $d_1+d_2\in\operatorname{Range}(I+C)$ 且 $d_1-d_2\in\operatorname{Range}(I-C)$。

    按原卷“对某个初值收敛”的字面含义，充要条件就是上述系统有解：若有解，取该解本身为初值，迭代每一步都不变；反过来，若某条迭代轨道收敛到 $x^*$，把极限代入连续的仿射更新式，便得到固定点方程，所以系统必须有解。

    若题意本想问“对任意初值收敛到唯一解”，则令误差 $e_r=(x_1^r-x_1^*,x_2^r-x_2^*)^T$，有

    $$e_{r+1}=T e_r,\qquad T=\begin{pmatrix}0&-C\\-C&0\end{pmatrix}.$$

    对误差作可逆变量变换 $u=e_1+e_2$、$v=e_1-e_2$，得到 $u'=-Cu$、$v'=Cv$，所以 $T$ 与 $\operatorname{diag}(-C,C)$ 相似，$\rho(T)=\rho(C)$。Stage 1 的定常迭代判据给出 $T^r\to0$ 当且仅当 $\rho(T)<1$。故任意初值收敛到唯一解的充要条件为 $\rho(A^{-1}B)<1$；该条件充分保证上面的两个方程对任意右端均唯一可解。

## Convergence of the Power Method

*2020 Written Contest · Individual · Problem 3 · [Original paper (PDF)](../assets/yau-papers/2020-written-individual.pdf)*

$A$ 有完整正交单位特征向量 $q_j$，特征值满足 $|\lambda_1|>|\lambda_2|>|\lambda_3|$、$\lambda_j\ge\lambda_{j+1}$（$j\ge3$）。$v^{(k)}=Av^{(k-1)}/\lambda_1$，$v^{(0)}=\sum_j\alpha_jq_j$，$\alpha_1\alpha_2\ne0$。讨论是否线性收敛到 $\alpha_1q_1$，因子为 $|\lambda_2/\lambda_1|$。

??? proof "答案"

    原卷只按大小排列 $\lambda_3,\lambda_4,\ldots$，没有限制它们的绝对值，因此给出的结论不成立。例如 $A=\operatorname{diag}(3,2,1,-4)$ 满足 $|\lambda_1|>|\lambda_2|>|\lambda_3|$ 且 $\lambda_j\ge\lambda_{j+1}$（$j\ge3$）；若 $\alpha_4\ne0$，第四坐标按 $(-4/3)^k$ 增长，不收敛到 $\alpha_1q_1$。

    若补充条件 $\max_{j\ge3}|\lambda_j|<|\lambda_2|$，则由特征向量展开

    $$
    v^{(k)}-\alpha_1q_1=\sum_{j\ge2}\alpha_j(\lambda_j/\lambda_1)^kq_j.
    $$

    正交性给

    $$
    \|v^{(k)}-\alpha_1q_1\|_2^2=\sum_{j\ge2}|\alpha_j|^2|\lambda_j/\lambda_1|^{2k}.
    $$

    因 $\alpha_2\ne0$，误差范数至少含非零项 $|\alpha_2||\lambda_2/\lambda_1|^k$；其余项按补充条件更快衰减。除以 $|\lambda_2/\lambda_1|^k$ 后，平方误差趋于 $|\alpha_2|^2$，所以误差的渐近收敛因子恰为 $|\lambda_2/\lambda_1|$。

## Stability under a Bounded Perturbation

*2020 Written Contest · Individual · Problem 5 · [Original paper (PDF)](../assets/yau-papers/2020-written-individual.pdf)*

**Extension — prerequisite.** This is a discrete Grönwall estimate: first prove the noncommutative telescoping identity below, then derive the scalar recurrence and exponential bound.

若 $u^{n+1}=Bu^n$ 稳定，即 $\|B^j\|\le K$ 对 $j\Delta t\le T$ 一致成立，且 $\|C(\Delta t)\|\le M$，证明 $u^{n+1}=(B+\Delta tC(\Delta t))u^n$ 稳定。

??? proof "答案"

    设 $D=B+\Delta t\,C(\Delta t)$，且 $n\Delta t\le T$。先对 $n$ 归纳证明恒等式，不交换 $B$ 与 $C$。$n=1$ 时右边为 $B+C(\Delta t)\Delta t=D$。若对 $n$ 成立，则左乘 $B$ 并加上 $\Delta t C(\Delta t)D^n$：

    $$BD^n+\Delta t C(\Delta t)D^n=B^{n+1}+\Delta t\sum_{j=0}^{n-1}B^{n-j}C(\Delta t)D^j+\Delta t B^0C(\Delta t)D^n=B^{n+1}+\Delta t\sum_{j=0}^{n}B^{n-j}C(\Delta t)D^j.$$

    左端等于 $(B+\Delta t C(\Delta t))D^n=D^{n+1}$，故归纳完成。

    因为所有指数 $0\le n-1-j\le n$ 对应的物理时间不超过 $T$，假设给出 $\|B^{n-1-j}\|\le K$；又 $\|C(\Delta t)\|\le M$。令 $a_n=\|D^n\|$，则

    $$a_n\le K+\Delta t KM\sum_{j=0}^{n-1}a_j.$$

    对 $n$ 作归纳可直接得到 $a_n\le K(1+\Delta t KM)^n$：若此前各项满足该界，则

    $$K+\Delta t KM\sum_{j=0}^{n-1}K(1+\Delta t KM)^j=K(1+\Delta t KM)^n.$$

    由 $1+s\le e^s$ 得

    $$\|D^n\|\le K e^{KMn\Delta t}\le K e^{KMT}.$$

    右端与步长及 $n$ 无关，因此扰动后的格式在同一有限时间区间上一致稳定。

## Pseudoinverses and Tikhonov Regularization

*2020 Final Contest · Individual · Set I · Problem I(1)、(2) · [Original paper (PDF)](../assets/yau-papers/2020-final-individual-set1.pdf)*

$A=VFU^T$ 为 SVD，定义 $A^+=UF^+V^T$。(1) 证明 $A^+b$ 是最小二乘解；(2) 证明 $\lim_{\alpha\downarrow0}(\alpha I+A^TA)^{-1}A^T=A^+$。

??? proof "答案"

    令紧致 SVD 为 $A=U_1\Sigma V_1^T$，其中 $\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_r)$、各 $\sigma_i>0$；把 $U_1,V_1$ 分别补成正交基。写 $c=U^Tb$。对任意 $x=Vz$，残差平方为

    $$\|Ax-b\|_2^2=\sum_{i=1}^r(\sigma_i z_i-c_i)^2+\sum_{i=r+1}^m c_i^2.$$

    第一项逐个在 $z_i=c_i/\sigma_i$ 时取到零，$z_{r+1},\ldots,z_n$ 不影响 $Ax$。因此最小二乘解存在，所有解的有效部分相同，且 $A^+b=\sum_{i=1}^r(c_i/\sigma_i)v_i$ 是其中唯一的最小范数解。

    对 $\alpha>0$，Tikhonov 正则化把最小二乘目标改为

    $$J_\alpha(x)=\|Ax-b\|_2^2+\alpha\|x\|_2^2.$$

    记 $G=A^TA+\alpha I$、$h=A^Tb$。展开可得 $J_\alpha(x)=x^TGx-2h^Tx+b^Tb$。对任意 $z\ne0$，$z^TGz=\|Az\|_2^2+\alpha\|z\|_2^2>0$，所以 $G$ 可逆。令 $x_\alpha=G^{-1}h$，则 $Gx_\alpha=h$；代入并配方：

    $$J_\alpha(x)=(x-x_\alpha)^TG(x-x_\alpha)+b^Tb-x_\alpha^TGx_\alpha.$$

    第一项在 $x=x_\alpha$ 时为零，其他 $x$ 时严格为正，因此 $x_\alpha=(A^TA+\alpha I)^{-1}A^Tb$ 是唯一最小化正则化目标的向量。这一结论只用到二次型展开和正定性。

    对正则化极限，把 $A^T$ 作用于左奇异向量 $u_i$ 得 $A^Tu_i=\sigma_i v_i$；正交补空间被映为零。于是

    $$
    (\alpha I+A^TA)^{-1}A^Tu_i=
    \begin{cases}\dfrac{\sigma_i}{\alpha+\sigma_i^2}v_i,&i\le r,\\0,&i>r.\end{cases}
    $$

    每个非零奇异方向的系数趋于 $1/\sigma_i$，零奇异方向始终为零。有限维空间中逐基向量取极限，得到算子极限 $\sum_{i=1}^r\sigma_i^{-1}v_iu_i^T=A^+$。

## Least-Squares Solutions and Sensitivity Bounds

*2021 Written Contest · Individual · Problem 4(a)、(b) · [Original paper (PDF)](../assets/yau-papers/2021-written-individual.pdf)*

$A\in\mathbb R^{m\times n}$，$m\ge n$，秩 $r<n$，紧致 SVD 为 $A=U_1\Sigma_1V_1^T$，令 $V_2$ 补全右正交基，$\sigma=\sigma_{\min}(\Sigma_1)>0$。对 $\min_x\|Ax-b\|_2$，(a) 求全部解；(b) 求最小范数解并证明其范数不超过 $\|b\|_2/\sigma$。

??? proof "答案"

    令 $U=[U_1,U_2]$、$V=[V_1,V_2]$ 为正交矩阵，并写 $x=V_1z_1+V_2z_2$、$b=U_1c_1+U_2c_2$，其中 $c_1=U_1^Tb,c_2=U_2^Tb$。由紧致 SVD，$Ax=U_1\Sigma_1z_1$，因此

    $$\|Ax-b\|_2^2=\|\Sigma_1z_1-c_1\|_2^2+\|c_2\|_2^2.$$

    第一项最小值为零，且只在 $z_1=\Sigma_1^{-1}c_1$ 时达到；$z_2$ 任意。故全部最小二乘解为

    $$x=V_1\Sigma_1^{-1}U_1^Tb+V_2z_2.$$

    $V_1,V_2$ 的列正交，所以 $\|x\|_2^2=\|\Sigma_1^{-1}U_1^Tb\|_2^2+\|z_2\|_2^2$。最小范数在且仅在 $z_2=0$ 达到。又 $\|\Sigma_1^{-1}\|_2=1/\sigma$、$\|U_1^Tb\|_2\le\|b\|_2$，故

    $$\|x_{\min}\|_2\le\frac{\|b\|_2}{\sigma}.$$

    等号界不能普遍改小：取 $b=\sigma u_i$ 对应最小非零奇异值方向，即达到该比值。

## Sequential Fixed-Point Iteration and Contractions

*2022 Written Contest · Individual · Problem 2 · [Original paper (PDF)](../assets/yau-papers/2022-written-individual.pdf)*

$H=(f,g)^T$ 连续可微，在不动点 $p=(x_*,y_*)$ 有 $\|J_H(p)\|_\infty<1$。证明采用 $x_{r+1}=f(x_r,y_r)$、$y_{r+1}=g(x_{r+1},y_r)$ 的先后更新，从充分靠近 $p$ 的初值出发收敛到 $p$。

??? proof "答案"

    取 $q$ 严格介于 $\|J_H(p)\|_\infty$ 与 $1$ 之间。由 $J_H$ 连续，可取以 $p$ 为中心、半径 $\delta>0$ 的闭正方形 $D$，使 $D$ 内每一点的两行绝对导数和均不超过 $q$。记 $z=(x,y)$、$p=(x_*,y_*)$，并令 $E=\|z-p\|_\infty$。因为正方形凸，线段 $p+t(z-p)$（$0\le t\le1$）全在 $D$。对 $\phi=f$ 或 $g$，一元链式法则和微积分基本定理给出

    $$\phi(z)-\phi(p)=\int_0^1\nabla\phi(p+t(z-p))\cdot(z-p)\,dt.$$

    逐项取绝对值，利用 $|x-x_*|,|y-y_*|\le E$ 及导数行和界：

    $$|\phi(z)-\phi(p)|\le\int_0^1\bigl(|\phi_x|\,|x-x_*|+|\phi_y|\,|y-y_*|\bigr)dt\le\int_0^1qE\,dt=qE.$$

    又因 $p$ 是不动点，$f(p)=x_*$、$g(p)=y_*$，于是

    $$|f(x,y)-x_*|\le qE,\qquad |g(x,y)-y_*|\le qE.$$

    令 $E_r=\max(|x_r-x_*|,|y_r-y_*|)$，并从 $E_0<\delta$ 开始。第一更新给 $|x_{r+1}-x_*|\le qE_r$，且 $|y_r-y_*|\le E_r$，所以混合点 $(x_{r+1},y_r)$ 仍在 $D$。对第二更新再用同一估计：

    $$|y_{r+1}-y_*|\le q\max(|x_{r+1}-x_*|,|y_r-y_*|)\le qE_r.$$

    因此两个新分量都离 $p$ 不超过 $qE_r<\delta$，邻域保持不变，且 $E_{r+1}\le qE_r$。归纳得到 $E_r\le q^rE_0\to0$，故从该邻域内的初值出发，顺序更新收敛到 $p$。

## Diagonal Dominance and Spectral Norm Bounds

*2022 Written Contest · Individual · Problem 3(a)–(d) · [Original paper (PDF)](../assets/yau-papers/2022-written-individual.pdf)*

设实方阵 $A=(a_{ij})$ 满足

$$
a_{ii}\ge\sum_{j\ne i}|a_{ij}|+2,\qquad a_{ii}\le7.
$$

(a) 证明可逆；(b) 从定义证明无穷范数等于最大绝对行和；(c) 给出该范数的上下界；(d) 当 $A=A^T$ 时给出 $\|A\|_2$、$\|A^{-1}\|_2$ 的界。

??? proof "答案"

    (a) 若 $Ax=0$ 且 $x\ne0$，取 $i$ 使 $|x_i|=\|x\|_\infty>0$。第 $i$ 行给

    $$a_{ii}|x_i|=\left|\sum_{j\ne i}a_{ij}x_j\right|\le\sum_{j\ne i}|a_{ij}|\,|x_j|\le(a_{ii}-2)|x_i|,$$

    矛盾，所以零空间只有零向量，方阵 $A$ 可逆。

    (b) 记 $R=\max_i\sum_j|a_{ij}|$。若 $\|x\|_\infty=1$，则 $|(Ax)_i|\le\sum_j|a_{ij}|$，故 $\|A\|_\infty\le R$。取达到最大行和的行 $i_*$，令 $x_j=1$ 当 $a_{i_*j}\ge0$、$x_j=-1$ 当 $a_{i_*j}<0$。则 $\|x\|_\infty=1$ 且 $(Ax)_{i_*}=R$，所以 $\|A\|_\infty=R$。

    (c) 每行 $a_{ii}\ge2$，且

    $$2\le a_{ii}+\sum_{j\ne i}|a_{ij}|\le2a_{ii}-2\le12,$$

    最后一步用 $a_{ii}\le7$。取最大行即可得 $2\le\|A\|_\infty\le12$。

    (d) 现在 $A=A^T$，特征值实，且由实对称谱定理可取特征向量 $x$。取坐标最大项 $|x_i|=\|x\|_\infty$，由 $Ax=\lambda x$ 得 $|\lambda-a_{ii}|\le\sum_{j\ne i}|a_{ij}|$。于是 $2\le a_{ii}-\sum_{j\ne i}|a_{ij}|\le\lambda\le a_{ii}+\sum_{j\ne i}|a_{ij}|\le12$。故 $A$ 正定；实对称矩阵的 $2$-范数是最大特征值，逆矩阵的范数是最小特征值倒数，因此

    $$2\le\|A\|_2\le12,\qquad 1/12\le\|A^{-1}\|_2\le1/2.$$

    这里用坐标最大项直接证明了所需谱界，不依赖未学的圆盘定理。

## Newton’s Method and a Parameter Bound

*2022 Final Contest · Individual · Problem II(a)、(b) · [Original paper (PDF)](../assets/yau-papers/2022-final-individual.pdf)*

$f(x)=x^{n+1}-b^nx+ab^n$，$a,b>0,n\ge1$。(a) 证明恰有两个不同正根当且仅当 $a<nb/(n+1)^{1+1/n}$；(b) 证明 Newton 从 $a$ 收敛到小根，从 $b$ 收敛到大根。

??? proof "答案"

    令 $s=b/(n+1)^{1/n}$。有 $f'(x)=(n+1)x^n-b^n$，故 $f$ 在 $(0,s)$ 严格递减，在 $(s,\infty)$ 严格递增；且 $f(0)=ab^n>0$、$f(x)\to\infty$。因此存在两个不同正根，当且仅当最小值 $f(s)<0$。直接代入

    $$f(s)=b^n\left(a-\frac{nb}{(n+1)^{1+1/n}}\right),$$

    得到题中条件。等号时 $s$ 是二重根，不是两个不同根。

    (b) 设两根为 $r_-<s<r_+$。题设条件给 $a<s$，且 $f(a)=a^{n+1}>0$、$f(s)<0$。由于 $f$ 在 $(0,s)$ 严格递减，介值定理给出唯一的零点 $r_-$，并且 $a<r_-<s$。又 $b>s$，且 $f(b)=ab^n>0$；由于 $f$ 在 $(s,\infty)$ 严格递增，介值定理给出唯一的零点 $r_+$，并且 $s<r_+<b$。

    对 $x>0$，有 $f''(x)=n(n+1)x^{n-1}>0$，所以 $f$ 严格凸。若 $x<r_-$ 且 $x>0$，则 $f(x)>0,f'(x)<0$。Newton 下一点 $N(x)=x-f(x)/f'(x)>x$；凸性意味着图像在切线之上，故切线在 $r_-$ 处不高于 $f(r_-)=0$，而切线斜率为负，所以其零点 $N(x)$ 不超过 $r_-$。于是从 $a$ 出发单调递增且不越过 $r_-$。同理，若 $x>r_+$，则 $f(x)>0,f'(x)>0$，故 $N(x)<x$；切线在 $r_+$ 处不高于零，斜率为正，所以 $N(x)\ge r_+$。从 $b$ 出发单调递减且不越过 $r_+$。两列分别有极限；把 Newton 公式取极限可知极限处 $f=0$，因此极限分别是 $r_-$ 和 $r_+$。

## Power Iteration and a Two-Variable Recurrence

*2023 Written Contest · Individual · Problem 3(a)、(b) · [Original paper (PDF)](../assets/yau-papers/2023-written-individual.pdf)*

**(a)** 实方阵有互异特征值且 $|\lambda_1|>|\lambda_2|\ge\cdots$，讨论 $z_r=A^rz_0/\|A^rz_0\|_\infty$ 的主特征方向收敛。**(b)** $x_0=y_0=1$，$x_{r+1}=x_r+y_r$，$y_{r+1}=x_{r+1}+x_r$，证明 $y_r/x_r\to\sqrt2$。

??? proof "答案"

    把实矩阵 $A$ 看作作用在 $\mathbb C^n$ 上。由于特征值互异，它们的特征向量构成复数域上的一组基。实矩阵的非实特征值成共轭对出现；若唯一模最大的 $\lambda_1$ 非实，其共轭也是同模的另一个特征值，矛盾。因此 $\lambda_1$ 是实数，并可取实特征向量 $v_1\in\mathbb R^n$。把其他特征向量按共轭成对选取后，实向量 $z_0$ 在该基下的主系数 $c_1$ 为实数。

    假设 $c_1\ne0$。于是 $A^rz_0\ne0$，归一化有定义。写 $z_0=\sum_i c_iv_i$，则

    $$
    A^rz_0=\lambda_1^r\left(c_1v_1+\sum_{i=2}^n c_i(\lambda_i/\lambda_1)^rv_i\right).
    $$

    对每个 $i\ge2$，$|\lambda_i/\lambda_1|<1$，故括号内趋于 $c_1v_1$。令 $s_r=\operatorname{sgn}(\lambda_1)^rz_r$。因为 $\lambda_1^r/|\lambda_1|^r=\operatorname{sgn}(\lambda_1)^r$，且范数连续，得到

    $$s_r\longrightarrow\frac{c_1}{|c_1|}\frac{v_1}{\|v_1\|_\infty}.$$

    若 $\lambda_1>0$，这就是 $z_r$ 的极限；若 $\lambda_1<0$，$z_r$ 的符号交替，向量序列通常不收敛，但无向特征直线收敛。令 $q=|\lambda_2/\lambda_1|<1$。有限维空间中坐标范数等价，因此括号内余项 $r_r$ 满足 $\|r_r\|_\infty\le C_0q^r$。记 $y_r=c_1v_1+r_r$、$y_*=c_1v_1\ne0$；充分大的 $r$ 有 $\|y_r\|_\infty\ge\|y_*\|_\infty/2$。对非零向量 $y,y_*$，三角不等式给出

    $$
    \left\|\frac{y}{\|y\|_\infty}-\frac{y_*}{\|y_*\|_\infty}\right\|_\infty
    \le \frac{\|y-y_*\|_\infty}{\|y\|_\infty}
    +\|y_*\|_\infty\left|\frac1{\|y\|_\infty}-\frac1{\|y_*\|_\infty}\right|
    \le \frac{2\|y-y_*\|_\infty}{\|y\|_\infty}.
    $$

    代入 $y=y_r$、$y_*=c_1v_1$，得到存在 $C>0$ 使

    $$\left\|s_r-\frac{c_1}{|c_1|}\frac{v_1}{\|v_1\|_\infty}\right\|_\infty\le Cq^r.$$

    若 $c_1=0$，则不能据此推出收敛到 $v_1$。


    (b) 由 $x_{r+1}=x_r+y_r$、$y_{r+1}=x_{r+1}+x_r=2x_r+y_r$，得到 $w_{r+1}=Mw_r$，其中 $M=\begin{pmatrix}1&1\\2&1\end{pmatrix}$。特征方程为 $(1-\lambda)^2-2=0$，特征值 $\lambda_+=1+\sqrt2$、$\lambda_-=1-\sqrt2$，特征向量分别可取 $v_+=(1,\sqrt2)^T$、$v_-=(1,-\sqrt2)^T$。解 $(1,1)^T=c_+v_++c_-v_-$ 得 $c_+=(1+1/\sqrt2)/2$、$c_-=(1-1/\sqrt2)/2$。故

    $$
    x_r=c_+\lambda_+^r+c_-\lambda_-^r,\qquad
    y_r=\sqrt2c_+\lambda_+^r-\sqrt2c_-\lambda_-^r.
    $$

    因 $|\lambda_-/\lambda_+|<1$ 且 $c_+>0$，将分子分母同除以 $c_+\lambda_+^r$ 后，含 $\lambda_-^r$ 的项趋于零，得到 $y_r/x_r\to\sqrt2$。

## Rank-One Matrix Updates and Fast Linear Solves

*2024 Written Contest · Individual · Problem 1(a)、(b) · [Original paper (PDF)](../assets/yau-papers/2024-written-individual.pdf)*

**Extension — prerequisite.** The fast solve uses the rank-one inverse formula and reuses solutions of Az=b and Ap=u; it is an algorithmic extension of matrix inversion.

设 $A$ 可逆，$\widehat A=A+uv^T$。(a) 求 $\widehat A$ 可逆的充要条件；(b) 假定用 $A$ 求解线性方程一次只需 $O(n)$ 次浮点运算，设计 $\widehat Ax=b$ 的 $O(n)$ 算法。

??? proof "答案"

    (a) 令 $p=A^{-1}u$，则 $\widehat A=A(I+pv^T)$。置 $d=1+v^Tp$。若 $d\ne0$，

    $$
    (I+pv^T)\left(I-\frac{pv^T}{d}\right)
    =I+pv^T-\frac{pv^T}{d}-\frac{p(v^Tp)v^T}{d}=I,
    $$

    故 $\widehat A^{-1}=A^{-1}-A^{-1}uv^TA^{-1}/d$。若 $d=0$，则 $p\ne0$（否则 $d=1$），且 $(I+pv^T)p=0$，所以 $\widehat A$ 奇异。于是可逆的充要条件是 $1+v^TA^{-1}u\ne0$。

    (b) 在 (a) 的可逆条件 $d=1+v^Tp\ne0$ 下，先解 $Az=b$ 与 $Ap=u$，再计算标量 $s=v^Tz$，并返回 $x=z-p(s/d)$。验证：

    $$
    \widehat Ax=(A+uv^T)(z-ps/d)
    =b-us/d+u(s-v^Tps/d)=b,
    $$

    因 $v^Tp=d-1$，括号 $s-(d-1)s/d=s/d$，两项抵消。在题设每次结构化求解 $Az=b$、$Ap=u$ 各用至多 $c_1n$、$c_2n$ 次运算的前提下，先后两次求解共至多 $(c_1+c_2)n$ 次；点积 $v^Tz$ 用 $n$ 次乘法和至多 $n-1$ 次加法，向量修正 $z-p(s/d)$ 用至多 $2n$ 次乘法和 $n$ 次减法。因此总运算数不超过 $Cn$（其中 $C$ 与 $n$ 无关），复杂度为 $O(n)$。这里算法只做两次结构化求解、一个点积和一个向量更新；不计算稠密矩阵向量积。若 $A$ 是一般稠密矩阵，求解并非 $O(n)$，所以线性复杂度必须以存在该快速求解器为前提。

## Convergence Order of a Modified Newton Method

*2025 Written Contest · Individual · Problem 1 · [Original paper (PDF)](../assets/yau-papers/2025-written-individual.pdf)*

**Extension — prerequisite.** This higher-order Newton analysis requires Taylor expansions through cubic terms and the simple-root assumption f′(ξ) ≠ 0; the derivation is included below.

对简单根 $\xi$，研究

$$
x_{r+1}=x_r-\alpha\frac{f(x_r)}{f'\!\left(x_r-\beta f(x_r)/f'(x_r)\right)}.
$$

选择常数 $\alpha,\beta$，使方法对一般光滑函数达到最高的局部收敛阶。

??? proof "答案"

    设 $e=x-\xi$，并令 $c_2=f''(\xi)/(2f'(\xi))$、$c_3=f^{(3)}(\xi)/(6f'(\xi))$。假设 $f$ 在根附近有足够阶连续导数且 $f'(\xi)\ne0$。Taylor 展开并除以 $f'(\xi)$：

    $$\frac{f(x)}{f'(\xi)}=e+c_2e^2+c_3e^3+O(e^4),\qquad
    \frac{f'(x)}{f'(\xi)}=1+2c_2e+3c_3e^2+O(e^3).$$

    用 $1/(1+u)=1-u+u^2+O(u^3)$，其中 $u=2c_2e+3c_3e^2+O(e^3)$，有

    $$\left(\frac{f'(x)}{f'(\xi)}\right)^{-1}=1-2c_2e+(4c_2^2-3c_3)e^2+O(e^3).$$

    逐项相乘：

    $$\frac{f(x)}{f'(x)}=(e+c_2e^2+c_3e^3)(1-2c_2e+(4c_2^2-3c_3)e^2)+O(e^4)
    =e-c_2e^2+(2c_2^2-2c_3)e^3+O(e^4).$$

    令 $y=x-\beta f(x)/f'(x)$，于是

    $$y-\xi=(1-\beta)e+\beta c_2e^2-\beta(2c_2^2-2c_3)e^3+O(e^4).$$

    再在 $\xi$ 处展开 $f'(y)$，保留到 $e^2$：

    $$\frac{f'(y)}{f'(\xi)}=1+2c_2(1-\beta)e+[2\beta c_2^2+3c_3(1-\beta)^2]e^2+O(e^3).$$

    迭代为 $x_{r+1}=x_r-\alpha f(x_r)/f'(y_r)$。将上式的倒数展开后乘以 $f(x)/f'(\xi)$，$e$、$e^2$ 项分别合并为

    $$e_{r+1}=(1-\alpha)e_r-\alpha(2\beta-1)c_2e_r^2+O(e_r^3).$$

    要消去一次项必须取 $\alpha=1$；在此条件下，要消去二次项（对一般 $c_2$）必须取 $\beta=1/2$。下面直接展示该选择后的三次项。代入 $\beta=1/2$，

    $$y-\xi=\frac12e+\frac12c_2e^2+O(e^3),\qquad
    \frac{f'(y)}{f'(\xi)}=1+c_2e+\left(c_2^2+\frac34c_3\right)e^2+O(e^3).$$

    因此

    $$\left(\frac{f'(y)}{f'(\xi)}\right)^{-1}=1-c_2e-\frac34c_3e^2+O(e^3).$$

    再与 $f(x)/f'(\xi)=e+c_2e^2+c_3e^3+O(e^4)$ 逐项相乘：

    $$\frac{f(x)}{f'(y)}=e+0\cdot e^2+\left(\frac14c_3-c_2^2\right)e^3+O(e^4).$$

    故

    $$e_{r+1}=e_r-\frac{f(x_r)}{f'(y_r)}=\left(c_2^2-\frac14c_3\right)e_r^3+O(e_r^4).$$

    这证明误差至多为三阶；若三次项系数非零，才可称恰为三阶。例如 $f(x)=x+x^3$、$\xi=0$ 时 $c_2=0,c_3=1$，系数为 $-1/4\ne0$。

## Spectral Radius of an Inverse Tridiagonal Matrix

*2025 Written Contest · Individual · Problem 2 · [Original paper (PDF)](../assets/yau-papers/2025-written-individual.pdf)*

$A$ 为 $8\times8$ 矩阵，主对角元全为零，上、下第一副对角元全为 $1$，其余为零。求 $\rho(A^{-1})$。

??? proof "答案"

    对 $j=1,\ldots,8$ 取 $\theta_j=j\pi/9$，令 $v_r^{(j)}=\sin(r\theta_j)$（$r=1,\ldots,8$），并设虚拟端点 $v_0=v_9=0$。用 $\sin((r-1)\theta)+\sin((r+1)\theta)=2\cos\theta\sin(r\theta)$，逐行得到

    $$Av^{(j)}=2\cos(\theta_j)v^{(j)}.$$

    每个向量非零，因为第一项 $\sin\theta_j\ne0$。八个特征值互异，故这些向量构成特征向量基；并且没有特征值为零，因为 $j\pi/9\ne\pi/2$。于是 $A$ 可逆，且 $A^{-1}$ 的特征值为 $1/(2\cos(j\pi/9))$。因此

    $$
    \rho(A^{-1})=\max_j\frac1{|2\cos(j\pi/9)|}
    =\frac1{2\cos(4\pi/9)}=\frac1{2\sin(\pi/18)}.
    $$

    最小绝对值出现在 $j=4,5$，数值约为 $2.879385242$。

## Optimal Orthonormal Projection and Principal Components

*2025 Written Contest · Individual · Problem 4 · [Original paper (PDF)](../assets/yau-papers/2025-written-individual.pdf)*

**Extension — prerequisite.** Principal component analysis here is the best-subspace problem for singular values of a data matrix; it uses orthogonal projection and the Frobenius norm.

给定 $y_1,\ldots,y_n\in\mathbb R^m$，令 $V=\operatorname{span}\{y_j\}$。对给定 $1\le\ell\le\dim V$，寻找 $\ell$ 个正交单位向量 $\psi_i$，使

$$
J=\sum_{j=1}^n\left\|y_j-\sum_{i=1}^\ell(y_j^T\psi_i)\psi_i\right\|_2^2
$$

最小。（$\ell=0$ 的空子空间情形显然，误差为 $\sum_j\|y_j\|_2^2$。）

??? proof "答案"

    令 $Y=[y_1,\ldots,y_n]$，$\Psi=[\psi_1,\ldots,\psi_\ell]$。因 $\psi_i$ 正交单位，投影矩阵 $P=\Psi\Psi^T$ 满足 $P^T=P$、$P^2=P$。按定义 $\|Z\|_F^2=\sum_{ij}Z_{ij}^2=\operatorname{tr}(Z^TZ)$，所以

    $$J=\|(I-P)Y\|_F^2=\operatorname{tr}(Y^T(I-P)^T(I-P)Y)=\operatorname{tr}(Y^T(I-P)Y).$$

    逐项求和可验证 $\operatorname{tr}(RS)=\sum_{i,j}R_{ij}S_{ji}=\operatorname{tr}(SR)$，因此可以循环移动迹内乘积的因子，得到

    $$J=\operatorname{tr}(Y^TY)-\operatorname{tr}(PYY^T)=\|Y\|_F^2-\operatorname{tr}(PYY^T).$$

    设 $YY^T u_j=\sigma_j^2u_j$，$\sigma_1\ge\sigma_2\ge\cdots\ge0$。对任意正交单位列 $\psi_i$，令 $a_j=\sum_{i=1}^{\ell}|u_j^T\psi_i|^2=\|P u_j\|^2$。投影不增范数，所以 $0\le a_j\le1$；且

    $$\sum_j a_j=\sum_{i=1}^{\ell}\sum_j|u_j^T\psi_i|^2=\ell.$$

    因此 $\operatorname{tr}(PYY^T)=\sum_j\sigma_j^2a_j\le\sum_{j=1}^{\ell}\sigma_j^2$。逐项核验这个不等式：令 $q=\sum_{j\le\ell}(1-a_j)$。由 $\sum_j a_j=\ell$，也有 $q=\sum_{j>\ell}a_j$。于是

    $$
    \sum_{j\le\ell}\sigma_j^2-\sum_j\sigma_j^2a_j
    =\sum_{j\le\ell}\sigma_j^2(1-a_j)-\sum_{j>\ell}\sigma_j^2a_j
    \ge\sigma_\ell^2q-\sigma_\ell^2q=0,
    $$

    因为前 $\ell$ 个奇异值平方至少是 $\sigma_\ell^2$，后面的至多是 $\sigma_\ell^2$。

    取 $\psi_i=u_i$（$i=1,\ldots,\ell$）时 $a_1=\cdots=a_\ell=1$、其余为零，达到上界。因此

    $$J_{\min}=\|Y\|_F^2-\sum_{j=1}^{\ell}\sigma_j^2=\sum_{j>\ell}\sigma_j^2.$$

    若并列奇异值跨越第 $\ell$ 位，最优子空间可能不唯一；若无并列则由所选主特征子空间给出最优解。

## Fixed Vectors, Singular Values, and Normal Matrices

*2026 Written Contest · Individual · Problem 5(a)–(c) · [Original paper (PDF)](../assets/yau-papers/2026-written-individual.pdf)*

**Extension — prerequisite.** The final equivalence uses the spectral theorem for real symmetric matrices applied to AᵀA; the normal-matrix statement is an extension beyond the core stage-one material.

对实方阵 $A$，称 $Ax=x$ 的向量为其不动点。(a) 若最大奇异值 $\sigma_1(A)\le1$，证明这些向量也满足 $A^Tx=x$；(b) 用 $A=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ 说明范数条件不可直接删去；(c) 若 $AA^T=A^TA$，证明相同结论。

??? proof "答案"

    记 $\|A\|_2=\sigma_1(A)$。

    (a) 若 $x=0$，结论显然。对 $x\ne0$，由 $Ax=x$ 得 $\|Ax\|_2=\|x\|_2$。取 SVD $A=U\Sigma V^T$，令 $z=V^Tx$。则

    $$\|x\|_2^2-\|Ax\|_2^2=\sum_i(1-\sigma_i^2)z_i^2=0.$$

    题设给 $0\le\sigma_i\le1$，所以每项 $(1-\sigma_i^2)z_i^2\ge0$；总和为零迫使每一项为零。于是 $\Sigma^2z=z$，也就是 $A^TAx=x$。再用 $Ax=x$ 左乘 $A^T$，得到 $A^Tx=A^TAx=x$。

    (b) 令 $x=(s,t)^T$。此矩阵满足 $Ax=(s+t,0)^T$，所以 $Ax=x$ 当且仅当 $t=0$；每个 $x=(s,0)^T$ 都是固定向量。可是 $A^Tx=(s,s)^T$，当 $s\ne0$ 时不等于 $x$。该矩阵确实不满足 (a) 的范数条件：$A^TA=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ 的最大特征值是 $2$，故 $\sigma_1(A)=\sqrt2>1$。

    (c) 令 $B=A-I$。由 $AA^T=A^TA$，展开可得

    $$BB^T=(A-I)(A^T-I)=AA^T-A-A^T+I=A^TA-A-A^T+I=B^TB.$$

    题设 $Ax=x$ 即 $Bx=0$。于是

    $$\|B^Tx\|_2^2=x^TBB^Tx=x^TB^TBx=\|Bx\|_2^2=0.$$

    范数为零只可能是零向量，因此 $B^Tx=0$，即 $(A^T-I)x=0$，所以 $A^Tx=x$。
