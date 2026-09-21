# 从零开发项目

本场景含 7 个技能的真实目录，可按项目取用。先读 AGENTS.md，再按任务需要读取具体 SKILL.md；不必全部调用。

| 中文用途 | 简称 | 实际技能入口 | 类型 |
|---|---|---|---|
| 从零启动项目 | `start` | [project-start](project-start/SKILL.md) | 本地新编 |
| 测试驱动开发 | `test` | [test-driven-development](test-driven-development/SKILL.md) | 上游适配 |
| 故障定位 | `debug` | [systematic-debugging](systematic-debugging/SKILL.md) | 上游适配 |
| 代码审查 | `review` | [requesting-code-review](requesting-code-review/SKILL.md) | 上游适配 |
| Web 视觉美化 | `ui` | [frontend-design](frontend-design/SKILL.md) | 上游适配 |
| 网页运行测试 | `web-test` | [webapp-testing](webapp-testing/SKILL.md) | 上游适配 |
| 完成前验收 | `verify` | [verification-before-completion](verification-before-completion/SKILL.md) | 上游适配 |

## 可以直接对 Agent 说

> 先读本场景的 AGENTS.md，按我的需求建立最小可运行项目。优先复用现有方案，逐步开发和测试，最后交付启动、使用和维护说明。

同名技能只安装一份。日常修改应在总目录 ALL Skills 中进行；本场景副本可用总目录的同步工具更新。来源与改动见各自 ORIGIN.md。

## 按需依赖

以下依赖不随技能包附送，也不会自动安装：

- **从零启动项目**: 项目读写权限；所选技术栈工具按需准备。
- **测试驱动开发**: 项目现有测试框架或明确的可重复验证方式。
- **故障定位**: 项目文件、日志及相应运行或测试工具。
- **代码审查**: 项目与代码差异；独立子代理可选而非必需。
- **Web 视觉美化**: 前端项目；视觉验收需要浏览器和可查看截图的模型。
- **网页运行测试**: Python 3.10+、Playwright 和 Chromium；自带脚本只做只读冒烟检查。
- **完成前验收**: 能够读取实际产物与运行对应验证命令。
