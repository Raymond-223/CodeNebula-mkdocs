# CodeNebula

CodeNebula is a compact learning website for **AI, robotics, and autonomous systems**, built with MkDocs Material.

The curriculum follows a **minimum sufficient knowledge system**: keep only prerequisite concepts and high-value engineering ideas, remove cross-Section duplication, and move specialist branches to **Further Reading**.

## Current scale

- **12 Sections** grouped into 5 domains
- **61 core chapters**
- **74 Markdown pages** including Home and Section overviews
- **49 local SVG teaching diagrams**
- **24 short Python examples** plus a few Bash/Docker snippets
- English top/left navigation; Chinese learning content with standard English terminology

## What changed in V5

This version is a section-by-section pruning pass. It removes content that is duplicated, too specialized for the first learning path, or easy to look up later.

1. **Perception no longer duplicates Robotics.** Visual Odometry & SLAM was removed from Perception; SLAM stays in Robotics, while feature matching remains as the visual prerequisite.
2. **Digital Twin is no longer a core Simulation chapter.** It is useful in some industrial systems but not required to understand modeling, reality gap, Sim2Real or Real2Sim.
3. **Algorithm catalogues were cut again.** Double DQN, A2C, MADDPG, support enumeration, nonlinear MPC, Particle Filter and similar branches moved to Further Reading.
4. **Engineering Sections keep code.** Short examples remain where they expose an update rule, interface, state transition or failure-handling pattern.
5. **Numerical computation stays core.** It is repeatedly used by control, robotics, simulation and optimization, so removing it would break downstream understanding.

## Curriculum

- **Foundations** — Mathematics for Intelligent Systems
- **Intelligent Systems** — Reinforcement Learning, Game Theory, Multi-Agent Systems
- **Robotics** — Control Theory, Robotics, Perception
- **Systems** — Distributed Systems & Networking, Software Engineering
- **Advanced Autonomous Systems** — Simulation & Sim2Real, Robustness & Safety, Human–AI Interaction

## Design rules

1. Keep a concept in the main path only if it is a prerequisite, repeatedly reused, or necessary to understand a real system.
2. If another Section already owns the topic, link to it instead of teaching it twice.
3. Use one or two representative algorithms per family; variants belong in Further Reading.
4. Use diagrams for structure and code for implementation intuition, not decoration.
5. Further Reading is optional and never blocks the main path.

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

`python scripts/check_docs.py` verifies curriculum size, English navigation, links, math delimiters, SVG validity, Python syntax, and bounded code/diagram density. GitHub Actions additionally runs `mkdocs build --strict` before Pages deployment.
