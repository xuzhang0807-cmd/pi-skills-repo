# Docker 检查维护：来源与维护

- 技能名：`docker-patterns`
- 类型：**上游适配**
- 记忆简称：`docker`（不是自动注册的斜杠命令）
- 收录版本/核对日期：2026.09.20 / 2026-09-20

## 上游

维护者/仓库：`affaan-m/ECC`

当前入口：https://github.com/affaan-m/ECC/blob/main/skills/docker-patterns/SKILL.md

技能目录提交历史：https://github.com/affaan-m/ECC/commits/main/skills/docker-patterns

此次核对的固定内容：https://github.com/affaan-m/ECC/blob/934195f955cf0da847d59fcd6f68856bce112d8b/skills/docker-patterns/SKILL.md

入口 blob SHA：`e60c1d20f7fe4502c099ec7a6bb306f1d492b7f4`

仓库提交 SHA：`934195f955cf0da847d59fcd6f68856bce112d8b`

本目录为中文轻量适配版，不是官方原样副本。只对已读取的技能工作流进行重组；未宣称收录整个上游目录。上游其他文件和后续变化请通过目录历史人工核对。

## 内容与修改

浓缩为通用 Docker 工作流；去掉 ECC 仓库专用安装器依赖、不必要的强制编排建议及破坏性清理捷径。

如有 scripts/，其中脚本均为本包本地编写，不是上游原脚本。

## 依赖

Docker CLI、可访问的 Docker Engine；Compose 操作需要相应插件。

## 更新原则

先备份，再人工对照上游；修改 ALL Skills 内的主库后同步场景副本。不要直接用上游整目录覆盖本包适配版。技能不包含执行许可、已配置的客户端、API 余额或软件运行环境。
