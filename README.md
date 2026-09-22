# CodeNebula

CodeNebula 是一套面向 **AI、Robotics 与 Autonomous Systems** 的紧凑型学习网站，使用 MkDocs Material 构建。

这一版采用“**最小充分知识体系 + 文章式讲解**”原则：只保留后续反复依赖、能够解释真实系统、或者删掉后会造成认知断层的内容。正文不是课程提纲，也不是算法百科，而是围绕一个具体主题逐层解释定义、机制、公式、例子和工程边界。

## Current scale

- **12 Sections**，分成 5 个知识域
- **61 core chapters**
- **74 Markdown pages**（含 Home 与 12 个 Section 首页）
- **47 local SVG teaching diagrams**
- **28 short Python examples**，另有少量 Bash / YAML / Dockerfile 示例
- 顶部和左侧导航使用英文；正文使用中文并保留标准英文术语

## Curriculum

- **Foundations** — Mathematics, Control Theory
- **Decision & Learning** — Reinforcement Learning, Game Theory, Multi-Agent Systems
- **Robotics & Perception** — Robotics, Perception
- **Systems & Simulation** — Distributed Systems & Networking, Software Engineering, Simulation & Sim2Real
- **Safety & Human Factors** — Robustness & Safety, Human–AI Interaction

## Content rules

1. 一个主题只有在它是必要前置、会被后续反复使用，或直接帮助理解真实系统时才进入正文。
2. 同一知识点只由一个 Section 负责，其他 Section 只自然引用，不重复开课。
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
├── mathematics/
├── reinforcement-learning/
├── game-theory/
├── multi-agent-systems/
├── control-theory/
├── robotics/
├── perception/
├── distributed-systems/
├── software-engineering/
├── simulation-sim2real/
├── robustness-safety/
└── human-ai-interaction/
```

`python scripts/check_docs.py` 会检查目录规模、英文导航、本地链接、公式分隔、SVG、Python 语法、文章长度、图片/代码密度、重复图片和代码长度。GitHub Actions 仍负责在完整环境中执行 `mkdocs build --strict`。
