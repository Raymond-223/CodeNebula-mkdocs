# 价值学习：Q-Learning 与 DQN

价值学习不直接输出“应该做什么”，而是先学习**每个动作的长期价值**，再从价值中选动作。Q-Learning 是最典型的表格方法，DQN 则把同一思想扩展到高维状态。

## TD 学习与自举目标

如果直接用完整回报 $G_t$ 更新 $V(s_t)$，必须等未来真正发生。TD 的做法是只走一步，就用当前估计构造目标：

$$
y_t=r_{t+1}+\gamma V(s_{t+1}).
$$

TD 误差为

$$
\delta_t=r_{t+1}+\gamma V(s_{t+1})-V(s_t),
$$

然后更新

$$
V(s_t)\leftarrow V(s_t)+\alpha\delta_t.
$$

它一半来自真实采样，一半来自自己的估计，因此称为 **bootstrapping（自举）**。优点是可以在线更新，代价是目标本身也在变化。

## Q-Learning 更新

Q-Learning 用最优下一动作构造 TD 目标：

$$
y_t=r_{t+1}+\gamma\max_{a'}Q(s_{t+1},a').
$$

更新为

$$
Q(s_t,a_t)\leftarrow Q(s_t,a_t)
+\alpha\left[y_t-Q(s_t,a_t)\right].
$$

把更新拆开看更清楚：

$$
\underbrace{Q(s_t,a_t)}_{\text{当前估计}}
\leftarrow
\underbrace{Q(s_t,a_t)}_{\text{当前估计}}
+\alpha
\underbrace{\left(
\overbrace{r_{t+1}+\gamma\max_{a'}Q(s_{t+1},a')}^{\text{目标值}}
-Q(s_t,a_t)
\right)}_{\text{更新方向：TD error}}.
$$

当前估计回答“现在认为这个动作值多少”，目标值混合了即时奖励与下一状态的最优估计，二者之差决定应该上调还是下调。

这里最容易混淆的是：**执行时可以探索，学习目标仍然使用下一状态的最大 Q 值**。这就是它被称为 off-policy 的原因之一。

## 探索机制

如果每次都选择当前 $Q$ 最大的动作，早期一次错误估计可能让其他动作永远得不到尝试。

最常见的入门方法是 $\varepsilon$-greedy：

$$
a_t\sim
\begin{cases}
\text{在动作集合中随机选择}, & \text{概率 }\varepsilon,\\
\arg\max_a Q(s_t,a), & \text{概率 }1-\varepsilon.
\end{cases}
$$

探索解决“没有数据”的问题，价值更新解决“如何利用数据”的问题。两者不要混在一起理解。

在经典有限表格设定下，Q-Learning 的收敛需要包括状态—动作对持续被访问、合适的学习率序列和稳定 MDP 等条件；“用了 Q-Learning”本身并不自动保证收敛。

## 表格方法的适用边界

假设状态由 20 个连续量组成，就不可能给每种状态都单独存一个 Q 表条目。更重要的是，彼此相近的状态本应共享经验。

因此把表格替换为参数化函数：

$$
Q(s,a;\theta)\approx Q^*(s,a).
$$

神经网络的价值不只是“容量大”，而是能在相似输入之间形成**泛化**。

![DQN 网络结构](../img/05-dqn-network.png)

## DQN 的 Bellman 目标

DQN 的目标没有变，只是 Q 值由网络输出：

$$
y=r+\gamma\max_{a'}Q(s',a';\theta^-).
$$

在线网络参数是 $\theta$，目标网络参数是 $\theta^-$。训练损失可以写成

$$
L(\theta)=\mathbb E\left[(y-Q(s,a;\theta))^2\right].
$$

真正让 DQN 比“直接拿神经网络替 Q 表”稳定的，是两个工程结构。

### Experience Replay

把交互得到的 $(s,a,r,s')$ 先放进 replay buffer，再随机抽样，使训练样本更接近独立抽样。对一批样本，仍然最小化 Bellman 目标与当前预测之间的平方误差：

$$
L(\theta)=\frac{1}{|B|}\sum_{(s,a,r,s')\in B}
\left[r+\gamma\max_{a'}Q(s',a';\theta^-)-Q(s,a;\theta)\right]^2.
$$

随机抽样可以降低连续轨迹样本之间的强相关，并提高历史数据利用率。

### Target Network

如果同一个网络既产生预测值又立即产生学习目标，参数每更新一次，目标也跟着移动。目标网络用一份较慢更新的参数 $\theta^-$ 生成 TD target，让目标暂时更稳定。

它们不能从理论上保证深度 Q-Learning 一定收敛，但显著改善了实际训练稳定性。

## 价值方法的适用范围

价值方法特别适合**离散动作**：例如左/右/前进/停止，或有限个策略选项。得到 $Q(s,a)$ 后，只需比较各动作价值即可决策。

如果动作本身是连续值，例如转向角、力矩、速度，直接枚举 $\arg\max_a Q(s,a)$ 会变困难，这时策略方法通常更自然。

所以从 Q-Learning 到 DQN 最需要记住的不是算法名字，而是一条主线：

> **Bellman target → TD error → 价值更新 → 用价值选择动作。**

## 最大化偏差与过估计

当目标使用多个含噪价值估计的最大值时，取最大操作更容易选中偶然偏高的估计，从而产生系统性过估计。Double Q 思想把动作选择与动作评价部分分离，用来减弱这种偏差。它说明稳定训练不仅取决于损失函数，也取决于目标如何构造。
