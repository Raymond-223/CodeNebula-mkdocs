# 策略梯度、Actor–Critic 与 PPO

价值方法先估计“动作有多好”，再选最大值；策略方法则直接学习一个参数化策略 $\pi_\theta(a\mid s)$。这使它天然适合随机策略和连续动作，但也带来更高的梯度方差。

## 策略目标与梯度

目标可以写成期望回报：

$$
J(\theta)=\mathbb E_{\tau\sim\pi_\theta}[G_0].
$$

策略梯度的核心形式为

$$
\nabla_\theta J(\theta)
=
\mathbb E\left[
\nabla_\theta\log\pi_\theta(a_t\mid s_t)
\,Q^{\pi}(s_t,a_t)
\right].
$$

直观理解很简单：

- 如果一次动作带来较高长期回报，就提高它在类似状态下的概率；
- 如果表现差，就降低它的概率。

这里使用 $\nabla\log\pi$ 的好处，是不需要知道环境转移模型的导数，只需要能从策略采样。

## Baseline 与方差降低

直接使用回报做权重通常方差很大。可以减去一个只依赖状态的 baseline：

$$
Q^\pi(s,a)-V^\pi(s)=A^\pi(s,a).
$$

$A^\pi(s,a)$ 称为 advantage，表示“这个动作相比当前状态下的平均水平好多少”。

只要 baseline 不依赖当前采样动作，它不会改变策略梯度的期望方向，却能明显降低方差。因此 $V^\pi(s)$ 是最自然的 baseline。

## Actor–Critic 架构

Actor–Critic 把两件事拆开：

- **Actor**：策略 $\pi_\theta$，决定动作；
- **Critic**：价值函数 $V_\phi$ 或 $Q_\phi$，评价当前策略。

![Actor-Critic 架构](../img/06-actor-critic.png)

最简单情况下，Critic 的 TD error

$$
\delta_t=r_{t+1}+\gamma V_\phi(s_{t+1})-V_\phi(s_t)
$$

可以作为 advantage 的一个低成本估计，然后 Actor 使用

$$
\theta\leftarrow
\theta+\alpha\,\delta_t\nabla_\theta\log\pi_\theta(a_t\mid s_t).
$$

它的逻辑可以写成两条互相配合的更新：

$$
\delta_t=r_{t+1}+\gamma V_\phi(s_{t+1})-V_\phi(s_t),
$$

$$
\theta\leftarrow\theta+\alpha_\theta\delta_t
\nabla_\theta\log\pi_\theta(a_t\mid s_t),
\qquad
\phi\leftarrow\phi-\alpha_\phi\nabla_\phi\delta_t^2.
$$

Critic 先用 TD error 衡量“结果比预期好还是差”，Actor 再据此提高或降低所选动作的概率。两者共享同一个评价信号，但优化的对象不同。

Critic 引入了自举偏差，但换来了更低方差和更高样本利用率。

## PPO 的更新约束

策略梯度最大的问题之一，是参数一步改得过大时，采样数据很快变成“旧策略的数据”，性能甚至可能突然崩掉。

PPO 先定义新旧策略对同一动作的概率比：

$$
\rho_t(\theta)=
\frac{\pi_\theta(a_t\mid s_t)}
{\pi_{\theta_{old}}(a_t\mid s_t)}.
$$

再使用裁剪目标：

$$
L^{CLIP}(\theta)=
\mathbb E_t\left[
\min\left(
\rho_t(\theta)\hat A_t,
\operatorname{clip}(\rho_t(\theta),1-\varepsilon,1+\varepsilon)\hat A_t
\right)
\right].
$$

![PPO 裁剪目标函数](../img/06-ppo-clip.png)

当某个更新已经把概率比推得很远时，继续沿“让代理目标更大”的方向推进不会继续得到同样收益，因此梯度会被抑制。

需要注意：**clip 不是硬约束**。它不能保证所有状态动作上的概率比始终落在 $[1-\varepsilon,1+\varepsilon]$ 内，只是用一个简单的代理目标降低过大更新的风险。

## 优势估计的偏差—方差权衡

只看一步 TD error 方差低，但偏差依赖 Critic；直接使用完整回报偏差小，但方差大。GAE 用参数 $\lambda$ 把多步 TD error 加权起来：

$$
\hat A_t^{GAE}
=
\sum_{l=0}^{\infty}(\gamma\lambda)^l\delta_{t+l}.
$$

因此它的作用不是增加一个新的学习目标，而是**给 PPO/Actor–Critic 提供更平滑的 advantage 估计**。

## 连续动作与随机策略

在连续动作空间里，无法像 DQN 那样枚举所有动作并取最大值。Actor 可以直接输出动作分布参数，例如高斯分布的均值和方差，再从中采样控制量。

SAC 是一个代表性方法：它在回报目标之外加入策略熵，鼓励策略在学习阶段保持一定随机性：

$$
J(\pi)=\mathbb E\left[\sum_t
\gamma^t\big(r_{t+1}+\alpha\mathcal H(\pi(\cdot\mid s_t))\big)
\right].
$$

对入门学习而言，不需要继续展开 DDPG、TD3、TRPO 等算法谱系。真正需要掌握的是：

> **Policy Gradient 给出方向；Critic 降低估计方差；PPO 控制更新尺度；SAC 展示连续控制中的随机 Actor–Critic。**

## 策略改进与数据有效期

策略更新后，旧策略采集的数据与新策略分布之间会出现偏差。PPO 的概率比正是用来衡量样本在新旧策略下的相对权重；更新过大时，旧数据就不再能可靠代表当前策略。因此每批数据可重复使用多少次，应和策略变化幅度一起判断。
