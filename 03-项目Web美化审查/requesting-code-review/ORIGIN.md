# 代码审查：来源与维护

- 技能名：`requesting-code-review`
- 类型：**上游适配**
- 记忆简称：`review`（不是自动注册的斜杠命令）
- 收录版本/核对日期：2026.09.20 / 2026-09-20

## 上游

维护者/仓库：`obra/superpowers`

当前入口：https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md

技能目录提交历史：https://github.com/obra/superpowers/commits/main/skills/requesting-code-review

此次核对的固定内容：https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/requesting-code-review/SKILL.md

入口 blob SHA：`6d995da5c7d8d6c5a3cc63ddb701427f88ec2021`

仓库提交 SHA：`5bf4e78011075bcfc0dc295f0724994cd123ee71`

本目录为中文轻量适配版，不是官方原样副本。只对已读取的技能工作流进行重组；未宣称收录整个上游目录。上游其他文件和后续变化请通过目录历史人工核对。

## 内容与修改

改为没有子代理也能执行的审查流程；明确自查不等于独立审查，纳入未提交修改，内联审查模板。

如有 scripts/，其中脚本均为本包本地编写，不是上游原脚本。

## 依赖

项目与代码差异；独立子代理可选而非必需。

## 更新原则

先备份，再人工对照上游；修改 ALL Skills 内的主库后同步场景副本。不要直接用上游整目录覆盖本包适配版。技能不包含执行许可、已配置的客户端、API 余额或软件运行环境。
