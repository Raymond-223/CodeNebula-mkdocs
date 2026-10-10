# Yau Contest

本专题是一套面向零基础读者的数学讲解手册。这里的“零基础”指：不假设读者仍记得大学线性代数、微积分或数值分析中的定义；每个后续要使用的概念都会先定义、再计算、最后证明。它并不表示可以跳过代数运算，而是表示知识依赖不会被隐藏。

## Scope and Conventions

本阶段只建立四条相互连接的主线：

1. 矩阵、范数、特征值与谱半径；
2. 正交投影、Singular Value Decomposition (SVD) 与 least squares；
3. 线性迭代、fixed-point iteration 与 contraction mapping；
4. Taylor theorem、Newton's method 与 order of convergence。

正文中的重要术语第一次出现时给出英文标准名称。证明中使用的记号遵守以下约定：

- 标量用小写字母，如 $a,x,\lambda$；
- 向量默认是列向量，如 $x\in\mathbb R^n$；
- 矩阵用大写字母，如 $A\in\mathbb R^{m\times n}$；
- $A^T$ 表示转置，$I_n$ 表示 $n$ 阶单位矩阵；
- $\ker(A)$、$\operatorname{Col}(A)$ 分别表示零空间和列空间；
- 除非另行说明，向量范数是 Euclidean norm $\|x\|_2$，矩阵范数是与它诱导的 operator norm $\|A\|_2$。

## Dependency Graph

```text
Proof language and calculus
          |
          v
Matrix norms and spectral theory
       /                    \
      v                      v
SVD and least squares   Linear iterations
                              |
                              v
                    Fixed-point theorem
                              |
                              v
                    Newton convergence
```

依赖箭头表示“后者的证明会直接调用前者”。阅读时不要先背结论：如果一个符号尚不能解释，就回到箭头上游。

## Chapters

| Chapter | Core knowledge | Completion standard |
| --- | --- | --- |
| [Proof Language & Calculus](00-proof-skills-notation.md) | 量词、充分必要条件、极限、Taylor theorem | 能把命题写成带量词的形式，并检查证明是否覆盖全部条件 |
| [Matrix Norms & Spectral Theory](01-matrix-norms-spectral.md) | vector norm、operator norm、spectral radius、spectral theorem | 能证明次乘性、Rayleigh quotient 界和谱半径基本结论 |
| [SVD & Least Squares](02-svd-least-squares.md) | 正交投影、SVD、pseudoinverse、最小范数解、low-rank approximation | 能从 $A^TA$ 手算 SVD，推导全部最小二乘解，并证明最佳低秩误差 |
| [Linear Iterations & Power Method](03-linear-iterations-power.md) | stationary iteration、谱半径判据、power method | 能从迭代式推出误差方程并证明充要条件 |
| [Fixed Points & Contractions](04-fixed-points-contractions.md) | complete metric space、Banach theorem、误差界 | 能逐步证明存在性、唯一性、收敛性和迭代次数界 |
| [Newton's Method & Convergence Order](05-newton-convergence.md) | Taylor remainder、局部二次收敛、重根 | 能写出带邻域条件的局部收敛证明 |
| [Worked Problems](06-stage-one-workbook.md) | 综合证明与计算 | 能独立完成完整解答，而不是只给出公式或提示 |

## Theorem Reading Method

阅读每个定理时固定做四件事：

1. 圈出对象，例如“非空完备度量空间”或“实对称矩阵”；
2. 标记每个假设，例如“$f'(\alpha)\ne0$”不能省略；
3. 分开结论，例如存在、唯一、算法收敛是三个命题；
4. 检查反例，确认删去哪条假设会失败。

例如 $\rho(B)<1$ 与 $B^k\to0$ 是等价命题，但 $\rho(B)<1$ 与 $\|B\|_2<1$ 并不等价。后者是更强的充分条件。手册会反复区分这种逻辑强弱。

## Formula Reading Method

遇到公式先检查尺寸，再做代数。例如

$$
A\in\mathbb R^{m\times n},\qquad x\in\mathbb R^n,
$$

则 $Ax\in\mathbb R^m$、$A^TA\in\mathbb R^{n\times n}$、$AA^T\in\mathbb R^{m\times m}$。维数检查能够在计算开始前排除大量错误。

对于极限或误差式，还要说明趋近过程。写 $o(e_k^2)$ 时隐含 $e_k\to0$；写 $B^k\to0$ 时应说明矩阵收敛是在任意等价矩阵范数下成立。

## Chapter Workflow

每章按同一方式使用：

1. 先手算定义后的第一个例子；
2. 再阅读定理证明，并在纸上补全等号之间的理由；
3. 检查反例，确认定理条件不是装饰；
4. 最后完成章末练习，再进入下一章。

专题的完成标准是：能够从定义重新推出结论，并能说明每一步为何成立。

**Start:** [Proof Language & Calculus](00-proof-skills-notation.md)
