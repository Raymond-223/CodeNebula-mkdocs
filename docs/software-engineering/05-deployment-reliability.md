# Containers, Deployment & Reliability

> **Section:** Software Engineering

## Why it matters

交付不仅是“能启动”，还包括依赖隔离、配置管理、健康检查、日志监控和故障后的恢复能力。

## Visual intuition

<figure markdown="span">
  ![可靠交付需要让代码变更、自动验证、部署和运行观测形成闭环。](../assets/diagrams/ci-loop.svg)
  <figcaption>可靠交付需要让代码变更、自动验证、部署和运行观测形成闭环。</figcaption>
</figure>

<figure markdown="span">
  ![容器隔离依赖，但设备、网络、数据和配置仍必须显式连接到运行环境。](../assets/diagrams/container-boundary.svg)
  <figcaption>“装进容器”不会自动解决设备权限、GPU、ROS/DDS 网络或持久化数据问题。</figcaption>
</figure>

## Core ideas

- **Image**：应用及其依赖的不可变模板。
- **Container**：镜像的运行实例。
- **Environment**：运行时配置、设备与网络。
- **CI/CD**：自动构建、测试和交付流程。
- **Monitoring**：观察系统状态与趋势。
- **Fallback**：主路径失败时的受限替代行为。

## Key theory

### Containers & Deployment

容器解决的是依赖隔离与可重复运行，不是虚拟机的完全替代。部署还必须显式处理 GPU、设备、网络、数据卷、权限和版本。

### Reliability & Maintenance

可靠性不是“永不失败”，而是让失败**可检测、影响受控、能够恢复、不会静默扩散**。维护阶段还需要兼顾依赖升级、配置漂移和接口兼容。

## Representative methods

- Dockerfile：固定系统/语言依赖。
- CI pipeline：每次提交自动测试并构建。
- Health check + logging：确认服务是否健康并能定位问题。
- Rollback / safe mode：失败后恢复到已知可用状态。

## Minimal code

一个可复现镜像的起点通常很短：固定基础环境、复制依赖、安装、再复制应用。复杂编排放到真正需要时再学。

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
CMD ["python", "-m", "src.main"]
```

## Worked example

**Containers & Deployment：**把规划模块放入容器后，需要明确挂载配置、暴露 ROS/DDS 网络、GPU/设备访问；“镜像能启动”不等于“系统能集成”。

**Reliability & Maintenance：**规划服务异常时，地面站应看到明确状态；底盘进入预设安全模式；修复版本上线后还能回滚到上一稳定版本。

## Connections

- → Distributed Systems：容器之间仍通过网络通信。
- → Simulation：仿真环境也应版本化。
- → Robustness & Safety。
- → Human-AI Interaction：人在环需要可理解的状态和接管入口。

## Further Reading

- Compose/Kubernetes、SRE、SBOM 与更完整供应链安全。

> 这一部分不属于主学习路径；需要做论文、项目或深入证明时再回来查。

## Learning path

[← Section overview](index.md) · [← Testing & Debugging](04-testing-debugging.md)
