# CodeNebula

CodeNebula 是一套面向 **AI、Robotics 与 Autonomous Systems** 的紧凑型学习网站，使用 MkDocs Material 构建。

这一版采用“**最小充分知识体系 + 文章式讲解**”原则：只保留后续反复依赖、能够解释真实系统、或者删掉后会造成认知断层的内容。正文不是课程提纲，也不是算法百科，而是围绕一个具体主题逐层解释定义、机制、公式、例子和工程边界。

## Curriculum

站点由 **5 个知识域** 与 **Yau Contest 专题** 组成，共 **14 个 Section**、**73 篇正文**：

| 板块 | Section | 回答的问题 | 核心章数 |
|---|---|---|---:|
| Foundations | Mathematics, Control Theory | 系统如何表示、方法在什么条件下成立 | 13 |
| Decision & Learning | Reinforcement Learning, Game Theory, Multi-Agent Systems | 如何在交互中做序贯决策 | 16 |
| Robotics & Perception | Robotics, Perception | 如何感知世界并让本体动起来 | 10 |
| Systems & Simulation | Distributed Systems, Software Engineering, Simulation & Sim2Real | 如何让算法成为可运行、可观察、可恢复的系统 | 14 |
| Safety & Human Factors | Robustness & Safety, Human–AI Interaction | 条件变化、组件失效、与人协作时如何保持可接受行为 | 10 |
| Yau Contest | Stage 1: Matrix Theory & Iteration | 从大学数学起点重建竞赛所需的知识链 | 8 |

此外还有 **Machine Learning Foundations**（2 篇入门正文）。以上合计 **14 个 Section、73 篇正文**。

Yau Contest 与其余板块共用同一套写作与校验规范：定义—条件—完整证明—反例—手算例题—练习，定理与命题的证明统一收进默认关闭的 `proof` 折叠栏，并明确区分必要条件、充分条件与充要条件；导航与页面 H1 使用英文，正文使用中文并保留标准英文术语。它与其余板块的区别只在内容取向——竞赛需要的定义、推导与配套练习会在专题内重新完整给出，供需要一条选择性备赛线的读者使用；站点其余部分仍是一张面向智能系统的最小充分知识地图。

## Current scale

- **14 Sections**（5 个知识域 13 个 + Yau Contest 专题 1 个）
- **73 章正文**（5 个知识域 63 章 + Machine Learning 入门 2 章 + Yau Contest 专题 8 章）
- **88 Markdown pages**（含 Home 与 14 个 Section 首页）
- **65 local SVG teaching diagrams**
- **60 short Python examples**，另有少量 Bash / YAML / Dockerfile 示例
- 顶部和左侧导航使用英文；正文使用中文并保留标准英文术语

## Content rules

1. 一个主题只有在它是必要前置、会被后续反复使用，或直接帮助理解真实系统时才进入正文。
2. 同一知识点只由一个 Section 负责，其他 Section 自然引用；Yau Contest 为自足讲解，所需的先修数学在专题内重新完整给出。
3. 算法只保留能代表一类思想的方法，不铺算法谱系。
4. 图片只用于解释闭环、几何关系、数据流、系统边界和算法结构，不作装饰。
5. 代码只用于把公式或工程机制落到实现，保持短小；当前最长 Python 示例为 13 行。
6. 简单主题够用即止；MDP、状态空间、SLAM、CTDE 等地基主题允许更深入，但不扩展成完整教材章节树。

## Local build

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_docs.py
mkdocs serve
```

## Repository layout

```text
docs/
├── index.md
├── assets/diagrams/
├── foundations/
│   ├── mathematics/
│   └── control-theory/
├── decision-learning/
│   ├── machine-learning/
│   ├── reinforcement-learning/
│   ├── game-theory/
│   └── multi-agent-systems/
├── robotics-perception/
│   ├── robotics/
│   └── perception/
├── systems-simulation/
│   ├── distributed-systems/
│   ├── software-engineering/
│   └── simulation-sim2real/
├── safety-human-factors/
│   ├── robustness-safety/
│   └── human-ai-interaction/
├── yau-contest/
├── css/            # custom.css
├── stylesheets/    # extra.css
├── javascripts/    # mathjax.js
└── vendor/mathjax/ # offline MathJax
```

`python scripts/check_docs.py` 会检查目录规模、英文导航与 H1、中文知识点式小标题、本地链接、公式分隔、章节深度、每条定理是否带折叠证明、SVG、Python 语法、文章长度、图片/代码密度、重复图片和代码长度。GitHub Actions 在完整环境中执行 `mkdocs build --strict`。
