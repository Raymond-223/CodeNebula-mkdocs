# Newton's Method & Convergence Order

Newton's method 是局部线性化产生的求根方法。本章先从 Taylor theorem 推导迭代式，再严格证明简单根附近的局部二次收敛，并分析重根、割线法和 Steffensen acceleration。

## Root-Finding Problem

目标是求 $f(x)=0$ 的根 $\alpha$。当前近似为 $x_k$。在 $x_k$ 附近使用一阶 Taylor approximation：

$$
f(x)\approx f(x_k)+f'(x_k)(x-x_k).
$$

令近似式在 $x_{k+1}$ 为零：

$$
0=f(x_k)+f'(x_k)(x_{k+1}-x_k).
$$

若 $f'(x_k)\ne0$，得到 Newton iteration：

$$
\boxed{x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}}.
$$

实际实现中必须检查分母。$f'(x_k)$ 很小时，Newton step 可能非常大。

## Square-Root Example

求 $\sqrt a$ 等价于解 $f(x)=x^2-a=0$。Newton iteration 为

$$
x_{k+1}
=x_k-\frac{x_k^2-a}{2x_k}
=\frac12\left(x_k+\frac a{x_k}\right).
$$

对 $a=2$、$x_0=1$：

$$
x_1=1.5,
\quad
x_2=\frac{17}{12}\approx1.41667,
\quad
x_3\approx1.41422.
$$

这是数值现象；收敛性还需要证明。

## Order of Convergence

设 $e_k=x_k-\alpha$。若 $e_k\to0$，且存在 $p\ge1$、$C\in(0,\infty)$ 使

$$
\lim_{k\to\infty}\frac{|e_{k+1}|}{|e_k|^p}=C,
$$

则收敛阶为 $p$，$C$ 是 asymptotic error constant。

- $p=1$ 且 $C<1$：linear convergence；
- $1<p<2$：superlinear convergence；
- $p=2$：quadratic convergence。

若极限为零，实际阶数可能高于 $p$；若只知道 $|e_{k+1}|\le C|e_k|^p$，通常只能得到至少 $p$ 阶的控制。

## Local Quadratic Convergence Theorem

**定理。** 设 $f$ 在根 $\alpha$ 的某邻域中二次连续可微，满足

$$
f(\alpha)=0,
\qquad
f'(\alpha)\ne0.
$$

则存在 $\alpha$ 的一个闭邻域 $I$，使任意 $x_0\in I$ 产生的 Newton iteration 都有定义并收敛到 $\alpha$。此外存在 $C>0$ 使

$$
|e_{k+1}|\le C|e_k|^2.
$$

若进一步 $f''(\alpha)\ne0$，则

$$
\lim_{k\to\infty}
\frac{e_{k+1}}{e_k^2}
=\frac{f''(\alpha)}{2f'(\alpha)},
$$

故收敛阶恰为 $2$。

### Error Identity with Taylor Remainder

以 $x_k$ 为展开点，对根 $\alpha$ 使用 Taylor theorem：存在 $\xi_k$ 位于 $x_k$ 与 $\alpha$ 之间，使

$$
0=f(\alpha)
=f(x_k)+f'(x_k)(\alpha-x_k)
+\frac12f''(\xi_k)(\alpha-x_k)^2.
$$

除以 $f'(x_k)$ 并整理：

$$
\alpha-left(x_k-\frac{f(x_k)}{f'(x_k)}\right)
=\frac{f''(\xi_k)}{2f'(x_k)}(\alpha-x_k)^2.
$$

括号内正是 $x_{k+1}$，所以

$$
e_{k+1}
=\frac{f''(\xi_k)}{2f'(x_k)}e_k^2.
$$

### Invariant Neighborhood

因为 $f'(\alpha)\ne0$ 且 $f'$ 连续，可取半径 $r_0>0$ 和常数 $m>0$，使

$$
|f'(x)|\ge m
$$

在 $I_0=[\alpha-r_0,\alpha+r_0]$ 上成立。又因 $f''$ 连续，在紧区间上有界：

$$
|f''(x)|\le M.
$$

于是只要 $x_k\in I_0$，

$$
|e_{k+1}|\le\frac{M}{2m}|e_k|^2.
$$

记 $C=M/(2m)$。若 $C=0$，上式已经给出 $e_{k+1}=0$，Newton iteration 一步到根。以下设 $C>0$，缩小半径为

$$
r\le\min\{r_0,1/(2C)\}.
$$

若 $|e_k|\le r$，则

$$
|e_{k+1}|
\le C|e_k|^2
\le Cr|e_k|
\le\frac12|e_k|
\le r.
$$

因此区间不变，所有迭代都有定义，且误差至少按比例 $1/2$ 收缩到零。这完成局部收敛证明。

### Asymptotic Constant

当 $x_k\to\alpha$ 时，$\xi_k\to\alpha$。由连续性，

$$
\frac{e_{k+1}}{e_k^2}
=\frac{f''(\xi_k)}{2f'(x_k)}
\to\frac{f''(\alpha)}{2f'(\alpha)}.
$$

若极限非零，Newton's method 恰为二阶。

## Exact Error for the Square-Root Iteration

令 $\alpha=\sqrt a>0$。由

$$
x_{k+1}=\frac12\left(x_k+\frac{\alpha^2}{x_k}\right)
$$

可直接得到

$$
\begin{aligned}
e_{k+1}
&=\frac{x_k^2+\alpha^2-2\alpha x_k}{2x_k}\\
&=\frac{(x_k-\alpha)^2}{2x_k}\\
&=\frac{e_k^2}{2x_k}.
\end{aligned}
$$

若 $x_k\to\alpha$，则

$$
\frac{e_{k+1}}{e_k^2}\to\frac1{2\alpha},
$$

所以收敛阶恰为二阶。

对 $x_0>0$ 还能证明全局单调行为：由 AM–GM inequality，$x_1\ge\alpha$；当 $x_k\ge\alpha$ 时，$x_{k+1}\le x_k$ 且 $x_{k+1}\ge\alpha$。因此从第一步起单调有下界，极限只能是 $\alpha$。

## Multiple Roots

若 $\alpha$ 是重数 $m\ge2$ 的根，可写

$$
f(x)=(x-\alpha)^m h(x),
\qquad h(\alpha)\ne0.
$$

标准 Newton method 的渐近误差满足

$$
e_{k+1}=\frac{m-1}{m}e_k+O(e_k^2),
$$

所以只线性收敛。

以 $f(x)=(x-1)^3$ 为例，

$$
x_{k+1}
=x_k-\frac{(x_k-1)^3}{3(x_k-1)^2}
=1+\frac23(x_k-1),
$$

故 $e_{k+1}=(2/3)e_k$。

若已知重数 $m$，modified Newton method

$$
x_{k+1}=x_k-m\frac{f(x_k)}{f'(x_k)}
$$

可恢复局部二次收敛。

## Global Failure Example

对

$$
f(x)=x^3-2x+2,
$$

从 $x_0=0$ 出发，

$$
x_1=0-\frac2{-2}=1,
$$

$$
x_2=1-\frac1{1}=0.
$$

迭代进入周期 $0\leftrightarrow1$，不会趋向实根。这说明局部二次收敛不等于任意初值全局收敛。

## Secant Method

secant method 用割线斜率代替导数：

$$
f'(x_k)\approx
\frac{f(x_k)-f(x_{k-1})}{x_k-x_{k-1}}.
$$

得到

$$
\boxed{
x_{k+1}=x_k-f(x_k)
\frac{x_k-x_{k-1}}{f(x_k)-f(x_{k-1})}
}.
$$

要求 $x_k\ne x_{k-1}$ 且 $f(x_k)\ne f(x_{k-1})$。

在简单根附近，对足够光滑的 $f$，误差主项为

$$
e_{k+1}
=\frac{f''(\alpha)}{2f'(\alpha)}e_ke_{k-1}
+o(e_ke_{k-1}).
$$

若假设 $|e_k|\asymp |e_{k-1}|^p$，则一边量级为 $|e_k|^p$，另一边量级为 $|e_k||e_{k-1}|\asymp|e_{k-1}|^{p+1}$。比较指数得

$$
p^2=p+1,
$$

正根为

$$
p=\frac{1+\sqrt5}{2}\approx1.618.
$$

完整定理还需要证明误差比极限存在；这里保留主误差关系，是因为后续综合题会实际使用它。

## Steffensen Acceleration

设 fixed-point iteration $x_{k+1}=g(x_k)$，固定点为 $\alpha$。定义

$$
y=g(x),
\qquad
z=g(y),
$$

Steffensen map 为

$$
G(x)=x-\frac{(y-x)^2}{z-2y+x},
$$

前提是分母非零。

### Local Error Expansion

设 $g$ 三次连续可微，且

$$
g(\alpha+e)
=\alpha+ae+be^2+O(e^3),
$$

其中 $a=g'(\alpha)$、$b=g''(\alpha)/2$。则

$$
y-x=(a-1)e+be^2+O(e^3),
$$

并且

$$
z-2y+x=(a-1)^2e+b(a^2+a-2)e^2+O(e^3).
$$

当 $a\ne1$ 时，可约去一阶因子并展开分式，得到

$$
G(\alpha+e)-\alpha
=\frac{ab}{a-1}e^2+O(e^3).
$$

因此若 $a\ne1$ 且 $ab\ne0$，Steffensen iteration 局部恰为二阶；若二次系数为零，阶数可能更高。若 $a=1$，分母的一阶项消失，不能套用上述结论。

## Multivariate Newton Method

对 $F:\mathbb R^n\to\mathbb R^n$，一阶线性化为

$$
F(x_k+s)\approx F(x_k)+J_F(x_k)s.
$$

令右侧为零，Newton step $s_k$ 由线性方程

$$
J_F(x_k)s_k=-F(x_k)
$$

确定，再令 $x_{k+1}=x_k+s_k$。数值实现应求解线性方程，不应显式形成 $J_F(x_k)^{-1}$。

对于优化问题 $\min f(x)$，求解的是 $\nabla f(x)=0$，因此 Newton step 满足

$$
\nabla^2f(x_k)s_k=-\nabla f(x_k).
$$

根求解与优化形式相似，但对象不同。

## Exercises

1. 对 $f(x)=x^2-3$、$x_0=2$ 计算两次 Newton iteration。
2. 对 $f(x)=x^2$ 证明标准 Newton method 只线性收敛。
3. 从 Taylor remainder 重新证明 $|e_{k+1}|\le M|e_k|^2/(2m)$。
4. 对 $f(x)=(x-2)^4$ 推导标准 Newton iteration 的误差因子，并写出已知重数时的 modified method。
5. 验证 $g(x)=\cos x$ 的 Steffensen iteration 在其固定点附近满足二阶条件。

**Answers.** 第 1 题 $x_1=7/4$、$x_2=97/56$。第 2 题 $x_{k+1}=x_k/2$。第 4 题 $e_{k+1}=3e_k/4$，modified method 使用系数 $4$。

**Previous:** [Fixed Points & Contractions](04-fixed-points-contractions.md)  
**Next:** [Worked Problems](06-stage-one-workbook.md)
