# Neural Network Architectures

上一章解释网络怎样训练。本章只回答结构问题：图像为什么使用卷积，序列为什么需要状态，Attention 怎样计算相关性，以及 Transformer 在 Attention 外还增加了什么。每一部分先手算最小例子，再说明适用范围。

## 卷积神经网络（Convolutional Neural Network）

图像 $H\times W\times C$ 的相邻像素通常比相距很远的像素关系更强。若直接把所有像素接入全连接层，不仅参数很多，也没有利用这种局部结构。卷积神经网络（CNN）使用两个约束：

- 局部连接：一个输出只读取输入的一小块区域；
- 权重共享：同一个卷积核在所有空间位置使用相同参数。

### 一维卷积的手算

先用一维例子理解运算。输入和卷积核分别为

$$
x=(1,2,0,3),\qquad k=(2,-1).
$$

取步幅（stride）为 $1$，不补零。卷积核依次覆盖 $(1,2)$、$(2,0)$、$(0,3)$，得到

$$
y_1=2\cdot1-1\cdot2=0,
$$

$$
y_2=2\cdot2-1\cdot0=4,
$$

$$
y_3=2\cdot0-1\cdot3=-3.
$$

所以输出是 $y=(0,4,-3)$。深度学习库通常实现的是互相关运算，即不把核翻转；只要训练和推理使用同一约定，不影响权重学习。

若输入长度为 $N$、核大小为 $K$、两侧各补 $P$ 个零、步幅为 $S$，输出长度为

$$
N_{\mathrm{out}}
=\left\lfloor\frac{N+2P-K}{S}\right\rfloor+1.
$$

这个公式应在搭网络时逐层检查，否则张量尺寸会在拼接或全连接层处不匹配。

### 二维卷积与通道

对彩色图像，卷积核的深度必须覆盖全部输入通道。若输入有 $C_{\mathrm{in}}$ 个通道、输出要产生 $C_{\mathrm{out}}$ 张特征图，核大小为 $K_h\times K_w$，则权重参数量为

$$
K_hK_wC_{\mathrm{in}}C_{\mathrm{out}},
$$

若每个输出通道还有一个偏置，再加 $C_{\mathrm{out}}$。例如 $3\times3$ 核把 RGB 的 3 通道变成 16 通道，参数量为 $3\cdot3\cdot3\cdot16+16=448$，与输入图像的高宽无关。

多层卷积让感受野逐渐扩大：前层可响应边缘，后层组合出纹理和物体部件。池化或带步幅卷积会降低空间分辨率，但也可能丢失小目标信息，因此检测和分割网络常使用多尺度特征。

## 循环神经网络（Recurrent Neural Network）

时间序列中，当前输出可能依赖过去输入。循环神经网络（RNN）用隐藏状态保存历史摘要：

$$
h_t=\tanh(W_hh_{t-1}+W_xx_t+b),
\qquad
y_t=W_yh_t+c.
$$

相同的 $W_h,W_x$ 在每个时刻重复使用，这就是时间维度上的权重共享。

### 隐藏状态的手算

取标量模型

$$
h_t=\tanh(0.5h_{t-1}+x_t),
\qquad h_0=0,
$$

输入 $x_1=1,x_2=0$。则

$$
h_1=\tanh(1)\approx0.7616,
$$

$$
h_2=\tanh(0.5\times0.7616)
\approx\tanh(0.3808)\approx0.3634.
$$

虽然第二步输入为零，$h_2$ 仍保留第一步的信息。若不断对很长序列反向传播，梯度会反复乘 $W_h$ 和激活函数导数：乘积的模小于 1 时梯度消失，大于 1 时可能爆炸。LSTM 和 GRU 用门控路径缓解这个问题，但并不保证任意长依赖都能无损保留。

RNN 适合在线、按时间到达的数据；缺点是第 $t$ 步依赖第 $t-1$ 步，难以把整个序列完全并行处理。

## 注意力（Attention）

Attention 不把全部历史压进一个固定隐藏状态，而是让每个查询位置直接从一组位置中加权取值。缩放点积注意力为

$$
\operatorname{Attention}(Q,K,V)
=\operatorname{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V.
$$

矩阵尺寸为

$$
Q\in\mathbb R^{n_q\times d_k},\quad
K\in\mathbb R^{n_k\times d_k},\quad
V\in\mathbb R^{n_k\times d_v}.
$$

因此 $QK^T$ 是 $n_q\times n_k$ 的分数矩阵；softmax 对每一行做归一化；最终输出是 $n_q\times d_v$。

### 单个查询的数值计算

取

$$
q=(1,0),\quad
k_1=(1,0),\quad k_2=(0,1),\quad
v_1=(2,0),\quad v_2=(0,4).
$$

这里 $d_k=2$，所以缩放后的分数是

$$
s_1=\frac1{\sqrt2},\qquad s_2=0.
$$

softmax 权重为

$$
\alpha_1=\frac{e^{1/\sqrt2}}{e^{1/\sqrt2}+1}\approx0.6698,
\qquad
\alpha_2\approx0.3302.
$$

输出是值向量的加权和：

$$
o=\alpha_1v_1+\alpha_2v_2
\approx(1.3396,1.3208).
$$

这个例子把术语对应到具体计算：query 决定查什么，key 决定匹配分数，value 决定实际汇总的内容。除以 $\sqrt{d_k}$ 是为了避免维数增大时点积尺度过大，使 softmax 过早饱和。

## Transformer 的组成

Transformer 不等于单独一层 Attention。一个典型块还包括：

1. 多头注意力（multi-head attention）：把特征投影到多个子空间，分别计算 Attention 后再拼接；
2. 前馈网络（feed-forward network）：对每个位置独立应用同一个两层 MLP；
3. 残差连接（residual connection）：把模块输入直接加到输出，改善深层优化；
4. 层归一化（layer normalization）：控制每个样本特征维度的尺度；
5. 位置编码（positional encoding）：补充顺序信息，因为普通 self-attention 本身不区分位置排列。

自注意力（self-attention）令 $Q,K,V$ 都来自同一序列；交叉注意力（cross-attention）让查询来自一个序列，而键和值来自另一个序列。因果语言模型还会使用上三角掩码，阻止当前位置读取未来 token。

标准 self-attention 的分数矩阵大小为 $n\times n$，时间和显存通常随序列长度呈二次增长。长序列模型会使用稀疏、分块或低秩近似等结构减少代价；这些方法改变的是计算方式，不改变“按相关性加权汇总值向量”的基本概念。

## 结构选择与适用范围

| 数据结构 | 常用结构 | 主要归纳偏置 | 主要限制 |
| --- | --- | --- | --- |
| 图像与局部空间信号 | CNN | 局部性、平移共享 | 长距离关系需多层传播 |
| 在线时间序列 | RNN / GRU / LSTM | 递归状态、时间共享 | 串行计算、长依赖困难 |
| 全局序列或集合关系 | Transformer | 内容相关的全局汇总 | 标准注意力为二次复杂度 |

这张表不是排他规则。视觉 Transformer 可以处理图像，卷积也能处理一维序列；选择取决于数据量、延迟、序列长度和任务需要的归纳偏置。

## 练习

1. 对输入 $(2,1,3,0)$ 和核 $(1,-1)$ 计算不补零、步幅 1 的一维卷积输出。
2. 计算 $5\times5$ 单通道输入经过 $3\times3$ 核、补零 1、步幅 2 后的输出宽度。
3. 对 $h_t=0.5h_{t-1}+x_t$、$h_0=0$ 和输入 $(2,0,0)$ 计算三个隐藏状态。
4. 取 $q=(0,1)$，沿用本章的 $k_1,k_2,v_1,v_2$，计算 Attention 输出。

??? tip "第一步提示"

    第 1 题逐个滑动长度为 2 的窗口。第 2 题代入输出尺寸公式。第 3 题按时间顺序回代。第 4 题先算两个缩放点积，再做 softmax。

??? tip "关键转化"

    第 4 题中 $q$ 与 $k_2$ 完全对齐，因此第二个分数高于第一个；输出应更靠近 $v_2$，这可作为数值结果的方向检查。

??? proof "完整解答"

    第 1 题输出为 $(1,-2,3)$。第 2 题为 $\lfloor(5+2-3)/2\rfloor+1=3$。第 3 题依次为 $2,1,0.5$。第 4 题的权重顺序与正文互换，因此输出约为 $(0.6604,2.6792)$。

**上一章：** [机器学习训练基础](01-ml-neural-network-basics.md)  
**后续方向：** [价值方法与 DQN](../reinforcement-learning/02-value-based.md)、[Actor–Critic](../reinforcement-learning/03-policy-actor-critic.md) 或 [Perception](../../robotics-perception/perception/index.md)
