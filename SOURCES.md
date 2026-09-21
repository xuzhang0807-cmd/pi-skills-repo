# 收录地址与上游维护清单

核对日期：2026-09-20。17 个独立技能，12 个上游适配、5 个本地新编。下面的 SHA 指已读取的上游 SKILL.md 内容，不是本包改写后的文件哈希；后者另存 manifest.json 的 local_file_sha256。

这不是安装量排行榜，不沿用未经核实的使用量数字。记录“核对日期”不等于“上游最后更新日期”，也不保证每个单独文件与仓库同时更新。精确的目录变更请看各项提交历史。

## affaan-m/ECC

https://github.com/affaan-m/ECC

### 部署与回滚 · `deployment-patterns`

原入口：https://github.com/affaan-m/ECC/blob/main/skills/deployment-patterns/SKILL.md

目录历史：https://github.com/affaan-m/ECC/commits/main/skills/deployment-patterns

已核对入口 blob SHA：`b9d279f8a99889b6f36db99b17b762374474dc99`

本包变化：保留预检、健康检查、分阶段发布、回滚原则；移除旧版本模板和平台命令硬编码，补充数据库回滚与生产操作保护。

### Docker 检查维护 · `docker-patterns`

原入口：https://github.com/affaan-m/ECC/blob/main/skills/docker-patterns/SKILL.md

目录历史：https://github.com/affaan-m/ECC/commits/main/skills/docker-patterns

已核对入口 blob SHA：`e60c1d20f7fe4502c099ec7a6bb306f1d492b7f4`

本包变化：浓缩为通用 Docker 工作流；去掉 ECC 仓库专用安装器依赖、不必要的强制编排建议及破坏性清理捷径。

### 图片视频生成接口 · `fal-ai-media`

原入口：https://github.com/affaan-m/ECC/blob/main/skills/fal-ai-media/SKILL.md

目录历史：https://github.com/affaan-m/ECC/commits/main/skills/fal-ai-media

已核对入口 blob SHA：`b1e837bbb771d94f37e5e47e396b6c7dc84f57ae`

本包变化：保留统一生成流程；移除容易过期的模型 ID、参数和 npx 自动安装示例；改为实时发现并检查预算。

## anthropics/skills

https://github.com/anthropics/skills

### Web 视觉美化 · `frontend-design`

原入口：https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md

目录历史：https://github.com/anthropics/skills/commits/main/skills/frontend-design

已核对入口 blob SHA：`a5333457c414d20d625f307df945842c0952ecc3`

本包变化：依据当前上游设计原则整理中文流程；保留用户视觉要求优先，不把某一种流行风格设为默认。

### 网页运行测试 · `webapp-testing`

原入口：https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md

目录历史：https://github.com/anthropics/skills/commits/main/skills/webapp-testing

已核对入口 blob SHA：`4726215301db64a0cc4d41fc3219c61f37a30f4a`

本包变化：保留先侦察后交互的流程；不打包原 with_server.py，改用本地编写 smoke.py；以实际就绪元素替代强制等待 networkidle。

## obra/superpowers

https://github.com/obra/superpowers

### 故障定位 · `systematic-debugging`

原入口：https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md

目录历史：https://github.com/obra/superpowers/commits/main/skills/systematic-debugging

已核对入口 blob SHA：`095d194ac041502905f15b01d22d294fb94db8b2`

本包变化：保留四阶段排错方法；将必要技巧内联，去除插件命名空间依赖和可能打印密钥的诊断示例。

### 完成前验收 · `verification-before-completion`

原入口：https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md

目录历史：https://github.com/obra/superpowers/commits/main/skills/verification-before-completion

已核对入口 blob SHA：`7d45333cc4a49c57a80df6c1fe2fa777a207afbc`

本包变化：保留证据先于结论的原则，改为中文紧凑验收格式，避免无关仪式化步骤。

### 测试驱动开发 · `test-driven-development`

原入口：https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md

目录历史：https://github.com/obra/superpowers/commits/main/skills/test-driven-development

已核对入口 blob SHA：`46838cc9e893c06259e3bdad0fc2425b36242f15`

本包变化：保留红绿重构；不沿用无条件删除已有实现的要求；内联测试质量规则，不依赖未收录技能。

### 代码审查 · `requesting-code-review`

原入口：https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md

目录历史：https://github.com/obra/superpowers/commits/main/skills/requesting-code-review

已核对入口 blob SHA：`6d995da5c7d8d6c5a3cc63ddb701427f88ec2021`

本包变化：改为没有子代理也能执行的审查流程；明确自查不等于独立审查，纳入未提交修改，内联审查模板。

## remotion-dev/skills

https://github.com/remotion-dev/skills

### 程序化视频制作 · `remotion-create`

原入口：https://github.com/remotion-dev/skills/blob/main/skills/remotion-create/SKILL.md

目录历史：https://github.com/remotion-dev/skills/commits/main/skills/remotion-create

已核对入口 blob SHA：`73e582d75a4d19092702b510e5d1fdd2e350932b`

本包变化：整理为独立起步工作流；必要布局、分镜和按帧动画要求内联，不依赖整套 Remotion 技能。

### 视频渲染导出 · `remotion-render`

原入口：https://github.com/remotion-dev/skills/blob/main/skills/remotion-render/SKILL.md

目录历史：https://github.com/remotion-dev/skills/commits/main/skills/remotion-render

已核对入口 blob SHA：`6e60afb588b062203638594d1d6f45aef3821b68`

本包变化：保留真实渲染与静帧入口；补充输出检查、禁止覆盖原文件以及格式透明度需按当前文档校验。

## vercel-labs/agent-skills

https://github.com/vercel-labs/agent-skills

### Web 规范审查 · `web-design-guidelines`

原入口：https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md

目录历史：https://github.com/vercel-labs/agent-skills/commits/main/skills/web-design-guidelines

已核对入口 blob SHA：`ceae92ab319216a68274168fba9b63b998b65997`

本包变化：保留官方规则来源和文件行号输出；去除对 WebFetch 工具名的硬依赖，加入明确标注的离线检查降级。

## 本地新编，无第三方上游

以下 5 项用于补齐场景流程和审美验收，不能作为第三方社区精选的证据：

- `project-start` - 从零启动项目

- `image-design` - 图片制作与审美

- `image-review` - 图片成品审查

- `video-plan` - 视频策划与审美

- `video-review` - 视频成品审查
