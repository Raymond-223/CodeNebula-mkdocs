# Content Audit Report

## Audit Scope

本轮审校覆盖全站 88 个 Markdown 页面，重点重构独立的 `Yau Contest` 专题，并复核 `Foundations / Mathematics`、`Foundations / Control Theory` 以及报告中点名的 Robotics、Machine Learning、Multi-Agent Systems、Distributed Systems 与首页统计。标题、导航、公式、证明依赖、代码示例和静态资源均纳入检查。

## V8 Corrections

针对 v7 复核报告，本轮又完成以下确定性修正：

- 修正割线法误差对数递推的斐波那契下标，并用两步映射 $G(r)=(2r+1)/(r+1)$ 的压缩性补全比值极限证明；
- 把开区间不完备的反例改为 $x_k=1/(k+1)$，确保每一项都在 $(0,1)$ 中；
- 修正严格对角占优证明和压缩映射例题中误写成逗号的乘法；
- 把最小二乘正交性检查修正为 $A^Tr=0$，并明确超定系统不必然无解；
- 修正幂法与 Richardson 练习提示，并为五道题增加“关键转化”和折叠完整解答；
- 为反幂法明确增加 $\mu\notin\sigma(A)$；
- 同步 SVD 拆分后的章节介绍，清理低秩逼近证明的编辑残留并明确完整左奇异向量基上的求和范围；
- 在线性代数定理之前补充张成、线性无关、基、维数和完整三元高斯消元；在 Taylor 与投影部分增加可独立复算的小例题；
- 将机器学习训练机制与 CNN/RNN/Attention/Transformer 拆成两章，新增两层网络反向传播、卷积、循环状态和 Attention 的数值计算；
- 收紧路径规划中的 Dijkstra 扩展范围、RRT 步长度量、目标偏置、碰撞余量、采样次数和预测视界等适用条件。

## Yau Contest Reconstruction

专题从面向零基础读者的定义和计算起步，不再采用提纲、复习清单或考试策略式写法。页面 H1 和导航保留英文；H2/H3 改为中文知识点名称，重要术语在括号内标出英文。

当前知识链为：

1. `Proof Language & Calculus`：量词、证明方法、偏导数、实数完备性、极值与介值定理、中值定理、Taylor theorem、复数与代数基本定理；
2. `Matrix Norms & Spectral Theory`：矩阵乘法、Gaussian elimination、行列式、秩－零化度、有限维范数等价、spectral theorem、Rayleigh quotient、正定性、矩阵范数、spectral radius 与 Gershgorin theorem；
3. `SVD & Least Squares`：正交投影、最佳逼近、最小二乘正规方程、SVD 的推导和手工计算；
4. `Pseudoinverse & Low-Rank Approximation`：pseudoinverse、全部最小二乘解、minimum-norm solution、条件数、正规方程稳定性与 Eckart–Young theorem；
5. `Linear Iterations & Power Method`：迭代矩阵、谱半径收敛判据、Jacobi、Gauss–Seidel、Richardson、power method 与 inverse iteration；
6. `Fixed Points & Contractions`：完备度量空间、Banach fixed-point theorem、先验和后验误差界、迭代次数与二维推广；
7. `Newton's Method & Convergence Order`：Newton 法推导、局部二次收敛、重根反例、secant method、Steffensen acceleration 与多元 Newton；
8. `Worked Problems`：十一道完整推导题和进一步练习。

原先过长的 SVD 页面已经拆分为两个连续章节。每章练习增加默认折叠的“第一步提示”，但完整解答仍放在证明栏中，避免正文退化成答案清单。

## Mathematical Rigor

主要修正包括：

- 区分存在性、唯一性、稳定性和收敛性，不再混用这些结论；
- 给出秩－零化度、基扩充、标准正交基扩充、有限维范数等价、诱导范数、谱定理、Gershgorin theorem 等结果的证明；
- 用 $C[0,1]$ 上的上确界范数与积分范数说明无限维范数不等价，并明确有限维证明依赖紧致性；
- 从 $A^TA$ 的 spectral theorem 构造 SVD，逐步推导 pseudoinverse、全部最小二乘解、唯一最小范数解和低秩逼近；
- 证明 $\rho(B)<1\iff B^k\to0$，并区分谱半径收敛和非正规矩阵的瞬态放大；
- 完整证明 Banach fixed-point theorem，区分先验与后验误差界，并在二维闭区域上验证 self-map、Jacobian norm、唯一不动点和迭代次数；
- 以 Taylor remainder 建立 Newton 法的不变邻域和局部二次收敛，补充重根、错误初值等反例；
- 把 $|g'(x)|<1$ 修正为局部吸引的充分条件，并用 $g(x)=x-x^3$ 说明它不是必要条件；
- 修正 Markov 链第二特征值的代码、全变差距离定义，以及 M/M/1 在 $\lambda=\mu$ 时的零常返结论；
- 修正四邻域网格的最大相对路径误差、RRT 复杂度表述和路径参数化的加速度公式；
- 删除通信成功率、时延阈值、丢包性能等缺少模型假设的普适数值结论；
- 把伪 CAS 示例改为带锁的进程内原子操作，并说明数据库中必须使用原子条件更新、事务或原生 CAS；
- 修正单输入单输出可控/可观模态的适用条件，并给出重特征值反例和一般 rank/PBH 判据。

## Proof and Dependency Audit

所有明确标记为定理、命题、引理或推论的证明都放在 `??? proof` 折叠栏中，并默认关闭。知识依赖按照下列方向排列：

1. 逻辑与数系 → 微积分基本定理 → Taylor 余项；
2. 线性方程组与线性空间 → 范数 → 谱理论；
3. 正交投影 → 最小二乘 → SVD → 伪逆 → 低秩逼近；
4. 谱半径 → 线性定常迭代 → 幂法与反幂法；
5. 完备性与压缩映射 → Banach theorem → 误差估计与二维推广；
6. Taylor 公式 → Newton 收敛 → 重根、割线法与 Steffensen 加速。

原先提前使用 spectral theorem、singular value、multivariate integral 与 divided-difference continuity 的位置已改写或调序。自动检查固定了关键知识的出现顺序，并检查每个定理在下一个定理或二级标题前具有非空、默认关闭的证明栏。

## Formula and Rendering Verification

Yau Contest 各页构建后的数学节点数量如下：

| Page | Math expressions | Proof blocks |
| --- | ---: | ---: |
| Proof Language & Calculus | 298 | 12 |
| Matrix Norms & Spectral Theory | 353 | 17 |
| SVD & Least Squares | 141 | 5 |
| Pseudoinverse & Low-Rank Approximation | 149 | 7 |
| Linear Iterations & Power Method | 220 | 6 |
| Fixed Points & Contractions | 225 | 7 |
| Newton's Method & Convergence Order | 252 | 6 |
| Worked Problems | 150 | 11 |
| Overview | 23 | 0 |

MathJax 3.2.2 已随项目保存在 `docs/vendor/mathjax/`，网站不再依赖外部 CDN。浏览器实测 Newton 页面生成 504 个 `mjx-container` 节点，6 个 proof 折叠栏均保持关闭；新建的 Neural Network Architectures 页面生成 122 个数学节点。在 375×844 的窄屏视口下没有页面级横向溢出，控制台无 warning 或 error。

## Automated Checks

`scripts/check_docs.py` 检查：

- 页面 H1 为英文，非通用导航标签与 H1 一致；
- H2/H3 为中文知识点名称，不使用问句式、对话式或含公式标题；
- Yau 理论章节达到最低讲解深度，定理均具有默认关闭的证明栏；
- 关键知识按依赖次序出现，综合题解答不以展开标题泄漏；
- 公式分隔符、站内链接、导航文件、图片资源和字符编码有效；
- 每个普通理论页面至多保留两个可运行演示，防止正文退化为代码堆积；
- 定向运行 Markov 示例，并回归验证网格误差、可控性反例、非正规矩阵瞬态增长和导数等于 1 的不动点反例。

`scripts/test_numeric_examples.py` 使用独立断言执行上述数值回归，运行时 warning 被视为错误。本轮又加入割线法斐波那契恒等式、最小二乘残差正交性、压缩映射迭代次数和两层网络有限差分梯度回归。

## Current Scale and Validation

- 12 个主课程 Section，另有独立 Yau Contest；
- 63 篇主课程核心章节，另有 2 篇机器学习补充页和 8 篇 Yau 内容页；
- 88 个 Markdown 页面；
- 65 张本地 SVG；
- 60 个 Python 示例；
- 72 个 proof 折叠栏，全部默认关闭。

`python scripts/check_docs.py` 与 `python -m mkdocs build --strict` 均通过。严格构建没有报告失效页面、失效锚点或 Markdown 警告。
