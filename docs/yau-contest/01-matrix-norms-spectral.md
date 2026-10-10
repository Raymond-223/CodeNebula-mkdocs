# Matrix Norms & Spectral Theory

矩阵既可以看成数字表，也可以看成 linear map。后一个观点解释了范数、特征值、正定性和迭代收敛之间的关系。

## Linear Maps and Matrix Dimensions

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

### Rank, Kernel, and Column Space

零空间 kernel 与列空间 column space 定义为

$$
\ker(A)=\{x:Ax=0\},
\qquad
\operatorname{Col}(A)=\{Ax:x\in\mathbb R^n\}.
$$

rank–nullity theorem 给出

$$
\operatorname{rank}(A)+\dim\ker(A)=n.
$$

因此 $A$ 的列线性无关当且仅当 $\ker(A)=\{0\}$。

## Eigenvalues and Eigenvectors

非零向量 $v$ 若满足

$$
Av=\lambda v,
$$

则 $v$ 是 eigenvector，$\lambda$ 是 eigenvalue。它表示 $A$ 在方向 $v$ 上只做伸缩或反向。

方程可写为 $(A-\lambda I)v=0$。存在非零解当且仅当

$$
\det(A-\lambda I)=0.
$$

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

## Vector Norms

vector norm $\|\cdot\|$ 必须满足：

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

有限维空间中所有范数等价：任意两个范数 $\|\cdot\|_a,\|\cdot\|_b$ 之间存在常数 $c,C>0$，使

$$
c\|x\|_a\le\|x\|_b\le C\|x\|_a.
$$

因此有限维中的“是否收敛”不依赖所选范数，但数值界的常数会依赖范数。

## Induced Matrix Norms

由向量范数诱导的 operator norm 定义为

$$
\|A\|=\sup_{x\ne0}\frac{\|Ax\|}{\|x\|}
=\sup_{\|x\|=1}\|Ax\|.
$$

它表示 $A$ 对单位向量的最大放大倍数。由定义立即得到 compatibility：

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
\|A\|_2=\sigma_{\max}(A)
=\sqrt{\lambda_{\max}(A^TA)}.
$$

最后一个公式会在 SVD 章节证明。

### Frobenius Norm

Frobenius norm 定义为

$$
\|A\|_F=\sqrt{\sum_{i,j}a_{ij}^2}
=\sqrt{\operatorname{tr}(A^TA)}.
$$

它是矩阵元素构成向量后的 Euclidean norm，但对 $n>1$ 并不是由同一个 $n$ 维向量范数诱导的 operator norm。仍有

$$
\|AB\|_F\le\|A\|_2\|B\|_F.
$$

## Submultiplicativity

**定理。** 任意诱导矩阵范数满足

$$
\|AB\|\le\|A\|\|B\|.
$$

**证明。** 对任意 $x\ne0$，

$$
\|ABx\|
\le\|A\|\|Bx\|
\le\|A\|\|B\|\|x\|.
$$

两边除以 $\|x\|$，再对所有 $x\ne0$ 取上确界，即得结论。$\square$

这个证明说明“诱导”不是装饰：正是定义中的最大放大倍数带来了乘法相容性。

## Spectral Radius

spectral radius 定义为

$$
\rho(A)=\max_{\lambda\in\sigma(A)}|\lambda|,
$$

其中 $\sigma(A)$ 是全部特征值的集合。特征值可以是负数或复数，所以必须取模。

**定理。** 对任意诱导矩阵范数，

$$
\rho(A)\le\|A\|.
$$

**证明。** 若 $Av=\lambda v$ 且 $v\ne0$，则

$$
|\lambda|\|v\|
=\|\lambda v\|
=\|Av\|
\le\|A\|\|v\|.
$$

约去 $\|v\|$ 得 $|\lambda|\le\|A\|$，再对全部特征值取最大值。对于复特征值，在 $\mathbb C^n$ 上使用同一诱导范数。$\square$

反向不成立。矩阵

$$
A=\begin{pmatrix}0&10\\0&0\end{pmatrix}
$$

满足 $A^2=0$，故全部特征值为零，$\rho(A)=0$；但 $\|A\|_2=10$。

## Symmetric Matrices and Spectral Theorem

实矩阵 $A$ 若满足 $A^T=A$，称为 real symmetric matrix。

**Spectral Theorem.** 每个实对称矩阵都存在正交矩阵 $Q$ 和实对角矩阵 $\Lambda$，使

$$
A=Q\Lambda Q^T,
\qquad Q^TQ=I.
$$

$Q$ 的列是标准正交特征向量，$\Lambda$ 的对角元是对应特征值。

### Rayleigh Quotient

对 $x\ne0$，Rayleigh quotient 定义为

$$
R_A(x)=\frac{x^TAx}{x^Tx}.
$$

若 $A$ 对称，设 $A=Q\Lambda Q^T$ 且 $y=Q^Tx$。由于 $Q$ 正交，$x^Tx=y^Ty$，于是

$$
R_A(x)
=\frac{\sum_i\lambda_i y_i^2}{\sum_i y_i^2}.
$$

令 $w_i=y_i^2/\sum_jy_j^2$，则 $w_i\ge0$ 且 $\sum_iw_i=1$。因此 Rayleigh quotient 是特征值的加权平均：

$$
\lambda_{\min}(A)
\le R_A(x)
\le\lambda_{\max}(A).
$$

上下界分别在最小、最大特征值的特征向量方向取得。

## Positive Definiteness

实对称矩阵 $A$ 称为 positive definite，若对所有 $x\ne0$，

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

非对称矩阵即使特征值全正，也不能直接称作正定矩阵；二次型只依赖其对称部分 $(A+A^T)/2$。

## Gram Matrix

对任意 $A\in\mathbb R^{m\times n}$，

$$
(A^TA)^T=A^TA,
$$

且

$$
x^TA^TAx=\|Ax\|_2^2\ge0.
$$

所以 $A^TA$ 总是 symmetric positive semidefinite。并且

$$
A^TA\succ0
\quad\Longleftrightarrow\quad
\ker(A)=\{0\}
\quad\Longleftrightarrow\quad
A\text{ has full column rank}.
$$

这条结论解释了满列秩时正规方程具有唯一解，也构成 SVD 的入口。

## Gershgorin Circle Theorem

对方阵 $A=(a_{ij})$，定义第 $i$ 个 Gershgorin disc：

$$
D_i=\left\{z\in\mathbb C:
|z-a_{ii}|\le\sum_{j\ne i}|a_{ij}|
\right\}.
$$

**定理。** $A$ 的每个特征值至少落在一个 $D_i$ 中。

**证明。** 设 $Av=\lambda v$，选择满足 $|v_i|=\|v\|_\infty>0$ 的指标 $i$。第 $i$ 行给出

$$
(\lambda-a_{ii})v_i=\sum_{j\ne i}a_{ij}v_j.
$$

取绝对值并用 $|v_j|\le|v_i|$：

$$
|\lambda-a_{ii}|,|v_i|
\le\sum_{j\ne i}|a_{ij}|,|v_j|
\le\left(\sum_{j\ne i}|a_{ij}|\right)|v_i|.
$$

约去 $|v_i|$ 即得 $\lambda\in D_i$。$\square$

若 $|a_{ii}|>\sum_{j\ne i}|a_{ij}|$ 对每行成立，则零不属于任何圆盘，因此 $0$ 不是特征值，$A$ 可逆。

## Condition Number

若 $A$ 可逆，二范数 condition number 为

$$
\kappa_2(A)=\|A\|_2\|A^{-1}\|_2
=\frac{\sigma_{\max}(A)}{\sigma_{\min}(A)}.
$$

在线性系统 $Ax=b$ 中，若只有右端发生小扰动 $\delta b$，则

$$
\frac{\|\delta x\|}{\|x\|}
\le
\kappa(A)
\frac{\|\delta b\|}{\|b\|}.
$$

条件数描述问题对输入扰动的敏感性，不等于某个算法的舍入误差。

## Exercises

1. 计算 $A=\begin{pmatrix}2&-1\\1&3\end{pmatrix}$ 的 $1$-norm、$\infty$-norm 与 Frobenius norm。
2. 证明 $\|A^k\|\le\|A\|^k$。
3. 对 $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ 计算 Rayleigh quotient 的最小值和最大值。
4. 证明严格行对角占优矩阵可逆，不使用 Gershgorin theorem，而从 $Ax=0$ 选取最大模分量证明。
5. 给出 $\rho(A)<1$ 但 $\|A\|_2>1$ 的矩阵，并直接计算验证。

**Answers.** 第 1 题为 $4,4,\sqrt{15}$。第 3 题为 $1,3$。第 5 题可用本章的幂零矩阵例子。

**Previous:** [Proof Language & Calculus](00-proof-skills-notation.md)  
**Next:** [SVD & Least Squares](02-svd-least-squares.md)
