# Content Audit Report

## Audit Scope

本轮审校覆盖独立的 `Yau Contest` 专题、`Foundations / Mathematics`、`Foundations / Control Theory`，并检查由标题变更影响的站内链接、导航和公式渲染配置。

## Yau Contest Reconstruction

原专题具有三个结构问题：先修内容被追加在章节末尾；证明、学习建议和考试策略混排；若干高级术语只被点名，没有形成可计算、可证明的知识链。本轮将全部八个页面按教材结构重写。

当前内容为：

1. `Proof Language & Calculus`：量词、逻辑、证明方法、极限、完备性、导数、Taylor theorem 与收敛阶；
2. `Matrix Norms & Spectral Theory`：向量范数、诱导矩阵范数、次乘性、spectral radius、spectral theorem、Rayleigh quotient、正定性与 Gershgorin theorem；
3. `SVD & Least Squares`：正交投影、正规方程、SVD 构造、pseudoinverse、全部最小二乘解、minimum-norm solution 与 low-rank approximation；
4. `Linear Iterations & Power Method`：误差矩阵、谱半径充要条件、Jordan block 证明、stationary iterations 与 power method；
5. `Fixed Points & Contractions`：完备度量空间、Banach fixed-point theorem 的完整证明、先验与后验误差界，以及二维压缩映射算例；
6. `Newton's Method & Convergence Order`：带余项的局部二次收敛证明、重根、secant method、Steffensen acceleration 与多元 Newton；
7. `Worked Problems`：十一道完整推导题和进一步练习。

删除了学习日程、通关标准、错题复盘和按年份刷题等复习资料结构。没有后续用途且未展开的术语也已删除；保留的算法均给出定义、成立条件或后续练习。

## Mathematical Rigor

主要修正包括：

- 把存在性、唯一性和迭代收敛性分为不同命题；
- 给出 $\rho(B)<1\iff B^k\to0$ 对不可对角化矩阵的 Jordan block 证明；
- 给出 SVD 从 $A^TA$ 的 spectral theorem 出发的构造，并逐项检查矩阵尺寸；
- 推导全部 least-squares solutions 与唯一 minimum-norm solution；
- 证明 Eckart–Young theorem 在 operator norm 与 Frobenius norm 下的最佳低秩误差；
- 完整证明 Banach fixed-point theorem，并区分先验和后验误差界；
- 在二维闭区域上逐项验证 self-map、Jacobian norm、唯一不动点和迭代次数；
- 使用 Taylor remainder 建立 Newton invariant neighborhood，而不是只给渐近展开；
- 对重根、错误初值、非正规矩阵瞬态放大等情况给出反例。

## Heading Normalization

- 顶部导航和页面 H1 使用英文；
- 全站 H2/H3 使用中文知识点名称，重要英文术语仅作为括号内标准名称保留；
- 问句式、对话式和“复习资料式”标题改为知识点名称；
- 公式不再出现在 Yau Contest 的 H2/H3 中，降低目录与锚点渲染风险；
- 为 `Gradient, Jacobian and Hessian` 与 `Lie Group boxplus` 设置稳定显式锚点，并修复 Robotics 中的旧链接。

## Formula Verification

八个 Yau 页面中的 display-math 分隔符全部成对，行内公式没有未闭合美元符号。构建后生成的 `arithmatex` 节点数量与 Markdown 源公式数量逐页一致：

| Page | Math expressions |
| --- | ---: |
| Proof Language & Calculus | 144 |
| Matrix Norms & Spectral Theory | 133 |
| SVD & Least Squares | 197 |
| Linear Iterations & Power Method | 130 |
| Fixed Points & Contractions | 179 |
| Newton's Method & Convergence Order | 144 |
| Worked Problems | 150 |
| Overview | 23 |

## Automated Checks

`scripts/check_docs.py` 新增以下约束：

- 页面 H1 必须为英文；
- 非通用导航标签应与页面 H1 一致；
- 全站不允许问句式或对话式 H2/H3，并要求二级及以下标题包含中文；
- Yau Contest 的小标题不允许嵌入行内公式；
- Yau 理论章节必须达到最低讲解深度；
- 检测 Unicode replacement character，防止编码损坏；
- 检测未被讲解、也未被使用的高级术语重新进入专题。

## Current Scale and Validation

- 12 个主课程 Section，另有独立 Yau Contest；
- 63 篇主课程核心章节；
- 86 个 Markdown 页面；
- 60 张本地 SVG；
- 60 个 Python 示例。

静态内容检查通过，`mkdocs build --strict` 通过。构建过程没有报告失效页面、失效锚点或 Markdown 警告。
