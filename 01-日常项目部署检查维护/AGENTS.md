# 日常项目部署、检查、维护：任务路由

只读取当前步骤需要的入口。简单任务省略无关步骤，不强制使用子代理，不批量加载全部内容。以下路径相对本场景目录。

- 发布准备、健康检查、回滚：读取 `deployment-patterns/SKILL.md`。
- Dockerfile、Compose、网络与数据卷：读取 `docker-patterns/SKILL.md`。
- 发生异常：读取 `systematic-debugging/SKILL.md`，先取证。
- 实际修复代码：按需要读取 `test-driven-development/SKILL.md`，保护现有实现。
- 宣称修好或上线之前：读取 `verification-before-completion/SKILL.md`。

禁止为检查方便删除容器数据卷、重置仓库或打印完整密钥。生产变更必须具备明确授权和回滚条件。

所有技能都服从用户已给定需求、真实工具能力和授权边界。先查看实际文件、日志或作品再判断；不得虚构测试、生成结果或上线状态。自动发现没有生效时，直接读取对应 SKILL.md，而不是臆造斜杠指令。
