# 日常项目部署、检查、维护

本场景含 5 个技能的真实目录，可按项目取用。先读 AGENTS.md，再按任务需要读取具体 SKILL.md；不必全部调用。

| 中文用途 | 简称 | 实际技能入口 | 类型 |
|---|---|---|---|
| 部署与回滚 | `deploy` | [deployment-patterns](deployment-patterns/SKILL.md) | 上游适配 |
| Docker 检查维护 | `docker` | [docker-patterns](docker-patterns/SKILL.md) | 上游适配 |
| 故障定位 | `debug` | [systematic-debugging](systematic-debugging/SKILL.md) | 上游适配 |
| 测试驱动开发 | `test` | [test-driven-development](test-driven-development/SKILL.md) | 上游适配 |
| 完成前验收 | `verify` | [verification-before-completion](verification-before-completion/SKILL.md) | 上游适配 |

## 可以直接对 Agent 说

> 先读本场景的 AGENTS.md，检查当前项目的部署和运行状态。先做只读检查，定位问题后给出最小修复与回滚方法，完成后提供验证证据。

同名技能只安装一份。日常修改应在总目录 ALL Skills 中进行；本场景副本可用总目录的同步工具更新。来源与改动见各自 ORIGIN.md。

## 按需依赖

以下依赖不随技能包附送，也不会自动安装：

- **部署与回滚**: 目标项目与部署环境访问权限；实际发布按平台另需 CLI 或 SSH。
- **Docker 检查维护**: Docker CLI、可访问的 Docker Engine；Compose 操作需要相应插件。
- **故障定位**: 项目文件、日志及相应运行或测试工具。
- **测试驱动开发**: 项目现有测试框架或明确的可重复验证方式。
- **完成前验收**: 能够读取实际产物与运行对应验证命令。
