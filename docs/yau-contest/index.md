# Yau Contest

> **独立竞赛专题 · Computational and Applied Mathematics · Stage 1**  
> 这里是 CodeNebula 的丘成桐大学生数学竞赛（丘赛）备赛区。它与 `Foundations / Mathematics` **完全独立**：不假设你记得高等数学、线性代数或数值计算，也不要求你去另一个栏目寻找定义。同一个概念即使 Foundations 已经讲过，这里也会为了竞赛证明而**重新定义、重新推导、重新练习**。

---

## 一、为什么要单独设一个专题

你学过高等数学、线性代数、离散数学、组合数学、概率论与随机过程、优化分析基础、数值计算、数学物理方程，但这些课主要偏向**公式运用、计算题与程序实现**。丘赛应用与计算数学的难点通常不是会不会按公式算数，而是能不能从假设出发写出**完整、可检验的数学证明**。

这里不走“九本大部头教材通读”的路线，也不追求每届试卷所有题都能做。专题执行四条筛选原则：

1. **已有基础优先**：矩阵运算、SVD、线性方程组、Newton法与收敛性，能从学过的课程平滑切入。
2. **低补课成本优先**：能用少量基本定理覆盖一组真题的内容，优先形成完整得分能力。
3. **未来科研有用优先**：矩阵计算、固定点、优化求解、算法稳定性，对机器学习、强化学习与AI算法有长期价值。
4. **允许放弃**：第一阶段不学习高等有限元误差理论、特殊函数全套理论、辛几何等补习成本大的专题。

!!! important "学习边界"
    **本次只交付 Stage 1 的完整知识材料**（矩阵理论 + 线性迭代 + 不动点 + Newton法），不把后续 ODE、PDE、凸优化等阶段写成空壳章节，不为补目录而把整门课摊开。先把第一阶段练到会证明，再进入下一阶段。

## 二、这一阶段到底学什么

阶段内的七章是相互独立成文、又有建议顺序的一套**零基础重学材料**：

| 学习顺序 | 章节 | 从哪里讲起 | 最后必须会什么 |
| --- | --- | --- | --- |
| 00 | [Proof Skills & Notation](00-proof-skills-notation.md) | 数、向量、求和、逻辑、极限、大 O | 能写清楚“已知—目标—推理—结论” |
| 01 | [Matrix Norms & Spectral Theory](01-matrix-norms-spectral.md) | 矩阵乘法、转置、特征值、对角化 | 证明范数、Rayleigh商、谱半径相关结论 |
| 02 | [SVD & Least Squares](02-svd-least-squares.md) | 投影、正交、秩、最小二乘 | 推导伪逆、秩亏最小范数解、截断SVD |
| 03 | [Linear Iterations & Power Method](03-linear-iterations-power.md) | 线性方程组、误差、迭代矩阵 | 用谱半径分析收敛、证明幂法/反幂法 |
| 04 | [Fixed Points & Contractions](04-fixed-points-contractions.md) | 函数、导数、区间、序列 | 用压缩映射严格证明存在唯一性和迭代次数 |
| 05 | [Newton's Method & Convergence Order](05-newton-convergence.md) | Taylor展开、导数、误差记号 | 证明Newton二次收敛、分析割线与加速迭代 |
| 06 | [Stage 1 Exam Workbook](06-stage-one-workbook.md) | 从题目读条件、拆小问 | 有依据地选择和完成历年真题 |

每章都遵循固定阅读方式：**先用计算理解问题 → 定义术语 → 亲手推导公式 → 写严格证明 → 做含解答的例题 → 再试真题**。

## 三、它和原来的 Mathematics 有什么不同

| 对比 | Foundations / Mathematics | Yau Contest |
| --- | --- | --- |
| 目标 | 读懂后续控制、AI与工程公式 | 在限时试卷中独立证明定理、解答理论题 |
| 读者预设 | 只要够用，可以回查 | 允许忘光了；每个重要概念从头解释 |
| 同一知识出现两遍 | Foundations 仍保留自己的内容 | **本栏目重新完整讲解**，不依赖跨栏链接 |
| 学习方法 | 以概念理解和工程使用为主 | 逐步证明、练习、纠错、限时训练 |
| 知识范围 | 通用最小充分知识地图 | 依据丘赛与AI价值筛选的考试专题 |

这个专题不修改 Foundations 内的任何文章，也不会让旧章节搬家；打开顶部 **Yau Contest** 就是一套自足的课程。

## 四、从计算题到证明题：一个最小例子

在原来的线性代数课中，题目可能是：计算矩阵

$$
A=\begin{pmatrix}2&0\\0&5\end{pmatrix}
$$

的特征值。按行列式公式算出 $2,5$ 就结束了。

丘赛式问题可能是：**证明**对于任意实对称矩阵 $A$，单位向量 $x$ 的二次型 $x^TAx$ 一定落在最小与最大特征值之间。

这里的核心不是求根，而是：

1. 写出假设：$A=A^T$，因此可以正交对角化 $A=Q\Lambda Q^T$。
2. 作代换：$y=Q^Tx$，所以 $\|y\|_2=1$。
3. 计算：$x^TAx=\sum_i\lambda_i y_i^2$。
4. 用 $\sum_i y_i^2=1$ 把它解释为特征值的加权平均。
5. 下结论：$\lambda_{\min}\le x^TAx\le\lambda_{\max}$；并说明取对应单位特征向量时等号可达。

这就是这套课程要培养的技能：**每一步都知道凭什么成立**。

## 五、三周怎么安排

下面以每周 8–12 小时为例；不是说三周后必然达到获奖水平，只是完成第一轮基础重建。

| 周次 | 主要章节 | 练习和验收 |
| --- | --- | --- |
| Week 1 | 00、01、02 | 亲手证明谱定理的常用推论、范数不等式、SVD最小二乘，做 2021 Problem 4 |
| Week 2 | 03、04 | 做幂法/线性迭代的误差推导，完成 2017 Problem 4(a)(b)、2020 Problem 3、2021 Problem 3 |
| Week 3 | 05、06 | 证明Newton局部二次收敛，处理 2017 Problem 2、2022 Problem 2，独立限时测评并复盘 |

!!! tip "如何判断学会了"
    不以“读完”或“代码能跑”为标准，而以以下四项为标准：**符号能解释、条件能列全、证明能独立写、反例能说出**。证明卡住时，先回本专题对应章节，不要求你跳回 Foundations。

## 六、历年真题怎么对照

本专题题目索引依照你上传的 **2010–2026历年笔试真题** 中应用与计算数学的个人笔试整理。**2010–2011年的命题安排与后续年份不同**，本阶段优先参考2012年以后的独立应用与计算数学卷。

| 真题 | 为什么纳入 Stage 1 | 学习入口 |
| --- | --- | --- |
| 2016 Problem 4 | 位移反幂法与扰动 | [Linear Iterations & Power Method](03-linear-iterations-power.md) |
| 2017 Problem 2 | Steffensen加速与二次收敛 | [Newton's Method & Convergence Order](05-newton-convergence.md) |
| 2017 Problem 4 | 线性迭代必要充分条件、谱半径 | [Linear Iterations & Power Method](03-linear-iterations-power.md) |
| 2020 Problem 3 | 幂法收敛 | [Linear Iterations & Power Method](03-linear-iterations-power.md) |
| 2021 Problem 3 | 标量不动点、唯一解及误差次数 | [Fixed Points & Contractions](04-fixed-points-contractions.md) |
| 2021 Problem 4 | 秩亏矩阵、SVD最小范数解 | [SVD & Least Squares](02-svd-least-squares.md) |
| 2022 Problem 2 | 二维不动点迭代 | [Fixed Points & Contractions](04-fixed-points-contractions.md) |
| 2022 Problem 3 | 对角占优、矩阵范数、可逆性 | [Matrix Norms & Spectral Theory](01-matrix-norms-spectral.md) |
| 2023 Problem 3 | 幂法与迭代条件 | [Linear Iterations & Power Method](03-linear-iterations-power.md) |
| 2025 Problem 2 | 三对角矩阵与谱半径 | [Matrix Norms & Spectral Theory](01-matrix-norms-spectral.md) |
| 2026 Problem 4 | 位移QR迭代（进阶选做） | [Stage 1 Exam Workbook](06-stage-one-workbook.md) |
| 2026 Problem 5 | 奇异值与矩阵不动点 | [SVD & Least Squares](02-svd-least-squares.md) |

!!! note "关于年份和题目"
    每一年的问题可能包含多个小问；表中仅表示与本阶段**有关的部分**，不是说本专题学完就能保证整道题全解。原始试卷以你提供的官方真题压缩包为准，本专题的讲解例题是重新编写的教学题，不冒充原题。

## 七、从哪里开始

如果你离开数学课程已经一段时间，从 [Proof Skills & Notation](00-proof-skills-notation.md) 开始；如果矩阵乘法和导数仍熟悉，可以阅读每章的“起点小测”，答不出才回头补。

**导航**：[Proof Skills & Notation →](00-proof-skills-notation.md)
