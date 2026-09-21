# Web 规范审查：来源与维护

- 技能名：`web-design-guidelines`
- 类型：**上游适配**
- 记忆简称：`ui-check`（不是自动注册的斜杠命令）
- 收录版本/核对日期：2026.09.20 / 2026-09-20

## 上游

维护者/仓库：`vercel-labs/agent-skills`

当前入口：https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md

技能目录提交历史：https://github.com/vercel-labs/agent-skills/commits/main/skills/web-design-guidelines

此次核对的固定内容：https://api.github.com/repos/vercel-labs/agent-skills/git/blobs/ceae92ab319216a68274168fba9b63b998b65997

入口 blob SHA：`ceae92ab319216a68274168fba9b63b998b65997`

仓库提交 SHA：`未取得仓库提交 SHA；已记录入口文件 blob SHA，不冒充提交号。`

本目录为中文轻量适配版，不是官方原样副本。只对已读取的技能工作流进行重组；未宣称收录整个上游目录。上游其他文件和后续变化请通过目录历史人工核对。

## 内容与修改

保留官方规则来源和文件行号输出；去除对 WebFetch 工具名的硬依赖，加入明确标注的离线检查降级。

如有 scripts/，其中脚本均为本包本地编写，不是上游原脚本。

## 依赖

前端源码；完整当前规则需联网，实际视觉与交互检查需浏览器。

## 更新原则

先备份，再人工对照上游；修改 ALL Skills 内的主库后同步场景副本。不要直接用上游整目录覆盖本包适配版。技能不包含执行许可、已配置的客户端、API 余额或软件运行环境。
