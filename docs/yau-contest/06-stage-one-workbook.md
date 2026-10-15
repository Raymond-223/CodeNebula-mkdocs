# 丘赛真题

## 2010 · 笔试·个人赛

### [第 5(1)–(3) 题](../assets/yau-papers/2010-written-individual.pdf)

设 $S=\begin{pmatrix}\sigma&u^T\\0&S_c\end{pmatrix}$、$T=\begin{pmatrix}\tau&v^T\\0&T_c\end{pmatrix}$、$b=(\beta,b_c^T)^T$。

(1) 已知 $(S_cT_c-\lambda I)x_c=b_c$ 和 $w_c=T_cx_c$，证明取 $\gamma=(\beta-\sigma v^Tx_c-u^Tw_c)/(\sigma\tau-\lambda)$ 后，$x=(\gamma,x_c^T)^T$ 解 $(ST-\lambda I)x=b$。

(2) 对上三角 $U_1,U_2$，设计 $O(n^2)$ 算法解 $(U_1U_2-\lambda I)x=b$。

(3) 推广到 $p$ 个上三角矩阵乘积，要求 $O(pn^2)$。后两问均假定系数矩阵非奇异。

??? proof "答案"

    (1) $ST$ 的右上块为 $\sigma v^T+u^TT_c$。下方程已满足，上方程就是 $(\sigma\tau-\lambda)\gamma+\sigma v^Tx_c+u^Tw_c=\beta$。公式要求 $\sigma\tau\ne\lambda$。

    (2)(3) 从 $i=n$ 到 $1$ 回代，并保存中间向量 $z^{(p)}=x$、$z^{(r-1)}=U_rz^{(r)}$。记

    $$
    d_r=(U_r)_{ii},\quad t_r=\sum_{j>i}(U_r)_{ij}z_j^{(r)}.
    $$

    令 $a_p=1,c_p=0$，依次计算 $a_{r-1}=d_ra_r$、$c_{r-1}=d_rc_r+t_r$。于是 $z_i^{(0)}=a_0x_i+c_0$，取 $x_i=(b_i-c_0)/(a_0-\lambda)$，再更新每个 $z_i^{(r)}$。非奇异性保证所有分母非零。第 $i$ 行花费 $O(p(n-i)+p)$，总计 $O(pn^2)$；$p=2$ 即第二问。

### [第 6(1)、(2) 题](../assets/yau-papers/2010-written-individual.pdf)

(1) 对 $A\in\mathbb R^{m\times n}$，证明存在正交 $U,V$，使 $U^TAV$ 为矩形非负对角矩阵，奇异值递减排列。

(2) 若 $\operatorname{rank}(A)=r$，$0<k<r$，证明 $\min_{\operatorname{rank}(B)=k}\|A-B\|_2=\sigma_{k+1}$。

??? proof "答案"

    (1) 正交对角化 $A^TA$，取单位特征向量 $v_i$ 和 $\sigma_i=\sqrt{\lambda_i(A^TA)}$。对 $\sigma_i>0$ 令 $u_i=Av_i/\sigma_i$，这些 $u_i$ 正交，再扩充两侧的正交基，便有 $A=U\Sigma V^T$。

    (2) 取 $A_k=\sum_{i\le k}\sigma_i u_iv_i^T$，误差为 $\sigma_{k+1}$。任意秩 $k$ 的 $B$ 在 $\operatorname{span}(v_1,\ldots,v_{k+1})$ 中有单位零向量 $z$；故 $\|A-B\|_2\ge\|(A-B)z\|_2=\|Az\|_2\ge\sigma_{k+1}$。

## 2010 · 笔试·团体赛

### [第 5(i)、(ii) 题](../assets/yau-papers/2010-written-team.pdf)

周期网格上，$u_j^{n+1}=(1-\lambda)u_j^n+\lambda u_{j-1}^n$，$\lambda=\Delta t/\Delta x$。

(i) 当 $0\le\lambda\le1$ 时，证明 $\ell^2$、$\ell^\infty$ 稳定性。

(ii) 一位学生认为有限维范数等价，所以一个范数下与网格无关的稳定性自动推出任意范数下的稳定性。是否正确？

??? proof "答案"

    (i) 设周期移位 $S$，则 $\|S\|_2=\|S\|_\infty=1$。更新矩阵 $B=(1-\lambda)I+\lambda S$ 满足两种范数下 $\|B\|\le1$，故 $\|u^n\|\le\|u^0\|$。

    (ii) 不正确。范数等价常数可能依赖维数，而维数随网格细化增加。例如 $\|x\|_\infty\le\|x\|_2\le\sqrt N\|x\|_\infty$。因此转换出的稳定性常数可能随 $N$ 发散。

### [第 6(i)–(iii) 题](../assets/yau-papers/2010-written-team.pdf)

$A,B$ 可对角化且特征值均实，周期方程 $u_t+Au_x=0$、$u_t+Bu_x=0$。(i) 证明两者 $L^2$ 适定；(ii) $C=A+B$ 对应方程是否必适定？(iii) 各自稳定的一致差分算子 $A_h,B_h$，其分裂乘积 $B_hA_h$ 是否必稳定？

??? proof "答案"

    (i) 写 $A=S\Lambda S^{-1}$。特征坐标中的每个分量仅作实速度平移，保持 $L^2$ 范数，所以 $\|u(t)\|\le\|S\|\|S^{-1}\|\|u(0)\|$；$B$ 同理。

    (ii) 否。取 $A=\begin{pmatrix}1&1\\0&-1\end{pmatrix}$、$B=\begin{pmatrix}-1&0\\-1&1\end{pmatrix}$，两者特征值 $\pm1$，但 $C=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ 特征值 $\pm i$。空间频率 $m$ 的解算子 $e^{-imCt}$ 有增长 $e^{|m|t}$，不存在与频率无关的界。

    (iii) 否。取时间步等于空间步 $h$，分别用各特征分量向对应方向平移一个网格点的精确输运差分，单个算子的任意次幂均由各自固定的对角化条件数控制，且一致。频率角 $\theta=\pi/2$ 上，因 $A^2=B^2=I$，其因子分别为 $-iA,-iB$；分裂因子为 $-BA$，谱半径 $(1+\sqrt5)/2>1$。取周期网格数为 $4$ 的倍数即可得到该模式，其累计增长随 $T/h$ 指数发散。

## 2011 · 笔试·个人赛

### [第 1(1)–(4) 题](../assets/yau-papers/2011-written-individual.pdf)

给定正权 $\rho$ 和内积 $\langle f,g\rangle=\int_a^b\rho fg$。令 $p_0=1$、$p_1=x-a_1$，$p_n=(x-a_n)p_{n-1}-b_np_{n-2}$，其中 $a_n=\langle xp_{n-1},p_{n-1}\rangle/\|p_{n-1}\|^2$、$b_n=\langle xp_{n-1},p_{n-2}\rangle/\|p_{n-2}\|^2$。

(1) 证明 $p_n$ 为首一正交多项式；(2) 证明首一正交多项式唯一，且在所有同次首一多项式中范数最小；(3) 对 $\rho=(1-x^2)^{-1/2}$、$[a,b]=[-1,1]$，验证 $T_n(x)=\cos(n\arccos x)$ 的正交性与递推式；(4) 求该权下 $x^3$ 的最佳二次逼近。

??? proof "答案"

    (1) 递推保持首一。对 $j<n-2$，$\langle xp_{n-1},p_j\rangle=\langle p_{n-1},xp_j\rangle=0$；对 $j=n-1,n-2$，系数 $a_n,b_n$ 恰好消去内积，归纳即得正交性。

    (2) 任意另一首一多项式写成 $q=p_n+r$，$\deg r<n$，于是 $\|q\|^2=\|p_n\|^2+\|r\|^2$。唯一最小者为 $p_n$。

    (3) 令 $x=\cos\theta$，内积化为 $\int_0^\pi\cos(n\theta)\cos(m\theta)\,d\theta$，异次为零。和角公式给出 $T_{n+1}=2xT_n-T_{n-1}$。$T_n$ 的首项系数为 $2^{n-1}$（$n\ge1$），因此首一归一化应是 $2^{1-n}T_n$，原卷将 $T_n$ 直接称为首一时需作此修正。

    (4) $x^3=(T_3+3T_1)/4$，最佳二次逼近为 $3x/4$。

### [第 2 题](../assets/yau-papers/2011-written-individual.pdf)

五次多项式 $p,q$ 满足 $p(i)=q(i)=1/i$（$i=2,3,4,5,6$），且 $p(1)=1,q(1)=2$。求 $p(0)-q(0)$。

??? proof "答案"

    $p(x)-q(x)=C\prod_{j=2}^6(x-j)$。代入 $x=1$ 得 $C=1/120$，故 $p(0)-q(0)=-720/120=-6$。

## 2011 · 笔试·团体赛

### [第 1(a)–(d) 题](../assets/yau-papers/2011-written-team.pdf)

设 $A$ 对称正定。共轭梯度递推为 $r_0=b-Ax_0,p_0=r_0$，

$$
\alpha_k=\frac{r_k^Tr_k}{p_k^TAp_k},\quad x_{k+1}=x_k+\alpha_kp_k,\quad r_{k+1}=r_k-\alpha_kAp_k,
\quad\beta_k=-\frac{r_{k+1}^TAp_k}{p_k^TAp_k},\quad p_{k+1}=r_{k+1}+\beta_kp_k.
$$

(a) 证明 $\alpha_k$ 最小化 $f(x_k+\alpha p_k)$，$f(x)=x^TAx/2-b^Tx$；(b) 证明 $p_i^Tr_k=0$（$i<k$）及 $p_i^TAp_j=0$（$i\ne j$）；(c) 证明前 $k$ 个搜索方向与残差张成同一空间 $K_k$；(d) 证明 $r_k\perp K_k$。

??? proof "答案"

    归纳同时得到残差两两正交、搜索方向 $A$-共轭及 $p_k^Tr_k=r_k^Tr_k$。因此

    $$
    \frac d{d\alpha}f(x_k+\alpha p_k)=-p_k^Tr_k+\alpha p_k^TAp_k,
    $$

    唯一零点即 $\alpha_k$。更新残差后，对 $i\le k$ 有 $p_i^Tr_{k+1}=0$：$i<k$ 时使用 $A$-共轭，$i=k$ 时使用 $\alpha_k$ 的定义。新方向与 $p_k$ 的 $A$-内积由 $\beta_k$ 消去；对 $i<k$，利用 $Ap_i=(r_i-r_{i+1})/\alpha_i$ 和残差正交性，仍得零。又 $p_k=r_k+\beta_{k-1}p_{k-1}$ 是对角为 $1$ 的三角基变换，所以两组向量张成相同的 $K_k$，且 $r_k$ 与此前各向量正交。残差为零时停止，分母仅在未停止时使用。

### [第 2(i)、(ii) 题](../assets/yau-papers/2011-written-team.pdf)

周期网格上用 $u_j^{n+1}=a u_{j-2}^n+b u_{j-1}^n+c u_j^n$ 逼近 $u_t+u_x=0$，$\lambda=\Delta t/\Delta x$。(i) 求二阶准确的系数；(ii) 验证 $\lambda=1,2$ 时精确，并求 $\ell^2$ 稳定范围。

??? proof "答案"

    Taylor 匹配给出 $a+b+c=1$、$2a+b=\lambda$、$4a+b=\lambda^2$，因此

    $$
    a=\frac{\lambda(\lambda-1)}2,\quad b=\lambda(2-\lambda),\quad c=\frac{(\lambda-1)(\lambda-2)}2.
    $$

    $\lambda=1,2$ 时分别是一格、两格精确移位。对周期移位的特征值 $e^{-i\theta}$，更新因子为 $g=a e^{-2i\theta}+b e^{-i\theta}+c$，且

    $$
    |g|^2=1+\lambda(\lambda-2)(\lambda-1)^2(1-\cos\theta)^2.
    $$

    移位可被单位正交的复指数基对角化，故稳定范围为 $0\le\lambda\le2$。两个特殊步长处精确，本身不构成对中间步长的稳定性证明。

## 2012 · 笔试·个人赛

### [第 1 题](../assets/yau-papers/2012-written-individual.pdf)

求 $a,b,c$，使 $\int_{-1}^1 f(x)\,dx\approx af(-1)+bf(c)$ 对尽可能高次数的全部多项式精确；给出最高次数。

??? proof "答案"

    匹配 $1,x,x^2$ 得 $a+b=2$、$-a+bc=0$、$a+bc^2=2/3$，唯一解为 $a=1/2,b=3/2,c=1/3$。对 $x^3$，公式给出 $-4/9$ 而真积分为 $0$，故最高次数为 $2$。

### [第 2(a)–(c) 题](../assets/yau-papers/2012-written-individual.pdf)

给定中心 $\bar x$、$K>m$ 个互异点 $x_k$，令 $h=\max_k|x_k-\bar x|$。以 $P(t)=\sum_{i=0}^m c_i(t-\bar x)^i$ 最小化 $\sum_k|P(x_k)-f(x_k)|^2$。

(a) 证明解唯一；(b) 对光滑 $f$，证明 $|c_i-f^{(i)}(\bar x)/i!|\le C h^{m+1-i}$；(c) 若采样点关于 $\bar x$ 对称，证明与 $m$ 同奇偶的 $i$ 有 $|c_i-f^{(i)}(\bar x)/i!|\le C h^{m+2-i}$。

??? proof "答案"

    (a) 设计矩阵 $V_{ki}=(x_k-\bar x)^i$ 满列秩：$Vc=0$ 的多项式有至少 $m+1$ 个不同零点，只能恒为零。因此 $V^TV$ 正定。

    (b) 对任意 $m+1$ 个采样点的插值多项式，用 Newton 插值表示及反复 Rolle 定理，可得它与中心 $m$ 次 Taylor 多项式的第 $i$ 个系数差为 $O(h^{m+1-i})$，常数由 $m$ 及 $\sup|f^{(m+1)}|$ 控制。最小二乘多项式是这些插值多项式的凸组合，组合权重为

    $$
    \omega_J=\frac{\det(V_J)^2}{\sum_{|L|=m+1}\det(V_L)^2}.
    $$

    该恒等式由 Cramer 法则和 Cauchy–Binet 展开得到。因此同阶系数界对最小二乘解也成立。

    (c) 对称采样下，奇、偶多项式子空间正交，投影保持奇偶性。$m+1$ 次 Taylor 项与 $m$ 反奇偶，其投影不影响同奇偶的 $c_i$。对 $m+2$ 阶余项再用 (b) 的论证，得到提高一阶的界。此问需 $f$ 的相应高阶导数有界；原卷中的等式应理解为带常数的误差上界。

### [第 3(i)–(iii) 题](../assets/yau-papers/2012-written-individual.pdf)

对周期平流 $u_t+u_x=0$ 用前向时间、中心空间格式 $v_j^{n+1}=v_j^n-\frac{k}{2h}(v_{j+1}^n-v_{j-1}^n)$。(i) 求模及稳定性；(ii) 给出稳定并收敛的网格限制；(iii) 给出满足 CFL 时稳定的修改。

??? proof "答案"

    (i) 因子 $g=1-i(k/h)\sin\theta$，非零模式 $|g|>1$，固定非零 $k/h$ 时不稳定。

    (ii) $|g|\le\exp(k^2/(2h^2))$，若 $k/h^2\le C$，有限时间累计因子至多 $e^{CT/2}$。一致性误差 $O(k+h^2)$，稳定递推保证对光滑解收敛。

    (iii) 例如上风 $v_j^{n+1}=(1-\lambda)v_j^n+\lambda v_{j-1}^n$，$0\le\lambda=k/h\le1$；Lax–Friedrichs 或 Lax–Wendroff 也在 $|\lambda|\le1$ 下稳定。前者由非负权重、后两者由逐模式 $|g|\le1$ 验证。

### [第 4(1)–(3) 题](../assets/yau-papers/2012-written-individual.pdf)

已知 Hermitian 矩阵 $C,D$ 的递减特征值满足 $\sum_i(\lambda_i(C)-\lambda_i(D))^2\le\|C-D\|_F^2$。

(1) 证明任意复方阵 $A,B$ 的奇异值满足 $\sum_i(\sigma_i(A)-\sigma_i(B))^2\le\|A-B\|_F^2$。


**原卷：** [2012 应用与计算数学个人赛，第 2–3 页](../assets/yau-papers/2012-computational-applied.pdf#page=2)。**先修：** [伪逆与低秩逼近](02-pseudoinverse-low-rank.md)。

**(2)** 设 $A=U\Sigma V^T\in\mathbb R^{n\times n}$ 且 $\operatorname{rank}(A)>k$。证明截断矩阵 $A_k=\sum_{i=1}^k\sigma_i u_iv_i^T$ 达到最佳秩 $k$ 的 Frobenius 逼近，误差平方为 $\sum_{i>k}\sigma_i^2$。

**(3)** 对样本矩阵 $X=[x_1,\ldots,x_n]$，寻找 $c\in\mathbb R^n$、$W\in\mathbb R^{n\times d}$（$W^TW=I_d$）和坐标矩阵 $R$，使 $\|X-c\mathbf1^T-WR\|_F$ 最小。

??? proof "答案"

    (1) 对 $H(A)=\begin{pmatrix}0&A\\A^*&0\end{pmatrix}$ 和 $H(B)$ 应用已给定的特征值不等式。SVD 给出 $H(A)$ 的特征值为 $\sigma_1,\ldots,\sigma_n,-\sigma_n,\ldots,-\sigma_1$，同时 $\|H(A)-H(B)\|_F^2=2\|A-B\|_F^2$；两侧约去 $2$。

    **(2)** 任意秩不超过 $k$ 的 $B$，令 $P$ 为其列空间的正交投影，则 $PB=B$，并有

    $$
    \|A-B\|_F^2\ge\|(I-P)(A-B)\|_F^2
    =\|A\|_F^2-\operatorname{tr}(PAA^T).
    $$

    设 $AA^T=U\operatorname{diag}(\sigma_i^2)U^T$，$p_i=u_i^TPu_i$。投影性质给出 $0\le p_i\le1$、$\sum_i p_i\le k$。由于 $\sigma_i^2$ 递减，$\sum_i\sigma_i^2p_i\le\sum_{i=1}^k\sigma_i^2$：将权重从较小系数移到较大系数只会增大和，最大值由前 $k$ 个权重取 $1$ 达到。因此误差至少为 $\sum_{i>k}\sigma_i^2$。$A_k$ 恰好达到该下界，且因 $\sigma_k>0$，秩确为 $k$。

    **(3)** 令 $\bar x=X\mathbf1/n$、$H=I-\mathbf1\mathbf1^T/n$、$X_c=XH=X-\bar x\mathbf1^T$。固定 $c,W$ 时，按列正交投影得最优 $R=W^T(X-c\mathbf1^T)$。误差为

    $$
    \|(I-WW^T)X_c\|_F^2
    +n\|(I-WW^T)(\bar x-c)\|_2^2.
    $$

    交叉项为零，因为 $X_c\mathbf1=0$。可取 $c=\bar x$，再对 $X_c$ 做 SVD，取 $W$ 为前 $d$ 个左奇异向量，$R=W^TX_c$。最小误差平方为 $\sum_{i>d}\sigma_i(X_c)^2$。

    这是一个最优解；中心不必唯一。$c=\bar x+Wa$ 配合 $R=W^TX_c-a\mathbf1^T$ 给出同一重建。重奇异值也可能导致最优基不唯一。

### [第 5 题](../assets/yau-papers/2012-written-individual.pdf)

$N=pq$，素数 $q=p+2$。如何分解 $N$？

??? proof "答案"

    $N=(p+1)^2-1$，所以 $a=\sqrt{N+1}$ 为整数，$p=a-1,q=a+1$。只需一次整数平方根与验证，无须逐个试除。

## 2012 · 笔试·团体赛

### [第 1 题](../assets/yau-papers/2012-written-team.pdf)

$u\in C^{k+1}[0,2]$，次数不超过 $k$ 的 $p_n$ 满足 $\max_{0\le x\le1/n}|u(x)-p_n(x)|\le Cn^{-k-1}$。证明相邻区间 $[1/n,2/n]$ 上也有同阶界，常数与 $n$ 无关。

??? proof "答案"

    取 $u$ 在 $0$ 的 $k$ 次 Taylor 多项式 $T_k$。在 $[0,2/n]$ 上 $|u-T_k|\le M(2/n)^{k+1}/(k+1)!$。令 $q_n(t)=n^{k+1}(p_n(t/n)-T_k(t/n))$，其次数至多 $k$，在 $[0,1]$ 上一致有界。固定有限维多项式空间上，$\max_{[1,2]}|q|\le C_k\max_{[0,1]}|q|$，于是相邻区间也一致有界；加回 Taylor 余项即得结论。

### [第 3(1)、(3)、(4) 题](../assets/yau-papers/2012-written-team.pdf)

设 $A=I+L+U$ 严格行对角占优，$L,U$ 严格下、上三角，$\Omega=\operatorname{diag}(\omega_i)$，$0\le\alpha\le1$，

$$
M=(I+\alpha\Omega L)^{-1}\big((I-\Omega)-(1-\alpha)\Omega L-\Omega U\big).
$$

(1) 证明 $Ax=b$ 唯一可解；(3) 令 $l_i=\sum_{j<i}|a_{ij}|,u_i=\sum_{j>i}|a_{ij}|$，证明当 $|\alpha\omega_i|l_i<1$ 时

$$
\rho(M)\le\max_i\frac{|1-\omega_i|+|\omega_i|((1-\alpha)l_i+u_i)}{1-|\alpha\omega_i|l_i};
$$

(4) 证明实参数 $0<\omega_i<2/(1+l_i+u_i)$ 足以保证迭代矩阵收敛。

??? proof "答案"

    (1) 对假定的非零零向量，取绝对值最大分量，第 $i$ 行推出 $1\le l_i+u_i<1$，矛盾。

    (3) 取 $Mv=\lambda v$ 和 $|v_i|=\|v\|_\infty$，按该行取绝对值得

    $$
    |\lambda|(1-|\alpha\omega_i|l_i)\le |1-\omega_i|+|\omega_i|((1-\alpha)l_i+u_i).
    $$

    (4) 所给区间保证 $\omega_i l_i<1$，且 $|1-\omega_i|+\omega_i(l_i+u_i)<1$。代入 (3) 得 $\rho(M)<1$。若用于求 $Ax=b$，常数项应为 $(I+\alpha\Omega L)^{-1}\Omega b$；原卷式中的 $\Omega$ 漏写时，固定方程会变成 $\Omega Ax=b$。

### [第 3(2) 题](../assets/yau-papers/2012-written-team.pdf)

$A=I+L+U$ 严格行对角占优，$\Omega=\operatorname{diag}(\omega_i)$，$0\le\alpha\le1$。对 $M=(I+\alpha\Omega L)^{-1}[I-\Omega-(1-\alpha)\Omega L-\Omega U]$，原卷要求证明收敛的必要条件 $\prod_i|1-\omega_i|<1$。

??? proof "答案"

    当 $\alpha=1$ 时成立：括号中的矩阵上三角，$\det M=\prod_i(1-\omega_i)$，而 $\rho(M)<1$ 必有 $|\det M|<1$。

    对所写的一般 $\alpha$，结论不成立。取 $A=\begin{pmatrix}1&-.84&-.04\\-.41&1&-.30\\.55&-.37&1\end{pmatrix}$、$\Omega=\operatorname{diag}(1.71,2.70,1.83)$、$\alpha=.54$。各行严格占优，但乘积为 $1.00181>1$。直接计算 $M$ 的特征多项式为 $p(r)=r^3+(131713203339477/62500000000000)r^2+(62574213705573/31250000000000)r+49828567531877/62500000000000$。$p'$ 恒正，唯一实根在 $(-.857,-.856)$；其余两根共轭，模的平方为常数项除以实根绝对值，小于 $1$。故 $\rho(M)<1$，给出反例。

### [第 4 题](../assets/yau-papers/2012-written-team.pdf)

生成 RSA 模数时，从随机奇数开始搜索第一个素数 $p$，再从 $p+2$ 搜索下一个素数 $q$。已知相邻素数平均间距约 $\log p$。评价这一方法并给出分解算法。

??? proof "答案"

    相邻素数过近使模数容易被 Fermat 分解。令 $a=\lceil\sqrt N\rceil$，逐次检查 $a^2-N$ 是否为平方 $b^2$；成功时 $p=a-b,q=a+b$。需要搜索的量约为 $(p+q)/2-\sqrt{pq}=(q-p)^2/[2(\sqrt p+\sqrt q)^2]$。平均间距仅约 $\log p$ 时，这远小于 $1$，通常第一次平方检查即成功。平均间距不是所有样本的严格上界，但足以说明该生成方式缺乏所需的素数间隔。

### [第 5(a)–(c) 题](../assets/yau-papers/2012-written-team.pdf)

$h_t=(h^2)_{rr}+r^{-1}(h^2)_r$，$h_r(0,t)=0$、$\int_0^\infty h(r,t)rdr=1/64$，在移动边缘外为零。(a) 求保持方程和质量的缩放；(b) 令 $h=t^\alpha\Phi(\eta),r=t^\beta\eta$，求相似 ODE；(c) 求显式非负剖面及边缘 $r_*(t)$。

??? proof "答案"

    (a) $r=T^{1/4}\widetilde r,t=T\widetilde t,h=T^{-1/2}\widetilde h$。

    (b) 质量给 $\alpha+2\beta=0$，方程给 $\alpha-1=2\alpha-2\beta$，所以 $\alpha=-1/2,\beta=1/4$。ODE 为 $-\Phi/2-\eta\Phi'/4=(\Phi^2)''+(\Phi^2)'/\eta$。

    (c) $\Phi(\eta)=(1-\eta^2)_+/16$，$h=t^{-1/2}(1-r^2t^{-1/2})_+/16$、$r_*(t)=t^{1/4}$。直接代回支持内部的 ODE，并计算质量 $\int_0^1(1-\eta^2)\eta d\eta/16=1/64$。截断边缘按通量为零的弱意义理解。

## 2012 · 总决赛·个人赛

### [第 1 题](../assets/yau-papers/2012-final-individual.pdf)

以均匀网格 $x_j=jh$、$h=1/N$ 近似 $\int_0^1f(x)dx$，取 $h[a_0(f_0+f_N)+a_1(f_1+f_{N-1})+\sum_{j=2}^{N-2}f_j]$。求使误差阶最高的 $a_0,a_1$ 及最高阶。

??? proof "答案"

    $a_0=5/12,a_1=13/12$，最高为三阶。常函数精确要求 $a_0+a_1=3/2$。令 $\delta=a_1-1$，梯形公式的误差为 $h^2[f'(1)-f'(0)]/12+O(h^4)$，附加修正为 $-\delta h^2[f'(1)-f'(0)]+\delta h^3[f''(0)+f''(1)]/2+O(h^4)$。因此必须 $\delta=1/12$，而三阶项一般不为零。

### [第 2 题](../assets/yau-papers/2012-final-individual.pdf)

利用 $\gcd(2k,2l)=2\gcd(k,l)$、$\gcd(2k+1,2l)=\gcd(2k+1,l)$ 和 $\gcd(2k+1,l)=\gcd(2k+1-l,l)$，设计只使用减法与除以 $2$ 的最大公因数算法，并估计算术操作次数。

??? proof "答案"

    先提取两数共有的 $2$ 的幂；随后反复把偶数除以 $2$。两数均为奇数时，把较大数改为两数之差，再除以 $2$；一数为零时返回另一数乘上先提取的公因子。所给恒等式保证正确。每次“奇数相减再除以 $2$”使两数乘积至少减半，单独除以 $2$ 也使乘积减半，因此总算术操作次数 $O(\log(mn))=O(\log n)$（$m\le n$）；这是算术操作模型，未把长整数位运算记作常数成本。

## 2012 · 总决赛·综合个人赛

### [第 1(a)、(b) 题](../assets/yau-papers/2012-final-overall.pdf)

将 $[0,1]$ 分成长度 $h=1/N$ 的区间，$V_h$ 为各区间上次数不超过 $k$ 的分段多项式空间。$u_h$ 是 $u$ 的 $L^2$ 正交投影，$u,\phi\in C^{k+2}[0,1]$。

(1) 证明 $\|u-u_h\|_2\le Ch^{k+1}$；(2) 证明 $|\int_0^1(u-u_h)\phi|\le Ch^{2k+2}$，说明常数依赖。

??? proof "答案"

    每个区间取左端点的 $k$ 次 Taylor 多项式，拼成 $T_hu\in V_h$。Taylor 余项给出 $\|u-T_hu\|_2\le h^{k+1}\|u^{(k+1)}\|_\infty/(k+1)!$。最佳投影误差不会更大。

    由正交性，$\langle u-u_h,T_h\phi\rangle=0$，所以

    $$
    |\langle u-u_h,\phi\rangle|\le\|u-u_h\|_2\,\|\phi-T_h\phi\|_2
    \le\frac{\|u^{(k+1)}\|_\infty\|\phi^{(k+1)}\|_\infty}{((k+1)!)^2}h^{2k+2}.
    $$

## 2012 · 总决赛·团体赛

### [第 1 题](../assets/yau-papers/2012-final-team.pdf)

对 $u_t+u_x=u$，能否构造一致且满足 $\|v^{n+1}\|\le\|v^n\|$ 的差分格式？如果不能，给出适当的稳定性定义及一个格式。

??? proof "答案"

    不能要求每步范数不增长：空间常数解为 $u(t)=e^tu(0)$，一致格式的常数模式放大因子为 $1+k+o(k)>1$。合适要求为有限时间 $\|v^n\|\le Ce^{CT}\|v^0\|$，常数与网格无关。可用 $v_j^{n+1}=e^k[(1-\lambda)v_j^n+\lambda v_{j-1}^n]$，$\lambda=k/h\in[0,1]$。移位保持 $\ell^2,\ell^\infty$ 范数，故因子至多 $e^k$，累计至多 $e^T$；Taylor 展开验证一致性。

## 2013 · 笔试·个人赛

### [第 2(a)–(c) 题](../assets/yau-papers/2013-written-individual.pdf)

非负 $C^1$ 函数满足 $y'\le\alpha-\beta y^a$，$\beta>0$。(a) $a>1,\alpha>0$ 时证明 $y(t)\le(\alpha/\beta)^{1/a}+[\beta(a-1)t]^{-1/(a-1)}$；(b) $a=1$ 时证明 $y(t)\le\alpha/\beta+y(0)e^{-\beta t}$；(c) $\alpha=0,a<1$ 时求有限消失时间上界。

??? proof "答案"

    (a) 令 $r=(\alpha/\beta)^{1/a}$。在 $y>r$ 时，$z=y-r$ 满足 $z'\le-\beta z^a$，因为 $(r+z)^a\ge r^a+z^a$。对 $z^{1-a}$ 求导，得 $(z^{1-a})'\ge\beta(a-1)$，进而 $z(t)\le[\beta(a-1)t]^{-1/(a-1)}$；到达 $z=0$ 后不能向上越过。

    (b) $(e^{\beta t}(y-\alpha/\beta))'\le0$，故更精确的界为 $y(t)\le\alpha/\beta+(y(0)-\alpha/\beta)e^{-\beta t}$。

    (c) 对通常的 $0<a<1$，在 $y>0$ 时 $(y^{1-a})'\le-\beta(1-a)$，所以 $T_{\rm ext}\le y(0)^{1-a}/(\beta(1-a))$；此后由非负性与单调性恒为零。若允许 $a<0$，$y=0$ 处的 $y^a$ 未定义，原卷还需要对该端点补充约定。

### [第 3(a)–(c) 题](../assets/yau-papers/2013-written-individual.pdf)

球在黏性液体中下落，满足 $m v'=F-\zeta v$、$v(0)=v_0$，其中 $m=4\pi R^3\rho/3$、$F=4\pi R^3(\rho-\rho_f)g/3$、$\zeta=6\pi R\mu$。(a) 无量纲化；(b) 求解；(c) 描述比终端速度快、慢的情况，并求到达 $(v_0+V)/2$ 的时间。

??? proof "答案"

    取 $T=m/\zeta=2R^2\rho/(9\mu)$、$V=F/\zeta=2R^2(\rho-\rho_f)g/(9\mu)$，令 $t=T\tilde t,v=V\tilde v$，得 $d\tilde v/d\tilde t=1-\tilde v$、$\tilde v(0)=v_0/V$。

    $$
    v(t)=V+(v_0-V)e^{-t/T}.
    $$

    $v_0>V$ 时单调下降，$v_0<V$ 时单调上升；$v_0\ne V$ 时到中点的时间为 $T\log2$。若 $v_0=V$，从初始时刻已经达到目标。此缩放要求 $V\ne0$；中性浮力情形直接解 $v'=-(\zeta/m)v$。

### [第 4(1)、(2) 题](../assets/yau-papers/2013-written-individual.pdf)

将 $[0,1]$ 分成长度 $h=1/N$ 的区间，$V_h$ 为各区间上次数不超过 $k$ 的分段多项式空间。$u_h$ 是 $u$ 的 $L^2$ 正交投影，$u,\phi\in C^{k+2}[0,1]$。

(1) 证明 $\|u-u_h\|_2\le Ch^{k+1}$；(2) 证明 $|\int_0^1(u-u_h)\phi|\le Ch^{2k+2}$，说明常数依赖。

??? proof "答案"

    每个区间取左端点的 $k$ 次 Taylor 多项式，拼成 $T_hu\in V_h$。Taylor 余项给出 $\|u-T_hu\|_2\le h^{k+1}\|u^{(k+1)}\|_\infty/(k+1)!$。最佳投影误差不会更大。

    由正交性，$\langle u-u_h,T_h\phi\rangle=0$，所以

    $$
    |\langle u-u_h,\phi\rangle|\le\|u-u_h\|_2\,\|\phi-T_h\phi\|_2
    \le\frac{\|u^{(k+1)}\|_\infty\|\phi^{(k+1)}\|_\infty}{((k+1)!)^2}h^{2k+2}.
    $$

### [第 6 题](../assets/yau-papers/2013-written-individual.pdf)

$F_0=0,F_1=1,F_{n+2}=F_{n+1}+F_n$。求 $\begin{pmatrix}0&1\\1&1\end{pmatrix}^n$ 与 Fibonacci 数的关系，并设计比逐项递推更快的算法，估计运算次数。

??? proof "答案"

    对 $n\ge1$，归纳得 $M^n=\begin{pmatrix}F_{n-1}&F_n\\F_n&F_{n+1}\end{pmatrix}$。按二进制快速幂：偶指数先算 $M^{n/2}$ 再平方，奇指数再乘一次 $M$。每层固定次数的 $2\times2$ 乘法，层数 $O(\log n)$，所以算术运算次数为 $O(\log n)$。这是算术次数，不是将增长的整数位数视为免费的位复杂度。

## 2013 · 笔试·团体赛

### [第 1(a) 题](../assets/yau-papers/2013-written-team.pdf)

$U>0$ 在 $[0,\infty)$ 上递增，且 $\lim_{t\to\infty}U(tx)/U(t)=\psi(x)\in(0,\infty)$ 对全部 $x>0$ 成立。证明 $\psi(x)=x^\alpha$，其中 $\alpha\ge0$。

??? proof "答案"

    将 $U(txy)/U(t)$ 分解为 $[U(txy)/U(tx)][U(tx)/U(t)]$，得 $\psi(xy)=\psi(x)\psi(y)$。$\psi$ 递增，$\psi(1)=1$。令 $F(s)=\log\psi(e^s)$，则 $F(s+t)=F(s)+F(t)$ 且 $F$ 递增。有理数上 $F(q)=qF(1)$；以有理数从两侧夹逼任意实数，得 $F(s)=\alpha s$，$\alpha=F(1)\ge0$。

### [第 2(a)–(c) 题](../assets/yau-papers/2013-written-team.pdf)

光滑周期 $\phi$，$Fu=-\Delta u-\nabla\cdot(u\nabla\phi)$、$Wu=-\Delta u+\nabla\phi\cdot\nabla u$、$Su=-\Delta u+(|\nabla\phi|^2/4-\Delta\phi/2)u$。(a) 将 $F$ 写为 $-\nabla\cdot(e^{-\phi}\nabla(e^\phi u))$；(b) 证明三算子的特征值相同；(c) 求全部平衡解。

??? proof "答案"

    (a) 乘积法则给 $e^{-\phi}\nabla(e^\phi u)=\nabla u+u\nabla\phi$，再取负散度。

    (b) 直接展开得到 $F(e^{-\phi}v)=e^{-\phi}Wv$、$W(e^{\phi/2}z)=e^{\phi/2}Sz$。指数倍乘可逆，故每个特征函数在三个方程间一一对应，特征值保持。

    (c) 周期分部积分给 $\int e^{-\phi}vWv=\int e^{-\phi}|\nabla v|^2$，所以 $Wv=0$ 迫使 $v$ 为常数。由 (b)，$F,W,S$ 的平衡解分别为 $Ce^{-\phi},C,Ce^{-\phi/2}$（连通周期域）。

### [第 3 题](../assets/yau-papers/2013-written-team.pdf)

以均匀网格 $x_j=jh$、$h=1/N$ 近似 $\int_0^1f(x)dx$，取 $h[a_0(f_0+f_N)+a_1(f_1+f_{N-1})+\sum_{j=2}^{N-2}f_j]$。求使误差阶最高的 $a_0,a_1$ 及最高阶。

??? proof "答案"

    $a_0=5/12,a_1=13/12$，最高为三阶。常函数精确要求 $a_0+a_1=3/2$。令 $\delta=a_1-1$，梯形公式的误差为 $h^2[f'(1)-f'(0)]/12+O(h^4)$，附加修正为 $-\delta h^2[f'(1)-f'(0)]+\delta h^3[f''(0)+f''(1)]/2+O(h^4)$。因此必须 $\delta=1/12$，而三阶项一般不为零。

### [第 4(1) 题](../assets/yau-papers/2013-written-team.pdf)

$u_t+u_x=0,v_t-v_x=0$，$u(-1,t)=v(-1,t),v(1,t)=u(1,t)$。证明 $\frac d{dt}\int_{-1}^1(u^2+v^2)dx=0$。

??? proof "答案"

    对光滑解，导数为 $\int[-(u^2)_x+(v^2)_x]dx=[-u^2+v^2]_{-1}^1=0$，两端均由给定边界条件抵消。

### [第 4(2)、(3) 题](../assets/yau-papers/2013-written-team.pdf)

离散格式为 $u_j^{n+1}=(1-\lambda)u_j^n+\lambda u_{j-1}^n$（$j=-N+1,\ldots,N$），$v_j^{n+1}=(1-\lambda)v_j^n+\lambda v_{j+1}^n$（$j=-N,\ldots,N-1$），边界 $u_{-N}^n=v_{-N}^n,v_N^n=u_N^n$。

(2) 求使 $E^n=\sum_{j=-N+1}^N(u_j^n)^2+\sum_{j=-N}^{N-1}(v_j^n)^2$ 不增的步长限制；(3) 在同样限制下证明最大范数不增。

??? proof "答案"

    把 $u_{-N+1},\ldots,u_N,v_{N-1},\ldots,v_{-N}$ 排成一个向量，更新恰好为 $(1-\lambda)I+\lambda S$，其中 $S$ 是周期置换。$0\le\lambda\le1$ 时，两种诱导范数均不超过 $1$，所以 $E^{n+1}\le E^n$ 且最大范数不增。边界分量等于已包含分量，不改变最大值。

### [第 6 题](../assets/yau-papers/2013-written-team.pdf)

$F_0=0,F_1=1,F_{n+2}=F_{n+1}+F_n$。求 $\begin{pmatrix}0&1\\1&1\end{pmatrix}^n$ 与 Fibonacci 数的关系，并设计比逐项递推更快的算法，估计运算次数。

??? proof "答案"

    对 $n\ge1$，归纳得 $M^n=\begin{pmatrix}F_{n-1}&F_n\\F_n&F_{n+1}\end{pmatrix}$。按二进制快速幂：偶指数先算 $M^{n/2}$ 再平方，奇指数再乘一次 $M$。每层固定次数的 $2\times2$ 乘法，层数 $O(\log n)$，所以算术运算次数为 $O(\log n)$。这是算术次数，不是将增长的整数位数视为免费的位复杂度。

## 2013 · 总决赛·个人赛

### [第 1(a)、(b) 题](../assets/yau-papers/2013-final-individual.pdf)

$A$ 可逆。(a) 求 $A+uv^T$ 可逆的条件及逆矩阵；(b) 将 $A$ 第一列替换为 $b$，求新矩阵的逆。

??? proof "答案"

    (a) 可逆当且仅当 $1+v^TA^{-1}u\ne0$，逆为 $A^{-1}-A^{-1}uv^TA^{-1}/(1+v^TA^{-1}u)$，直接相乘验证；分母为零时 $A^{-1}u$ 给出非零核向量。

    (b) 令 $p=A^{-1}b$，$\bar A=A+(b-Ae_1)e_1^T$。可逆当且仅当 $p_1\ne0$，$\bar A^{-1}=A^{-1}-(p-e_1)e_1^TA^{-1}/p_1$。

### [第 2(1)–(3) 题](../assets/yau-papers/2013-final-individual.pdf)

三角网格 $M=(V,E,F)$，$\chi=|V|-|E|+|F|$。内点曲率为 $2\pi$ 减相邻角之和，边界点为 $\pi$ 减相邻角之和。证明 $\sum_vK(v)=2\pi\chi$：(1) 闭三角网格；(2) 一般平面多边形面；(3) 边界分量互不相交的三角网格。

??? proof "答案"

    (1) 总角为 $\pi|F|$，且 $3|F|=2|E|$，所以 $\sum K=2\pi|V|-\pi|F|=2\pi\chi$。

    (2) 每个多边形加对角线三角剖分，不增加顶点；每加一条内部对角线，边、面数各增 $1$，$\chi$ 和原顶点总角均保持不变，归结为 (1) 或 (3)。

    (3) 记内、边界点数为 $V_i,V_b$，内、边界边数为 $E_i,E_b$。边界为互不相交的闭折线，故 $E_b=V_b$，且 $3F=2E_i+E_b$。于是 $\sum K=2\pi V_i+\pi V_b-\pi F=2\pi(V_i+V_b-E_i-E_b+F)$。

## 2014 · 笔试·个人赛

### [第 1 题](../assets/yau-papers/2014-written-individual.pdf)

$c_n=\binom{2n}n/(n+1)$。证明半角展开 $\sin^2(\theta/2)=\sum_{n=1}^\infty c_{n-1}(\sin\theta/2)^{2n}$。

??? proof "答案"

    由 $\sqrt{1-4z}$ 的 Taylor 展开，$F(z)=\sum_{n\ge0}c_nz^n=(1-\sqrt{1-4z})/(2z)$，$|z|<1/4$，并可取端点连续极限。因此右侧为 $zF(z)=(1-|\cos\theta|)/2$，$z=\sin^2\theta/4$。它与左侧 $(1-\cos\theta)/2$ 相同的条件是 $\cos\theta\ge0$。原卷未写角度范围，任意角度版本为假，例如 $\theta=\pi$ 左侧 $1$、右侧 $0$。

### [第 2(i)、(ii) 题](../assets/yau-papers/2014-written-individual.pdf)

次数 $n$ 的多项式 $f$，指数 $N$ 很大。(i) 高效求 $\gcd(f,X^N-1)$；(ii) 推广到 $\gcd(f,\sum_{i=1}^mA_iX^{N_i}+A_{m+1})$。已知 $g\equiv h\pmod f$ 时 $\gcd(f,g)=\gcd(f,h)$。

??? proof "答案"

    (i) 用二进制快速幂计算 $r=X^N\bmod f$，每次乘法后立即取次数小于 $n$ 的余式，再计算 $\gcd(f,r-1)$。朴素多项式运算需 $O(n^2\log N)$，避免构造 $N$ 次多项式。

    (ii) 分别算 $r_i=X^{N_i}\bmod f$，组成 $r=\sum A_ir_i+A_{m+1}\bmod f$，然后求 $\gcd(f,r)$。可共享各次 $X^{2^j}\bmod f$，减少重复平方。正确性直接来自题中给定的同余恒等式。

### [第 3(i)、(ii) 题](../assets/yau-papers/2014-written-individual.pdf)

周期半离散格式为 $u_j'=-(f(u_j)-f(u_{j-1}))/h$，$f'\ge0$。(a) 证明 $E_1=h\sum_j|u_j|^2$ 不增；(b) 判断任意正整数 $p$ 的 $E_p=h\sum_j|u_j|^{2p}$ 是否不增，并证明。

??? proof "答案"

    两者都不增。令 $\Phi_p'(s)=s^{2p-1}f'(s)$。因 $s\mapsto s^{2p-1}$ 递增，任意 $a,b$ 满足

    $$
    a^{2p-1}(f(a)-f(b))\ge\Phi_p(a)-\Phi_p(b).
    $$

    周期求和后右边为零，因此 $E_p'=-2p\sum_j u_j^{2p-1}(f(u_j)-f(u_{j-1}))\le0$。$p=1$ 即第一问。

### [第 4(i)–(iii) 题](../assets/yau-papers/2014-written-individual.pdf)

**原卷：** [2014 应用与计算数学个人赛，第 2–3 页](../assets/yau-papers/2014-computational-applied.pdf#page=2)。**选取：** (i)–(iii)。**先修：** [线性迭代](03-linear-iterations-power.md)、[条件数](02-pseudoinverse-low-rank.md)。

设 $A$ 全部特征值为正实数，最小、最大者记为 $a,b$。对 $Ax=c$ 使用 $x^{(k+1)}=(I-\omega A)x^{(k)}+\omega c$。(i) 求对任意初值收敛的参数区间；(ii) 求使迭代矩阵谱半径最小的参数与分段表达；(iii) 对称正定时用 $\kappa_2(A)$ 表示最优收敛因子。

??? proof "答案"

    精确解 $x^*$ 存在，误差满足 $e_{k+1}=G_\omega e_k$，$G_\omega=I-\omega A$。特征值为 $1-\omega\lambda_i$，谱半径判据给出

    $$
    \rho(G_\omega)<1\iff |1-\omega\lambda_i|<1\ (\forall i)
    \iff 0<\omega<2/b.
    $$

    该判据无需 $A$ 可对角化。因为 $\lambda\mapsto|1-\omega\lambda|$ 凸且两端均为实际特征值，

    $$
    \rho(G_\omega)=\max\{|1-\omega a|,|1-\omega b|\}.
    $$

    令两端等模异号，得 $\omega_*=2/(a+b)$，最优值 $(b-a)/(b+a)$。进一步

    $$
    \rho(G_\omega)=\begin{cases}
    1-\omega a,&\omega\le\omega_*,\\
    \omega b-1,&\omega\ge\omega_*.
    \end{cases}
    $$

    左支随 $\omega$ 减小，右支随 $\omega$ 增大，所以交点确为全局最小点。若 $A$ 对称正定，$\kappa_2(A)=b/a$，故

    $$
    \rho(G_{\omega_*})=\frac{\kappa_2(A)-1}{\kappa_2(A)+1}.
    $$

### [第 5 题](../assets/yau-papers/2014-written-individual.pdf)

设 $\lambda=k/h^2>0$，$U_j^{n+1}-U_j^n=\lambda(U_{j-1}^{n+1}-2U_j^{n+1}+U_{j+1}^{n+1})$，$j=1,\ldots,N-1$，边界 $U_0=u_0,U_N=u_1$。证明

$$
\frac12\sum_{j=1}^{N-1}\big((U_j^{n+1})^2-(U_j^n)^2\big)
\le-\lambda\sum_{j=1}^{N-2}(U_{j+1}^{n+1}-U_j^{n+1})^2
-\frac\lambda2((U_1^{n+1})^2+(U_{N-1}^{n+1})^2)+\frac\lambda2(u_0^2+u_1^2).
$$

??? proof "答案"

    以 $U_j^{n+1}$ 乘更新式并求和。用 $a(a-b)\ge(a^2-b^2)/2$，右边离散分部求和为

    $$
    -\lambda\sum_{j=1}^{N-2}(U_{j+1}^{n+1}-U_j^{n+1})^2
    -\lambda((U_1^{n+1})^2+(U_{N-1}^{n+1})^2)
    +\lambda(u_0U_1^{n+1}+u_1U_{N-1}^{n+1}).
    $$

    最后对两个边界乘积使用 $ab\le(a^2+b^2)/2$。

## 2014 · 笔试·团体赛

### [第 1 题](../assets/yau-papers/2014-written-team.pdf)

正 Borel 测度 $\mu$ 定义在 $[0,1]$，$c_j=\int_0^1x^j\,d\mu(x)$，$Sc_j=c_{j+1}$。证明 $(I-S)^kc_j\ge0$（$j,k\ge0$）。

??? proof "答案"

    二项式展开与积分线性性给出 $(I-S)^kc_j=\int_0^1x^j(1-x)^k\,d\mu(x)\ge0$。

### [第 3 题](../assets/yau-papers/2014-written-team.pdf)

周期标量守恒律 $u_t+f(u)_x=0$、$f'\ge0$。分片多项式空间上的上风 DG 格式为 $\int_{I_j}(u_h)_tv-\int_{I_j}f(u_h)v_x+f(u_j^-)v_j^--f(u_{j-1}^-)v_{j-1}^+=0$。证明 $\frac d{dt}\int u_h^2dx\le0$。

??? proof "答案"

    取 $v=u_h$，令 $F'=f$，在每段用链式法则 $\int f(u_h)(u_h)_x=F(u_j^-)-F(u_{j-1}^+)$。求和后，每个界面左、右值 $a,b$ 的贡献为 $f(a)(a-b)-F(a)+F(b)=\int_a^b[f(s)-f(a)]ds\ge0$，最后不等式对 $b>a$ 与 $b<a$ 均由 $f$ 递增得到。因此 $\frac12\frac d{dt}\|u_h\|_2^2$ 为这些非负项和的相反数。

### [第 4(a)–(d) 题](../assets/yau-papers/2014-written-team.pdf)

$Ax=b$，GMRES 在 $K_m=\operatorname{span}\{r_0,Ar_0,\ldots,A^{m-1}r_0\}$ 中求修正，使残差与 $AK_m$ 正交。(i) 写最小二乘问题及三角化；(ii) 讨论原卷所写残差与 $v_1,\ldots,v_{k-1}$ 的正交性；(iii) 求残差范数；(iv) 写完整算法。原卷写 $v_0=r_0,v_1=Av_0/\|Av_0\|$ 并称所得系统正交。

??? proof "答案"

    (i) 以真正正交的 Arnoldi 基 $Q_m$ 写 $AQ_m=Q_{m+1}\bar H_m$、$r_0=\beta q_1$，最小化 $\|\beta e_1-\bar H_my\|_2$，$x_m=x_0+Q_my$。用 Givens 旋转对 $\bar H_m$ 做 QR，得到上三角系统 $R_my=c_{1:m}$。

    (ii) 精确的最优条件是 $r_m\perp AK_m$。若题中的 $v_j$ 属于 $\operatorname{span}\{Ar_0,\ldots,A^{k-1}r_0\}$，则要求的正交性成立。若把它们理解成对含 $r_0$ 的整个 Krylov 空间标准正交化所得后续基，结论一般为假：取 $A=\operatorname{tridiag}(1,2,1)$、$b=e_1,x_0=0,m=2$，则 $q_2=e_2$，残差为 $(1/14,-1/7,3/14)^T$，并不与 $q_2$ 正交。原卷的 $v_1=Av_0/\|Av_0\|$ 也不能保证与 $v_0$ 正交，需区分上述两种基。

    (iii) 若旋转后的右端为 $c$，最小残差范数为 $|c_{m+1}|$。

    (iv) 计算初始残差并归一化；逐次将 $Aq_j$ 对已有列做 Gram–Schmidt，得到 Hessenberg 列；用已有和新增 Givens 旋转更新三角矩阵及右端；由 $|c_{j+1}|$ 判断终止；回代并计算 $x=x_0+Q_jy$。残差空间逐次扩大，最小残差非增。正交化提前零余量时，检查相应最小二乘；$A$ 可逆时不变 Krylov 空间已含精确修正。

### [第 5(i)、(ii) 题](../assets/yau-papers/2014-written-team.pdf)

$x_0=0,x_k=2x_{k-1}+b_k$。(i) 写成 $Ax=b$，并对 $b_1=-1/3,b_k=(-1)^k$（$k\ge2$）验证 $x_k=(-1)^k/3$；(ii) 求 $A^{-1}$ 和 $1$-范数条件数。

??? proof "答案"

    $A$ 的主对角为 $1$，第一下对角为 $-2$，其余为 $0$。将 $x_k=(-1)^k/3$ 代回即满足递推。

    $$
    (A^{-1})_{ij}=\begin{cases}2^{i-j},&i\ge j,\\0,&i<j.\end{cases}
    $$

    当 $n\ge2$，$\|A\|_1=3$、$\|A^{-1}\|_1=2^n-1$，故 $\kappa_1(A)=3(2^n-1)$；$n=1$ 时条件数为 $1$。

## 2014 · 总决赛·个人及综合个人赛

### [三对角矩阵题](../assets/yau-papers/2014-final-individual.pdf)

$A$ 为 $N$ 阶三对角矩阵，下对角 $a$、对角 $b$、上对角 $c$，$ac>0$。求其特征值和特征向量。

??? proof "答案"

    取 $d=\sqrt{a/c}>0$，$D=\operatorname{diag}(1,d,\ldots,d^{N-1})$，$\tau=\operatorname{sgn}(a)\sqrt{ac}$。$D^{-1}AD$ 两侧非对角均为 $\tau$。令 $\theta_j=j\pi/(N+1)$，则 $\lambda_j=b+2\tau\cos\theta_j$，对应向量分量 $v_i=d^{i-1}\sin(i\theta_j)$。将正弦加法公式代回各行即可验证，$j=1,\ldots,N$ 给出全部特征对。

### [圆堆积题2、网格题3](../assets/yau-papers/2014-final-individual.pdf)

三角形顶点圆半径 $r_i,r_j,r_k>0$，相互外切，$l_i=r_j+r_k$，令 $u_i=\log r_i$，三角形内切圆半径为 $r$。题2：证明 $\partial_{u_j}\theta_i=\partial_{u_i}\theta_j=r/l_k$、对角项为另外两项的负和，并证明 $\sum u_i=0$ 到正角单纯形的映射是微分同胚。题3：对整个三角网格，证明 $u\mapsto K$ 在 $\sum u_i=0$ 上是微分同胚。

??? proof "答案"

    题2：链式法则及余弦定理给 $\partial_{u_j}\theta_i=r_jl_i(1-\cos\theta_j)/(2A)=r_ir_jr_k/(Al_k)$。Heron 公式 $A^2=sr_ir_jr_k$、$r=A/s$ 给该值为 $r/l_k$。共同缩放不改变角，故行和为零。

    全局逆映射可显式写出：给 $\theta_i,\theta_j,\theta_k>0$、和为 $\pi$，取 $r=[\prod\cot(\theta_i/2)]^{-1/3}$、$r_i=r\cot(\theta_i/2)$，各半径乘积为 $1$，对应 $\sum u_i=0$；三角形边长为切线长度之和，正反映射均光滑且互逆。

    题3：曲率 Jacobian 为加权图 Laplacian，相邻顶点权为其相邻三角形贡献的正数 $r/l$ 之和。其二次型为 $\sum_{ij}w_{ij}(v_i-v_j)^2$。对连通网格，在和为零的子空间严格正定；沿连接两个参数的线段积分该二次型，得到严格单调，从而映射单射。Jacobian 在该子空间可逆，局部逆可由压缩映射构造，故全局为到其像的微分同胚。原卷未给具体像，不能理解为满射到整个 $\mathbb R^n$；若网格不连通，还需对每个连通分量单独固定尺度。

### [均匀边染色题](../assets/yau-papers/2014-final-individual.pdf)

已给图的合法 $k$ 边染色，相邻边颜色不同。证明可改为均匀合法染色，即任意两种颜色的边数之差至多 $1$。

??? proof "答案"

    若颜色 $a,b$ 的边数相差至少 $2$，只看这两色的边，因合法性每顶点度至多 $2$，各连通分量为交替路径或偶圈。圈及偶长路径的两色数相等，奇长路径相差 $1$，因此必有一条以较多色开始和结束的路径。在该路径交换两色，合法性保持，总体两色差减少 $2$，各色边数平方和严格下降。该非负整数不能无限下降，终止时任意两色差至多 $1$。

### [导数余弦定理题1](../assets/yau-papers/2014-final-individual.pdf)

三角形对边 $l_i,l_j,l_k$、角 $\theta_i,\theta_j,\theta_k$、面积 $A$。证明 $\partial\theta_i/\partial l_i=l_i/(2A)$、$\partial\theta_i/\partial l_j=-l_i\cos\theta_k/(2A)$。

??? proof "答案"

    对 $\cos\theta_i=(l_j^2+l_k^2-l_i^2)/(2l_jl_k)$ 求偏导，以 $2A=l_jl_k\sin\theta_i$ 化简，分别得到两式。

### [能量稳定题](../assets/yau-papers/2014-final-individual.pdf)

$E(u)=\int_0^1[\varepsilon^2u_x^2/2+u^4/4-u^2/2]dx$，Neumann 边界。时间离散 $(u^{n+1}-u^n)/k=\varepsilon^2u_{xx}^{n+1}-(u^{n+1})^3+u^n$。证明 $E(u^{n+1})\le E(u^n)$。

??? proof "答案"

    令 $v=u^{n+1},w=u^n$。凸函数 $z^4/4$ 给 $v^4/4-w^4/4\le v^3(v-w)$；$-z^2/2$ 给 $-(v^2-w^2)/2\le-w(v-w)$。梯度项给 $\varepsilon^2(\|v_x\|^2-\|w_x\|^2)/2\le\varepsilon^2\langle v_x,(v-w)_x\rangle$。相加、分部积分并代入格式，得 $E(v)-E(w)\le-\|v-w\|_2^2/k\le0$。

## 2014 · 总决赛·团体赛

### [受迫热方程题](../assets/yau-papers/2014-final-team.pdf)

$u_t-u_{xx}=f$，零 Dirichlet 边界，$\|f(t)\|_2\le M$，已知 $\|w\|_2\le C_2\|w_x\|_2$。对时间后向 Euler 半离散解，证明 $\|u^n\|_2^2\le\|u^0\|_2^2+C_2^4M^2$。

??? proof "答案"

    将离散方程乘 $2ku^{n+1}$、分部积分，得 $\|u^{n+1}\|^2-\|u^n\|^2+\|u^{n+1}-u^n\|^2+2k\|u_x^{n+1}\|^2\le2kM\|u^{n+1}\|$。由已给 Poincaré 不等式及 Young 不等式，$(1+k/C_2^2)\|u^{n+1}\|^2\le\|u^n\|^2+kC_2^2M^2$。归纳得更强的 $\|u^n\|^2\le\max(\|u^0\|^2,C_2^4M^2)$。

### [无爪图题](../assets/yau-papers/2014-final-team.pdf)

图 $G$ 无爪（不存在一个顶点与三个两两不邻接的顶点组成的诱导子图），有 $n$ 个顶点、最小度 $\delta$。证明独立数 $\alpha(G)\le2n/(\delta+2)$。

??? proof "答案"

    取任意独立集 $I$。每个 $I$ 内顶点至少有 $\delta$ 条边连到外部，每个外部顶点至多邻接两个 $I$ 内顶点，否则形成爪。因此 $\delta|I|\le2(n-|I|)$，整理后取最大独立集即可。

## 2015 · 笔试·个人赛

### [第 1 题](../assets/yau-papers/2015-written-individual.pdf)

互素正整数 $r,s$。从 $(0,0)$ 到 $(r,s)$，只走 $(1,0),(0,1)$ 且不越过 $ry=sx$ 的格路径，证明其数量为 $\binom{r+s}s/(r+s)$。

??? proof "答案"

    所有词共有 $\binom{r+s}s$ 个。给水平步权 $-s$、竖直步权 $r$，总和为零。前 $r+s$ 个循环前缀和两两不同：相等会要求某个真子段的两类步数满足 $ra=sb$，互素性迫使其包含全部步数，矛盾。每个词在唯一最大前缀和后开始的循环移位，恰使全部前缀和非正，即所求路径。又词不可能有真周期，否则重复次数同时整除 $r,s$。所以每个循环轨道有 $r+s$ 个词、恰一条合格路径，得到公式。

### [第 2(a)、(b) 题](../assets/yau-papers/2015-written-individual.pdf)

**原卷：** [2015 应用与计算数学个人赛，第 1 页](../assets/yau-papers/2015-computational-applied.pdf#page=1)。**选取：** 仅 (a)。**先修：** [SVD](02-svd-least-squares.md)、[谱理论](01-matrix-norms-spectral.md)。

$A\in\mathbb R^{m\times n}$ 满列秩，$n\le m$，$\alpha\ge0$。求

$$
C(\alpha)=\begin{pmatrix}\alpha I_m&A\\A^T&0\end{pmatrix}
$$

的全部特征值，用 $A$ 的奇异值表示。



**(b)** 求增广矩阵的最优 $2$-范数条件数与对应 $\alpha$；原卷给出的结论为最优 $\alpha=\sigma_n/\sqrt2$、$\sqrt2\kappa_2(A)\le\min_\alpha\kappa_2(C(\alpha))\le2\kappa_2(A)$，并要求说明最大值可超过 $\kappa_2(A)^2$。

??? proof "答案"

    取完整 SVD $A=U\Sigma V^T$，以正交矩阵 $Q=\operatorname{diag}(U,V)$ 做相似变换，得到

    $$
    Q^TC(\alpha)Q=\begin{pmatrix}\alpha I_m&\Sigma\\\Sigma^T&0\end{pmatrix}.
    $$

    重新排列坐标后，此矩阵由 $n$ 个 $2\times2$ 块 $\begin{pmatrix}\alpha&\sigma_i\\\sigma_i&0\end{pmatrix}$ 和 $m-n$ 个标量块 $\alpha$ 组成。每个二维块的特征方程为 $\lambda^2-\alpha\lambda-\sigma_i^2=0$，所以

    $$
    \lambda_i^\pm=\frac\alpha2\pm\sqrt{\frac{\alpha^2}{4}+\sigma_i^2},
    \quad i=1,\ldots,n,
    $$

    另外 $\alpha$ 重复 $m-n$ 次，特征值总数为 $m+n$。当 $m>n$ 且 $\alpha=0$ 时，增广矩阵有零特征值；不能在该情形下直接使用可逆矩阵的条件数公式。

    **(b)** 令 $L_i=(\alpha+\sqrt{\alpha^2+4\sigma_i^2})/2$、$M_i=(\sqrt{\alpha^2+4\sigma_i^2}-\alpha)/2$。当 $m>n,\alpha>0$，

    $$
    \kappa_2(C)=\frac{L_1}{\min(\alpha,M_n)}.
    $$

    在 $\alpha<M_n$ 区间它随 $\alpha$ 减小，在 $\alpha>M_n$ 区间增大；两支相交于 $\alpha=\sigma_n/\sqrt2$。令 $\kappa=\sigma_1/\sigma_n$，最优值为 $(1+\sqrt{1+8\kappa^2})/2$，位于 $[\sqrt2\kappa,2\kappa]$。$\alpha\to\infty$ 时条件数趋于无穷，故可超过 $\kappa^2$。

    原卷允许 $m=n$，但此时没有额外的 $\alpha$ 特征值，条件数为 $L_1/M_n$，最小值在 $\alpha=0$ 达到且等于 $\kappa$。因此原卷所述最优参数和下界需要 $m>n$，不能用于方阵情况。

### [第 3(a)–(d) 题](../assets/yau-papers/2015-written-individual.pdf)

$u_t+au_x=0$，格式 $(v^{n+1}-v^n)/k+aD_0v^n=0$。(a) 固定 $k/h>0$ 时是否一致？(b) 是否稳定？(c) 缩小 $k/h$ 是否能稳定？(d) 是否值得采用，给出固定比例时稳定的修改。

??? proof "答案"

    (a) Taylor 截断误差 $O(k+h^2)$，一致。

    (b) 因子 $1-ia(k/h)\sin\theta$；$a\ne0$ 且比例固定时不稳定。

    (c) 需进一步控制 $k/h^2\le C$，而不只是 $k/h\to0$。累计因子至多 $\exp(a^2Tk/(2h^2))$，在此限制下稳定。

    (d) 时间步需降到 $O(h^2)$，效率较低。改为沿 $a$ 方向的上风差分，$|a|k/h\le1$ 下更新为两个值的凸组合，最大与 $2$ 范数均稳定。

### [第 4 题](../assets/yau-papers/2015-written-individual.pdf)

$A,H,Q\in\mathbb C^{n\times n}$，$Q$ 可逆，$H=Q^{-1}AQ$ 是每个次对角元均非零的上 Hessenberg 矩阵。记 $q_j$ 为 $Q$ 的第 $j$ 列。证明 $\operatorname{span}(q_1,\ldots,q_j)=\operatorname{span}(q_1,Aq_1,\ldots,A^{j-1}q_1)$。

??? proof "答案"

    $AQ=QH$ 给出 $Aq_j=\sum_{i\le j+1}h_{ij}q_i$，且 $h_{j+1,j}\ne0$。$j=1$ 显然。若前 $j$ 个空间相等，则 $Aq_j$ 属于第 $j+1$ 个 Krylov 空间；反解非零的 $h_{j+1,j}$ 得 $q_{j+1}$ 也属于其中。反向包含由 Hessenberg 的零元素结构直接推出，归纳完成。

## 2015 · 笔试·团体赛

### [第 5(a)–(c) 题](../assets/yau-papers/2015-written-team.pdf)

$A=U\Sigma V^T\in\mathbb R^{n\times m}$，秩 $r$。(a) $r<\min(m,n)$ 时，证明任意 $\epsilon>0$ 都有满秩 $A_\epsilon$ 且 $\|A-A_\epsilon\|_2=\epsilon$；(b) 证明截断 SVD $A_k$ 是最佳秩不超过 $k$ 的算子范数逼近；(c) $r=\min(m,n)$ 时，证明 $\|A-B\|_2<\sigma_r$ 推出 $B$ 满秩。

??? proof "答案"

    (a) 将 $\Sigma$ 原来为零的对角元全换成 $\epsilon$，非零元保持不变，所得矩阵满秩且差的算子范数恰为 $\epsilon$。

    (b) 截断误差为 $\sigma_{k+1}$。任意秩不超过 $k$ 的 $B$，在前 $k+1$ 个右奇异向量张成空间内有单位零向量 $z$，故 $\|A-B\|_2\ge\|Az\|_2\ge\sigma_{k+1}$。

    (c) 若 $A$ 满列秩而 $Bz=0$、$\|z\|=1$，则 $\|A-B\|_2\ge\|Az\|_2\ge\sigma_r$，矛盾。满行秩时对转置作同样论证。

## 2015 · 总决赛·个人赛

### [第 1 题](../assets/yau-papers/2015-final-individual.pdf)

$A=I+rS$，$S$ 为周期移位矩阵。证明 $Ax=b$ 的解满足 $\|x\|\le C\|b\|$，$C$ 与维数无关。

??? proof "答案"

    在 $2$ 或最大范数中 $\|Sx\|=\|x\|$，反三角不等式给 $\|(I+rS)x\|\ge|1-|r||\|x\|$。因此 $|r|\ne1$ 时可取 $C=1/|1-|r||$。原卷未限制 $r$，结论并非无条件成立：$r=-1$ 时常数向量在核中；$r=1$ 且维数为偶数时交替向量在核中。

### [第 3 题](../assets/yau-papers/2015-final-individual.pdf)

$C>0,k\ge2$，Newton 迭代 $x_{n+1}=x_n-(x_n^k-C)/(kx_n^{k-1})$。证明任意 $x_0>0$ 都收敛。

??? proof "答案"

    令 $r=C^{1/k}$。$f(x)=x^k-C$ 在正半轴严格递增、凸，其切线交点总在 $r$ 的右侧，所以 $x_1\ge r$。当 $x_n\ge r$，$r\le x_{n+1}\le x_n$。序列趋于 $L\ge r>0$，对迭代式取极限得 $L^k=C$，即 $L=r$。

## 2015 · 总决赛·综合个人赛

### [第 1 题](../assets/yau-papers/2015-final-overall.pdf)

$\varepsilon>0$ 很小，求 $\varepsilon x^3-x-2=0$ 的三个实根的渐近展开。

??? proof "答案"

    一个根为 $x_0=-2-8\varepsilon-96\varepsilon^2+O(\varepsilon^3)$；其余两个为 $x_\pm=\pm\varepsilon^{-1/2}+1\mp\tfrac32\sqrt\varepsilon+4\varepsilon+O(\varepsilon^{3/2})$。分别代入 $x=-2+a\varepsilon+b\varepsilon^2$ 及 $x=y/\sqrt\varepsilon$、$y=\pm1+c\sqrt\varepsilon+d\varepsilon+e\varepsilon^{3/2}$，逐次比较幂次即可。$0<\varepsilon<1/27$ 时局部极大、极小值异号，确有三个不同实根。

## 2015 · 总决赛·团体赛

### [第 1 题](../assets/yau-papers/2015-final-team.pdf)

$A=\operatorname{tridiag}(-1,2,-1)$，$B=\operatorname{tridiag}(1,4,1)$。求广义特征问题 $Av=\lambda Bv$ 的特征对。

??? proof "答案"

    $\theta_j=j\pi/(n+1)$，$v_i^{(j)}=\sin(i\theta_j)$，$\lambda_j=(2-2\cos\theta_j)/(4+2\cos\theta_j)$。正弦加法公式同时对角化 $A,B$，且 $4+2\cos\theta_j>0$。

### [第 2 题](../assets/yau-papers/2015-final-team.pdf)

$A$ 对称正定，最小化 $f(x)=x^TAx$。最速下降沿 $-\nabla f(x)$ 作精确线搜索。求步长并证明能量线性收敛界。

??? proof "答案"

    $\nabla f=2Ax$，最优 $\alpha=(x^TA^2x)/(2x^TA^3x)$。令 $a=\lambda_{\min},b=\lambda_{\max},\kappa=b/a$，则 $f(x_{k+1})\le[(\kappa-1)/(\kappa+1)]^2f(x_k)$。证明：在 $A^{1/2}x$ 的单位谱权重 $p_i$ 下，能量下降比例为 $(\sum p_i\lambda_i)^2/(\sum p_i\lambda_i^2)$；由 $\lambda_i^2\le(a+b)\lambda_i-ab$，该比例至少 $4ab/(a+b)^2$。

## 2016 · 笔试·个人赛

### [第 1(1)、(2) 题](../assets/yau-papers/2016-written-individual.pdf)

对周期平流方程 $u_t+a u_x=f$，令 $\delta_0u_j=(u_{j+1}-u_{j-1})/(2h)$、$\delta^2u_j=(u_{j+1}-2u_j+u_{j-1})/h^2$，使用

$$
\frac{u_j^{n+1}-u_j^{n-1}}{2k}+a(I+h^2\delta^2/6)^{-1}\delta_0u_j^n=f_j^n.
$$

(1) 证明时间二阶、空间四阶；(2) 求稳定条件。

??? proof "答案"

    令 $P=I+h^2\delta^2/6$。Taylor 展开得 $\delta_0u-Pu_x=-h^4u^{(5)}/180+O(h^6)$。周期网格上 $P$ 的特征值为 $(2+\cos\theta)/3\in[1/3,1]$，逆算子一致有界，因此空间误差 $O(h^4)$；中心时间差商误差 $O(k^2)$。

    空间算子的特征值为 $3i\sin\theta/[h(2+\cos\theta)]$，其绝对值最大为 $\sqrt3/h$。时间递推的特征多项式为 $r^2+2i\eta r-1$，$\eta=3ak\sin\theta/[h(2+\cos\theta)]$。两根模为 $1$ 且无重根的条件是 $|\eta|<1$；故统一稳定限制为 $|ak/h|<1/\sqrt3$。端点产生单位圆重根，不能对一般起始误差保证一致有界。

### [第 3 题](../assets/yau-papers/2016-written-individual.pdf)

正整数向量 $u=(u_1,\ldots,u_n)$ 满足 $\|u\|_\infty\le H$，且有非零整数 $k$ 使 $\prod_i u_i^{k_i}=1$。利用原卷给出的整数核向量界，证明可取 $\|k\|_\infty\le(2n\log H/\log2)^{n-1}$。

??? proof "答案"

    对所有出现的素数 $p$，写 $u_j=\prod_p p^{a_{pj}}$。乘法依赖等价于整数矩阵方程 $Ak=0$，而 $0\le a_{pj}\le\log H/\log2$。由已给的整数核向量界即得结论。若 $H=1$，所有 $u_i=1$，直接取单位向量；原卷右边在 $H=1,n>1$ 为零，需将该端点单独处理，或把右边改为 $\max\{1,(2n\log H/\log2)^{n-1}\}$。

### [第 4(1)–(3) 题](../assets/yau-papers/2016-written-individual.pdf)

$A$ 实对称，$\lambda_i$ 是单特征值，单位特征向量为 $q_i$。反幂迭代的计算向量满足 $(A-\mu I+\delta A)\tilde y=x_k$、$\|x_k\|_2=1$，令 $\tilde x=\tilde y/\|\tilde y\|_2$、$\alpha_i=q_i^Tx_k$。

(1) 证明 $\|(A-\lambda_iI)\tilde x\|_2\le|\mu-\lambda_i|+\|\delta A\|_2+1/\|\tilde y\|_2$；(2) 证明 $\|\tilde y\|_2\ge|\alpha_i|/(|\mu-\lambda_i|+\|\delta A\|_2)$；(3) 推出归一化特征向量的误差阶。

??? proof "答案"

    (1) 将方程改写为 $(A-\lambda_iI)\tilde y=x_k+(\mu-\lambda_i)\tilde y-\delta A\tilde y$，取范数并除以 $\|\tilde y\|$。

    (2) 左乘 $q_i^T$，得到 $\alpha_i=(\lambda_i-\mu)q_i^T\tilde y+q_i^T\delta A\tilde y$，再用 Cauchy–Schwarz。

    (3) 设 $\eta=|\mu-\lambda_i|+\|\delta A\|$、$g=\min_{j\ne i}|\lambda_j-\lambda_i|$。若 $|\alpha_i|\ge c>0$、$g\ge g_0>0$，则 (1)(2) 给出残差 $\le(1+1/c)\eta$。按正交特征向量展开，有 $\|(I-q_iq_i^T)\tilde x\|\le(1+1/c)\eta/g_0$，因而 $\min_\pm\|\tilde x\mp q_i\|=O(|\mu-\lambda_i|+\epsilon)$。原卷只写谱间距 $O(1)$，还需要不趋零的下界及非零主分量；$\alpha_i=0$ 时该结论不成立。

### [第 5(a)–(c) 题](../assets/yau-papers/2016-written-individual.pdf)

$f\in C^2(\mathbb R^n)$、$m>0$。证明下列等价：(a) $\nabla^2f(x)\succeq mI$；(b) $f(tx+(1-t)y)\le tf(x)+(1-t)f(y)-mt(1-t)\|x-y\|^2/2$；(c) $\langle\nabla f(x)-\nabla f(y),x-y\rangle\ge m\|x-y\|^2$。

??? proof "答案"

    令 $F(x)=f(x)-m\|x\|^2/2$。(a) 等价于 $\nabla^2F\succeq0$。沿任意直线限制为一元函数，其二阶导非负，故凸；展开 $F$ 的凸不等式即得 (b)。反过来，(b) 令两端点为 $x\pm hv$、$t=1/2$，除以 $h^2$ 并令 $h\to0$，得 $v^T\nabla^2f(x)v\ge m\|v\|^2$。

    (a) 沿 $y+s(x-y)$ 积分梯度差，得 (c)；反过来在 (c) 中取 $y=x+hv$，除以 $h^2$ 并趋零，恢复 (a)。

## 2016 · 笔试·团体赛

### [第 1(1)、(2) 题](../assets/yau-papers/2016-written-team.pdf)

对 $u_t+u_x=0$，用 $u_j^{n+1}=a u_j^n+b u_{j-1}^n+c u_{j-2}^n$，$\lambda=\Delta t/\Delta x$。(1) 求二阶系数；(2) 求 $\ell^2$ 稳定的网格比例范围。

??? proof "答案"

    $a=(\lambda-1)(\lambda-2)/2$、$b=\lambda(2-\lambda)$、$c=\lambda(\lambda-1)/2$。由 Taylor 矩条件 $a+b+c=1,b+2c=\lambda,b+4c=\lambda^2$ 得到。

    周期模式的放大因子满足 $|g|^2=1+\lambda(\lambda-2)(\lambda-1)^2(1-\cos\theta)^2$，故 $0\le\lambda\le2$。对无限网格也可直接展开平方和得到同一范数界。

### [第 2(a) 题](../assets/yau-papers/2016-written-team.pdf)

一维振子满足 $x''=-u'(x)$。证明 $\frac12(x')^2+u(x)$ 为常数。

??? proof "答案"

    直接求导：$\frac d{dt}(\frac12(x')^2+u(x))=x'(x''+u'(x))=0$。

### [第 3 题](../assets/yau-papers/2016-written-team.pdf)

整数矩阵 $A\in\mathbb Z^{m\times n}$ 满足 $\operatorname{rank}(A)=r<n$、$|a_{ij}|\le H$。证明存在非零整数向量 $x\in\ker A$ 且 $\|x\|_\infty\le(2nH)^{n-1}$。

??? proof "答案"

    若 $r=0$，取一个标准基向量。否则选 $r$ 个独立行和 $r+1$ 列，其中前 $r$ 列的 $r$ 阶子式非零。以该 $r\times(r+1)$ 矩阵删去各列后的带符号子式作为 $x$ 的相应分量，其余分量取零。Laplace 展开给出 $Ax=0$，其中至少一个分量非零。每个子式绝对值至多 $r!H^r\le(2nH)^{n-1}$。独立行张成全部行空间，故全部方程都满足。

### [第 4(1)–(5) 题](../assets/yau-papers/2016-written-team.pdf)

对可逆 $A$，取 $x_{k+1}=x_k+\beta_kp_k$，使残差 $r_{k+1}=b-Ax_{k+1}$ 的 $2$-范数最小。(1) 求 $\beta_k$；(2) 证明 $r_{k+1}\perp Ap_k$；(3) 以 $r_k,Ap_k$ 的夹角 $\theta_k$ 表示误差因子；(4) 若每步内积非零，是否必然收敛？(5) 若 $A$ 正定且 $p_k=r_k$，证明任意初值收敛。

??? proof "答案"

    (1)(2)(3) 当 $p_k\ne0$，

    $$
    \beta_k=\frac{(Ap_k)^Tr_k}{\|Ap_k\|^2},\qquad r_{k+1}^TAp_k=0,
    \qquad\|r_{k+1}\|=\|r_k\|\,|\sin\theta_k|.
    $$

    (4) 不一定。取 $A=I$，每步选择与当前残差夹角的余弦为 $2^{-k-2}$ 的方向。内积始终非零，但残差范数乘积 $\prod_k\sqrt{1-2^{-2k-4}}>0$，不会趋零。

    (5) 设 $r^TAr\ge m\|r\|^2$，$\|A\|=M$。则 $|\cos\theta_k|\ge m/M$，故 $\|r_{k+1}\|\le\sqrt{1-m^2/M^2}\|r_k\|$。几何收敛，$x_k\to A^{-1}b$。残差为零时停止。

### [第 5(1)–(3) 题](../assets/yau-papers/2016-written-team.pdf)

$f\in C^1(\mathbb R^n)$ 凸且有局部极小点 $x^*$。(1) 它是否全局极小？(2) 对任意 $t>0$ 的隐式更新 $x_k=x_{k-1}-t\nabla f(x_k)$，证明 $f(x_k)$ 收敛；(3) 若 $\langle\nabla f(x)-\nabla f(y),x-y\rangle\ge m\|x-y\|^2$，证明 $x_k$ 收敛。

??? proof "答案"

    (1) 是。若有更小的 $f(y)$，凸组合 $(1-s)x^*+sy$ 对任意小的 $s>0$ 都有更小函数值，矛盾。

    (2) 更新解是 $f(x)+\|x-x_{k-1}\|^2/(2t)$ 的唯一极小点；该目标强制增长且严格凸，所以解存在唯一。凸函数支持不等式给出 $f(x_{k-1})\ge f(x_k)+t\|\nabla f(x_k)\|^2$，故函数值单调并有下界 $f(x^*)$，任意 $t>0$ 都可。

    (3) 记 $e_k=x_k-x^*$。由于 $\nabla f(x^*)=0$，有 $e_{k-1}^Te_k\ge(1+tm)\|e_k\|^2$，于是 $\|e_k\|\le(1+tm)^{-1}\|e_{k-1}\|$，收敛到唯一的 $x^*$。

## 2016 · 总决赛·个人赛

### [第 1(a)–(c) 题](../assets/yau-papers/2016-final-individual.pdf)

Arnoldi 产生正交基 $Q_n$ 和 $AQ_n=Q_{n+1}\bar H_n$，$H_n$ 为删去最后一行的矩阵。(a) 写算法；(b) 若 $h_{n+1,n}=0$，证明 Krylov 空间不变及 $H_n$ 特征值属于 $A$；(c) 证明 $\min_{p\text{首一},\deg p=n}\|p(A)b\|_2$ 的一个极小者为 $H_n$ 的特征多项式。

??? proof "答案"

    (a) $q_1=b/\|b\|$，逐次对 $Aq_j$ 作 Gram–Schmidt：$h_{ij}=q_i^TAq_j$，减去各投影，将余向量归一化。

    (b) 余量为零给 $AQ_n=Q_nH_n$，空间对 $A$ 不变，后续 Krylov 空间不再增长。$H_nz=\lambda z$ 则 $A(Q_nz)=\lambda Q_nz$，$Q_nz\ne0$。

    (c) 设 $\chi_n=\det(tI-H_n)$。上 Hessenberg 关系与 Cayley–Hamilton 恒等式给 $\chi_n(A)b=\|b\|\prod_{j=1}^nh_{j+1,j}\,q_{n+1}$，与 $K_n$ 正交；任意另一个首一 $p$ 有 $(p-\chi_n)(A)b\in K_n$。Pythagoras 证明其范数不小于 $\|\chi_n(A)b\|$。提前终止时余量为零，最小值已为零；未终止时低阶 Krylov 向量独立，极小多项式唯一。

### [第 2(b) 题](../assets/yau-papers/2016-final-individual.pdf)

FitzHugh–Nagumo 模型 $\varepsilon\dot v=v-v^3/3-w+I_{\rm ext}$、$\dot w=v+a-bw$。以 $T=t/\varepsilon$、$v=V_0(T)+\varepsilon V_1(T)+\cdots$、$w=W_0(T)+\varepsilon W_1(T)+\cdots$ 求主阶快速方程。

??? proof "答案"

    链式法则给 $V_0'=V_0-V_0^3/3-W_0+I_{\rm ext}$、$W_0'=0$，导数均相对于 $T$。所以快速阶段 $W_0$ 为常数，$V_0$ 解这一维自治方程。

## 2016 · 总决赛·综合个人赛

### [第 1 题](../assets/yau-papers/2016-final-overall.pdf)

给定实数 $a_1,\ldots,a_n$，用线性时间求连续子段和的最大值。

??? proof "答案"

    令 $s_1=a_1,m_1=a_1$，迭代 $s_i=\max(a_i,s_{i-1}+a_i)$、$m_i=\max(m_{i-1},s_i)$，输出 $m_n$。$s_i$ 是以 $i$ 结尾的最佳非空子段，归纳证明这两个更新式；每项常数次运算，总 $O(n)$、额外空间 $O(1)$。若允许空子段，最终再与 $0$ 取最大。

## 2017 · 笔试·个人赛

### [第 1 题](../assets/yau-papers/2017-written-individual.pdf)

$T_n(x)=\cos(n\arccos x)$。证明 $T_{n+1}(x)-T_{n-1}(x)$ 的极值包络形成椭圆。

??? proof "答案"

    令 $x=\cos\theta$，有 $T_{n+1}-T_{n-1}=-2\sin(n\theta)\sin\theta$，所以 $y^2\le4(1-x^2)$。两条包络曲线为 $y=\pm2\sqrt{1-x^2}$，即 $x^2+y^2/4=1$。当 $n$ 增大，内部极值点满足 $n\cos(n\theta)\sin\theta+\sin(n\theta)\cos\theta=0$，可在任意内部角附近选极值点，使 $|\sin(n\theta)|\to1$，故极值的极限包络确为该椭圆。单个有限 $n$ 的全部极值点并不都严格位于椭圆上。

### [第 2(a)、(b) 题](../assets/yau-papers/2017-written-individual.pdf)

**原卷：** [2017 应用与计算数学个人赛，第 1 页](../assets/yau-papers/2017-computational-applied.pdf#page=1)。**选取：** (a) 的重启迭代形式。**先修：** [Steffensen 加速](05-newton-convergence.md)。

对光滑不动点映射 $g$，$g(\alpha)=\alpha$，定义

$$
G(x)=x-\frac{(g(x)-x)^2}{g(g(x))-2g(x)+x}.
$$

分析 $x_{r+1}=G(x_r)$ 的局部收敛阶。

(a) 分析加速迭代的二次收敛性；(b) 给出二维推广。

??? proof "答案"

    设 $g$ 在根附近 $C^3$，记 $e=x-\alpha$、$a=g'(\alpha)$、$b=g''(\alpha)/2$。当 $a\ne1$，

    $$
    g(x)-\alpha=ae+be^2+O(e^3),
    \quad g(g(x))-\alpha=a^2e+ab(1+a)e^2+O(e^3).
    $$

    所以分子与分母分别为

    $$
    (g(x)-x)^2=(a-1)^2e^2+2(a-1)be^3+O(e^4),
    $$

    $$
    g(g(x))-2g(x)+x=(a-1)^2e+b(a-1)(a+2)e^2+O(e^3).
    $$

    对充分小的非零 $e$ 分母非零，相除并代回得

    $$
    G(x)-\alpha=\frac{ab}{a-1}e^2+O(e^3).
    $$

    故存在邻域和常数 $C$ 使 $|e_{r+1}|\le C|e_r|^2$。缩小邻域到 $C|e_0|<1$ 即保证迭代留在邻域并趋零。若 $ab\ne0$，阶数恰为 $2$；若 $ab=0$，只能说至少二阶，可能更高阶或有限终止。根处的 $0/0$ 应通过停止迭代处理，或连续定义 $G(\alpha)=\alpha$。

    缺少 $a\ne1$ 会怎样：取 $g(x)=x-x^3$、$\alpha=0$。对小的非零初值，原迭代确实收敛，但

    $$
    g(g(x))-2g(x)+x=3x^5-3x^7+x^9,
    \quad G(x)=\frac23x+O(x^3),
    $$

    加速迭代仍只有线性阶。原序列的 Aitken 后处理与反复重启 $G$ 也不能在没有额外论证时混为同一条迭代轨道。

    **(b)** 对二维映射，令 $H(x)=g(x)-x$，$h=\|H(x)\|_2$，以差商矩阵

    $$
    D(x)_{ij}=\frac{H_i(x+h e_j)-H_i(x)}h,\qquad x_+=x-D(x)^{-1}H(x)
    $$

    推广。若 $H\in C^2$ 且 $J_H(\alpha)$ 可逆，$D(x)=J_H(x)+O(\|x-\alpha\|)$，Newton 误差分解给出 $\|x_+-\alpha\|=O(\|x-\alpha\|^2)$。$H(x)=0$ 时停止。二维中不能直接把同一个标量 Aitken 分母应用到耦合的两个分量。

### [第 3 题](../assets/yau-papers/2017-written-individual.pdf)

$f(x)=f_1(x)$（$x\le0$）、$f_2(x)$（$x>0$），两侧光滑且 $f_1(0)\ne f_2(0)$。$p$ 在 $k+1$ 个等距点 $x_j$ 插值 $f$，其中 $x_i<0<x_{i+1}$。证明网格步长足够小时，$p'$ 在 $[x_i,x_{i+1}]$ 不为零。

??? proof "答案"

    先把自变量缩放到节点 $0,1,\ldots,k$，考虑左边数据全为 $0$、右边全为 $1$ 的插值多项式 $P$。Rolle 定理在左侧节点间给出 $i$ 个导数零点，右侧给出 $k-i-1$ 个，共 $k-1$ 个，已经占满 $P'$ 的次数。因此中央区间 $[i,i+1]$ 没有导数零点；由 $P(i+1)-P(i)=1$，该区间 $P'>0$ 且有正下界。

    原数据为两侧常数值加 $O(h)$，固定节点插值线性算子使缩放后的导数扰动为 $O(h)$。故 $h p'(x)=(f_2(0)-f_1(0))P'(t)+O(h)$，足够小 $h$ 时不会为零。

### [第 4(a)–(d) 题](../assets/yau-papers/2017-written-individual.pdf)

**原卷：** [2017 应用与计算数学个人赛，第 2 页](../assets/yau-papers/2017-computational-applied.pdf#page=2)。**选取：** (a)–(d)。**先修：** [定常迭代与幂零](03-linear-iterations-power.md)。

设 $A$ 可逆。(a) 给出 $Ax_{k+1}=b-Bx_k$ 对任意初值收敛到唯一解的充要条件；(b) 若 $\rho(A^{-1}B)=0$，证明至多 $n$ 步到达解；(c) 对称正定 $M$、$\omega_1>1$、$\omega_i>0$，分析 $x^{(r+1)}=\omega_1x^{(r)}+\sum_{i=2}^s\omega_i(c_{i-1}-Mx^{(r)})$；(d) 比较同时更新和先后更新的两块迭代：

$$
\begin{aligned}
(*)&\quad Ax_1^{(r+1)}=b_1-Bx_2^{(r)},\quad Ax_2^{(r+1)}=b_2-Bx_1^{(r)},\\
(**)&\quad Ax_1^{(r+1)}=b_1-Bx_2^{(r)},\quad Ax_2^{(r+1)}=b_2-Bx_1^{(r+1)}.
\end{aligned}
$$

用 $s$ 表示 (c) 中权重个数、$r$ 表示迭代次数，以区分原卷复用的指标。

??? proof "答案"

    **(a)** 令 $C=A^{-1}B$、$d=A^{-1}b$，则迭代矩阵为 $-C$。结论是 $\rho(C)<1$。充分性：$I+C$ 可逆，固定点 $x^*=(I+C)^{-1}d$ 唯一，$e_k=(-C)^ke_0\to0$。必要性：若任意初值均收敛到同一解，任意两条轨道的差 $(-C)^k(x_0-y_0)$ 必须趋零；对基向量逐一取差得 $(-C)^k\to0$，因此 $\rho(C)<1$。

    若“收敛”仅指每条轨道各自存在某个极限，不要求共同解，上述必要性并不成立。例如 $B=-A,b=0$ 时每条轨道恒定。这里采用数值求解中的标准含义。

    **(b)** $\rho(C)=0$ 意味着特征多项式为 $t^n$。Cayley–Hamilton 给出 $C^n=0$，故 $e_n=(-C)^ne_0=0$。

    **(c)** 令 $S=\sum_{i=2}^s\omega_i>0$。误差矩阵 $G=\omega_1I-SM$ 的特征值为 $\omega_1-S\lambda_j(M)$。所以

    $$
    \rho(G)<1\iff\frac{\omega_1-1}{S}<\lambda_j(M)<\frac{\omega_1+1}{S}\quad(\forall j).
    $$

    **(d)** 两种方法的固定方程相同。其分块误差矩阵分别为

    $$
    T_* =\begin{pmatrix}0&-C\\-C&0\end{pmatrix},
    \qquad T_{**}=\begin{pmatrix}0&-C\\0&C^2\end{pmatrix}.
    $$

    对第一矩阵，以 $(v,v)$、$(v,-v)$ 的坐标分解，得到与 $\operatorname{diag}(-C,C)$ 相似；第二矩阵为块上三角。因此

    $$
    \rho(T_*)=\rho(C),\qquad \rho(T_{**})=\rho(C)^2.
    $$

    二者对任意初值收敛到共同固定点的条件都是 $\rho(C)<1$。若 $0<\rho(C)<1$，先后更新的每轮渐近谱因子更小；这是每完整轮的比较，并非声称每一步误差范数必然减小。当 $\rho(C)=0$ 时，两种方法均有限步终止。

### [第 5(a)、(b) 题](../assets/yau-papers/2017-written-individual.pdf)

周期半离散格式为 $u_j'=-(f(u_j)-f(u_{j-1}))/h$，$f'\ge0$。(a) 证明 $E_1=h\sum_j|u_j|^2$ 不增；(b) 判断任意正整数 $p$ 的 $E_p=h\sum_j|u_j|^{2p}$ 是否不增，并证明。

??? proof "答案"

    两者都不增。令 $\Phi_p'(s)=s^{2p-1}f'(s)$。因 $s\mapsto s^{2p-1}$ 递增，任意 $a,b$ 满足

    $$
    a^{2p-1}(f(a)-f(b))\ge\Phi_p(a)-\Phi_p(b).
    $$

    周期求和后右边为零，因此 $E_p'=-2p\sum_j u_j^{2p-1}(f(u_j)-f(u_{j-1}))\le0$。$p=1$ 即第一问。

## 2017 · 笔试·团体赛

### [第 1 题](../assets/yau-papers/2017-written-team.pdf)

正整数向量 $u\in\mathbb N^n$，寻找非零整数 $k$，$\|k\|_\infty\le K$、$\prod_iu_i^{k_i}=1$。给出约 $O((2K+1)^{n/2})$ 的算法，可用无限内存及排序、二分查找。

??? proof "答案"

    将坐标分为两半。枚举第一半的所有指数，存有理数积及指数向量并排序；枚举第二半，计算其积的倒数，在第一表二分查找。若找到且总指数非零，即输出；有重复积时须保留足以排除全零解的指数记录。列表长度为 $(2K+1)^{\lceil n/2\rceil}$ 和 $(2K+1)^{\lfloor n/2\rfloor}$，复杂度含排序的对数因子，为 $\widetilde O((2K+1)^{\lceil n/2\rceil})$，比全枚举指数减半。比较有理数用交叉相乘，整数位数仍为 $O(nK\log(\|u\|_\infty+1))$；默认所有 $u_i>0$。

### [第 2(1)、(2) 题](../assets/yau-papers/2017-written-team.pdf)

$u_t=H(u)_{xx}$，周期边界，$0\le H'(u)\le d$。用 $u_j^{n+1}=u_j^n+aH(u_{j-1}^n)+bH(u_j^n)+cH(u_{j+1}^n)$，$\mu=\Delta t/\Delta x^2$。(1) 求空间二阶系数；(2) 找一个保证稳定的步长条件并证明。

??? proof "答案"

    $a=c=\mu,b=-2\mu$，截断误差为 $O(\Delta t+\Delta x^2)$；$\mu$ 固定时整体为 $O(\Delta x^2)$，时间本身仅一阶。

    取 $0\le\mu\le1/(2d)$（$d=0$ 时无限制）。更新映射对全部输入分量单调，因为偏导为 $\mu H'$ 或 $1-2\mu H'$，均非负；它保持每个常数向量。将输入夹在常数 $\pm\|u^n\|_\infty$ 之间，得 $\|u^{n+1}\|_\infty\le\|u^n\|_\infty$。

### [第 3(a)–(c) 题](../assets/yau-papers/2017-written-team.pdf)

$y''=-GM/(R+y)^2$、$y(0)=3,y'(0)=-V$。令 $y=LY,t=T\tau$，选择撞地时间为 $O(1)$ 的尺度，写主阶方程：(a) $R,M=O(1),V\to\infty$；(b) $R,V=O(1),M\to\infty$；(c) $R,V=O(1),M\to0$。

??? proof "答案"

    统一取 $L=3$，$\rho=R/3$，方程为 $Y''=-[GMT^2/27]/(\rho+Y)^2$，$Y(0)=1,Y'(0)=-VT/3$。

    (a) $T=3/V$，小参数 $\eta=GM/(3V^2)\to0$，主阶 $Y''=0,Y(0)=1,Y'(0)=-1$。

    (b) $T=\sqrt{27/(GM)}$，小参数 $\eta=V\sqrt{3/(GM)}\to0$，主阶 $Y''=-(\rho+Y)^{-2},Y(0)=1,Y'(0)=0$。

    (c) $T=3/V$，$\eta=GM/(3V^2)\to0$，主阶同 (a)。这些尺度下初始高度、主导运动及撞地时间均为常数量级。

### [第 4(a)–(c) 题](../assets/yau-papers/2017-written-team.pdf)

互异点 $x_1,\ldots,x_n$ 用于近似 $f'(x_0)\approx\sum_i c_if(x_i)$。(a) 解释矩方程 $\sum_i c_i(x_i-x_0)^j/j!=\delta_{j1}$（$j=0,\ldots,n-1$）为何唯一可解，并求三点 $x_0,x_0+h,x_0+2h$ 的系数；(b) 对 Lagrange 插值多项式 $p$，证明 $p'(x_0)$ 对次数至多 $n-1$ 的多项式精确；(c) 证明两种方法的系数一致。

??? proof "答案"

    (a) 系数矩阵是经过非零行缩放的 Vandermonde 矩阵。互异节点使其可逆。三点系数为 $(-3,4,-1)/(2h)$，故导数近似为 $[-3f(x_0)+4f(x_0+h)-f(x_0+2h)]/(2h)$。

    (b) 对次数至多 $n-1$ 的 $f$，插值唯一性给出 $p=f$，导数自然精确。

    (c) 令 $c_i=\ell_i'(x_0)$，其中 $\ell_i$ 是 Lagrange 基。对每个 $(x-x_0)^j$ 应用 (b)，得到完全相同的矩方程；由唯一性，两组系数一致。

### [第 5 题](../assets/yau-papers/2017-written-team.pdf)

$A$ 为 $n\times n$ 三对角矩阵，前 $n-1$ 个对角元为 $2$，最后为 $\gamma$，上、下副对角元均为 $-1$。求 $A^{-1}$，并判断所有元素非负的参数条件。原卷声称该条件为 $\gamma\ge1$。

??? proof "答案"

    令 $d=n\gamma-(n-1)$。$d\ne0$ 时

    $$
    (A^{-1})_{ij}=\frac{\min(i,j)\,[1+(n-\max(i,j))(\gamma-1)]}{d}.
    $$

    逐行代入 $AA^{-1}=I$ 可核对。由于 $(A^{-1})_{nn}=n/d$，非负性必需 $d>0$；此时全部分子为正，因为 $\gamma>1-1/n$。因此正确条件是 $\gamma>(n-1)/n$，$d=0$ 时不可逆。原卷的“当且仅当 $\gamma\ge1$”过强，例如 $n=2,\gamma=3/4$ 的逆矩阵全部为正。

## 2017 · 总决赛·个人赛

### [第 1(a) 题](../assets/yau-papers/2017-final-individual.pdf)

对 Burgers 方程 $u_t+uu_x=\nu u_{xx}$，$\nu>0$，$u=U_x$。令 $\phi=e^{-U/(2\nu)}$，证明 Hopf–Cole 变换将方程化为热方程。

??? proof "答案"

    对原方程关于 $x$ 积分，并利用 $U$ 可加任意时间函数的自由度，可选择 $U_t+U_x^2/2=\nu U_{xx}$。链式法则给 $\phi_t=-U_t\phi/(2\nu)$、$\phi_{xx}=[U_x^2/(4\nu^2)-U_{xx}/(2\nu)]\phi$，因此 $\phi_t=\nu\phi_{xx}$。不固定该时间规范时，右侧还可出现仅依赖时间的倍乘项。

## 2017 · 总决赛·综合个人赛

### [第 1(a)、(b) 题](../assets/yau-papers/2017-final-overall.pdf)

$x'=x\times a$，$a\in\mathbb R^3$ 为常向量。(1) 证明显式 Euler 不稳定；(2) 给出保持 $\|x\|_2$ 的改进格式并证明。

??? proof "答案"

    (1) $x^{n+1}=x^n+h(x^n\times a)$，垂直性给 $\|x^{n+1}\|^2=\|x^n\|^2+h^2\|x^n\times a\|^2$。$a\ne0$ 时垂直于 $a$ 的非零分量每步增长因子 $\sqrt{1+h^2\|a\|^2}>1$；$a=0$ 为平凡例外。

    (2) 用 $[x^{n+1}-x^n]/h=((x^{n+1}+x^n)/2)\times a$。与 $x^{n+1}+x^n$ 作内积，得平方范数差为零。等价于斜对称叉乘矩阵的 Cayley 变换，隐式矩阵可逆，故可直接求解。

## 2017 · 总决赛·团体赛

### [第 1(a)、(b) 题](../assets/yau-papers/2017-final-team.pdf)

三角形对边为 $l_i,l_j,l_k$、角为 $\theta_i,\theta_j,\theta_k$、面积 $A$。(a) 证明 $\partial_{l_i}\theta_i=l_i/(2A)$、$\partial_{l_j}\theta_i=-l_i\cos\theta_k/(2A)$；(b) 边长作 $l_i=e^{u_j+u_k}l_i^0$ 等变换，证明 $\partial_{u_j}\theta_i=\partial_{u_i}\theta_j=\cot\theta_k$、$\partial_{u_i}\theta_i=-\cot\theta_j-\cot\theta_k$。

??? proof "答案"

    (a) 对余弦定理 $\cos\theta_i=(l_j^2+l_k^2-l_i^2)/(2l_jl_k)$ 求偏导，并用 $2A=l_jl_k\sin\theta_i$ 即得。

    (b) 链式法则给 $\partial_{u_j}\theta_i=l_i\partial_{l_i}\theta_i+l_k\partial_{l_k}\theta_i=(l_i^2-l_il_k\cos\theta_j)/(2A)=\cot\theta_k$，最后一步用余弦定理。三个 $u$ 同增时只等比例缩放，角不变，故同一行偏导和为零，给出对角项。

### [第 1(c) 题](../assets/yau-papers/2017-final-team.pdf)

初始三角形为锐角，边长 $l_i=e^{u_j+u_k}l_i^0$。证明在 $u=0$ 附近，$\sum u_i=0$ 到 $\sum\theta_i=\pi$ 的角映射为微分同胚。

??? proof "答案"

    其 Jacobian 的非对角为 $\cot\theta_k$、对角为另外两项的负和。在锐角附近这些权正，二次型为 $-\sum_{ij}\cot\theta_k(v_i-v_j)^2$，在 $\sum v_i=0$ 上严格负，故限制后的 Jacobian 可逆。

    不需将逆函数定理作为额外黑箱：记该限制矩阵为 $J_0$，对目标角 $\eta$ 迭代 $u\mapsto u-J_0^{-1}(\theta(u)-\eta)$。由 Jacobian 连续性，在足够小球内导数范数小于 $1$，且对足够接近原角的 $\eta$ 保持该球，Banach 定理给唯一局部逆；差分商及链式法则给逆的导数 $J(u)^{-1}$，所以为局部微分同胚。

### [第 2(a)–(d) 题](../assets/yau-papers/2017-final-team.pdf)

对称 $A$，$\|q_1\|=1$，$q_0=0,\beta_0=0$。Lanczos 递推 $\alpha_j=q_j^TAq_j$、$r_j=Aq_j-\alpha_jq_j-\beta_{j-1}q_{j-1}$、$\beta_j=\|r_j\|$、$q_{j+1}=r_j/\beta_j$。(a) 写矩阵关系；(b) 证明列正交且张成 Krylov 空间；(c) 证明在 Krylov 维数处终止；(d) 说明用途。

??? proof "答案"

    (a) $AQ_k=Q_kT_k+\beta_kq_{k+1}e_k^T$，$T_k$ 的对角为 $\alpha_j$，相邻两侧为 $\beta_j$。

    (b) 归纳并利用 $A=A^T$：$q_i^TAq_j=(Aq_i)^Tq_j=0$ 对 $i\le j-2$；减去当前与前一方向后，余量与全部已有向量正交。非零余量归一化得到下一正交向量，递推也给出与 $\{q_1,Aq_1,\ldots,A^{k-1}q_1\}$ 相同的张成空间。

    (c) 终止等价于空间对 $A$ 不变，因此恰在其最终维数 $m$ 处出现零余量。

    (d) 将大对称矩阵投影为小对称三对角矩阵 $T_k=Q_k^TAQ_k$，用于特征值与线性系统近似。若 $T_kz=\lambda z$，其提升向量的残差为 $\beta_kq_{k+1}e_k^Tz$，范数 $|\beta_ke_k^Tz|$ 可直接计算。以上为精确算术结论。

### [最优运输题(1)、(2)](../assets/yau-papers/2017-final-team-transport.pdf)

$D$ 为单位圆盘，给定 $p_i,r_i$，幂距离 $|p-p_i|^2+r_i$ 的最小值区组成 $W_i$，面积为 $A_i$，将 $W_i\cap D$ 映到 $p_i$。(1) 证明在相同各目标面积的映射中此映射的平方距离运输成本最小；(2) 用仿射函数的上包络表示这些区域。

??? proof "答案"

    (1) 逐点最小性给 $|p-\phi(p)|^2+r_{\phi(p)}\le|p-\widetilde\phi(p)|^2+r_{\widetilde\phi(p)}$。积分后两边的权项均为 $\sum_ir_iA_i$，约去即得成本不等式。

    (2) 取 $h_i=-(|p_i|^2+r_i)/2$，$\pi_i(p)=p\cdot p_i+h_i$。幂距离为 $|p|^2-2\pi_i(p)$，所以取最小幂距离等价于取最大仿射值。$\max_i\pi_i$ 为凸分片线性函数，其上包络的投影恰给出该分区。

## 2018 · 笔试·个人赛

### [第 1 题](../assets/yau-papers/2018-written-individual.pdf)

周期对流扩散方程 $u_t+a u_x=b u_{xx}$，$b>0$，离散为

$$
\frac{u_j^{n+1}-u_j^n}{\Delta t}+a\frac{u_{j+1}^n-u_{j-1}^n}{2h}
=b\frac{u_{j+1}^{n+1}-2u_j^{n+1}+u_{j-1}^{n+1}}{h^2}.
$$

证明存在与 $h$ 无关的 $\Delta t\le c$ 保证 $\ell^2$ 稳定，并确定 $c$ 对 $a,b$ 的依赖。

??? proof "答案"

    周期移位的正交特征基中，$g(\theta)=[1-ia\Delta t\sin\theta/h]/[1+4b\Delta t\sin^2(\theta/2)/h^2]$。令 $s=\sin^2(\theta/2)$，$|g|\le1$ 等价于

    $$
    a^2\Delta t(1-s)\le2b+4b^2\Delta t\,s/h^2.
    $$

    所以 $a\ne0$ 时可取 $c=2b/a^2$，从而每个模式和总 $\ell^2$ 范数都不增长。$a=0$ 时任意时间步长均可。

### [第 2(a)、(b) 题](../assets/yau-papers/2018-written-individual.pdf)

$q''=-\nabla V(q)$。(a) 写成 Hamilton 系统并证明流映射的 Jacobian $\Phi$ 满足 $\Phi^TJ\Phi=J$，$J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}$，坐标顺序为 $(p,q)$；(b) 证明 Velocity–Verlet 的三步 $p_{n+1/2}=p_n-h\nabla V(q_n)/2$、$q_{n+1}=q_n+hp_{n+1/2}$、$p_{n+1}=p_{n+1/2}-h\nabla V(q_{n+1})/2$ 为辛且二阶。

??? proof "答案"

    (a) 取 $p=q'$、$\mathcal H=\|p\|^2/2+V(q)$，得 $p'=-\nabla V(q),q'=p$。线性化矩阵 $M=\begin{pmatrix}0&-\nabla^2V\\I&0\end{pmatrix}$ 满足 $M^TJ+JM=0$。由 $\Phi'=M\Phi$、$\Phi(0)=I$，求导得 $\frac d{dt}(\Phi^TJ\Phi)=0$。

    (b) 两次动量更新的 Jacobian 为 $\begin{pmatrix}I&-h\nabla^2V/2\\0&I\end{pmatrix}$，位置更新为 $\begin{pmatrix}I&0\\hI&I\end{pmatrix}$，分别直接满足辛恒等式，故复合也满足。展开得到

    $$
    q_{n+1}=q_n+hp_n-\tfrac12h^2\nabla V(q_n),
    \quad p_{n+1}=p_n-h\nabla V(q_n)-\tfrac12h^2\nabla^2V(q_n)p_n+O(h^3),
    $$

    与精确解二阶 Taylor 系数相同，局部误差 $O(h^3)$，在通常光滑性和有限时间区间下为二阶。

### [第 4(b)、(c) 题](../assets/yau-papers/2018-written-individual.pdf)

$H_n(x)=(-1)^ne^{x^2/2}(d^n/dx^n)e^{-x^2/2}$。(b) 证明 $H_{n+1}=xH_n-nH_{n-1}$，并证明相邻多项式无公共根；(c) 证明 $H_n'=nH_{n-1}$，并求 $xu'-u''=\lambda u$ 对 $u=H_n$ 的特征值。

??? proof "答案"

    由定义微分得 $H_{n+1}=xH_n-H_n'$。从 $H_0=1,H_1=x$ 同时归纳 $H_n'=nH_{n-1}$ 和三项递推：对 $H_{n+1}=xH_n-nH_{n-1}$ 求导，并用前一层递推，即得 $H_{n+1}'=(n+1)H_n$。

    若 $H_n,H_{n-1}$ 有公共根，递推迫使 $H_{n-2},\ldots,H_0$ 在该点都为零，矛盾。最后 $xH_n'-H_n''=n(xH_{n-1}-(n-1)H_{n-2})=nH_n$，故 $\lambda_n=n$。

### [第 5(1)–(4) 题](../assets/yau-papers/2018-written-individual.pdf)

**原卷：** [2018 应用与计算数学个人赛，第 3 页](../assets/yau-papers/2018-computational-applied.pdf#page=3)。**先修：** [SVD](02-svd-least-squares.md)、[谱定理](01-matrix-norms-spectral.md)。

定义实方阵的核范数 $\|A\|_* =\sum_i\sigma_i(A)$。证明 (1) $\|A\|_* =\operatorname{tr}\sqrt{A^TA}$；(2) $\|A\|_* =\max_{X^TX=I}\operatorname{tr}(AX)$；(3) 三角不等式 $\|A+B\|_*\le\|A\|_*+\|B\|_*$。



(4) 非严格地解释：为什么最小化 $\|A-A_0\|_F^2+\|A\|_*$ 可能得到 $A_0$ 的低秩逼近？

??? proof "答案"

    **(1)** 由 $A=U\Sigma V^T$ 得 $A^TA=V\Sigma^2V^T$，其正半定平方根为 $V\Sigma V^T$。迹在相似变换下不变，所以 $\operatorname{tr}\sqrt{A^TA}=\sum_i\sigma_i$。

    **(2)** 对任意正交 $X$，$Y=V^TXU$ 仍正交，其每个对角元 $Y_{ii}\le1$。迹的循环性质给出

    $$
    \operatorname{tr}(AX)=\operatorname{tr}(\Sigma V^TXU)
    =\sum_i\sigma_iY_{ii}\le\sum_i\sigma_i.
    $$

    取 $X=VU^T$，此时 $Y=I$，上界达到。注意原题写的是 $\operatorname{tr}(AX)$，因此实现极值的是 $VU^T$。

    **(3)** 由 (2)，任意正交 $X$ 满足

    $$
    \operatorname{tr}((A+B)X)=\operatorname{tr}(AX)+\operatorname{tr}(BX)
    \le\|A\|_*+\|B\|_*.
    $$

    对左侧取最大值即得结论。

    **(4)** 核范数对每个奇异值施加线性惩罚。沿 $A_0=U\operatorname{diag}(s_i)V^T$ 的奇异向量方向，目标的每一项为 $(t_i-s_i)^2+t_i$，$t_i\ge0$，最小者为 $t_i=\max(s_i-1/2,0)$。小奇异值被压到零，因此得到低秩矩阵。

## 2018 · 笔试·团体赛

### [第 2(1)–(5) 题](../assets/yau-papers/2018-written-team.pdf)

超立方体顶点为 $\{0,1\}^n$，只差一个坐标的顶点相邻。函数空间内积为 $\langle f,g\rangle=\sum_v f(v)g(v)$，定义 $\chi_u(v)=(-1)^{u\cdot v}$。

(1) 证明 $\langle\chi_u,\chi_w\rangle=2^n\delta_{uw}$；(2) 证明这些函数构成一组基；(3) 对 $\Phi f(v)=\sum_i f(v+e_i)$（模 $2$ 加法），证明其标准基矩阵是邻接矩阵；(4) 证明 $\Phi\chi_u=(n-2|u|)\chi_u$；(5) 求邻接矩阵的谱。

??? proof "答案"

    (1) 内积分解为 $\prod_{j=1}^n(1+(-1)^{u_j+w_j})$，等于 $2^n$ 或 $0$。

    (2) $2^n$ 个非零正交向量处在维数 $2^n$ 的空间中，所以是基。

    (3) $\Phi\delta_w(v)=1$ 当且仅当 $v,w$ 相邻，故矩阵元就是邻接关系。

    (4) $\chi_u(v+e_i)=(-1)^{u_i}\chi_u(v)$，求和得 $(n-2|u|)\chi_u(v)$。

    (5) 特征值为 $n-2r$（$r=0,\ldots,n$），重数 $\binom nr$。

### [第 3(1)、(2) 题](../assets/yau-papers/2018-written-team.pdf)

正规矩阵 $A=QDQ^*$，$Q$ 酉，$|\lambda_1|\ge\cdots\ge|\lambda_k|>|\lambda_{k+1}|\ge\cdots$。令 $P=Q\operatorname{diag}(I_k,0)Q^*$，$X^{(m+1)}=AX^{(m)}$，且 $PX^{(0)}$ 满列秩。

(1) 证明 $P$ 是前 $k$ 个特征向量空间的正交投影；(2) 找到 $\Lambda$，使任意非零 $y$ 满足

$$
\frac{\|(AX^{(m)}-X^{(m)}\Lambda)y\|}{\|PX^{(m)}y\|}
\le\left|\frac{\lambda_{k+1}}{\lambda_k}\right|^m
\frac{\|(AX^{(0)}-X^{(0)}\Lambda)y\|}{\|PX^{(0)}y\|}.
$$

??? proof "答案"

    (1) $P^*=P,P^2=P$，像空间恰为前 $k$ 列的张成空间。

    (2) 写 $Q=[Q_1,Q_2]$、$D=\operatorname{diag}(D_1,D_2)$，$C=Q_1^*X^{(0)}$ 可逆，取 $\Lambda=C^{-1}D_1C$。$R_0=AX^{(0)}-X^{(0)}\Lambda$ 满足 $PR_0=0$。故 $R_m=A^mR_0$，$\|R_my\|\le|\lambda_{k+1}|^m\|R_0y\|$；另一方面 $\|PX^{(m)}y\|=\|D_1^mCy\|\ge|\lambda_k|^m\|Cy\|$。相除即得。

### [第 4(1)、(2) 题](../assets/yau-papers/2018-written-team.pdf)

对周期平流 $u_t+a u_x=f$ 使用 $(3v^{n+1}-4v^n+v^{n-1})/(2k)+aD_0v^{n+1}=f^{n+1}$。(1) 求时间、空间准确阶；(2) 证明稳定性。

??? proof "答案"

    Taylor 展开给出 $O(k^2+h^2)$。$D_0$ 在周期正交模式上的特征值为纯虚数 $i\sin\theta/h$。各模式递推为 BDF2，特征方程 $(3-2z)r^2-4r+1=0$，$z=-iak\sin\theta/h$。BDF2 稳定域包含闭左半平面；也可直接乘 $v^{n+1}$，用恒等式 $2(3a-4b+c)a=a^2+(2a-b)^2-b^2-(2b-c)^2+(a-2b+c)^2$，以及 $\langle D_0v,v\rangle=0$，得到离散能量非增，因而对所有 $k,h>0$ 稳定。

### [第 5(1)、(2)、(3)(a)–(d) 题](../assets/yau-papers/2018-written-team.pdf)

凸函数的次梯度定义为 $f(y)\ge f(x)+g^T(y-x)$ 对所有 $y$ 成立，集合记为 $\partial f(x)$。

(1) 求 $f(x)=|x|$ 的 $\partial f(0)$；(2) 给出用次微分表达的全局极小充要条件；(3) 对 $x_{k+1}=x_k-\alpha g_k$，$g_k\in\partial f(x_k)$，假定 $f$ 为 $L$-Lipschitz、$\|x_1-x^*\|\le B$，依次证明一步误差界、累计界、最佳函数值界，并选择最优固定步长。

??? proof "答案"

    (1) $\partial|\cdot|(0)=[-1,1]$。(2) $x^*$ 是全局极小点当且仅当 $0\in\partial f(x^*)$，由定义直接得到。

    (3) Lipschitz 条件沿次梯度方向给出 $\|g_k\|\le L$。于是

    $$
    \|x_{k+1}-x^*\|^2\le\|x_k-x^*\|^2-2\alpha(f(x_k)-f(x^*))+\alpha^2L^2.
    $$

    求和得 $2\alpha\sum_{j=1}^k(f(x_j)-f(x^*))\le B^2+k\alpha^2L^2$，因此

    $$
    \min_{j\le k}f(x_j)-f(x^*)\le\frac{B^2}{2\alpha k}+\frac{\alpha L^2}{2}.
    $$

    固定 $\alpha$ 时极限差不超过 $\alpha L^2/2$；对给定迭代预算 $k$，最优 $\alpha=B/(L\sqrt k)$，上界为 $BL/\sqrt k$。

## 2018 · 总决赛·个人赛

### [第 1(a)、(b) 题](../assets/yau-papers/2018-final-individual.pdf)

在 $[a,b]$ 的均匀网格上用复合梯形公式。(a) 写求积公式；(b) 推导误差估计。

??? proof "答案"

    $T_h=h[f(a)/2+\sum_{j=1}^{N-1}f(a+jh)+f(b)/2]$。每段线性插值余项为 $f''(\xi_x)(x-x_j)(x-x_{j+1})/2$，积分绝对值不超过 $h^3\|f''\|_\infty/12$。相加得 $|T_h-\int_a^bf|\le(b-a)h^2\|f''\|_\infty/12$，故二阶。

## 2018 · 总决赛·综合个人赛

### [第 1、2 题](../assets/yau-papers/2018-final-overall.pdf)

$x'=x\times a$，$a\in\mathbb R^3$ 为常向量。(1) 证明显式 Euler 不稳定；(2) 给出保持 $\|x\|_2$ 的改进格式并证明。

??? proof "答案"

    (1) $x^{n+1}=x^n+h(x^n\times a)$，垂直性给 $\|x^{n+1}\|^2=\|x^n\|^2+h^2\|x^n\times a\|^2$。$a\ne0$ 时垂直于 $a$ 的非零分量每步增长因子 $\sqrt{1+h^2\|a\|^2}>1$；$a=0$ 为平凡例外。

    (2) 用 $[x^{n+1}-x^n]/h=((x^{n+1}+x^n)/2)\times a$。与 $x^{n+1}+x^n$ 作内积，得平方范数差为零。等价于斜对称叉乘矩阵的 Cayley 变换，隐式矩阵可逆，故可直接求解。

## 2018 · 总决赛·团体赛

### [第 1 题](../assets/yau-papers/2018-final-team.pdf)

**原卷：** [2025 应用与计算数学，第 2 页](../assets/yau-papers/2025-computational-applied.pdf#page=2)。**选取：** 全题。**先修：** [投影与 SVD](02-svd-least-squares.md)、[低秩逼近](02-pseudoinverse-low-rank.md)。

给定 $y_1,\ldots,y_n\in\mathbb R^m$，令 $V=\operatorname{span}\{y_j\}$。对给定 $1\le\ell\le\dim V$，寻找 $\ell$ 个正交单位向量 $\psi_i$，使

$$
J=\sum_{j=1}^n\left\|y_j-\sum_{i=1}^\ell(y_j^T\psi_i)\psi_i\right\|_2^2
$$

最小。（$\ell=0$ 的空子空间情形显然，误差为 $\sum_j\|y_j\|_2^2$。）

??? proof "答案"

    写 $Y=[y_1,\ldots,y_n]$、$\Psi=[\psi_1,\ldots,\psi_\ell]$、$P=\Psi\Psi^T$。目标为

    $$
    J=\|(I-P)Y\|_F^2=\|Y\|_F^2-\operatorname{tr}(PYY^T).
    $$

    由 2012 第 4 题中已经证明的投影迹上界，$\operatorname{tr}(PYY^T)\le\sum_{i=1}^\ell\sigma_i(Y)^2$。对 $Y=U\Sigma V^T$ 取 $\psi_i=u_i$，即可达到上界。故

    $$
    J_{\min}=\sum_{i>\ell}\sigma_i(Y)^2.
    $$

    等价地，求 $YY^T$ 的前 $\ell$ 个特征向量。由于 $\ell\le\operatorname{rank}(Y)$，这些向量属于样本张成空间。若边界奇异值相等，最优子空间可能不唯一。原题拟合的是通过原点的线性子空间，没有中心变量，因此这里不应自行对样本减均值。

### [第 2(1)、(2) 题](../assets/yau-papers/2018-final-team.pdf)

$n$ 个超平面将 $\mathbb R^d$ 分成凸区域，最大区域数为 $f_d(n)$。(1) 求 $d=2$；(2) 求一般 $d$ 并证明。

??? proof "答案"

    $f_d(n)=\sum_{j=0}^{\min(d,n)}\binom nj$，所以 $f_2(n)=1+n(n+1)/2$。新增一个超平面时，新增区域数等于旧超平面在其上形成的 $(d-1)$ 维区域数，至多 $f_{d-1}(n-1)$。适当一般位置的超平面可同时达到此界，故 $f_d(n)=f_d(n-1)+f_{d-1}(n-1)$，初值 $f_d(0)=1,f_0(n)=1$；用 Pascal 恒等式归纳即得。

## 2019 · 笔试·个人赛

### [第 1(i)、(ii) 题](../assets/yau-papers/2019-written-individual.pdf)

已给 $\Pi_H(m)$ 为 $m$ 个点上最大分类标签数、$\mathrm{VC}(H)=\max\{m:\Pi_H(m)=2^m\}$。(i) 一维区间分类器的 VC 维；(ii) 证明 $\mathbb R^d$ 仿射线性分类器 VC 维为 $d+1$。

??? proof "答案"

    (i) 为 $2$：两个有序点能实现全部标签；三个有序点的 $+,-,+$ 无法由一个区间实现。

    (ii) 取 $d+1$ 个仿射独立点，增广矩阵 $(x_i^T,1)$ 可逆，给任意 $\pm1$ 标签都可解线性方程得到分类器。反之任意 $d+2$ 个点存在非零 $c_i$ 使 $\sum c_i=0,\sum c_ix_i=0$。按 $c_i$ 的正、负号指定标签（零系数任意），若某个分类器实现，则每个非零 $c_i(w\cdot x_i+b)>0$，其和应正，但线性依赖又使其和为零，矛盾。

### [第 2(i)–(iii) 题](../assets/yau-papers/2019-written-individual.pdf)

对热方程 $u_t=u_{xx}$ 使用 $(v^{n+1}-v^{n-1})/(2k)=D_2v^n$。(i) 求截断误差；(ii) 是否稳定？(iii) 修改时间离散，给出稳定格式。

??? proof "答案"

    (i) 归一化截断误差 $O(k^2+h^2)$。

    (ii) 不稳定。$D_2$ 的非零周期模式特征值为 $-4\sin^2(\theta/2)/h^2$，相应递推根满足 $r^2+8(k/h^2)\sin^2(\theta/2)r-1=0$。两根乘积 $-1$，非零模式总有一根模大于 $1$。

    (iii) 改为后向 Euler：$(I-kD_2)v^{n+1}=v^n$。各模式因子为 $[1+4(k/h^2)\sin^2(\theta/2)]^{-1}\in(0,1]$，无条件稳定；时间一阶、空间二阶。

### [第 3(i)–(iii) 题](../assets/yau-papers/2019-written-individual.pdf)

$K\subset\mathbb R^n$ 为非空闭凸集，$\Pi_K(z)$ 最小化 $\|y-z\|^2/2$。(i) 证明 $y=\Pi_K(z)$ 当且仅当 $(z-y)^T(d-y)\le0$ 对所有 $d\in K$ 成立；(ii) 证明投影为 $1$-Lipschitz；(iii) 对 $\Theta(z)=\|z-\Pi_K(z)\|^2/2$，证明 $\nabla\Theta(z)=z-\Pi_K(z)$。

??? proof "答案"

    (i) 沿 $y+t(d-y)$ 对目标的一侧导数取 $t=0$，得到必要条件。反过来，$\|d-z\|^2-\|y-z\|^2=\|d-y\|^2-2(z-y)^T(d-y)\ge0$。

    (ii) 对 $p=\Pi_K(x),q=\Pi_K(z)$，将两条变分不等式相加得 $\|p-q\|^2\le(p-q)^T(x-z)$，用 Cauchy–Schwarz。

    (iii) 分别用 $p=\Pi_K(z)$、$q=\Pi_K(z+h)$ 作比较，并使用 (ii)，得

    $$
    -\frac12\|h\|^2\le\Theta(z+h)-\Theta(z)-(z-p)^Th\le\frac12\|h\|^2.
    $$

    故导数为 $z-p$，且由 (ii) 连续。极小解的存在性可把搜索限制在有界闭球后取最小值；唯一性来自平方距离的严格凸性。

## 2019 · 笔试·团体赛

### [第 1 题](../assets/yau-papers/2019-written-team.pdf)

证明 $\int_{-1}^1 f(x)/\sqrt{1-x^2}\,dx=(\pi/n)\sum_{j=0}^{n-1}f(\cos((2j+1)\pi/(2n)))$ 对次数不超过 $2n-1$ 的多项式精确。

??? proof "答案"

    以 $T_r(x)=\cos(r\arccos x)$（$0\le r\le2n-1$）作多项式基。代入 $x=\cos\theta$，积分对 $r=0$ 为 $\pi$，其余为零。节点和满足

    $$
    \sum_{j=0}^{n-1}\cos\frac{r(2j+1)\pi}{2n}=0\quad(1\le r\le2n-1),
    $$

    由有限几何级数或余弦和公式得到。因此在该基上精确，再由线性性推广。

### [第 2 题](../assets/yau-papers/2019-written-team.pdf)

对非零 $x\in\mathbb R^N$，定义 $\hat x_w=N^{-1/2}\sum_{t=0}^{N-1}x_t e^{-2\pi iwt/N}$。$\|x\|_0$ 表示非零分量数。证明 $\|x\|_0\|\hat x\|_0\ge N$。

??? proof "答案"

    令 $s=\|x\|_0,t=\|\hat x\|_0$。几何级数证明 DFT 矩阵酉，故 $\|\hat x\|_2=\|x\|_2$。又 $|\hat x_w|\le N^{-1/2}\|x\|_1\le\sqrt{s/N}\|x\|_2$，因此 $\|x\|_2^2\le t\|\hat x\|_\infty^2\le st\|x\|_2^2/N$。约去非零范数。

### [第 3(i)–(iii) 题](../assets/yau-papers/2019-written-team.pdf)

$X\in\mathbb R^{n\times m}$ 满列秩、$m\le n$，$A=\begin{pmatrix}I&X\\X^T&0\end{pmatrix}$。(i) 证明可逆；(ii) 用 $X$ 的奇异值给出全部特征值；(iii) 判断迭代 $z_{k+1}=z_k-(Az_k-b)$ 能否对任意初值收敛。

??? proof "答案"

    经 SVD 正交相似变换，$A$ 分解为二维块 $\begin{pmatrix}1&\sigma_i\\\sigma_i&0\end{pmatrix}$ 和 $n-m$ 个标量 $1$。特征值为 $(1\pm\sqrt{1+4\sigma_i^2})/2$ 以及重复 $n-m$ 次的 $1$，均非零，所以可逆。

    当 $m\ge1$ 时，每个二维块都有负特征值 $\lambda_-$，迭代矩阵 $I-A$ 对应特征值 $1-\lambda_->1$，因此没有满列秩的 $X$ 能保证该迭代对任意初值收敛。

### [第 4(i)–(iii) 题](../assets/yau-papers/2019-written-team.pdf)

$f\in C^1(\mathbb R^n)$ 凸且 $\nabla f$ 为 $L$-Lipschitz。证明：

$$
f(y)\le f(x)+\nabla f(x)^T(y-x)+\tfrac L2\|y-x\|^2;
$$

$$
f(y)\ge f(x)+\nabla f(x)^T(y-x)+\tfrac1{2L}\|\nabla f(y)-\nabla f(x)\|^2;
$$

$$
\tfrac1L\|\nabla f(y)-\nabla f(x)\|^2\le(\nabla f(y)-\nabla f(x))^T(y-x).
$$

??? proof "答案"

    第一式沿线段积分梯度差，绝对余项不超过 $\int_0^1 Lt\|y-x\|^2dt$。

    令 $F(z)=f(z)-\nabla f(x)^Tz$。凸性给出 $x$ 为 $F$ 的全局极小点。第一式用于 $z=y-\nabla F(y)/L$，得 $F(x)\le F(y)-\|\nabla F(y)\|^2/(2L)$，即第二式。交换 $x,y$ 后将两条第二式相加，即得第三式。

### [第 5(i) 题](../assets/yau-papers/2019-written-team.pdf)

用 $y_{n+2}-2y_{n+1}+y_n=h^2 f(t_{n+1},y_{n+1})$ 求解 $y''=f(t,y)$。求该 Störmer 格式的准确阶。

??? proof "答案"

    在 $t_{n+1}$ 两侧作 Taylor 展开，$(y(t+h)-2y(t)+y(t-h))/h^2=y''(t)+h^2y^{(4)}(t)/12+O(h^4)$。因此格式为二阶准确，归一化截断误差为 $h^2y^{(4)}(t)/12+O(h^4)$。

### [第 5(ii)、(iii) 题](../assets/yau-papers/2019-written-team.pdf)

(ii) 用中心空间差分与 Störmer 时间公式构造 $u_{tt}=u_{xx}$ 格式；(iii) 求稳定条件。

??? proof "答案"

    (ii) $v_j^{n+1}-2v_j^n+v_j^{n-1}=(k/h)^2(v_{j+1}^n-2v_j^n+v_{j-1}^n)$，截断误差 $O(k^2+h^2)$。

    (iii) $\lambda=k/h$，模式方程 $r^2-[2-4\lambda^2\sin^2(\theta/2)]r+1=0$，根在单位圆上的必要范围为 $\lambda\le1$。通常取 $\lambda<1$，并按初始位移和初始速度设置第一步；$\lambda=1$ 的最高频有重根，需兼容起步，否则可能出现线性增长。零频的线性时间项对应精确解中的常速度，不应仅以两个独立的位移初值来定义稳定范数。

## 2019 · 总决赛·个人赛

### [第 1 题](../assets/yau-papers/2019-final-individual.pdf)

伴随矩阵 $C$ 的最后一列为 $(-c_0,\ldots,-c_{n-1})^T$、下对角为 $1$，特征值 $\lambda_i$ 互异。令 $V_{ij}=\lambda_i^{j-1}$。证明 $VCV^{-1}=\operatorname{diag}(\lambda_i)$。

??? proof "答案"

    特征多项式为 $p(t)=t^n+c_{n-1}t^{n-1}+\cdots+c_0$。行向量 $(1,\lambda_i,\ldots,\lambda_i^{n-1})$ 乘 $C$，最后分量为 $-\sum_jc_j\lambda_i^j=\lambda_i^n$，故 $VC=\operatorname{diag}(\lambda_i)V$。互异节点的 Vandermonde 矩阵可逆，结论成立。

### [第 2 题](../assets/yau-papers/2019-final-individual.pdf)

证明 Simpson 误差 $\int_a^bf(x)dx-\frac{b-a}6[f(a)+4f((a+b)/2)+f(b)]=-(b-a)^5f^{(4)}(\xi)/2880$，$a<\xi<b$。

??? proof "答案"

    令 $m=(a+b)/2$，取匹配 $f(a),f(m),f'(m),f(b)$ 的三次 Hermite 多项式 $H$。反复 Rolle 定理给 $f(x)-H(x)=f^{(4)}(\xi_x)(x-a)(x-m)^2(x-b)/24$。该核在区间上不变号，积分中值定理给某个 $\xi$；直接积分核为 $-(b-a)^5/2880$。Simpson 对 $H$ 精确且与 $f$ 有相同节点值，故得到所求式（需 $f\in C^4$）。

### [第 3(a)、(b) 题](../assets/yau-papers/2019-final-individual.pdf)

$x_{n+1}=g(x_n)$。(a) 讨论不动点存在、唯一及收敛阶；(b) 令 $G(x)=x-[g(x)-x]^2/[g(g(x))-2g(x)+x]$，证明 $g$ 的不动点也是 $G$ 的不动点。

??? proof "答案"

    (a) 连续自映射闭区间有不动点；若该区间上 $|g'|\le q<1$，则唯一且迭代收敛。这是充分条件，不是必要条件。不动点必须满足 $g(\alpha)=\alpha$；局部吸引简单线性情形需要 $|g'(\alpha)|<1$，阶由 Taylor 首个非零项确定：若 $g^{(1)}(\alpha)=\cdots=g^{(p-1)}(\alpha)=0$、$g^{(p)}(\alpha)\ne0$，则 $e_{n+1}=g^{(p)}(\alpha)e_n^p/p!+o(e_n^p)$。

    (b) 在不动点处原式为 $0/0$，不能直接代入。若 $g'(\alpha)\ne1$，分子为 $O((x-\alpha)^2)$、分母为 $(g'(\alpha)-1)^2(x-\alpha)+O((x-\alpha)^2)$，所以连续延拓有 $G(\alpha)=\alpha$。没有非退化条件原式甚至可能在整段未定义，例如 $g(x)=x$。

### [第 4 题](../assets/yau-papers/2019-final-individual.pdf)

常系数热方程的紧致格式 $P(v^{n+1}-v^n)/k=aD_2(v^{n+1}+v^n)/2$，$P=I+h^2D_2/12$，时间二阶、空间四阶。对 $u_t=\sigma(x)u_{xx}$、$\sigma\ge\sigma_0>0$，如何保持准确阶？

??? proof "答案"

    改为 $P\{\sigma^{-1}(v^{n+1}-v^n)/k\}=D_2(v^{n+1}+v^n)/2$，$\sigma^{-1}$ 为节点逐点相乘，不能与 $P$ 随意交换。原方程写作 $\sigma^{-1}u_t=u_{xx}$，Taylor 展开 $Pu_{xx}=D_2u+O(h^4)$，时间平均与中心差商为二阶，故光滑解的截断误差 $O(k^2+h^4)$。

### [第 5 题](../assets/yau-papers/2019-final-individual.pdf)

$A$ 可逆，求解 $Ax_1+Bx_2=b_1$、$Bx_1+Ax_2=b_2$，同步迭代 $Ax_1^{k+1}=b_1-Bx_2^k$、$Ax_2^{k+1}=b_2-Bx_1^k$。给出收敛条件，注意原卷写的是“某个初值”。

??? proof "答案"

    令 $C=A^{-1}B$，误差矩阵 $T=\begin{pmatrix}0&-C\\-C&0\end{pmatrix}$，特征值为 $\pm\lambda_j(C)$。对任意初值收敛到唯一解的充要条件是 $\rho(C)<1$。

    若确实只要求某个初值，则不存在同样的必要谱条件：系统有解时从精确解出发即收敛。相对某个指定解，给定初值收敛到它的充要条件是 $T^ke^0\to0$，即初始误差属于 $T$ 的所有 $|\lambda|<1$ 的广义特征子空间之和；不稳定方向的初始分量必须为零。

## 2019 · 总决赛·综合个人赛

### [第 2 题](../assets/yau-papers/2019-final-overall.pdf)

$A$ 为 $2n$ 阶矩阵，$a_{ij}=1$ 当 $i+j$ 为偶数，其余为零。计算 Frobenius、最大行和范数，并证明 $\sum_{k=1}^{\infty}(1/(2n))^kA^k=A/n$。

??? proof "答案"

    每行恰 $n$ 个 $1$，共 $2n^2$ 个，故 $\|A\|_\infty=n$、$\|A\|_F=\sqrt2\,n$；原卷写 $\|A\|_F=n$ 有误。重排奇偶坐标后为两个全一 $n\times n$ 块，$A^2=nA$，所以 $A^k=n^{k-1}A$。级数等于 $(1/n)\sum_{k\ge1}2^{-k}A=A/n$。

### [第 3(1)–(4) 题](../assets/yau-papers/2019-final-overall.pdf)

Hilbert 空间 $X,Y$，有界算子 $T:X\to Y$、伴随 $T^*$。$f(\beta)$ 最小化 $J(f)=\|Tf-z\|_Y^2/2+\beta\|f\|_X^2/2$，$\beta>0$，$F(\beta)=J(f(\beta))$。(1) 求最优方程；(2) 求 $f^{(n)}$ 的方程；(3) 求 $F',F''$；(4) $T^*z\ne0$ 时证明严格递增且严格凹。

??? proof "答案"

    令 $H_\beta=T^*T+\beta I$。

    (1) 对任意方向 $g$，将 $J(f+tg)$ 展开并令 $t$ 的一次系数为零：$\langle Tf,Tg\rangle+\beta\langle f,g\rangle=\langle z,Tg\rangle$，即 $H_\beta f=T^*z$。$\langle H_\beta v,v\rangle\ge\beta\|v\|^2$ 保证唯一性。

    (2) 逐次求导：$H_\beta f^{(n)}=-nf^{(n-1)}$，因此 $f^{(n)}=(-1)^nn!H_\beta^{-(n+1)}T^*z$。所需逆算子存在可由压缩映射 $v\mapsto v-c(H_\beta v-T^*z)$ 证明：足够小 $c>0$ 使其 Lipschitz 因子小于 $1$；局部参数变化用 Neumann 级数证明可微。

    (3) 最优方程消去含 $f'$ 的项，$F'=\|f\|^2/2$、$F''=\langle f,f'\rangle=-\langle f,H_\beta^{-1}f\rangle$。

    (4) $T^*z\ne0$ 给 $f\ne0$，故 $F'>0,F''<0$。

## 2019 · 总决赛·团体赛

### [第 1(i)、(ii) 题](../assets/yau-papers/2019-final-team.pdf)

整数矩阵 $A$ 有 $n$ 列、秩不超过 $n-1$、$|a_{ij}|\le H$。(i) 估计 $\|x\|_\infty\le K$ 的整数向量数量；(ii) 用抽屉原理证明存在非零整数 $x$ 满足 $Ax=0$、$\|x\|_\infty\le(2nH)^{n-1}$。

??? proof "答案"

    (i) 恰有 $(2\lfloor K\rfloor+1)^n\le(2K+1)^n$ 个。

    (ii) $H=0$ 时取任意单位向量。否则令整数 $M=(2nH)^{n-1}$，考虑 $\{0,\ldots,M\}^n$ 的 $(M+1)^n$ 个点。取 $r\le n-1$ 个独立行，每个像分量在 $[-nHM,nHM]$，像数量至多 $(2nHM+1)^r<(M+1)^n$；最后严格不等式由 $M=(2nH)^{n-1}$ 和 Bernoulli 不等式得到。两个点的独立行像相同，则所有行像相同；其非零差向量满足要求。

### [第 2(i)、(ii) 题](../assets/yau-papers/2019-final-team.pdf)

(i) 求 $[(a_{i+1}+a_i)(u_{i+1}-u_i)-(a_i+a_{i-1})(u_i-u_{i-1})]/(2h^2)$ 对 $(au')'$ 的准确阶；(ii) 用它离散 $u-(au')'=f$、$u(0)=u(1)=0$、$a>0$，证明 Gauss–Seidel 对任意初值收敛。

??? proof "答案"

    (i) 对光滑 $a,u$ 对称 Taylor 展开，结果为 $au''+a'u'+O(h^2)$，二阶。

    (ii) 令 $c_{i+1/2}=(a_i+a_{i+1})/(2h^2)>0$。矩阵对角为 $1+c_{i-1/2}+c_{i+1/2}$，相邻项为 $-c_{i\pm1/2}$，严格行对角占优。若 Gauss–Seidel 误差矩阵有特征对 $(\lambda,x)$，取 $|x_i|$ 最大的行，令该行下、上对角绝对值和为 $l_i,u_i$，得 $|\lambda|d_i\le|\lambda|l_i+u_i$，所以 $|\lambda|\le u_i/(d_i-l_i)<1$。因此谱半径小于 $1$，迭代收敛。

### [第 3(i)、(ii) 题](../assets/yau-papers/2019-final-team.pdf)

最大化 $S(p)=-\sum_ip_i\log p_i$，约束 $p_i\ge0,\sum p_i=1,\sum_ip_if_j(x_i)=E_j$。(i) 推导指数族形式；(ii) 证明 $E_j=\partial_{\lambda_j}\log Z$。

??? proof "答案"

    若最优点各 $p_i>0$，梯度与所有约束核方向正交，故在约束矩阵行空间内：$-(1+\log p_i)=c-\sum_j\lambda_jf_j(x_i)$。归一化得到 $p_i=e^{\sum_j\lambda_jf_j(x_i)}/Z$。直接求导得 $\partial_{\lambda_j}\log Z=\sum_ip_if_j(x_i)=E_j$。严格凹性保证正的可行驻点是唯一最优点。

    若约束只允许边界解，有限参数指数族未必存在，例如约束强制某个 $p_i=0$；这时须在允许的支持上表述，或以参数极限表示。原卷未说明内点条件。

## 2020 · 笔试·个人赛

### [第 1 题](../assets/yau-papers/2020-written-individual.pdf)

$f\in C^{k+1}[-1,1]$，$I_j=[(j-1)h,jh]$。次数不超过 $k$ 的 $p_j$ 在 $I_j$ 满足 $\max|p_j-f|\le C_0h^{k+1}$，$C_0$ 与 $j$ 无关。证明相邻的 $I_{j\pm1}$ 上也有 $Ch^{k+1}$ 界。

??? proof "答案"

    取 $I_j$ 左端点的 $k$ 次 Taylor 多项式 $T_j$；在本区间及相邻区间，余项均由 $\sup|f^{(k+1)}|$ 和 $O(h^{k+1})$ 控制。缩放 $x=x_j+ht$ 后，$h^{-k-1}(p_j-T_j)$ 是固定次数的多项式，在本区间一致有界。有限维多项式的区间范数等价，将界延伸到相邻区间，常数只依赖 $k,C_0$ 和高阶导数界。

### [第 2 题](../assets/yau-papers/2020-written-individual.pdf)

考虑固定锚点迭代 $x_{n+1}=x_n-(x_n-x_0)f(x_n)/(f(x_n)-f(x_0))$。$f\in C^2$，假定序列收敛到简单根 $\xi$。求收敛速率。

??? proof "答案"

    若 $f(x_0)\ne0$，其映射在 $\xi$ 的导数为 $a=1+(\xi-x_0)f'(\xi)/f(x_0)$，所以 $e_{n+1}=ae_n+O(e_n^2)$。当 $0<|a|<1$，线性收敛因子为 $|a|$；当 $a=0$，至少二阶，二次系数为 $-f''(\xi)/(2f'(\xi))$。$|a|=1$ 时仅凭“收敛”不能断言线性几何速率。

    锚点与迭代初值必须区分：从同一个 $x_0$ 直接执行首步会出现 $0/0$，需另给 $x_1$。若锚点本身是根，可直接停止。

### [第 3 题](../assets/yau-papers/2020-written-individual.pdf)

$A$ 有完整正交单位特征向量 $q_j$，特征值满足 $|\lambda_1|>|\lambda_2|>|\lambda_3|$、$\lambda_j\ge\lambda_{j+1}$（$j\ge3$）。$v^{(k)}=Av^{(k-1)}/\lambda_1$，$v^{(0)}=\sum_j\alpha_jq_j$，$\alpha_1\alpha_2\ne0$。讨论是否线性收敛到 $\alpha_1q_1$，因子为 $|\lambda_2/\lambda_1|$。

??? proof "答案"

    原卷的后半段按数值递减，并不能控制绝对值。例如 $A=\operatorname{diag}(3,2,1,-4)$ 满足所写条件，但含第四方向的初值会发散。

    若补为 $\max_{j\ge3}|\lambda_j|<|\lambda_2|$，则

    $$
    v^{(k)}-\alpha_1q_1=\sum_{j\ge2}\alpha_j(\lambda_j/\lambda_1)^kq_j,
    $$

    正交性及 $\alpha_2\ne0$ 给出相邻误差范数比趋于 $|\lambda_2/\lambda_1|$。

### [第 4(a)–(c) 题](../assets/yau-papers/2020-written-individual.pdf)

对 $y'=f(t,y)$，使用 $y_{n+1}=4y_n/3-y_{n-1}/3+2hf(t_{n+1},y_{n+1})/3$，首步 $y_1=y_0+hf(t_1,y_0)$。(a) 求准确阶；(b) 分析稳定多项式；(c) 给出绝对稳定域。

??? proof "答案"

    (a) 主格式归一化截断误差为 $-h^2y^{(3)}(t_{n+1})/3+O(h^3)$。首步误差 $O(h^2)$，因此在光滑、Lipschitz 条件下整体二阶。

    (b) 零稳定多项式 $3r^2-4r+1=(r-1)(3r-1)$，单位根简单，其余根 $1/3$，满足根条件。

    (c) 对 $y'=\lambda y$，$z=h\lambda$，放大根满足 $(3-2z)r^2-4r+1=0$。绝对稳定域为两根均在闭单位圆内且圆上根简单的 $z$ 集合；边界

    $$
    z(\theta)=\frac{3-4e^{-i\theta}+e^{-2i\theta}}2,
    \quad\Re z=(1-\cos\theta)^2.
    $$

    稳定域是该闭曲线围成区域的外部及满足简单根条件的边界，包含整个左半平面，所以方法 A-稳定。$z=3/2$ 处递推不可解，不属于稳定域。

### [第 5 题](../assets/yau-papers/2020-written-individual.pdf)

若 $u^{n+1}=Bu^n$ 稳定，即 $\|B^j\|\le K$ 对 $j\Delta t\le T$ 一致成立，且 $\|C(\Delta t)\|\le M$，证明 $u^{n+1}=(B+\Delta tC(\Delta t))u^n$ 稳定。

??? proof "答案"

    展开 $(B+\Delta tC)^n$，含 $j$ 个 $C$ 的每一项中，$B$ 被分成至多 $j+1$ 段，所以其范数不超过 $K^{j+1}(\Delta tM)^j$。无须假定 $B,C$ 可交换。求和得 $\|(B+\Delta tC)^n\|\le K(1+\Delta tKM)^n\le Ke^{KMT}$。

### [第 6 题](../assets/yau-papers/2020-written-individual.pdf)

可逆矩阵 $A$，$\mathcal P_n$ 为 $n$ 次首一多项式，且 $\inf_{p\in\mathcal P_n}\|p(A)\|_2=\|p_*(A)\|_2>0$。证明极小多项式唯一。

??? proof "答案"

    若 $p_1,p_2$ 都极小，令 $p=(p_1+p_2)/2$，其范数仍为极小值 $s>0$。对 $p(A)$ 的最大奇异值对应单位对 $u_j,v_j$，三角不等式达到等号，迫使 $p_1(A)v_j=p_2(A)v_j=su_j$，同理 $p_1(A)^*u_j=p_2(A)^*u_j=sv_j$。

    令 $r=p_1-p_2\ne0$，次数 $d<n$，取首一 $q(z)=z^{n-d}r(z)/\operatorname{lead}(r)$。因矩阵多项式可交换，$q(A)v_j=q(A)^*u_j=0$。在上述左右奇异向量分块中，$(1-\epsilon)p(A)+\epsilon q(A)$ 的最大奇异块变为 $(1-\epsilon)sI$；其余块原范数严格小于 $s$，足够小的 $\epsilon>0$ 后仍小于 $s$。这给出范数小于 $s$ 的首一多项式，矛盾。

## 2020 · 总决赛·个人赛

### [试卷一 · 第 I(1)、(2) 题](../assets/yau-papers/2020-final-individual-set1.pdf)

$A=VFU^T$ 为 SVD，定义 $A^+=UF^+V^T$。(1) 证明 $A^+b$ 是最小二乘解；(2) 证明 $\lim_{\alpha\downarrow0}(\alpha I+A^TA)^{-1}A^T=A^+$。

??? proof "答案"

    (1) 在正交坐标中，目标为 $\sum_{i\le r}(\sigma_i z_i-c_i)^2+\sum_{i>r}c_i^2$。取 $z_i=c_i/\sigma_i$（$i\le r$）、其余为零，得到 $A^+b$，且它是全部最小二乘解中范数最小者。

    (2) 相同 SVD 坐标下，非零方向的系数为 $\sigma_i/(\alpha+\sigma_i^2)\to1/\sigma_i$，零奇异值方向系数恒为零。因此矩阵范数下收敛到 $A^+$。

### [试卷二 · 第 I(1)、(2) 题](../assets/yau-papers/2020-final-individual-set2.pdf)

对称 $A$，$\|q_1\|=1$，$q_0=0,\beta_0=0$。Lanczos 递推 $\alpha_j=q_j^TAq_j$、$r_j=Aq_j-\alpha_jq_j-\beta_{j-1}q_{j-1}$、$\beta_j=\|r_j\|$、$q_{j+1}=r_j/\beta_j$。(1) 未提前终止时，证明 $Q_k$ 列正交且张成 $K_k$；(2) 说明该算法的用途并证明。

??? proof "答案"

    (1) 归纳并利用 $A=A^T$：$q_i^TAq_j=(Aq_i)^Tq_j=0$ 对 $i\le j-2$；减去当前与前一方向后，余量与全部已有向量正交。非零余量归一化得到下一正交向量，递推也给出与 $\{q_1,Aq_1,\ldots,A^{k-1}q_1\}$ 相同的张成空间。

    (2) 将大对称矩阵投影为小对称三对角矩阵 $T_k=Q_k^TAQ_k$，用于特征值与线性系统近似。若 $T_kz=\lambda z$，其提升向量的残差为 $\beta_kq_{k+1}e_k^Tz$，范数 $|\beta_ke_k^Tz|$ 可直接计算。以上为精确算术结论。

### [试卷一 · 第 II 题](../assets/yau-papers/2020-final-individual-set1.pdf)

对周期平流方程 $u_t+a u_x=f$，令 $\delta_0u_j=(u_{j+1}-u_{j-1})/(2h)$、$\delta^2u_j=(u_{j+1}-2u_j+u_{j-1})/h^2$，使用

$$
\frac{u_j^{n+1}-u_j^{n-1}}{2k}+a(I+h^2\delta^2/6)^{-1}\delta_0u_j^n=f_j^n.
$$

证明稳定条件，并将格式推广到变系数 $a=a(x)$ 且保持准确阶。

??? proof "答案"

    令 $P=I+h^2\delta^2/6$。Taylor 展开得 $\delta_0u-Pu_x=-h^4u^{(5)}/180+O(h^6)$。周期网格上 $P$ 的特征值为 $(2+\cos\theta)/3\in[1/3,1]$，逆算子一致有界，因此空间误差 $O(h^4)$；中心时间差商误差 $O(k^2)$。

    空间算子的特征值为 $3i\sin\theta/[h(2+\cos\theta)]$，其绝对值最大为 $\sqrt3/h$。时间递推的特征多项式为 $r^2+2i\eta r-1$，$\eta=3ak\sin\theta/[h(2+\cos\theta)]$。两根模为 $1$ 且无重根的条件是 $|\eta|<1$；故统一稳定限制为 $|ak/h|<1/\sqrt3$。端点产生单位圆重根，不能对一般起始误差保证一致有界。


    变系数时用 $[v^{n+1}-v^{n-1}]/(2k)+\operatorname{diag}(a_j)P^{-1}D_0v^n=f^n$。先用紧致算子逼近 $u_x$，再逐点乘 $a_j$，由同一 Taylor 余项保持时间二阶、空间四阶；这只说明准确阶，变系数稳定性不能直接套用常系数模式结论。

### [试卷二 · 第 II(1)、(2) 题](../assets/yau-papers/2020-final-individual-set2.pdf)

$y''+\lambda^2y+g(y)=0$，$y(0)=\alpha,y'(0)=\beta$。(1) 写变常数积分公式；(2) 原卷给出 $y_{n+1}=2\cos(\lambda\tau)y_n-y_{n-1}-[\sin(\lambda\tau)/\lambda]g(y_n)$，要求证明二阶收敛。

??? proof "答案"

    (1) $y(t)=\alpha\cos(\lambda t)+(\beta/\lambda)\sin(\lambda t)-\int_0^t[\sin(\lambda(t-s))/\lambda]g(y(s))ds$，直接求导两次验证。

    (2) 所印系数不一致，不能证明二阶。取 $g\equiv1$，精确的两步强迫项为 $-2[1-\cos(\lambda\tau)]/\lambda^2=-\tau^2+O(\tau^4)$，原式却为 $-\tau+O(\tau^3)$。应将其改为 $-2[1-\cos(\lambda\tau)]g(y_n)/\lambda^2$；对应首步强迫项为 $-[1-\cos(\lambda\tau)]g(\alpha)/\lambda^2$。在足够光滑条件下，对对称积分公式 Taylor 展开再累积误差，可得到修正格式的二阶结论。

## 2020 · 总决赛·综合个人赛

### [第 II(1)、(2) 题](../assets/yau-papers/2020-final-overall.pdf)

$y'=-A^T(Ax-b)$、$y\in\partial\psi(x)$，$\psi(x)=\|x\|_1+\|x\|_2^2/(2\alpha)$、$b=Ax^*$、$\lambda_{\min}(A^TA)=\gamma>0$。$D=\psi(x^*)-\psi(x)-y\cdot(x^*-x)$。(1) 证明 $D'=-\|A(x-x^*)\|^2$；(2) 对 $\tau=\inf\{t>0:\operatorname{sign}x(t)=\operatorname{sign}x^*\}$，求有限上界。

??? proof "答案"

    (1) 沿可微轨迹，$d\psi(x)/dt=y\cdot x'$；非光滑点按分段或几乎处处的链式法则理解。求导抵消 $y\cdot x'$，得 $D'=-y'\cdot(x^*-x)=-\|A(x-x^*)\|^2$。

    (2) 所写的全坐标签一致不能保证有限时间。取 $A=I_2,\alpha=1,x^*=(1,0)$、$x(0)=(1,1)$。轨迹 $x(t)=(1,e^{-t})$、$y(t)=(2,1+e^{-t})$ 满足全部方程，但第二坐标始终为正，目标为零，故 $\tau=+\infty$，尽管最小非零幅值为 $1$。若只要求目标非零支持上的符号一致，可另由 $D'\le-\gamma\|x-x^*\|^2$ 推出对应的有限时间界；这与原卷定义不同。

## 2021 · 笔试·个人赛

### [第 1(a)、(b) 题](../assets/yau-papers/2021-written-individual.pdf)

(a) 证明 $T_n(x)=\cos(n\arccos x)$ 是 $n$ 次多项式，首项系数 $2^{n-1}$，极值节点 $x_j=\cos(j\pi/n)$；(b) $f\in C^{n+1}[-1,1]$，$P$ 为这些节点上的 $n$ 次插值，证明 $\|f-P\|_\infty\le\|f^{(n+1)}\|_\infty/[2^{n-1}(n+1)!]$。

??? proof "答案"

    (a) $T_0=1,T_1=x$，$T_{n+1}=2xT_n-T_{n-1}$，归纳得次数与首项系数（$n\ge1$）。令 $x=\cos\theta$，极值值为 $\cos(j\pi)=(-1)^j$，内部节点导数为零。

    (b) 节点多项式 $\omega(x)=\prod_{j=0}^n(x-x_j)=(x^2-1)T_n'(x)/(n2^{n-1})$，故 $|\omega(x)|\le2^{1-n}$。用反复 Rolle 定理得插值余项 $f(x)-P(x)=f^{(n+1)}(\xi)\omega(x)/(n+1)!$，立即得到所需界。

### [第 2 题](../assets/yau-papers/2021-written-individual.pdf)

三次样条 $S$ 在相邻节点间为三次多项式，整体 $C^2$。若它在 $[t_1,t_2]$ 和 $[t_3,t_4]$ 为直线，证明在 $[t_2,t_3]$ 也为直线。

??? proof "答案"

    $C^2$ 连续性给出 $S''(t_2)=S''(t_3)=0$。中间段的 $S''$ 是一次多项式，有两个不同零点，只能恒为零，故该段为直线。

### [第 3(a)–(c) 题](../assets/yau-papers/2021-written-individual.pdf)

$f(x)=2x-\cos x$。(a) 证明唯一根在 $(1/4,1/2)$；(b) 证明 $x_n=\frac12\cos x_{n-1}$ 从任意初值收敛；(c) $x_0=\pi/6$ 时给出保证误差小于 $\frac12\,10^{-8}$ 的次数，$x_0=20$ 时给出保证误差小于 $1/4$ 的次数。

??? proof "答案"

    (a) $f'=2+\sin x\ge1$，严格递增，$f(1/4)<0<f(1/2)$。

    (b) $g=\cos x/2$ 在 $\mathbb R$ 上压缩因子可取 $q=1/2$，由 Banach 定理从任意初值收敛到唯一根。

    (c) 后验/先验界为 $|x_n-x^*|\le2^{1-n}|x_1-x_0|$。第一初值有 $|x_1-x_0|=\pi/6-\sqrt3/4\approx0.090586$，取 $n=26$ 足够。第二初值可用 $|x_1-x_0|\le20.5$，取 $n=8$ 足够；利用一次更新后 $x_1\in[-1/2,1/2]$、$x^*\in(1/4,1/2)$，较紧的统一估计给出 $n=4$ 也足够。

### [第 4(a)、(b) 题](../assets/yau-papers/2021-written-individual.pdf)

$A\in\mathbb R^{m\times n}$，$m\ge n$，秩 $r<n$，紧致 SVD 为 $A=U_1\Sigma_1V_1^T$，令 $V_2$ 补全右正交基，$\sigma=\sigma_{\min}(\Sigma_1)>0$。对 $\min_x\|Ax-b\|_2$，(a) 求全部解；(b) 求最小范数解并证明其范数不超过 $\|b\|_2/\sigma$。

??? proof "答案"

    把 $x=V_1z_1+V_2z_2$、$b=U_1c_1+U_2c_2$ 分解，残差平方为 $\|\Sigma_1z_1-c_1\|^2+\|c_2\|^2$。全部解为 $x=V_1\Sigma_1^{-1}U_1^Tb+V_2z_2$。两部分正交，所以唯一最小范数解取 $z_2=0$，且 $\|x\|\le\|\Sigma_1^{-1}\|\,\|U_1^Tb\|\le\|b\|/\sigma$。

### [第 5(a)、(b) 题](../assets/yau-papers/2021-written-individual.pdf)

半隐式 Runge–Kutta 方法为 $k_1=f(y_n+\beta hk_1)$、$k_2=f(y_n+hk_1+\beta hk_2)$、$y_{n+1}=y_n+h[(1/2+\beta)k_1+(1/2-\beta)k_2]$。(a) 求准确阶和局部误差主项；(b) 证明 $\beta>1/2$ 时负实轴在绝对稳定域内。

??? proof "答案"

    令 $J=f'(y)$、$H=f''(y)$，光滑情形下“数值一步减精确一步”为

    $$
    h^3\left[(\beta-\beta^2-\tfrac16)J^2f+(\tfrac1{12}-\tfrac12\beta^2)H(f,f)\right]+O(h^4).
    $$

    二次 Taylor 系数总是匹配，两组三次系数不能同时为零，所以通用准确阶为 $2$。

    对 $f(y)=\lambda y$，$R(z)=[1+(1-2\beta)z+(\beta^2-2\beta+1/2)z^2]/(1-\beta z)^2$。令 $z=-s<0$，分母 $D=(1+\beta s)^2$，分子 $N$ 满足 $D-N=s+(2\beta-1/2)s^2>0$、$D+N=2+(4\beta-1)s+2(\beta-1/2)^2s^2>0$，故 $|R(-s)|<1$。

## 2021 · 总决赛·个人赛

### [第 I(1)–(3) 题](../assets/yau-papers/2021-final-individual.pdf)

**原卷：** [2014 应用与计算数学个人赛，第 2–3 页](../assets/yau-papers/2014-computational-applied.pdf#page=2)。**选取：** (i)–(iii)。**先修：** [线性迭代](03-linear-iterations-power.md)、[条件数](02-pseudoinverse-low-rank.md)。

设 $A$ 全部特征值为正实数，最小、最大者记为 $a,b$。对 $Ax=c$ 使用 $x^{(k+1)}=(I-\omega A)x^{(k)}+\omega c$。(i) 求对任意初值收敛的参数区间；(ii) 求使迭代矩阵谱半径最小的参数与分段表达；(iii) 对称正定时用 $\kappa_2(A)$ 表示最优收敛因子。

??? proof "答案"

    精确解 $x^*$ 存在，误差满足 $e_{k+1}=G_\omega e_k$，$G_\omega=I-\omega A$。特征值为 $1-\omega\lambda_i$，谱半径判据给出

    $$
    \rho(G_\omega)<1\iff |1-\omega\lambda_i|<1\ (\forall i)
    \iff 0<\omega<2/b.
    $$

    该判据无需 $A$ 可对角化。因为 $\lambda\mapsto|1-\omega\lambda|$ 凸且两端均为实际特征值，

    $$
    \rho(G_\omega)=\max\{|1-\omega a|,|1-\omega b|\}.
    $$

    令两端等模异号，得 $\omega_*=2/(a+b)$，最优值 $(b-a)/(b+a)$。进一步

    $$
    \rho(G_\omega)=\begin{cases}
    1-\omega a,&\omega\le\omega_*,\\
    \omega b-1,&\omega\ge\omega_*.
    \end{cases}
    $$

    左支随 $\omega$ 减小，右支随 $\omega$ 增大，所以交点确为全局最小点。若 $A$ 对称正定，$\kappa_2(A)=b/a$，故

    $$
    \rho(G_{\omega_*})=\frac{\kappa_2(A)-1}{\kappa_2(A)+1}.
    $$

### [第 II(1)、(3) 题](../assets/yau-papers/2021-final-individual.pdf)

$E(u)=\int_0^1[u_x^2/2+(1-u^2)^2/(4\varepsilon^2)]dx$，自然边界，$u_t=-\delta E/\delta u$。(1) 证明能量下降；(3) 构造保持能量下降的时间半离散格式。

??? proof "答案"

    (1) $u_t=u_{xx}+\varepsilon^{-2}(u-u^3)$，光滑解直接求导、分部积分得 $E'=-\int u_t^2dx\le0$。

    (3) 取 $(v-w)/k=v_{xx}-\varepsilon^{-2}(v^3-w)$。对凸四次项及凹二次项分别用切线不等式，梯度项用平方差恒等式，可得 $E(v)-E(w)\le-\|v-w\|^2/k\le0$。

### [第 III(1)、(2) 题](../assets/yau-papers/2021-final-individual.pdf)

$a_k'=2(b_k^2-b_{k-1}^2)$、$b_k'=b_k(a_{k+1}-a_k)$，$b_0=b_n=0$。$L$ 对称三对角，对角 $a_k$、非对角 $b_k$。(1) 证明特征值不变；(2) 证明 $b_k(t)\to0$。

??? proof "答案"

    (1) 取斜对称 $B$，上对角 $b_k$、下对角 $-b_k$，直接相乘得 $L'=[B,L]$。于是 $d\operatorname{tr}(L^m)/dt=m\operatorname{tr}(L^{m-1}[B,L])=0$，由特征多项式系数与幂和的恒等式，全部特征值不变。

    (2) $\operatorname{tr}L^2$ 恒定，故 $a_k,b_k$ 一致有界，导数也有界。令 $F=\sum_{k=1}^nka_k$，则 $F'=-2\sum_{k=1}^{n-1}b_k^2$。$F$ 有界，所以 $\int_0^\infty\sum b_k^2dt<\infty$；有界导数使这非负函数一致连续。若不趋于零，就有无穷多个固定宽度的正高脉冲，积分发散，矛盾。

## 2021 · 总决赛·综合个人赛

### [第 I(1)、(2) 题](../assets/yau-papers/2021-final-overall.pdf)

正规矩阵 $A=QDQ^*$，$|\lambda_1|\ge\cdots\ge|\lambda_k|>|\lambda_{k+1}|$。向量与子空间的角由最小夹角定义。(1) 若 $P$ 为到 $W$ 的正交投影，证明余弦、正弦、正切分别为 $\|Px\|/\|x\|$、$\|x-Px\|/\|x\|$、$\|x-Px\|/\|Px\|$；(2) 对 $x_{m+1}=Ax_m$，证明到主子空间的正切每步至多缩小 $|\lambda_{k+1}/\lambda_k|$，假设初始主投影非零。

??? proof "答案"

    (1) Pythagoras 给 $\|x\|^2=\|Px\|^2+\|x-Px\|^2$。对 $W$ 内任意单位向量 $w$，$|\langle x,w\rangle|=|\langle Px,w\rangle|\le\|Px\|$，在投影方向达到等号，得到三式；$Px=0$ 时正切按无穷解释。

    (2) $\|(I-P)Ax\|\le|\lambda_{k+1}|\|(I-P)x\|$、$\|PAx\|\ge|\lambda_k|\|Px\|$，相除即得逐步界。

### [第 II(1)–(4) 题](../assets/yau-papers/2021-final-overall.pdf)

$Ax=b$，GMRES 在 $K_m=\operatorname{span}\{r_0,Ar_0,\ldots,A^{m-1}r_0\}$ 中求修正，使残差与 $AK_m$ 正交。(i) 写最小二乘问题及三角化；(ii) 讨论原卷所写残差与 $v_1,\ldots,v_{k-1}$ 的正交性；(iii) 求残差范数；(iv) 写完整算法。原卷写 $v_0=r_0,v_1=Av_0/\|Av_0\|$ 并称所得系统正交。

??? proof "答案"

    (i) 以真正正交的 Arnoldi 基 $Q_m$ 写 $AQ_m=Q_{m+1}\bar H_m$、$r_0=\beta q_1$，最小化 $\|\beta e_1-\bar H_my\|_2$，$x_m=x_0+Q_my$。用 Givens 旋转对 $\bar H_m$ 做 QR，得到上三角系统 $R_my=c_{1:m}$。

    (ii) 精确的最优条件是 $r_m\perp AK_m$。若题中的 $v_j$ 属于 $\operatorname{span}\{Ar_0,\ldots,A^{k-1}r_0\}$，则要求的正交性成立。若把它们理解成对含 $r_0$ 的整个 Krylov 空间标准正交化所得后续基，结论一般为假：取 $A=\operatorname{tridiag}(1,2,1)$、$b=e_1,x_0=0,m=2$，则 $q_2=e_2$，残差为 $(1/14,-1/7,3/14)^T$，并不与 $q_2$ 正交。原卷的 $v_1=Av_0/\|Av_0\|$ 也不能保证与 $v_0$ 正交，需区分上述两种基。

    (iii) 若旋转后的右端为 $c$，最小残差范数为 $|c_{m+1}|$。

    (iv) 计算初始残差并归一化；逐次将 $Aq_j$ 对已有列做 Gram–Schmidt，得到 Hessenberg 列；用已有和新增 Givens 旋转更新三角矩阵及右端；由 $|c_{j+1}|$ 判断终止；回代并计算 $x=x_0+Q_jy$。残差空间逐次扩大，最小残差非增。正交化提前零余量时，检查相应最小二乘；$A$ 可逆时不变 Krylov 空间已含精确修正。

## 2022 · 笔试·个人赛

### [第 1 题](../assets/yau-papers/2022-written-individual.pdf)

正权内积 $\langle f,g\rangle=\int_{-1}^1fgw$ 对应正交多项式 $p_j$。$x_0,\ldots,x_n$ 为 $p_{n+1}$ 的根。构造次数至多 $n$ 的多项式空间的一组正交单位基，使展开系数为节点函数值的固定倍数。

??? proof "答案"

    取 Lagrange 基 $\ell_i(x)=\prod_{j\ne i}(x-x_j)/(x_i-x_j)$。当 $i\ne j$，$\ell_i\ell_j$ 被 $p_{n+1}$ 整除，商次数至多 $n-1$，因此 $\langle\ell_i,\ell_j\rangle=0$。令 $R_i=\ell_i/\|\ell_i\|$，则 $f=\sum_i f(x_i)\ell_i=\sum_i[\|\ell_i\|f(x_i)]R_i$。

    根确为 $n+1$ 个互异内点：若 $p_{n+1}$ 的内点变号根不足 $n+1$ 个，将这些一次因子相乘为 $q$，则 $p_{n+1}q$ 在区间内固定符号且不恒零，其正权积分非零，与正交性矛盾。

### [第 2 题](../assets/yau-papers/2022-written-individual.pdf)

**原卷：** [2022 应用与计算数学，第 1 页](../assets/yau-papers/2022-computational-applied.pdf#page=1)。**选取：** 全题。**先修：** [向量压缩映射](04-fixed-points-contractions.md)。

$H=(f,g)^T$ 连续可微，在不动点 $p=(x_*,y_*)$ 有 $\|J_H(p)\|_\infty<1$。证明采用 $x_{r+1}=f(x_r,y_r)$、$y_{r+1}=g(x_{r+1},y_r)$ 的先后更新，从充分靠近 $p$ 的初值出发收敛到 $p$。

??? proof "答案"

    取 $q$ 严格介于 $\|J_H(p)\|_\infty$ 与 $1$ 之间。连续性保证在某个以 $p$ 为中心的闭正方形 $D$ 上，两行绝对导数和均不超过 $q$。在凸集上沿线段积分，得

    $$
    |f(x,y)-x_*|\le q\|(x,y)-p\|_\infty,
    \quad |g(x,y)-y_*|\le q\|(x,y)-p\|_\infty.
    $$

    若 $E_r=\max(|x_r-x_*|,|y_r-y_*|)$ 不超过方形半径，则 $|x_{r+1}-x_*|\le qE_r$，混合点 $(x_{r+1},y_r)$ 也在 $D$ 内。因此

    $$
    |y_{r+1}-y_*|\le q\max(|x_{r+1}-x_*|,|y_r-y_*|)\le qE_r.
    $$

    两个新分量均在 $D$，且 $E_{r+1}\le qE_r$。归纳得 $E_r\le q^rE_0\to0$。这同时证明邻域不变和局部收敛，不能将固定点处的导数条件误写成任意初值的全局收敛。

### [第 3(a)–(d) 题](../assets/yau-papers/2022-written-individual.pdf)

**原卷：** [2022 应用与计算数学，第 1 页](../assets/yau-papers/2022-computational-applied.pdf#page=1)。**选取：** (a)–(d)。**先修：** [矩阵范数与谱理论](01-matrix-norms-spectral.md)。

设实方阵 $A=(a_{ij})$ 满足

$$
a_{ii}\ge\sum_{j\ne i}|a_{ij}|+2,\qquad a_{ii}\le7.
$$

(a) 证明可逆；(b) 从定义证明无穷范数等于最大绝对行和；(c) 给出该范数的上下界；(d) 当 $A=A^T$ 时给出 $\|A\|_2$、$\|A^{-1}\|_2$ 的界。

??? proof "答案"

    **(a)** 若 $Ax=0$ 且 $x\ne0$，取 $|x_i|=\|x\|_\infty>0$。第 $i$ 行推出

    $$
    a_{ii}|x_i|\le\sum_{j\ne i}|a_{ij}|\,|x_j|
    \le(a_{ii}-2)|x_i|,
    $$

    矛盾。因此零空间为零，$A$ 可逆。

    **(b)** 对 $\|x\|_\infty=1$，逐行三角不等式给出

    $$
    \|Ax\|_\infty\le R,\qquad R=\max_i\sum_j|a_{ij}|.
    $$

    取达到最大行和的行 $i_*$，令 $x_j=\operatorname{sgn}(a_{i_*j})$；零元素对应的 $x_j$ 可取 $1$。则 $\|x\|_\infty=1$ 且 $(Ax)_{i_*}=R$，上界达到，故 $\|A\|_\infty=R$。

    **(c)** 对每一行，$a_{ii}\ge2$，且

    $$
    2\le a_{ii}+\sum_{j\ne i}|a_{ij}|
    \le2a_{ii}-2\le12.
    $$

    所以 $2\le\|A\|_\infty\le12$。下界由 $A=2I$ 达到，上界可由 $\begin{pmatrix}7&5\\5&7\end{pmatrix}$ 达到。

    **(d)** 对称性保证全部特征值实。Gershgorin 给出

    $$
    2\le a_{ii}-\sum_{j\ne i}|a_{ij}|\le\lambda
    \le a_{ii}+\sum_{j\ne i}|a_{ij}|\le12.
    $$

    因而 $A$ 正定，并且

    $$
    2\le\|A\|_2=\lambda_{\max}\le12,
    \qquad \frac1{12}\le\|A^{-1}\|_2=\frac1{\lambda_{\min}}\le\frac12.
    $$

### [第 4(a)、(b) 题](../assets/yau-papers/2022-written-individual.pdf)

假定前向 Euler 步 $U+kf(U)$ 在 $0\le k\le k_{FE}$ 时不增加给定范数。两阶段格式为 $U^{(1)}=U^n+k\beta_{10}f(U^n)$，

$$
U^{n+1}=\alpha_{20}U^n+k\beta_{20}f(U^n)+\alpha_{21}U^{(1)}+k\beta_{21}f(U^{(1)}),
$$

所有系数非负，$\alpha_{20}+\alpha_{21}=1$。(a) 给出保证范数不增的步长限制；(b) 在二阶准确条件下使允许步长最大。

??? proof "答案"

    (a) 将最后一步写成两个 Euler 步的凸组合，得到

    $$
    k\le k_* =k_{FE}\min\{1/\beta_{10},\alpha_{20}/\beta_{20},\alpha_{21}/\beta_{21}\}.
    $$

    零的 $\beta$ 对应无限制；若 $\alpha=0,\beta>0$，该支不能由此保证正步长稳定。

    (b) 二阶条件为 $\beta_{20}+\beta_{21}+\alpha_{21}\beta_{10}=1$、$\beta_{10}\beta_{21}=1/2$。令 $M=\max(\beta_{10},\beta_{20}/\alpha_{20},\beta_{21}/\alpha_{21})$，则 $1\ge1/(2\beta_{10})+1/(2M)\ge1/M$，故 $M\ge1$。最优为 $\beta_{10}=1,\beta_{20}=0,\beta_{21}=\alpha_{20}=\alpha_{21}=1/2$，$k_*=k_{FE}$，即 $U^{n+1}=(U^n+U^{(1)}+kf(U^{(1)}))/2$。

### [第 5(a)、(b) 题](../assets/yau-papers/2022-written-individual.pdf)

对 $u_t+a u_x=0$、$a>0$，先将 $u(t+k,x)$ 展开至三次时间项，以方程转换为空间导数，再用节点 $x-2h,x-h,x,x+h$ 的三次插值多项式导数替代。(a) 写出格式；(b) $h=O(k)$ 时验证归一化截断误差为 $O(k^3)$。

??? proof "答案"

    记 $\nu=ak/h$，得

    $$
    U_j^{n+1}=U_j^n-\frac\nu6(U_{j-2}^n-6U_{j-1}^n+3U_j^n+2U_{j+1}^n)
    +\frac{\nu^2}2(U_{j-1}^n-2U_j^n+U_{j+1}^n)
    -\frac{\nu^3}6(-U_{j-2}^n+3U_{j-1}^n-3U_j^n+U_{j+1}^n).
    $$

    三次插值的一、二、三阶导误差分别为 $O(h^3),O(h^2),O(h)$。一步 Taylor 余项为 $O(k^4)$，故除以 $k$ 后总误差 $O(h^3+kh^2+k^2h+k^3)=O(k^3)$。

### [第 6 题](../assets/yau-papers/2022-written-individual.pdf)

$d_1,d_2,d_3$ 为非负整数、和不超过 $6$。正投资收益为 $r_1(d)=(7d+2)10$、$r_2(d)=(3d+7)10$、$r_3(d)=(4d+5)10$，零投资收益为零。求总收益最大配置。

??? proof "答案"

    最优 $(d_1,d_2,d_3)=(4,1,1)$，按所印函数计算总值 $490$。枚举活跃投资集合：固定集合后，把每个选中项先分配一单位，再将余量全部给该集合中斜率最大者；比较七种非空集合，最优为三个均选。原卷金额单位与公式末尾的 $\times10$ 不一致，因此这里以明确给出的整数约束和收益公式计算，不另作金额换算。

## 2022 · 总决赛·个人赛

### [第 I(1)、(2) 题](../assets/yau-papers/2022-final-individual.pdf)

Allen–Cahn 方程 $u_t=u_{xx}+u(1-u^2)$，Neumann 边界。(1) 证明能量 $E=\int_0^1[u_x^2/2+(u^2-1)^2/4]dx$ 下降；(2) 证明 $(u^{n+1}-u^n)/k=u_{xx}^{n+1}-(u^{n+1})^3+u^n$ 能量稳定。

??? proof "答案"

    (1) 对光滑解直接求导并分部积分：$E'=\int(-u_{xx}+u^3-u)u_tdx=-\int u_t^2dx\le0$。原卷能量如果印成 $(u-1)^2/4$，与方程不匹配，应为 $(u^2-1)^2/4$。

    (2) 令 $v=u^{n+1},w=u^n$。凸函数 $z^4/4$ 给 $v^4/4-w^4/4\le v^3(v-w)$；$-z^2/2$ 给 $-(v^2-w^2)/2\le-w(v-w)$。梯度项给 $\varepsilon^2(\|v_x\|^2-\|w_x\|^2)/2\le\varepsilon^2\langle v_x,(v-w)_x\rangle$。相加、分部积分并代入格式，得 $E(v)-E(w)\le-\|v-w\|_2^2/k\le0$。

### [第 II(a)、(b) 题](../assets/yau-papers/2022-final-individual.pdf)

$f(x)=x^{n+1}-b^nx+ab^n$，$a,b>0,n\ge1$。(a) 证明恰有两个不同正根当且仅当 $a<nb/(n+1)^{1+1/n}$；(b) 证明 Newton 从 $a$ 收敛到小根，从 $b$ 收敛到大根。

??? proof "答案"

    (a) $f$ 在正半轴严格凸，唯一极小点 $s=b/(n+1)^{1/n}$；$f(s)=b^n[a-nb/(n+1)^{1+1/n}]$。$f(0)>0$、$f(+\infty)=+\infty$，故恰有两个正根等价于该极小值为负。

    (b) $f(a)=a^{n+1}>0$，且条件给 $a<s$，所以 $a<r_-<s$；$f(b)=ab^n>0$、$b>s$，所以 $s<r_+<b$。凸函数切线与横轴的交点使从 $a$ 出发的序列单调递增且不超过 $r_-$，从 $b$ 出发的序列单调递减且不低于 $r_+$。极限代入 Newton 式得到对应根。

### [第 III(1)(a)–(c) 题](../assets/yau-papers/2022-final-individual.pdf)

非奇异三对角 $A=L+D+U$，三个对角上的元素均非零。$B_J=-D^{-1}(L+U)$、$B_{GS}=-(L+D)^{-1}U$。(a) 求特征多项式；(b) 证明 $\det(\lambda^2L+\lambda^2D+U)=\lambda^n\det(L+\lambda D+U)$；(c) 比较谱半径与收敛速度。

??? proof "答案"

    (a) 按 $p_B(\lambda)=\det(\lambda I-B)$，$p_J=\det(D^{-1})\det(L+\lambda D+U)$、$p_{GS}=\det((L+D)^{-1})\det(\lambda L+\lambda D+U)$。原卷前因子的负号按这一特征多项式约定应删去。

    (b) $\lambda\ne0$ 时取 $S=\operatorname{diag}(1,\lambda,\ldots,\lambda^{n-1})$，$S^{-1}(\lambda^2L+\lambda^2D+U)S=\lambda(L+\lambda D+U)$，取行列式。$\lambda=0$ 由多项式连续性得到。

    (c) $p_{GS}(\lambda^2)=\lambda^np_J(\lambda)$，故 $\rho(B_{GS})=\rho(B_J)^2$。两者均收敛且 $0<\rho(B_J)<1$ 时，Gauss–Seidel 按完整一轮迭代的渐近因子更小；谱半径为零时不能断言严格更快。

## 2022 · 总决赛·综合个人赛

### [第 I(1) 题](../assets/yau-papers/2022-final-overall.pdf)

$\varepsilon^2y''+(\mu^2+\varepsilon^{-2})y=f(y)$，$y(0)=y_0$。写积分形式。

??? proof "答案"

    令 $\omega=\sqrt{\mu^2+\varepsilon^{-2}}/\varepsilon$，则 $y(t)=y_0\cos(\omega t)+(v_0/\omega)\sin(\omega t)+\int_0^t\sin(\omega(t-s))f(y(s))/(\varepsilon^2\omega)ds$。$v_0=y'(0)$ 必须另给；原卷只给 $y(0)$，不能唯一确定二阶方程的解。

### [第 II 题](../assets/yau-papers/2022-final-overall.pdf)

对 $u_t=u_{xx}+u$ 用 $v_j^{n+1}=v_j^n+kD_2v_j^n+kv_j^n$，证明在适当步长限制下最大范数稳定。

??? proof "答案"

    取 $r=k/h^2\le1/2$。更新权重为 $r,1+k-2r,r$，非负且和为 $1+k$，所以 $\|v^{n+1}\|_\infty\le(1+k)\|v^n\|_\infty$。累计到 $nk\le T$ 得 $\|v^n\|_\infty\le e^T\|v^0\|_\infty$，常数与网格无关。

## 2023 · 笔试·个人赛

### [第 1(a)–(c) 题](../assets/yau-papers/2023-written-individual.pdf)

**原卷：** [2023 应用与计算数学，第 1 页](../assets/yau-papers/2023-computational-applied.pdf#page=1)。**选取：** (a)–(c)。**先修：** [Taylor 定理](00-proof-skills-notation.md)。

令 $D_h^+f(x)=(f(x+h)-f(x))/h$、$D_h^0f(x)=(f(x+h)-f(x-h))/(2h)$。(a) 证明分别为一阶、二阶逼近；(b) 用两种步长的前向差分消去一阶误差；(c) 对 $f(x)=\sin x$、$x=0$，证明两式相同且均二阶。

??? proof "答案"

    **(a)** 对邻域内光滑的 $f$，Taylor 展开给出

    $$
    D_h^+f(x)=f'(x)+\frac h2f''(x)+\frac{h^2}{6}f'''(x)+O(h^3),
    $$

    $$
    D_h^0f(x)=f'(x)+\frac{h^2}{6}f'''(x)+O(h^4).
    $$

    故一般误差分别为 $O(h)$、$O(h^2)$；特殊函数可因主系数为零而有更高阶。

    **(b)** $2D_{h/2}^+-D_h^+$ 消去 $hf''/2$：

    $$
    R_h=\frac{-3f(x)+4f(x+h/2)-f(x+h)}h
    =f'(x)-\frac{h^2}{12}f'''(x)+O(h^3).
    $$

    这里的 Richardson 外推是消去误差项，与线性方程组的 Richardson 定常迭代是两种不同方法。

    **(c)** $D_h^+\sin(0)=D_h^0\sin(0)=\sin h/h$，而

    $$
    \frac{\sin h}{h}=1-\frac{h^2}{6}+O(h^4).
    $$

    $f'(0)=1$，主误差系数非零，所以两式在此处恰好都是二阶。

### [第 2(a)–(d) 题](../assets/yau-papers/2023-written-individual.pdf)

$\langle f,g\rangle=\int_0^1f(x)g(x)\log(1/x)dx$，$P_n$ 为首一正交多项式、$Q_n=P_n/\|P_n\|$。(a) 求 $P_1$ 及单节点 Gauss 公式；(b) 求 $P_n$ 的三项递推；(c) 求 $Q_n$ 的三项递推；(d) 写出节点等价于其特征值的四阶对称三对角矩阵。

??? proof "答案"

    (a) $\int_0^1x^j\log(1/x)dx=1/(j+1)^2$，所以 $P_1=x-1/4$，节点 $1/4$、权 $1$。

    (b) 令 $h_n=\langle P_n,P_n\rangle$、$a_n=\langle xP_n,P_n\rangle/h_n$、$b_n=h_n/h_{n-1}$，则 $P_{n+1}=(x-a_n)P_n-b_nP_{n-1}$，$P_0=1$；$n=0$ 时删去最后一项。这由 $xP_n$ 对 $P_j$（$j\le n-2$）正交得到。

    (c) $xQ_n=\sqrt{b_{n+1}}Q_{n+1}+a_nQ_n+\sqrt{b_n}Q_{n-1}$。

    (d) $J_4=\operatorname{tridiag}(\sqrt{b_1},\sqrt{b_2},\sqrt{b_3};a_0,a_1,a_2,a_3)$，其中 $a_n,b_n$ 按 (b) 的积分公式确定。递推行列式给出 $\det(xI-J_4)=P_4(x)$，所以其特征值恰为四节点 Gauss 公式的节点。具体为 $a_0=1/4,a_1=13/28,a_2=8795/18116,a_3=124351943/252694908$，$b_1=7/144,b_2=647/11025,b_3=71180289/1172105200$。

### [第 3(a)、(b) 题](../assets/yau-papers/2023-written-individual.pdf)

**原卷：** [2023 应用与计算数学，第 2 页](../assets/yau-papers/2023-computational-applied.pdf#page=2)。**选取：** (a)、(b)。**先修：** [幂法](03-linear-iterations-power.md)。

**(a)** 实方阵有互异特征值且 $|\lambda_1|>|\lambda_2|\ge\cdots$，讨论 $z_r=A^rz_0/\|A^rz_0\|_\infty$ 的主特征方向收敛。**(b)** $x_0=y_0=1$，$x_{r+1}=x_r+y_r$，$y_{r+1}=x_{r+1}+x_r$，证明 $y_r/x_r\to\sqrt2$。

??? proof "答案"

    **(a) 原卷的“任意初值”不成立。** $z_0=0$ 时分母为零；取 $A=\operatorname{diag}(2,1)$、$z_0=(0,1)^T$，归一化方向始终为第二特征向量。必须要求初值在主特征向量上的系数非零。

    在复特征向量基中写 $z_0=\sum_i c_iv_i$，要求 $c_1\ne0$。唯一严格最大的特征值对实矩阵必为实数，否则其共轭也是同模特征值。取实的 $v_1$，则

    $$
    A^rz_0=\lambda_1^r\left(c_1v_1+\sum_{i\ge2}c_i(\lambda_i/\lambda_1)^rv_i\right).
    $$

    括号中的余项趋零，主方向误差为 $O((|\lambda_2|/|\lambda_1|)^r)$。若 $\lambda_1>0$，$z_r\to\operatorname{sgn}(c_1)v_1/\|v_1\|_\infty$；若 $\lambda_1<0$，归一化向量通常逐步变号，只能断言无向直线收敛，或给出奇偶子序列的两个极限。

    **(b)** 更新矩阵为 $M=\begin{pmatrix}1&1\\2&1\end{pmatrix}$，特征值 $\lambda_\pm=1\pm\sqrt2$，特征向量 $v_\pm=(1,\pm\sqrt2)^T$。初值分解系数为

    $$
    c_+=\frac{1+1/\sqrt2}{2}>0,
    \qquad c_-=\frac{1-1/\sqrt2}{2}.
    $$

    因而

    $$
    \frac{y_r}{x_r}=\sqrt2\,
    \frac{c_+-c_-(\lambda_-/\lambda_+)^r}{c_++c_-(\lambda_-/\lambda_+)^r}
    \longrightarrow\sqrt2.
    $$

    分母非零，因为递推使 $x_r,y_r$ 始终为正；$|\lambda_-/\lambda_+|<1$ 保证极限成立。

### [第 4(a)、(b) 题](../assets/yau-papers/2023-written-individual.pdf)

$y'=f(t,y)$，使用 $y_{n+1}=y_n+\alpha hf(t_n,y_n)+\beta hf(t_n+\gamma h,y_n+\gamma hf(t_n,y_n))$。(a) 证明一致性当且仅当 $\alpha+\beta=1$，且阶数不超过 $2$；(b) 对二阶格式作用于 $y'=-\lambda y$、$\lambda>0,y_0=1$，证明有界当且仅当 $h\le2/\lambda$，并证明 $|y(t_n)-y_n|\le\lambda^3h^2t_n/6$。

??? proof "答案"

    (a) 展开得一次系数 $\alpha+\beta$、二次系数 $\beta\gamma$，二阶条件为 $\alpha+\beta=1,\beta\gamma=1/2$。在线性测试方程上放大多项式次数至多 $2$，不能匹配指数的三次项，故通用阶不超过 $2$。

    (b) 令 $s=\lambda h$，$R=1-s+s^2/2$。$R>0$ 且 $R\le1$ 当且仅当 $0\le s\le2$，所以有界范围如题。$|e^{-s}-R|\le s^3/6$，对两个 $n$ 次幂作差并逐项估计，得 $|e^{-ns}-R^n|\le ns^3/6=\lambda^3h^2t_n/6$。

### [第 5(a)–(c) 题](../assets/yau-papers/2023-written-individual.pdf)

热方程 $u_t=D u_{xx}$，零 Dirichlet 边界，显式格式 $U_j^{n+1}=(1-2r)U_j^n+rU_{j-1}^n+rU_{j+1}^n$，$r=D\Delta t/h^2$，初值取节点真值。(a) 证明一致性；(b) $r\le1/2$ 时证明最大范数稳定；(c) 证明同条件下收敛。

??? proof "答案"

    (a) 对充分光滑的精确解，Taylor 余项给出归一化截断误差 $O(\Delta t+h^2)$。

    (b) $0\le r\le1/2$ 时更新是非负权重的凸组合，行和至多 $1$，故 $\|U^{n+1}\|_\infty\le\|U^n\|_\infty$。

    (c) 误差满足 $e^{n+1}=Be^n+\Delta t\tau^n$，$e^0=0$，因此在 $t_n\le T$ 上 $\|e^n\|_\infty\le T\max_j\|\tau^j\|_\infty\le CT(\Delta t+h^2)\to0$。此 Taylor 误差率要求解的相应导数在所考虑闭时间区间有界。

### [第 6(a)、(b) 题](../assets/yau-papers/2023-written-individual.pdf)

$i\varepsilon\psi_t=-\varepsilon^2\Delta\psi/2+V(x)\psi$，取 $\psi=Ae^{iS/\varepsilon}$，$A,S$ 为实函数。(a) 推导主阶振幅与相位方程；(b) 令 $u=\nabla S$，推导 $u$ 的方程，并判断光滑初值是否保证全时间光滑解。

??? proof "答案"

    代入并按实、虚部整理：$S_t+|\nabla S|^2/2+V=\varepsilon^2\Delta A/(2A)$（$A\ne0$），$A_t+\nabla S\cdot\nabla A+A\Delta S/2=0$。主阶舍去前式的 $O(\varepsilon^2)$ 项，得到 Hamilton–Jacobi 方程；对 $x$ 求导得 $u_t+(u\cdot\nabla)u=-\nabla V$。

    不能保证全时间光滑。$u(x,t)=-x/(1-t)$ 对 $t<1$ 直接满足该方程，初值 $u(x,0)=-x$ 光滑，而 $u_x=-1/(1-t)$ 在 $t\uparrow1$ 发散。

## 2023 · 总决赛·个人赛

### [第 1(a)、(b) 题](../assets/yau-papers/2023-final-individual.pdf)

$U\in\mathbb R^{n\times n}$ 正交且 $\det U=1$。(a) 证明可写成有限个 Givens 旋转的乘积；(b) 给出计算算法。

??? proof "答案"

    逐列用两坐标旋转，从下往上消去当前对角以下的元素，选 $c=a/\sqrt{a^2+b^2},s=b/\sqrt{a^2+b^2}$ 使当前二元向量变为 $(\sqrt{a^2+b^2},0)$；二元向量为零时跳过。得到的上三角正交矩阵为对角 $\pm1$。其负号数为偶数，用每对负号坐标上的 $\pi$ 旋转改为 $I$。记录全部旋转，倒序取逆即得 $U$ 的分解；至多 $n(n-1)/2$ 次消元旋转再加有限次符号旋转。

### [第 2(a)–(c) 题](../assets/yau-papers/2023-final-individual.pdf)

正规矩阵 $A=QDQ^*$，$Q$ 酉，$|\lambda_1|\ge\cdots\ge|\lambda_k|>|\lambda_{k+1}|\ge\cdots$。令 $P=Q\operatorname{diag}(I_k,0)Q^*$，$X^{(m+1)}=AX^{(m)}$，且 $PX^{(0)}$ 满列秩。

(c) 证明 $P$ 是前 $k$ 个特征向量空间的正交投影；(c) 找到 $\Lambda$，使任意非零 $y$ 满足

$$
\frac{\|(AX^{(m)}-X^{(m)}\Lambda)y\|}{\|PX^{(m)}y\|}
\le\left|\frac{\lambda_{k+1}}{\lambda_k}\right|^m
\frac{\|(AX^{(0)}-X^{(0)}\Lambda)y\|}{\|PX^{(0)}y\|}.
$$

另证 (a) $PX^{(m)}$ 的列独立；(b) $X^{(m)}$ 的列独立。

??? proof "答案"

    (a) 在主特征坐标写 $PX^{(m)}=Q_1D_1^mC$，$C=Q_1^*X^{(0)}$ 可逆、$D_1$ 可逆，所以列独立。(b) 若 $X^{(m)}y=0$，投影给 $PX^{(m)}y=0$，故 $y=0$。

    (c) (1) $P^*=P,P^2=P$，像空间恰为前 $k$ 列的张成空间。

    (2) 写 $Q=[Q_1,Q_2]$、$D=\operatorname{diag}(D_1,D_2)$，$C=Q_1^*X^{(0)}$ 可逆，取 $\Lambda=C^{-1}D_1C$。$R_0=AX^{(0)}-X^{(0)}\Lambda$ 满足 $PR_0=0$。故 $R_m=A^mR_0$，$\|R_my\|\le|\lambda_{k+1}|^m\|R_0y\|$；另一方面 $\|PX^{(m)}y\|=\|D_1^mCy\|\ge|\lambda_k|^m\|Cy\|$。相除即得。

### [第 3(a)、(b) 题](../assets/yau-papers/2023-final-individual.pdf)

多速率 Euler：$x_{j+1/2}=x_j+(k/2)f(x_j,y_j)$、$x_{j+1}=x_{j+1/2}+(k/2)f(x_{j+1/2},y_j)$、$y_{j+1}=y_j+kg(x_j,y_j)$。(a) 求局部误差阶；(b) 对 $x'=-x+y,y'=-y$，求对任意初值趋零的步长范围。

??? proof "答案"

    (a) 光滑条件下，两分量一步都与精确解差 $O(k^2)$。这是“局部误差二阶”，整体仅一阶，不能把它说成全局二阶方法。

    (b) 更新矩阵为 $\begin{pmatrix}(1-k/2)^2&k(1-k/4)\\0&1-k\end{pmatrix}$。两特征值模都严格小于 $1$ 等价于 $0<k<2$，这正是任意初值趋零的范围；端点有单位模根。

### [第 4(a)、(b) 题](../assets/yau-papers/2023-final-individual.pdf)

$u_t+au_x=0$、$a>0$，格式 $v_j^{n+1}=(v_{j-1}^n+v_{j+1}^n)/2+(ak/(12h))(v_{j+2}^n-8v_{j+1}^n+8v_{j-1}^n-v_{j-2}^n)$。(a) 求依赖域 CFL 条件；(b) 求放大因子及稳定条件。

??? proof "答案"

    (a) 每步最远依赖距离为 $2h$，故必要 CFL 为 $ak/h\le2$。

    (b) 令 $\nu=ak/h$，$g(\theta)=\cos\theta-i(\nu/3)\sin\theta(4-\cos\theta)$。$|g|\le1$ 等价于 $\nu^2(4-\cos\theta)^2\le9$ 对所有非零 $\sin\theta$ 成立，故 $0\le\nu\le3/5$。这比依赖域条件严格。

## 2023 · 总决赛·团体赛

### [第 1(i)、(ii) 题](../assets/yau-papers/2023-final-team.pdf)

实三对角矩阵 $A$ 用部分选主元 LU。(i) 若 $a_* =\max|a_{ij}|$，证明 $|u_{ii}|\le2a_*$、$|u_{ij}|\le a_*$（$j>i$），增长因子至多 $2$；(ii) 若列对角占优，证明不需实际交换主元。

??? proof "答案"

    (i) 每步只需比较当前对角 $p$ 和其下方 $\beta$。未交换时 $|\beta/p|\le1$，新主元为 $a-(\beta/p)q$，模至多 $2a_*$；上方超对角保持原值。交换时乘子 $p/\beta$ 模至多 $1$，新主元 $q-(p/\beta)a$ 同样至多 $2a_*$；新第一、第二超对角为原来 $a,\gamma$ 或 $-(p/\beta)\gamma$，模均至多 $a_*$。归纳得到各界。

    (ii) 用列占优归纳：当前列有 $|p|\ge|\beta|$，故选当前主元；消元后 $p_{\rm new}=a-\beta q/p$，其模至少 $|a|-|q|\ge|\beta_{\rm next}|$，因为该列原来满足 $|a|\ge|q|+|\beta_{\rm next}|$。因此每步无需交换，平局取当前行。若出现零主元，则下方也为零；完整非奇异 LU 结论需要矩阵非奇异，否则应停止或跳过零列，原卷未明示这一条件。

### [第 2(ii) 题](../assets/yau-papers/2023-final-team.pdf)

$f\in C^2(\mathbb R^n)$，定义 $\xi=xe^{-\lambda f(x)}$、$g(\xi)=[1-e^{-\lambda f(x)}]/\lambda$。计算变换 Jacobian 并证明 $\nabla_\xi g=\nabla f(x)/[1-\lambda x\cdot\nabla f(x)]$。

??? proof "答案"

    $D_x\xi=e^{-\lambda f}(I-\lambda x\nabla f^T)$，$\nabla_xg=e^{-\lambda f}\nabla f$。在 $1-\lambda x\cdot\nabla f\ne0$ 的局部可逆处，用链式法则及秩一逆公式，$(D_x\xi)^{-T}\nabla_xg=\nabla f/(1-\lambda x\cdot\nabla f)$。$\lambda=0$ 按连续极限解释。

### [第 3(ii) 题](../assets/yau-papers/2023-final-team.pdf)

$F:\widehat K\to K$，$F(\widehat x)=B\widehat x+b$，$B$ 可逆。$h_K,h_{\widehat K}$ 为直径，$\rho_K,\rho_{\widehat K}$ 为最大内接球的直径。证明 $\|B\|_2\le h_K/\rho_{\widehat K}$、$\|B^{-1}\|_2\le h_{\widehat K}/\rho_K$。

??? proof "答案"

    取单位向量 $v$，在 $\widehat K$ 内半径任意接近 $\rho_{\widehat K}/2$ 的内接球中选两个相对点，其差任意接近 $\rho_{\widehat K}v$。像点都在 $K$ 中，距离至多 $h_K$，故 $\rho_{\widehat K}\|Bv\|\le h_K$；取单位向量上确界。对逆仿射映射重复得到第二式。

## 2024 · 笔试·个人赛

### [第 1(a)、(b) 题](../assets/yau-papers/2024-written-individual.pdf)

**原卷：** [2024 应用与计算数学，第 1 页](../assets/yau-papers/2024-computational-applied.pdf#page=1)。**选取：** (a)、(b)。**先修：** [可逆性与矩阵运算](01-matrix-norms-spectral.md)。

设 $A$ 可逆，$\widehat A=A+uv^T$。(a) 求 $\widehat A$ 可逆的充要条件；(b) 假定用 $A$ 求解线性方程一次只需 $O(n)$ 次浮点运算，设计 $\widehat Ax=b$ 的 $O(n)$ 算法。

??? proof "答案"

    **(a)** 令 $p=A^{-1}u$，则 $\widehat A=A(I+pv^T)$。记 $d=1+v^Tp$。若 $d=0$，$p\ne0$ 且 $(I+pv^T)p=0$，因此不可逆。若 $d\ne0$，直接相乘验证

    $$
    (I+pv^T)^{-1}=I-\frac{pv^T}{d}.
    $$

    所以充要条件为 $1+v^TA^{-1}u\ne0$，并得 Sherman–Morrison 公式

    $$
    \widehat A^{-1}=A^{-1}-\frac{A^{-1}uv^TA^{-1}}{1+v^TA^{-1}u}.
    $$

    **(b)** 分别解 $Az=b$ 与 $Ap=u$；算 $d=1+v^Tp$ 与 $s=v^Tz$；返回

    $$
    x=z-p\frac{s}{d}.
    $$

    两次求解各为 $O(n)$，点积与向量更新也为 $O(n)$，总成本仍为 $O(n)$，且不必显式形成 $A^{-1}$。代回得到 $\widehat Ax=b$。这里将原题的 $O(n)$ 求解假定理解为 $A$ 对所需右端均有该成本；若只能解一个指定右端 $b$，无法据此保证求解 $Ap=u$ 的成本。$d\ne0$ 保证代数上可解，$d$ 很小时仍可能数值不稳定。

### [第 2(a)、(b) 题](../assets/yau-papers/2024-written-individual.pdf)

$f$ 连续、$f'(0)\ne0$，$f(x)=O(x^{-1-\alpha})$、$\alpha>0$。以 $n$ 个等长子区间的复合梯形公式近似 $\int_0^Lf(x)dx$。(a) 固定 $L$ 时求渐近误差；(b) 将其用于 $\int_0^\infty f(x)dx$ 时，如何选 $L(n)$ 优化总误差？

??? proof "答案"

    (a) 若有足够光滑性，$T_h-\int_0^Lf=h^2[f'(L)-f'(0)]/12+o(h^2)$，$h=L/n$。原卷只假设连续及 $f'(0)$ 存在，不能保证这个二阶渐近式；需补充区间上的相应光滑性。

    (b) 若另有 $f'(L)\to0$ 及对变化区间一致的梯形误差控制，尾部为 $O(L^{-\alpha})$，离散误差主项为 $O(L^2/n^2)$。平衡取 $L\asymp n^{2/(\alpha+2)}$，总误差 $O(n^{-2\alpha/(\alpha+2)})$。仅凭原卷的连续性和尾部衰减，不能无条件断言这一优化速率。

### [第 3(a)–(c) 题](../assets/yau-papers/2024-written-individual.pdf)

令 $T_n(\cos\theta)=\cos n\theta$，$U_n(\cos\theta)=\sin((n+1)\theta)/\sin\theta$。(a) 求导数关系及 $U_n$ 递推；(b) 证明权 $\sqrt{1-x^2}$ 下正交；(c) 求两节点最高精度 Gauss 公式。

??? proof "答案"

    (a) $T_{n+1}'=(n+1)U_n$，$U_0=1,U_1=2x,U_{n+1}=2xU_n-U_{n-1}$。若原卷写成 $T_n'=(n+1)U_n$，其下标应为 $n+1$。

    (b) 代入 $x=\cos\theta$ 得 $\int_{-1}^1U_mU_n\sqrt{1-x^2}dx=\int_0^\pi\sin((m+1)\theta)\sin((n+1)\theta)d\theta=(\pi/2)\delta_{mn}$。

    (c) 节点为 $U_2=4x^2-1$ 的根 $\pm1/2$，权重均为 $\pi/4$，精确到三次。四次不精确：积分为 $\pi/16$，公式为 $\pi/32$。

### [第 4(a)、(b) 题](../assets/yau-papers/2024-written-individual.pdf)

$-(a(x)u')'=f$，$u(0)=u(1)=0$，$a(x)>\delta\ge0$，只能调用 $a(x)$，不能调用其导数。均匀网格 $x_i=ih$。(a) 给出二阶三对角离散系统；(b) 给出保证包含全部特征值的复平面圆盘。

??? proof "答案"

    (a) 令 $a_{i+1/2}=a(x_i+h/2)$。非零矩阵元为 $A_{ii}=(a_{i-1/2}+a_{i+1/2})/h^2$、$A_{i,i\pm1}=-a_{i\pm1/2}/h^2$，右端为 $f(x_i)$，边界值为零。对足够光滑的 $a,u$，用中点通量的 Taylor 展开得二阶；仅有原卷的一阶可微假设时，不能保证这一二阶误差率。

    (b) 设 $a_{\min}=\min_i a_{i+1/2}>0$、$a_{\max}=\max_i a_{i+1/2}$，$n=1/h$。矩阵对称正定，二次型为 $h^{-2}\sum_i a_{i+1/2}(z_{i+1}-z_i)^2$，故

    $$
    L=\frac{4a_{\min}}{h^2}\sin^2\frac\pi{2n}\le\lambda(A)\le U=\frac{4a_{\max}}{h^2}.
    $$

    可取圆盘 $|z-(L+U)/2|\le(U-L)/2$。若用实际极端特征值替代 $L,U$，则给出覆盖此实谱的最小圆盘。

### [第 5(b) 题](../assets/yau-papers/2024-written-individual.pdf)

对 $u_t=u_{xxx}$，原卷格式 $[v^{n+1}-v^{n-1}]/(2k)=[-v_{j-2}/2+v_{j-1}-v_{j+1}+v_{j+2}/2]/h$。求稳定条件。

??? proof "答案"

    按所印分母 $h$，空间模式特征值为 $i[\sin(2\theta)-2\sin\theta]/h$，其最大绝对值 $3\sqrt3/(2h)$。leapfrog 根条件要求严格 $|k\lambda_\theta|<1$，所以统一限制 $k/h<2/(3\sqrt3)$，端点重根不能对一般起始扰动保证稳定。

    原卷分母若要逼近三阶导数，应为 $h^3$；修正后相应限制为 $k/h^3<2/(3\sqrt3)$。所印 $h$ 的格式对目标 PDE 不一致。

### [第 6(a)–(d) 题](../assets/yau-papers/2024-written-individual.pdf)

周期热方程 $u_t=\mu u_{xx}$，$\mu>0$。前向 Euler 为 $v^{n+1}=v^n+\mu kD_2v^n$，原卷另一式为 $v^{n+1}=v^n+\mu k(D_2v^n+D_2v^{n+1})$。(a) 求 $D_2$ 准确阶；(b) 求两格式各 Fourier 系数的更新（含零频）；(c) 偶数网格、$v_j^0=(-1)^j$ 时求两格式的数值解；(d) 求各自稳定限制。

??? proof "答案"

    (a) 二阶：$D_2u=u_{xx}+h^2u_{xxxx}/12+O(h^4)$。

    (b) $\lambda_\ell=-4h^{-2}\sin^2(\pi\ell/N)$，因子分别为 $1+\mu k\lambda_\ell$、$(1+\mu k\lambda_\ell)/(1-\mu k\lambda_\ell)$；零频均为 $1$。

    (c) 分别为 $(1-4\mu k/h^2)^n(-1)^j$、$[(1-4\mu k/h^2)/(1+4\mu k/h^2)]^n(-1)^j$。

    (d) 前者要求 $k\le h^2/(2\mu)$，后者任意 $k>0$ 都稳定。原卷后一式缺少通常 Crank–Nicolson 的 $1/2$，虽稳定却逼近 $u_t=2\mu u_{xx}$；补上两个 $1/2$ 后，才是时间二阶且无条件稳定的 Crank–Nicolson。

## 2024 · 总决赛·个人赛

### [第 1 题](../assets/yau-papers/2024-final-individual.pdf)

$S,T$ 为上三角矩阵，$ST-\lambda I$ 非奇异。设计 $O(n^2)$ 算法解 $(ST-\lambda I)x=b$。

??? proof "答案"

    从末行向上回代，并同时维护 $w=Tx$。已知下方 $x_j,w_j$ 后，取 $x_i=[b_i-S_{ii}\sum_{j>i}T_{ij}x_j-\sum_{j>i}S_{ij}w_j]/(S_{ii}T_{ii}-\lambda)$，再取 $w_i=T_{ii}x_i+\sum_{j>i}T_{ij}x_j$。分母非零由非奇异上三角矩阵的对角决定；每行 $O(n-i)$，总 $O(n^2)$，不必显式形成 $ST$。

### [第 2 题](../assets/yau-papers/2024-final-individual.pdf)

非负序列 $d^n,g^n,h^n$ 满足 $(d^{n+1}-d^n)/k\le g^nd^n+h^n$。任意长度 $N+1$ 的滑动窗口有 $k\sum g^n\le a_1,k\sum h^n\le a_2,k\sum d^n\le a_3$，$Nk=r$。证明 $d^n\le(a_2+a_3/r)e^{a_1}$，$n\ge n_0+N$。

??? proof "答案"

    在 $n-N,\ldots,n-1$ 中选 $j$ 使 $d^j\le a_3/(Nk)=a_3/r$。逐步迭代 $d^{i+1}\le(1+kg^i)d^i+kh^i$，使用 $\prod(1+kg^i)\le e^{k\sum g^i}\le e^{a_1}$，得 $d^n\le(d^j+k\sum_{i=j}^{n-1}h^i)e^{a_1}\le(a_3/r+a_2)e^{a_1}$。

### [第 4(a)、(b) 题](../assets/yau-papers/2024-final-individual.pdf)

$u_t=\beta u_{xx}+f(u)$，齐次 Neumann 边界，$f\in C^2,f(0)=0,|f'|\le K$。构造显式中心差分并证明最大范数稳定及收敛。

??? proof "答案"

    内点取 $v_j^{n+1}=rv_{j-1}^n+(1-2r)v_j^n+rv_{j+1}^n+kf(v_j^n)$，$r=\beta k/h^2\le1/2$；边界用反射虚点保持 Neumann 条件。$|f(v)|\le K|v|$，故 $\|v^{n+1}\|_\infty\le(1+kK)\|v^n\|_\infty$，累计至多 $e^{KT}$。对两个输入也有相同 Lipschitz 界。将光滑精确解代入，截断误差 $O(k+h^2)$，误差递推给 $\|e^n\|_\infty\le e^{KT}(\|e^0\|_\infty+CT(k+h^2))$。边界达到该阶还需足够的光滑性及边界相容性。

## 2024 · 总决赛·综合个人赛

### [第 1(a)、(b) 题](../assets/yau-papers/2024-final-overall.pdf)

$C_s=\{\eta:\exists S,|S|\le s,\|\eta_S\|_1\ge\|\eta_{S^c}\|_1\}$。(a) 证明每个 $s$ 稀疏 $x_0$ 是 $\min\|x\|_1$、$Ax=Ax_0$ 的唯一解，当且仅当 $\ker A\cap C_s=\{0\}$；(b) 定义 $\|x\|_{(s)}=\inf\sum_i\|x_i\|_2$，和式分解中的每个 $x_i$ 均 $s$ 稀疏。证明 $\eta\in C_s,\|\eta\|_2\le1$ 时 $\|\eta\|_{(s)}\le C$，$C$ 普适。

??? proof "答案"

    (a) 对可行扰动 $\eta\in\ker A\setminus\{0\}$、$S=\operatorname{supp}x_0$，有 $\|x_0+\eta\|_1\ge\|x_0\|_1-\|\eta_S\|_1+\|\eta_{S^c}\|_1>\|x_0\|_1$。反向若某个 $\eta\ne0$ 属于交集，取 $x_0=-\eta_S$，则 $x_0+\eta=\eta_{S^c}$ 的 $1$ 范数不更大，破坏唯一性。

    (b) 按绝对值递减分成每组 $s$ 个坐标的块 $T_1,T_2,\ldots$。后续块满足 $\sum_{j\ge2}\|\eta_{T_j}\|_2\le\|\eta\|_1/\sqrt s$。又 $\eta\in C_s$ 给 $\|\eta\|_1\le2\|\eta_S\|_1\le2\sqrt s\|\eta\|_2$，故 $\|\eta\|_{(s)}\le\|\eta_{T_1}\|_2+\|\eta\|_1/\sqrt s\le3$，可取 $C=3$（$s\ge1$）。

### [第 2(a)、(b) 题](../assets/yau-papers/2024-final-overall.pdf)

每步时间 $\tau$，(a) 一维粒子等概率向左、右各走 $h$；(b) 二维粒子向四方向各以概率 $p\le1/4$ 走 $h$，其余概率不动。$h^2/\tau\to d$，推导密度的极限方程。

??? proof "答案"

    (a) 概率守恒更新 $q(x,t+\tau)=[q(x-h,t)+q(x+h,t)]/2$，光滑 Taylor 展开并除以 $\tau$，得到 $q_t=(d/2)q_{xx}$。

    (b) 更新为 $q(t+\tau)=(1-4p)q+p[q(x\pm h,y)+q(x,y\pm h)]$，同样得到 $q_t=pd(q_{xx}+q_{yy})$。这是对光滑密度的形式极限推导。

## 2024 · 总决赛·团体赛

### [第 1 题](../assets/yau-papers/2024-final-team.pdf)

$\phi:(0,\infty)\to(0,\infty)$ 连续递增，$M>0$，$0<T_*<\int_M^\infty dz/\phi(z)$。非负量满足 $z_n+k\sum_{j<n}w_j\le y_n=M+k\sum_{j<n}\phi(z_j)$，$nk\le T_*$。证明 $y_n\le C_*$ 与 $k$ 无关。

??? proof "答案"

    $z_n\le y_n$，$y_{n+1}-y_n=k\phi(z_n)\le k\phi(y_n)$。递增性给 $\int_{y_n}^{y_{n+1}}dz/\phi(z)\le(y_{n+1}-y_n)/\phi(y_n)\le k$。累加得 $\int_M^{y_n}dz/\phi(z)\le nk\le T_*$。取唯一 $C_*$ 满足 $\int_M^{C_*}dz/\phi(z)=T_*$，便有 $y_n\le C_*$；同时 $k\sum_{j<n}w_j\le C_*$。

### [第 2(a-i)、(b) 题](../assets/yau-papers/2024-final-team.pdf)

周期平流半离散 $v_t+Dv=0$，$D_-,D_+,D_0$ 为后向、前向、中心差分。(a-i) 哪一种不稳定？(b) 对时间格式 $(v^{n+1}-v^n)/k+D[(v^{n+1}+v^n)/2]=0$，证明 $D_0$ 保持离散 $2$ 范数、$D_-$ 使其不增。

??? proof "答案"

    (a-i) 前向差分 $D_+$ 不稳定，模式的特征值实部为 $(\cos\theta-1)/h\le0$，所以 $-D_+$ 对非零模式产生指数增长。

    (b) 令 $w=(v^{n+1}+v^n)/2$，与 $w$ 作离散内积：$[\|v^{n+1}\|_h^2-\|v^n\|_h^2]/(2k)=-\langle Dw,w\rangle_h$。周期移位给 $D_0$ 斜对称，内积为零；$D_-=D_0-(h/2)D_+D_-$，且 $\langle-D_+D_-w,w\rangle=\|D_-w\|^2$，故右侧非正。原卷将这一时间公式称为 forward Euler，实际是梯形/隐式中点公式。

## 2025 · 笔试·个人赛

### [第 1 题](../assets/yau-papers/2025-written-individual.pdf)

**原卷：** [2025 应用与计算数学，第 1 页](../assets/yau-papers/2025-computational-applied.pdf#page=1)。**选取：** 全题。**先修：** [Newton 法与收敛阶](05-newton-convergence.md)。

对简单根 $\xi$，研究

$$
x_{r+1}=x_r-\alpha\frac{f(x_r)}{f'\!\left(x_r-\beta f(x_r)/f'(x_r)\right)}.
$$

选择常数 $\alpha,\beta$，使方法对一般光滑函数达到最高的局部收敛阶。

??? proof "答案"

    设 $f$ 在 $\xi$ 附近 $C^4$，$f'(\xi)\ne0$。记 $e=x-\xi$，$c_2=f''(\xi)/(2f'(\xi))$、$c_3=f'''(\xi)/(6f'(\xi))$。归一化 Taylor 展开为

    $$
    \frac{f(x)}{f'(\xi)}=e+c_2e^2+c_3e^3+O(e^4),
    \quad\frac{f(x)}{f'(x)}=e-c_2e^2+(2c_2^2-2c_3)e^3+O(e^4).
    $$

    内部点 $y=x-\beta f(x)/f'(x)$ 满足 $y-\xi=(1-\beta)e+\beta c_2e^2+O(e^3)$，因此

    $$
    \frac{f'(y)}{f'(\xi)}=1+2c_2(1-\beta)e+
    \left(2\beta c_2^2+3c_3(1-\beta)^2\right)e^2+O(e^3).
    $$

    相除后，误差的一阶、二阶系数为

    $$
    e_{r+1}=(1-\alpha)e-\alpha(2\beta-1)c_2e^2+O(e^3).
    $$

    为对一般函数消去一阶项，必须 $\alpha=1$；再消去二阶项，必须 $\beta=1/2$。代回三阶项，得到

    $$
    \boxed{\alpha=1,\quad\beta=\frac12},
    \qquad e_{r+1}=\left(c_2^2-\frac14c_3\right)e_r^3+O(e_r^4).
    $$

    该参数选择至少局部三阶；若三阶系数非零，恰为三阶。充分小邻域内 $f'(x)$、$f'(y)$ 都非零，且 $|e_{r+1}|\le C|e_r|^3$，取 $C|e_0|^2<1$ 保证局部收敛。

    三阶系数不可能对所有 $f$ 恒为零：取 $f(x)=(x-\xi)+(x-\xi)^2$，有 $c_2=1,c_3=0$。因此此二参数族的通用最高阶为 $3$，特定函数可能偶然更高阶，不能由此声称通用四阶。

### [第 2 题](../assets/yau-papers/2025-written-individual.pdf)

**原卷：** [2025 应用与计算数学，第 1 页](../assets/yau-papers/2025-computational-applied.pdf#page=1)。**选取：** 全题。**先修：** [谱理论](01-matrix-norms-spectral.md)。

$A$ 为 $8\times8$ 矩阵，主对角元全为零，上、下第一副对角元全为 $1$，其余为零。求 $\rho(A^{-1})$。

??? proof "答案"

    对 $j=1,\ldots,8$，令 $\theta_j=j\pi/9$，构造向量 $v^{(j)}$，其第 $r$ 分量为 $\sin(r\theta_j)$。设虚拟端点 $v_0=v_9=0$，则

    $$
    (Av^{(j)})_r=\sin((r-1)\theta_j)+\sin((r+1)\theta_j)
    =2\cos\theta_j\sin(r\theta_j).
    $$

    于是八个互异特征值为 $\lambda_j=2\cos(j\pi/9)$。它们均非零，故 $A$ 可逆。逆矩阵的特征值为 $1/\lambda_j$，所以

    $$
    \rho(A^{-1})=\frac1{\min_j|\lambda_j|}
    =\frac1{2\cos(4\pi/9)}
    =\frac1{2\sin(\pi/18)}\approx2.879385242.
    $$

    最小绝对值在 $j=4,5$ 达到。这里不能把 $\rho(A^{-1})$ 写成 $1/\rho(A)$。

### [第 3(a)、(b) 题](../assets/yau-papers/2025-written-individual.pdf)

$P_k$ 为 $k$ 次 Legendre 多项式，$P_k^1(x)=-(1-x^2)^{1/2}P_k'(x)$。(a) 对互异 $x_i\in(-1,1)$，证明 $\sum_{k=1}^N a_kP_k^1(x_i)=y_i$ 的系数矩阵非奇异；(b) 对 $\min_a\|f-\sum_{k=1}^N a_kP_k^1\|_{L^2[-1,1]}^2$，给出线性系统并证明非奇异。

??? proof "答案"

    (a) $P_k'$ 的次数为 $k-1$，首项非零，故它们构成次数至多 $N-1$ 的一组基。若插值齐次方程成立，去掉非零因子 $\sqrt{1-x_i^2}$ 后，一个次数至多 $N-1$ 的多项式有 $N$ 个不同根，只能为零；各系数因此为零。

    (b) 正规方程 $Ma=b$，其中 $M_{jk}=\int_{-1}^1P_j^1P_k^1\,dx$、$b_j=\int_{-1}^1 fP_j^1\,dx$。对 $c\ne0$，$c^TMc=\|\sum c_kP_k^1\|_{L^2}^2>0$，因为这些连续函数线性无关。因此 Gram 矩阵正定。

### [第 3(c) 题](../assets/yau-papers/2025-written-individual.pdf)

$P_k^1(x)=-\sqrt{1-x^2}P_k'(x)$，$P_k$ 为 Legendre 多项式。对于关于零对称的节点和权重构成的矩阵 $M_{jk}=\sum_iw_iP_j^1(x_i)P_k^1(x_i)$，证明 $j+k$ 为奇数时 $M_{jk}=0$。

??? proof "答案"

    Legendre 的首一正交多项式唯一性及对称权给出 $P_k(-x)=(-1)^kP_k(x)$，故 $P_k^1(-x)=(-1)^{k+1}P_k^1(x)$。乘积的奇偶性为 $(-1)^{j+k}$；奇数时，对称节点的贡献两两抵消，零节点的贡献也为零。

### [第 4 题](../assets/yau-papers/2025-written-individual.pdf)

**原卷：** [2025 应用与计算数学，第 2 页](../assets/yau-papers/2025-computational-applied.pdf#page=2)。**选取：** 全题。**先修：** [投影与 SVD](02-svd-least-squares.md)、[低秩逼近](02-pseudoinverse-low-rank.md)。

给定 $y_1,\ldots,y_n\in\mathbb R^m$，令 $V=\operatorname{span}\{y_j\}$。对给定 $1\le\ell\le\dim V$，寻找 $\ell$ 个正交单位向量 $\psi_i$，使

$$
J=\sum_{j=1}^n\left\|y_j-\sum_{i=1}^\ell(y_j^T\psi_i)\psi_i\right\|_2^2
$$

最小。（$\ell=0$ 的空子空间情形显然，误差为 $\sum_j\|y_j\|_2^2$。）

??? proof "答案"

    写 $Y=[y_1,\ldots,y_n]$、$\Psi=[\psi_1,\ldots,\psi_\ell]$、$P=\Psi\Psi^T$。目标为

    $$
    J=\|(I-P)Y\|_F^2=\|Y\|_F^2-\operatorname{tr}(PYY^T).
    $$

    由 2012 第 4 题中已经证明的投影迹上界，$\operatorname{tr}(PYY^T)\le\sum_{i=1}^\ell\sigma_i(Y)^2$。对 $Y=U\Sigma V^T$ 取 $\psi_i=u_i$，即可达到上界。故

    $$
    J_{\min}=\sum_{i>\ell}\sigma_i(Y)^2.
    $$

    等价地，求 $YY^T$ 的前 $\ell$ 个特征向量。由于 $\ell\le\operatorname{rank}(Y)$，这些向量属于样本张成空间。若边界奇异值相等，最优子空间可能不唯一。原题拟合的是通过原点的线性子空间，没有中心变量，因此这里不应自行对样本减均值。

### [第 5(a)、(b) 题](../assets/yau-papers/2025-written-individual.pdf)

$u_t=u_{xx}-u$，以 $\theta$ 方法 $[v^{n+1}-v^n]/k=(D_2-I)[\theta v^{n+1}+(1-\theta)v^n]$ 离散，$0\le\theta\le1$。(a) 求保证最大范数稳定的条件；(b) 求 $\ell^2$ 稳定条件。

??? proof "答案"

    (a) 若 $(1-\theta)k\le h^2/(2+h^2)$，右侧显式矩阵的各权重非负、行和 $1-(1-\theta)k$；隐式矩阵的逆最大范数至多 $1/(1+\theta k)$。所以每步范数因子至多 $[1-(1-\theta)k]/[1+\theta k]\le1$。

    (b) 对 $D_2-I$ 的特征值 $-s$，$1\le s\le1+4/h^2$，因子 $(1-(1-\theta)ks)/(1+\theta ks)$。$\theta\ge1/2$ 时无条件稳定；$\theta<1/2$ 时需 $(1-2\theta)k\le2h^2/(h^2+4)$。无限网格的同一界也可通过展开平方和获得。

### [第 6(a)–(d) 题](../assets/yau-papers/2025-written-individual.pdf)

$y' =Ay$，$A=\begin{pmatrix}-1000&999\\0&-1\end{pmatrix}$，$y(0)=(2,1)^T$。(a) 求精确解；(b) 求显式 Euler 的绝对稳定域，并证明 $h>0.002$ 时发散；(c) 证明隐式 Euler 对任意 $h>0$ 稳定；(d) 分析梯形格式稳定性。

??? proof "答案"

    (a) $y(t)=(e^{-1000t}+e^{-t},e^{-t})^T$，可直接代回验证。

    (b) 稳定域 $|1+z|\le1$。迭代解为 $y_n=((1-1000h)^n+(1-h)^n,(1-h)^n)^T$。$h>0.002$ 时第一特征方向因子绝对值大于 $1$，且初值在该方向系数非零，因而发散。端点 $h=0.002$ 有振荡但不衰减。

    (c) 隐式 Euler 的两个因子为 $(1+1000h)^{-1},(1+h)^{-1}$，都在 $(0,1)$，所以任意 $h>0$ 均收敛到零。

    (d) 梯形格式因子为 $R(z)=(1+z/2)/(1-z/2)$，负实 $z$ 上绝对值小于 $1$，任意 $h>0$ 稳定；但刚性方向在大步长下因子接近 $-1$，阻尼较差。

## 2025 · 总决赛·个人赛

### [第 2(a) 题](../assets/yau-papers/2025-final-individual.pdf)

$u_t+a(x)u_x+a'(x)u=0$，周期边界。写成守恒形式并解释守恒含义。

??? proof "答案"

    $u_t+(a(x)u)_x=0$。对整个周期积分，边界通量相同而抵消，所以 $d\int_0^1u(x,t)dx/dt=0$；任意子区间的总量变化等于左端流入减右端流出。

### [第 4 题](../assets/yau-papers/2025-final-individual.pdf)

证明 $x^4+y^4+z^4\le1$ 与平面 $x+y+z=0$ 的交集是圆盘。

??? proof "答案"

    在该平面 $xy+yz+zx=-(x^2+y^2+z^2)/2$，且 $(xy+yz+zx)^2=x^2y^2+y^2z^2+z^2x^2$。所以 $x^4+y^4+z^4=(x^2+y^2+z^2)^2/2$。交集恰为平面内 $x^2+y^2+z^2\le\sqrt2$，中心为原点、半径 $2^{1/4}$ 的圆盘。

## 2025 · 总决赛·综合个人赛

### [第 1(a)–(c) 题](../assets/yau-papers/2025-final-overall.pdf)

$\operatorname{prox}_{\alpha f}(x)=\arg\min_y\{f(y)+\|y-x\|_2^2/(2\alpha)\}$。(a) 求 $f=\|\cdot\|_1$；(b) 求 $f=\|\cdot\|_2$；(c) 证明 $\operatorname{prox}_{\alpha,f+g}=\operatorname{prox}_{\alpha,g}\circ\operatorname{prox}_{\alpha,f}$，$f=\|\cdot\|_1,g=\|\cdot\|_2$。

??? proof "答案"

    (a) 逐坐标软阈值 $S_\alpha(x)_i=\operatorname{sgn}(x_i)(|x_i|-\alpha)_+$。

    (b) 沿 $x$ 方向为最优，$\operatorname{prox}_{\alpha\|\cdot\|_2}(x)=(1-\alpha/\|x\|_2)_+x$，$x=0$ 时结果为零。

    (c) 对 $f(y)=a\|y\|_1+b\|y\|_2$，令 $z=S_{\alpha a}(x)$，结果为 $(1-\alpha b/\|z\|_2)_+z$，$z=0$ 时为零。逐坐标最优条件与径向缩放直接验证；严格凸二次项保证唯一。

### [第 2 题](../assets/yau-papers/2025-final-overall.pdf)

$\varepsilon y''+(1+\varepsilon)y'+y=0$，$y(0)=0,y(1)=1$，$0<\varepsilon\ll1$。求含边界层的近似解。

??? proof "答案"

    精确解 $y(x)=[e^{-x}-e^{-x/\varepsilon}]/[e^{-1}-e^{-1/\varepsilon}]$。因此统一近似为 $e^{1-x}-e^{1-x/\varepsilon}$，在 $[0,1]$ 上误差 $O(e^{-1/\varepsilon})$。第一项为外部解，第二项在 $x=0$、宽度 $O(\varepsilon)$ 内修正左边界。

## 2025 · 总决赛·团体赛

### [第 2(a)–(d) 题](../assets/yau-papers/2025-final-team.pdf)

$f(z)=\log\sum_ie^{z_i}$。(a) 证明凸；(b) 求凸共轭 $f^*(y)=\sup_z(y\cdot z-f(z))$；(c) 求二次共轭；(d) 求熵正则化最大值与最优分布。

??? proof "答案"

    (a) $p_i=e^{z_i}/\sum_je^{z_j}$，$\nabla f=p$、$\nabla^2f=\operatorname{diag}(p)-pp^T$，其二次型为加权方差，非负。

    (b) 若 $y_i\ge0,\sum y_i=1$，$f^*(y)=\sum_iy_i\log y_i$，约定 $0\log0=0$；否则为 $+\infty$。和不为 $1$ 时整体平移 $z$ 使上确界无穷；有负分量时将对应 $z_i\to-\infty$。单纯形内由驻点 $z_i=\log y_i+c$ 求值，零分量由极限处理。

    (c)、(d) $\sup_{y\ge0,\sum y_i=1}[z\cdot y-\sum y_i\log y_i]=\log\sum e^{z_i}$，唯一最优 $y_i=p_i$；所以 $f^{**}=f$。带熵系数 $\tau>0$ 时值为 $\tau\log\sum e^{z_i/\tau}$，最优为相应 softmax。

### [第 3(a)、(b)、(d) 题](../assets/yau-papers/2025-final-team.pdf)

(a) 对幂零矩阵 $N^r=0$ 求解析函数 $f(\lambda I+N)$；(b) 求矩阵指数；(d) 求 $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ 的 $e^{At}$ 并解释。

??? proof "答案"

    (a) $f(\lambda I+N)=\sum_{j=0}^{r-1}f^{(j)}(\lambda)N^j/j!$，幂零性使 Taylor 级数截断。

    (b) $e^{\lambda I+N}=e^\lambda\sum_{j=0}^{r-1}N^j/j!$。

    (d) $e^{At}=\begin{pmatrix}\cos t&\sin t\\-\sin t&\cos t\end{pmatrix}$，为顺时针旋转 $t$ 弧度。因为 $A^2=-I$，按偶、奇次项分开指数级数即可。

### [第 3(c) 题](../assets/yau-papers/2025-final-team.pdf)

实矩阵 $A$ 可能有复特征值，说明如何高效计算实矩阵 $e^{At}$。

??? proof "答案"

    可用实矩阵的缩放与平方：选 $s$ 使 $\|At/2^s\|$ 足够小，用有限 Taylor 多项式 $P_m=\sum_{j=0}^m(At/2^s)^j/j!$ 逼近，再平方 $s$ 次。每步均用实矩阵，误差界 $\|e^B-P_m(B)\|\le e^{\|B\|}\|B\|^{m+1}/(m+1)!$，选择 $m,s$ 控制精度。实践中也可将小矩阵指数用有理近似计算；有复特征值并不要求复数运算。

## 2026 · 笔试·个人赛

### [第 3(a)–(c) 题](../assets/yau-papers/2026-written-individual.pdf)

对 $x'=f(t,x)$，用 $x_{n+1}=x_n+(1-b)hf(t_n,x_n)+bhf(t_{n+1},x_{n+1})$，$0\le b\le1$。(a) 求使局部截断误差 $O(h^3)$ 的 $b$；(b) 对 $x'=\lambda x$ 求 $x_n=g(h\lambda)^nx_0$；(c) 求 A-稳定的参数。

??? proof "答案"

    (a) 二次项匹配要求 $b=1/2$。(b) $g(z)=[1+(1-b)z]/(1-bz)$，分母须非零。

    (c) 分母模平方减分子模平方为 $-2\Re z+(2b-1)|z|^2$。对整个左半平面非负当且仅当 $b\ge1/2$，且这些 $b$ 的分母在左半平面不为零。$b<1/2$ 时沿负实轴令 $z\to-\infty$ 即违反稳定性。

### [第 4(a)–(c) 题](../assets/yau-papers/2026-written-individual.pdf)

带位移 QR 迭代定义为 $A_n-\sigma_nI=Q_nR_n$、$A_{n+1}=R_nQ_n+\sigma_nI$，$Q_n$ 正交，$R_n$ 上三角且对角元正。(a) 若位移均非特征值，证明分解唯一及 $A_{n+1}=Q_n^TA_nQ_n=R_nA_nR_n^{-1}$；(b) $A$ 为二阶对称矩阵、$\sigma_0=\lambda_1$ 时，求 $A_1$；(c) 证明 $\widehat Q_{k+1}\widehat R_{k+1}=\prod_{i=0}^k(A-\sigma_iI)$，其中 $\widehat Q_{k+1}=Q_0\cdots Q_k$、$\widehat R_{k+1}=R_k\cdots R_0$。

??? proof "答案"

    (a) 对列向量 Gram–Schmidt 得到正对角 QR。若有两组分解，$Q_1^TQ_2=R_1R_2^{-1}$ 同时正交、上三角且正对角，只能为 $I$。两条相似关系由代入 $Q_nR_n=A_n-\sigma_nI$ 直接得到。

    (b) 按原卷严格定义没有这样的 $A_1$：$A-\lambda_1I$ 奇异，而正对角 $R_0$ 必可逆，两者矛盾。若允许 $R_0$ 有零对角元，分解不一定唯一，$A_1$ 也不能仅由两特征值唯一确定。选特征向量作为 $Q_0$ 时可得到对角排列；这是额外的选择，不能由原定义推出。

    (c) 由相似关系 $A\widehat Q_k=\widehat Q_kA_k$，得到 $(A-\sigma_kI)\widehat Q_k=\widehat Q_{k+1}R_k$。右乘 $\widehat R_k$，归纳即得乘积式；各因子都是 $A$ 的多项式，故可交换次序。

### [第 5(a)–(c) 题](../assets/yau-papers/2026-written-individual.pdf)

**原卷：** [2026 应用与计算数学，第 2 页](../assets/yau-papers/2026-computational-applied.pdf#page=2)。**选取：** (a)–(c)。**先修：** [SVD](02-svd-least-squares.md)、[正半定与范数](01-matrix-norms-spectral.md)。

对实方阵 $A$，称 $Ax=x$ 的向量为其不动点。(a) 若最大奇异值 $\sigma_1(A)\le1$，证明这些向量也满足 $A^Tx=x$；(b) 用 $A=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ 说明范数条件不可直接删去；(c) 若 $AA^T=A^TA$，证明相同结论。

??? proof "答案"

    **(a)** $\sigma_1(A)=\|A\|_2\le1$，所以 $S=I-A^TA$ 正半定。若 $Ax=x$，则

    $$
    x^TSx=\|x\|_2^2-\|Ax\|_2^2=0.
    $$

    用谱定理写 $S=Q\operatorname{diag}(s_i)Q^T$，其中 $s_i\ge0$。和式 $\sum_i s_i(Q^Tx)_i^2=0$ 的每项都为零，因此 $Sx=0$。于是 $A^TAx=x$，结合 $Ax=x$ 得 $A^Tx=x$。

    **(b)** 取 $x=(1,0)^T$。有 $Ax=x$，但 $A^Tx=(1,1)^T\ne x$。该矩阵 $\sigma_1(A)=\sqrt2>1$。

    **(c)** 令 $N=A-I$。由正规性 $AA^T=A^TA$ 得 $NN^T=N^TN$。对 $Nx=0$，

    $$
    \|N^Tx\|_2^2=x^TNN^Tx=x^TN^TNx=\|Nx\|_2^2=0.
    $$

    故 $N^Tx=0$，即 $A^Tx=x$。这里不要求 $A$ 对称，也不要求 $\|A\|_2\le1$。

### [第 6(a)、(b) 题](../assets/yau-papers/2026-written-individual.pdf)

凸函数的次梯度定义为 $f(z)\ge f(x)+y^T(z-x)$ 对所有 $z$ 成立。$f(x)=\max_i x_i$，$n\ge2$，$g(x)=\max_i x_i+\delta_{\mathbb R_+^n}(x)$，其中指示函数在非负正交锥为零、其他处为 $+\infty$。(a) 求 $\partial f(0)$；(b) 证明 $\partial g(0)=\partial f(0)-\mathbb R_+^n$。

??? proof "答案"

    (a) $\partial f(0)=\{y:y_i\ge0,\sum_i y_i=1\}$。取 $z=t\mathbf1$ 和 $z=-te_i$ 得到必要条件；反过来凸组合 $y^Tz\le\max_i z_i$。

    (b) 由定义，$y\in\partial g(0)$ 当且仅当 $y^Tz\le\max_i z_i$ 对所有 $z\ge0$ 成立，等价于 $\sum_i\max(y_i,0)\le1$。此条件又等价于存在概率向量 $p\ge y$：在 $y_+$ 的各分量上补足总和到 $1$。于是 $y=p-r$、$p\in\partial f(0),r\ge0$，得到所需集合等式。
