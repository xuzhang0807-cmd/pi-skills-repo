# 视频渲染导出：来源与维护

- 技能名：`remotion-render`
- 类型：**上游适配**
- 记忆简称：`render`（不是自动注册的斜杠命令）
- 收录版本/核对日期：2026.09.20 / 2026-09-20

## 上游

维护者/仓库：`remotion-dev/skills`

当前入口：https://github.com/remotion-dev/skills/blob/main/skills/remotion-render/SKILL.md

技能目录提交历史：https://github.com/remotion-dev/skills/commits/main/skills/remotion-render

此次核对的固定内容：https://api.github.com/repos/remotion-dev/skills/git/blobs/6e60afb588b062203638594d1d6f45aef3821b68

入口 blob SHA：`6e60afb588b062203638594d1d6f45aef3821b68`

仓库提交 SHA：`未取得仓库提交 SHA；已记录入口文件 blob SHA，不冒充提交号。`

本目录为中文轻量适配版，不是官方原样副本。只对已读取的技能工作流进行重组；未宣称收录整个上游目录。上游其他文件和后续变化请通过目录历史人工核对。

## 内容与修改

保留真实渲染与静帧入口；补充输出检查、禁止覆盖原文件以及格式透明度需按当前文档校验。

如有 scripts/，其中脚本均为本包本地编写，不是上游原脚本。

## 依赖

可运行的 Remotion 工程及渲染依赖；导出后建议用 FFprobe 验证。

## 更新原则

先备份，再人工对照上游；修改 ALL Skills 内的主库后同步场景副本。不要直接用上游整目录覆盖本包适配版。技能不包含执行许可、已配置的客户端、API 余额或软件运行环境。
