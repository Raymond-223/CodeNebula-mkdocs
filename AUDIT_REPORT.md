# CodeNebula V5 — Section-by-Section Minimality Audit

## Final result

This pass reviewed all **12 Sections one by one** using a strict minimum-sufficient rule:

1. keep it if later Sections depend on it;
2. keep it if it repeatedly appears in real engineering work;
3. remove or move it to Further Reading if it is mainly a variant, specialist branch, or duplicate of another Section.

Final scale:

- **12 Sections** in 5 domains
- **61 core chapters**
- **74 Markdown pages** including Home + 12 Section overviews
- **49 local SVG teaching diagrams**
- **24 short Python examples**, plus small Bash/Docker snippets
- English navigation; Chinese teaching content with standard English terminology

## Section-by-section decisions

### 1. Mathematics for Intelligent Systems — 6 chapters

**Kept:** vectors/matrices, gradients/Jacobians, numerical computation, probability, Bayes, Markov property, optimization and constraints.

**Removed from the main path:** stationary distributions, MLE, Binomial as a separate named method, Adam, CVaR/chance constraints, detailed DRO variants, Newton/quasi-Newton and Runge–Kutta families.

**Why:** the remaining material is exactly what RL, control, robotics, perception and simulation reuse. Numerical computation stays core because discretization, linear solves and numerical integration are prerequisites downstream.

### 2. Reinforcement Learning — 6 chapters

**Kept:** MDP/Bellman, Q-Learning/DQN, policy gradient/Actor–Critic, PPO/SAC as representatives, exploration/POMDP, model-based vs model-free, safe/offline RL concepts.

**Moved out of the main path:** Double DQN, A2C, REINFORCE as a named algorithm, Dyna, specific world-model families, TRPO/DDPG/TD3 and detailed offline-RL variants.

**Why:** the learner needs algorithm families and the reason each family exists, not an algorithm catalogue.

### 3. Game Theory — 5 chapters

**Kept:** players/strategies/payoffs, game classification, best response/Nash, minimax, sequential/Stackelberg, Bayesian games, repeated interaction.

**Removed from the main path:** support enumeration, signaling as a main method, PPAD complexity and detailed equilibrium-solving machinery.

**Why:** these are useful later, but they do not improve the first-pass mental model enough to justify the learning cost.

### 4. Multi-Agent Systems — 5 chapters

**Kept:** agent architectures, coordination, communication, task allocation + distributed execution, MARL/CTDE.

**Moved out of the main path:** BDI-specific details, learned communication, consensus-allocation variants, MADDPG and extra MARL algorithm families.

**Why:** the Section should explain how multiple agents are organized and coordinated before exposing algorithm variants.

### 5. Control Theory — 5 chapters

**Kept:** dynamic/state-space models, feedback/stability, PID, LQR and MPC.

**Removed from the main path:** pole placement, feedforward-control variants, finite/infinite LQR taxonomy, nonlinear/robust MPC branches and named PID tuning recipes.

**Why:** model → feedback → stability → PID → optimal control → constrained predictive control is already a complete control skeleton.

### 6. Robotics — 5 chapters

**Kept:** coordinate/kinematic models, sensing/state estimation, SLAM, planning, navigation/control.

**Moved out of the main path:** Ackermann/manipulator-specific branches, Particle Filter as a core estimator, NeRF/3D Gaussian mapping, Behavior Tree as a navigation prerequisite, and specific planner variants.

**Why:** the remaining five chapters form the full physical-robot loop without becoming a robotics encyclopaedia.

### 7. Perception — 5 chapters

**Kept:** camera model, feature matching, detection/segmentation, depth/point cloud, multimodal fusion.

**Removed as a duplicate chapter:** **Visual Odometry & SLAM**. Visual matching stays in Perception, but VO/SLAM is taught once in Robotics.

**Also pruned:** detailed detector architecture families, monocular-depth/3D-network catalogues and low-level point-cloud method lists.

**Why:** Perception should explain how observations become geometry/semantics; localization and map consistency belong to Robotics.

### 8. Distributed Systems & Networking — 5 chapters

**Kept:** network limits, TCP/UDP intuition, request-response/pub-sub, distributed time/asynchrony, consistency, fault tolerance, ROS2/DDS.

**Removed from the main path:** queue/backpressure as separate concepts, replication/partitioning method lists, CRDT as a core technique, QUIC/event-sourcing details.

**Why:** multi-node robotics mainly needs communication semantics, timing, state consistency, failures and middleware.

### 9. Software Engineering — 5 chapters

**Kept:** requirements/architecture, modular APIs, version control, testing/debugging, containers/deployment/reliability.

**Removed from the main path:** long architecture-style lists, SLO terminology, technical-debt theory, Compose as a required concept, SBOM/chaos-engineering/SRE details.

**Why:** the core should make research systems reproducible, testable, deployable and maintainable—not teach a full enterprise software curriculum.

### 10. Simulation & Sim2Real — 4 chapters

**Kept:** modeling/physics simulation, robot/sensor simulation, reality gap/randomization, Sim2Real/Real2Sim validation loop.

**Removed as a core chapter:** **Digital Twin**.

**Why:** Digital Twin is useful in some industrial workflows but is not a prerequisite for understanding simulation, reality gap or transfer. It remains a Further Reading concept.

### 11. Robustness & Safety — 5 chapters

**Kept:** uncertainty/distribution shift, robustness/risk/reliability, safety constraints, fault detection/tolerance, runtime safety.

**Compressed:** aleatoric/epistemic, shift/OOD and risk terms are grouped rather than taught as long taxonomies; CVaR, H-infinity and formal methods remain optional.

**Why:** the learner needs to recognize uncertainty, define safety boundaries, detect failures and design fallbacks—not memorize every safety-analysis framework.

### 12. Human–AI Interaction — 5 chapters

**Kept:** human/system roles and automation, HITL, shared autonomy, trust/explainability, intervention/takeover.

**Compressed:** long lists of interface techniques and feedback methods are reduced to status/alerts, authority allocation, escalation and safe handover.

**Why:** for autonomous systems, the essential question is who has authority, when the human enters the loop, and how control is safely transferred.

## Two whole chapters removed

1. `Perception / Visual Odometry & SLAM` — duplicated `Robotics / Mapping & SLAM`.
2. `Simulation / Digital Twin` — useful specialization, not a prerequisite for the main Sim2Real chain.

This reduced the curriculum from **63 to 61 core chapters** without removing any prerequisite node.

## Code and image policy after pruning

No code was removed merely to reduce counts. Engineering examples remain where they expose a real implementation idea: state update, PID, Kalman update, A*, ROS2 QoS, idempotency, Docker/API contracts, noisy sensors, watchdogs and safety filters.

Likewise, diagrams remain for loops, geometry, pipelines, information flow and system boundaries. The duplicate VO/SLAM diagram was removed with its duplicate chapter.

## Validation

Current offline checks pass:

```text
Documentation checks passed: 12 sections, 61 core chapters, 74 Markdown pages, 49 diagrams, 24 Python examples.
```

The checker validates navigation, local links, math delimiters, SVG XML, Python syntax, chapter-count bounds and bounded code/image density. V5 also adds a per-page cognitive-load guard: no chapter may expose more than **6 core concepts** or **4 representative methods** in the main path. GitHub Actions still runs `mkdocs build --strict` in a fully provisioned environment.
