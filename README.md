# CodeNebula

CodeNebula 是一套面向零基础读者的 **AI、机器人与自主系统讲解手册**，使用 MkDocs Material 构建。

这一版按“**实际依赖 + 逐步计算**”组织：后文不用的前置知识删除，后文使用的知识给出定义、符号、手算过程、适用条件和工程边界。代码用于验证已经讲清楚的计算或说明接口，不代替推导。

## Current scale

- **13 Sections**，分成 5 个知识域
- **64 core chapters**
- **78 Markdown pages**（含首页与 13 个 Section 导读）
- **60 local SVG teaching diagrams**
- **60 short Python examples**，另有少量 Bash / YAML / Dockerfile 示例
- 导航和页面一级标题使用英文；中文正文中的重要术语在首次出现时给出标准英文名称

## Curriculum

- **Foundations** — Mathematics, Control Theory
- **Decision & Learning** — Machine Learning, Reinforcement Learning, Game Theory, Multi-Agent Systems
- **Robotics & Perception** — Robotics, Perception
- **Systems & Simulation** — Distributed Systems & Networking, Software Engineering, Simulation & Sim2Real
- **Safety & Human Factors** — Robustness & Safety, Human–AI Interaction

## Content rules

1. 一个主题只有在它是必要前置、会被后续使用，或直接帮助理解真实系统时才进入正文。
2. 同一知识点只由一个 Section 负责，其他 Section 只自然引用，不重复开课。
3. 算法只保留能代表一类思想的方法，不铺算法谱系。
4. 图片只用于解释闭环、几何关系、数据流、系统边界和算法结构，不作装饰。
5. 代码只用于验证手算或把工程机制落到实现，不能代替推导。
6. 小标题直接使用知识点名称，不使用提问式或宣传式文案。
7. 没有适用条件的经验阈值不写成普遍结论。

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
└── safety-human-factors/
    ├── robustness-safety/
    └── human-ai-interaction/
```

`python scripts/check_docs.py` 会检查目录规模、英文导航与页面标题、本地链接、公式分隔、SVG、Python 语法、文章长度、问题式标题、孤立 QR 前置、重复图片和代码长度。GitHub Actions 仍负责在完整环境中执行 `mkdocs build --strict`。
