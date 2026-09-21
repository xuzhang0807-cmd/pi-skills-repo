# 项目 Web 美化、审查

本场景含 4 个技能的真实目录，可按项目取用。先读 AGENTS.md，再按任务需要读取具体 SKILL.md；不必全部调用。

| 中文用途 | 简称 | 实际技能入口 | 类型 |
|---|---|---|---|
| Web 视觉美化 | `ui` | [frontend-design](frontend-design/SKILL.md) | 上游适配 |
| Web 规范审查 | `ui-check` | [web-design-guidelines](web-design-guidelines/SKILL.md) | 上游适配 |
| 网页运行测试 | `web-test` | [webapp-testing](webapp-testing/SKILL.md) | 上游适配 |
| 代码审查 | `review` | [requesting-code-review](requesting-code-review/SKILL.md) | 上游适配 |

## 可以直接对 Agent 说

> 先读本场景的 AGENTS.md，在保留业务功能和我指定风格的前提下改进页面。检查桌面与手机效果、交互和可访问性，给出实际截图与问题位置。

同名技能只安装一份。日常修改应在总目录 ALL Skills 中进行；本场景副本可用总目录的同步工具更新。来源与改动见各自 ORIGIN.md。

## 按需依赖

以下依赖不随技能包附送，也不会自动安装：

- **Web 视觉美化**: 前端项目；视觉验收需要浏览器和可查看截图的模型。
- **Web 规范审查**: 前端源码；完整当前规则需联网，实际视觉与交互检查需浏览器。
- **网页运行测试**: Python 3.10+、Playwright 和 Chromium；自带脚本只做只读冒烟检查。
- **代码审查**: 项目与代码差异；独立子代理可选而非必需。
