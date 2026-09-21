# Version Control

> **Section:** Software Engineering

## Why it matters

版本控制不是备份工具，而是让变更可追踪、可评审、可回滚，并为并行协作提供共同历史。

## Core ideas

- **Commit**：一次有意义的变更快照。
- **Branch**：独立开发线。
- **Merge/Rebase**：整合历史的两种方式。
- **Remote**：团队共享仓库。

## Key theory

Git 的重点不是命令数量，而是保持历史可理解：**小而完整的提交、明确提交信息、代码审查前可重现**。不要把大文件、密钥、构建产物随意放进仓库。

## Representative methods

- Small commits + review：让变更可理解、可回滚。
- Tag/release：把代码版本与实验/交付绑定。
- `.gitignore`：排除缓存、密钥、生成物。

## Minimal commands

版本控制真正需要先掌握的命令很少：检查状态、只暂存本次变更、提交、查看差异。

```bash
git status
git diff
git add path/to/file
git commit -m "fix: handle stale sensor timestamp"
```

## Worked example

一次提交同时改 20 个无关文件很难审查；把“修传感器时间戳”和“重构 UI”分成两个提交，回滚和定位问题都更容易。

## Connections

- → Reliability：可回滚是工程恢复能力。
- → Experiment reproducibility：代码版本必须和结果绑定。

## Further Reading

- Rebase/merge 策略、monorepo tooling。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Modular Design & APIs](02-modular-apis.md) · [Testing & Debugging →](04-testing-debugging.md)
