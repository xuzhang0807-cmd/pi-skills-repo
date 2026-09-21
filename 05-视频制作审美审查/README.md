# 视频制作、审美、审查

本场景含 5 个技能的真实目录，可按项目取用。先读 AGENTS.md，再按任务需要读取具体 SKILL.md；不必全部调用。

| 中文用途 | 简称 | 实际技能入口 | 类型 |
|---|---|---|---|
| 视频策划与审美 | `video` | [video-plan](video-plan/SKILL.md) | 本地新编 |
| 视频成品审查 | `video-check` | [video-review](video-review/SKILL.md) | 本地新编 |
| 程序化视频制作 | `motion` | [remotion-create](remotion-create/SKILL.md) | 上游适配 |
| 视频渲染导出 | `render` | [remotion-render](remotion-render/SKILL.md) | 上游适配 |
| 图片视频生成接口 | `media` | [fal-ai-media](fal-ai-media/SKILL.md) | 上游适配 |

## 可以直接对 Agent 说

> 先读本场景的 AGENTS.md，先确定分镜、节奏和声音方案，再选择生成式视频或 Remotion 制作。交付前检查真实视频，说明哪些部分完整看过、哪些只是抽帧检查。

同名技能只安装一份。日常修改应在总目录 ALL Skills 中进行；本场景副本可用总目录的同步工具更新。来源与改动见各自 ORIGIN.md。

## 按需依赖

以下依赖不随技能包附送，也不会自动安装：

- **视频策划与审美**: 分镜与提示词无需 API；生成镜头需实际视频生成工具，程序化动画可用 Remotion。
- **视频成品审查**: 可查看视频或抽帧的模型；附加脚本需要 Python 3.10+、FFprobe，抽帧另需 FFmpeg。
- **程序化视频制作**: Node.js、Git 和对应项目的 Remotion/React 依赖；软件授权按上游条款，本包不包含这些软件。
- **视频渲染导出**: 可运行的 Remotion 工程及渲染依赖；导出后建议用 FFprobe 验证。
- **图片视频生成接口**: 用户授权的 fal.ai 账号/API 额度及经过审核的 MCP 或客户端；本包不安装 MCP、不包含密钥。
