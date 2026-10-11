# CodeNebula

CodeNebula 是一套面向 **AI、Robotics 与 Autonomous Systems** 的紧凑型学习网站，使用 MkDocs Material 构建。

这一版采用“**最小充分知识体系 + 文章式讲解**”原则：只保留后续反复依赖、能够解释真实系统、或者删掉后会造成认知断层的内容。正文不是课程提纲，也不是算法百科，而是围绕一个具体主题逐层解释定义、机制、公式、例子和工程边界。

## Standalone contest track

- 顶部导航新增 **Yau Contest**（`docs/yau-contest/`），完全位于 `Foundations` 之外。
- 当前交付 **Stage 1: Matrix Theory & Iteration**：一篇总览、六篇理论讲解和一篇完整例题集。
- 面向需要从定义重新建立知识链的读者：定理、符号与先修微积分都在专题内重讲，**不依赖 Foundations 文件内容**。
- 采用“定义—条件—完整证明—反例—手算例题—练习”结构，明确区分必要条件、充分条件和充要条件；证明放在默认关闭的 `proof` 折叠栏中。
- 全站二级及以下标题均使用中文知识点名称；导航与页面 H1 使用英文，重要术语采用“中文（English）”格式。

## Current scale

- **12 Sections**，分成 5 个知识域
- **63 core chapters**
- **86 Markdown pages**（含 Home、12 个 Section 首页与独立丘赛专题）
- **60 local SVG teaching diagrams**
- **60 short Python examples**，另有少量 Bash / YAML / Dockerfile 示例
- 顶部和左侧导航使用英文；正文使用中文并保留标准英文术语

## Curriculum

- **Foundations** — Mathematics, Control Theory
- **Decision & Learning** — Reinforcement Learning, Game Theory, Multi-Agent Systems
- **Robotics & Perception** — Robotics, Perception
- **Systems & Simulation** — Distributed Systems & Networking, Software Engineering, Simulation & Sim2Real
- **Safety & Human Factors** — Robustness & Safety, Human–AI Interaction

## Content rules

1. 一个主题只有在它是必要前置、会被后续反复使用，或直接帮助理解真实系统时才进入正文。
2. 原有主课程中，同一知识点只由一个 Section 负责，其他 Section 只自然引用。**独立丘赛专题例外**：为满足零基础自学与竞赛证明训练，所需数学概念会在专题内重新完整讲解，不依赖 Foundations。
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
├── assets/diagrams/
├── foundations/
│   ├── mathematics/
│   └── control-theory/
├── decision-learning/
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
    ├── robustness-safety/
│   └── human-ai-interaction/
└── yau-contest/  # standalone Stage 1 mathematical handbook
```

`python scripts/check_docs.py` 会检查目录规模、英文导航与 H1、中文知识点式小标题、本地链接、公式分隔、Yau 章节深度、每条定理是否带折叠证明、SVG、Python 语法、文章长度、图片/代码密度、重复图片和代码长度。GitHub Actions 仍负责在完整环境中执行 `mkdocs build --strict`。
