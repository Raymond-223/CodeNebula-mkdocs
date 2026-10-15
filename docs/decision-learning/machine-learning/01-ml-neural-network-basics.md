# Machine Learning Training Basics

> 本章只建立训练机制：数据怎样进入模型、损失如何衡量错误、链式法则怎样产生梯度、优化器怎样更新参数。CNN、RNN、Attention 与 Transformer 的结构放在下一章。

开始前应能完成三类基础计算：矩阵乘向量、对一元复合函数使用链式法则、理解训练集与概率的基本含义。若其中任何一项不熟悉，先看 [线性代数与微积分基础](../../foundations/mathematics/01-linear-algebra-calculus.md) 和 [概率与随机变量](../../foundations/mathematics/04-probability-random-variables.md)。本章结束后先学习 [Neural Network Architectures](02-neural-network-architectures.md)，再进入 DQN、Actor–Critic 或视觉模型章节。

## 一、机器学习的目标

普通程序是“人写规则，机器执行”；机器学习是“给数据和评价标准，让参数自己调整”。

一条数据通常写成

$$
(x,y),
$$

其中 $x$ 是**输入/特征**（feature），$y$ 是希望预测的**目标/标签**（target/label）。模型写成

$$
\hat y=f_\theta(x),
$$

$\theta$ 是模型里允许训练改变的参数。

三类最常见问题：

- **回归**：预测连续值，如距离、温度、速度；
- **分类**：预测离散类别，如猫/狗、可行驶/不可行驶；
- **无监督学习**：没有人工标签，从数据本身找结构，如聚类、降维。

后面的深度学习与强化学习，本质上仍是在调整 $\theta$，只是“标签从哪里来”和“损失怎么定义”不同。

## 二、损失函数：模型必须知道“错了多少”

训练必须先把好坏变成一个数，这个数叫**损失函数**（loss）。

回归常用均方误差：

$$
L=\frac1N\sum_{i=1}^N(\hat y_i-y_i)^2.
$$

分类模型通常先输出一组未归一化分数 **logits** $z_1,\dots,z_C$，再用 softmax 变成概率：

$$
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}.
$$

若真实类别是 $y$，交叉熵损失为

$$
L=-\log p_y.
$$

预测正确且概率高，损失小；把错误类别说得越肯定，损失越大。

## 三、训练集、验证集与测试集

如果模型在训练数据上表现很好，不代表它学会了规律，也可能只是把样本记住。这叫**过拟合**（overfitting）。

所以数据通常分成：

- **training set**：真正参与参数更新；
- **validation set**：选择超参数、决定何时停止；
- **test set**：最后一次评价泛化能力，不能拿来反复调参。

训练误差继续下降但验证误差开始上升，就是典型过拟合信号。

## 四、Batch、Epoch 和学习率

一次把所有训练数据都算完再更新参数很贵，所以通常每次只取一小批样本，这一批叫 **mini-batch**。

- **batch size**：一次更新用多少样本；
- **iteration / step**：完成一次参数更新；
- **epoch**：整个训练集大致被遍历一遍；
- **learning rate**：每次更新走多大一步。

学习率太大可能发散，太小则训练非常慢。

## 五、神经网络：很多“线性变换 + 非线性”串起来

最简单的一层写成

$$
z=Wx+b,
$$

但如果一直只堆线性层，多层仍等价于一层线性变换。必须插入**激活函数**（activation），例如 ReLU：

$$
\operatorname{ReLU}(z)=\max(0,z).
$$

于是一个多层感知机 MLP 可以写成

$$
h_1=\sigma(W_1x+b_1),\qquad
\hat y=W_2h_1+b_2.
$$

这里：

- 输入层接收特征；
- 隐藏层学习中间表示；
- 输出层产生最终 logits、数值或动作参数。

## 六、反向传播不是另一种优化算法

模型训练要最小化 $L(\theta)$。梯度下降需要 $\nabla_\theta L$。网络可能有几百万个参数，手工逐个求导不现实。

**反向传播（backpropagation）**做的只是高效应用链式法则：从损失开始，沿计算图反向把梯度传给每个参数。

例如

$$
x\rightarrow z=wx\rightarrow \hat y=\sigma(z)\rightarrow L
$$

有

$$
\frac{\partial L}{\partial w}
=
\frac{\partial L}{\partial \hat y}
\frac{\partial \hat y}{\partial z}
\frac{\partial z}{\partial w}.
$$

之后优化器（SGD、Adam 等）才使用这个梯度更新参数。**反向传播负责算梯度，优化器负责用梯度走一步。** 两者不要混淆。

### 一次完整的数值反向传播

先用只有一个参数的模型把全过程算完。设输入 $x=2$、目标 $y=1$、初始权重 $w=0.5$，模型与平方损失为

$$
\hat y=wx,
\qquad
L=\frac12(\hat y-y)^2.
$$

**前向计算。** 当前预测为 $\hat y=0.5\times2=1$，损失为零，因此梯度也为零。这个例子没有产生更新，所以把目标改成 $y=3$：

$$
\hat y=1,
\qquad
L=\frac12(1-3)^2=2.
$$

**反向计算。** 沿计算图从右向左：

$$
\frac{\partial L}{\partial \hat y}=\hat y-y=-2,
\qquad
\frac{\partial \hat y}{\partial w}=x=2,
$$

所以

$$
\frac{\partial L}{\partial w}
=\frac{\partial L}{\partial\hat y}
\frac{\partial\hat y}{\partial w}
=(-2)\times2=-4.
$$

**参数更新。** 取学习率 $\eta=0.1$，梯度下降得到

$$
w_{\text{new}}=w-\eta\frac{\partial L}{\partial w}
=0.5-0.1(-4)=0.9.
$$

再次前向计算，$\hat y_{\text{new}}=0.9\times2=1.8$，新损失为 $\tfrac12(1.8-3)^2=0.72$，确实低于原来的 $2$。多层网络只是把这条“前向保存中间量—反向乘局部导数—优化器更新参数”的链变长，并把标量换成向量和矩阵。

### 两层网络的完整梯度

标量例子之后，再算一次真正含隐藏层的网络。设输入 $x=2$，隐藏层有两个神经元：

$$
z=W_1x+b_1,
\qquad h=\operatorname{ReLU}(z),
\qquad \hat y=W_2h+b_2,
$$

其中

$$
W_1=\begin{pmatrix}1\\-0.5\end{pmatrix},\quad
b_1=\begin{pmatrix}0\\2\end{pmatrix},\quad
W_2=\begin{pmatrix}3&-1\end{pmatrix},\quad b_2=0.
$$

取目标 $y=4$、损失 $L=\tfrac12(\hat y-y)^2$。前向计算为

$$
z=\begin{pmatrix}2\\1\end{pmatrix},\qquad
h=\begin{pmatrix}2\\1\end{pmatrix},\qquad
\hat y=3\cdot2-1\cdot1=5,\qquad L=\frac12.
$$

反向计算从标量损失开始。先有

$$
\frac{\partial L}{\partial\hat y}=\hat y-y=1.
$$

输出层的局部关系是 $\hat y=W_2h+b_2$，所以

$$
\frac{\partial L}{\partial W_2}
=\frac{\partial L}{\partial\hat y}h^T
=\begin{pmatrix}2&1\end{pmatrix},
\qquad
\frac{\partial L}{\partial b_2}=1,
$$

并把梯度传回隐藏向量：

$$
\frac{\partial L}{\partial h}
=W_2^T\frac{\partial L}{\partial\hat y}
=\begin{pmatrix}3\\-1\end{pmatrix}.
$$

两个 $z$ 分量都为正，因此 ReLU 在这里的导数都是 $1$，从而 $\partial L/\partial z=(3,-1)^T$。最后由 $z=W_1x+b_1$ 得

$$
\frac{\partial L}{\partial W_1}
=\frac{\partial L}{\partial z}x
=\begin{pmatrix}6\\-2\end{pmatrix},
\qquad
\frac{\partial L}{\partial b_1}
=\begin{pmatrix}3\\-1\end{pmatrix}.
$$

这次计算展示了反向传播的两个核心规则：线性层的权重梯度是“上游梯度乘输入”，传回输入的梯度要乘转置矩阵；激活层则按分量乘局部导数。更深的网络只是在重复这两步。

## 七、正则化、Dropout 和归一化

为了减少过拟合，常见方法包括：

- **weight decay / L2 正则**：惩罚过大的权重；
- **dropout**：训练时随机屏蔽一部分神经元，减少对单一路径的依赖；
- **data augmentation**：对输入做合理变换，扩大有效训练分布；
- **early stopping**：验证集不再改善就停止。

输入数值尺度差异很大时，还要先做**归一化/标准化**，否则梯度在不同方向上的尺度差异会让优化变困难。

## 八、进入网络结构前应会的最小词表

| 术语 | 最小含义 |
|---|---|
| feature / label | 输入信息 / 监督目标 |
| regression / classification | 连续值预测 / 类别预测 |
| parameter $\theta$ | 训练会改变的模型参数 |
| loss | 衡量预测错误的标量 |
| logits | softmax 前的未归一化分类分数 |
| softmax | 把 logits 变成和为 1 的分布 |
| cross entropy | 分类常用损失 |
| batch / epoch | 一次更新的数据量 / 全数据大致遍历一次 |
| backprop | 用链式法则高效计算梯度 |
| MLP | 全连接神经网络 |
| overfitting | 训练集很好、未见数据变差 |

做到这里，已经具备理解网络结构如何训练的前置。下一章将分别计算卷积、循环状态和 Attention，而不只列出术语。

**下一章：** [神经网络结构](02-neural-network-architectures.md)
