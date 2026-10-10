# Machine Learning & Neural Network Basics

> 后面的 DQN、Actor–Critic、目标检测、分割、RNN 和 Transformer 都默认你知道这一章。这里不讲完整机器学习课程，只建立后文不再重复解释的最小前置。

## 一、机器学习到底在学什么

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

## 三、训练、验证、测试为什么必须分开

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

## 七、正则化、Dropout 和归一化

为了减少过拟合，常见方法包括：

- **weight decay / L2 正则**：惩罚过大的权重；
- **dropout**：训练时随机屏蔽一部分神经元，减少对单一路径的依赖；
- **data augmentation**：对输入做合理变换，扩大有效训练分布；
- **early stopping**：验证集不再改善就停止。

输入数值尺度差异很大时，还要先做**归一化/标准化**，否则梯度在不同方向上的尺度差异会让优化变困难。

## 八、CNN：为什么图像不用普通 MLP

图像 $H\times W\times C$ 的像素很多，普通全连接层会产生海量参数，而且完全忽略“相邻像素更相关”的结构。

卷积神经网络 **CNN** 用一个小窗口在整张图上共享同一组权重：

- **局部连接**：只看附近区域；
- **权重共享**：同一个卷积核在不同位置重复使用；
- 因而参数少，并天然适合提取边缘、纹理、局部形状。

卷积层输出通常叫 **feature map**。随着层数增加，感受野变大，特征从边缘逐步变成更高层语义。

## 九、RNN：为什么序列需要“记住前面”

对时间序列，只看当前 $x_t$ 往往不够。循环神经网络写成

$$
h_t=f(h_{t-1},x_t),
$$

$h_t$ 是**隐藏状态**，把过去压缩成当前记忆。LSTM/GRU 是更稳定的 RNN 变体，用门控缓解长序列训练中的梯度消失。

后面的 POMDP、轨迹预测和多传感器时序融合都会用到这个思路。

## 十、Attention 与 Transformer：让每个位置自己决定该看谁

RNN 必须按时间一步一步处理。Attention 的思路不同：每个位置直接对其他位置算“相关程度”。

最核心形式是

$$
\operatorname{Attention}(Q,K,V)
=\operatorname{softmax}\!\left(\frac{QK^\top}{\sqrt d}\right)V.
$$

可以把它理解为：

- $Q$（query）：我现在想找什么；
- $K$（key）：每个位置能提供什么索引；
- $V$（value）：真正要取回的信息；
- $QK^\top$：匹配程度；
- softmax：把匹配程度归一化成权重。

**Transformer**就是把多头 Attention、前馈网络、残差连接和归一化等模块堆起来。它本身不知道顺序，因此序列任务通常还要加入位置编码。

后文看到 DETR、视觉 Transformer、序列 Transformer 时，不需要重新把它当成一种神秘模型：核心仍是“按相关性加权汇总信息”。

## 十一、进入后续章节前应会的最小词表

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
| CNN | 利用局部连接和权重共享处理图像 |
| RNN | 用隐藏状态处理序列 |
| Attention | 按相关性从其他位置汇总信息 |
| Transformer | 以 Attention 为核心的序列/视觉架构 |
| overfitting | 训练集很好、未见数据变差 |

做到这里，后面的 DQN、Actor–Critic、检测、分割、RNN 与 Transformer 才算有完整前置。
