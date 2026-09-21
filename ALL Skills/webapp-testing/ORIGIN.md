# 网页运行测试：来源与维护

- 技能名：`webapp-testing`
- 类型：**上游适配**
- 记忆简称：`web-test`（不是自动注册的斜杠命令）
- 收录版本/核对日期：2026.09.20 / 2026-09-20

## 上游

维护者/仓库：`anthropics/skills`

当前入口：https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md

技能目录提交历史：https://github.com/anthropics/skills/commits/main/skills/webapp-testing

此次核对的固定内容：https://api.github.com/repos/anthropics/skills/git/blobs/4726215301db64a0cc4d41fc3219c61f37a30f4a

入口 blob SHA：`4726215301db64a0cc4d41fc3219c61f37a30f4a`

仓库提交 SHA：`未取得仓库提交 SHA；已记录入口文件 blob SHA，不冒充提交号。`

本目录为中文轻量适配版，不是官方原样副本。只对已读取的技能工作流进行重组；未宣称收录整个上游目录。上游其他文件和后续变化请通过目录历史人工核对。

## 内容与修改

保留先侦察后交互的流程；不打包原 with_server.py，改用本地编写 smoke.py；以实际就绪元素替代强制等待 networkidle。

如有 scripts/，其中脚本均为本包本地编写，不是上游原脚本。

## 依赖

Python 3.10+、Playwright 和 Chromium；自带脚本只做只读冒烟检查。

## 更新原则

先备份，再人工对照上游；修改 ALL Skills 内的主库后同步场景副本。不要直接用上游整目录覆盖本包适配版。技能不包含执行许可、已配置的客户端、API 余额或软件运行环境。
