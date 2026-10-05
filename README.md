# pi-skills-repo

按用途分组的 Agent Skills 仓库。**仓库内容只有三个分类文件夹 `office/`、`permanent/`、`project/`，加上 `INSTALL.md`、`scripts/`、`patches/`、`licenses/`、`upstream.json`。**

- `office/` — Anthropic 官方办公类技能（文档/表格/幻灯片/PDF）
- `permanent/` — 长期常驻技能，任何项目都可加载（含 grill 一组的四个依赖技能）
- `project/` — 具体项目阶段按需加载的设计与工程技能
- **`INSTALL.md` — 多 harness 安装与整改指南。拉库后先读它，再按当前环境整改。**
- `scripts/adapt.mjs` — 自动完成环境整改，只改安装副本，不改上游原文
- `patches/` — 适配时留下的原文备份与说明，可回滚
- `upstream.json` — 机器可读的上游来源与版本基线，供维护 Agent 定期比对
- `licenses/` — 各上游仓库的许可证原文

**最后核对日期：2026-10-04（UTC）。** 每个技能目录都是对应上游该日提交的完整快照（含脚本、references、data 等，非仅 SKILL.md）。

> **只做三件事就能用**：① 读 `INSTALL.md` 判断 harness；② 把 `permanent/*` 与 `project/*` 平铺复制到 harness 的技能搜索路径；③ 跑 `node scripts/adapt.mjs --apply --dest <安装路径> --repo-root "$PWD"`。

---

## 目录

| 分类 | 技能 | 数量 |
|---|---|---:|
| `office/` | docx, pdf, pptx, xlsx | 4 |
| `permanent/` | agent-browser, code-review, codebase-design, diagnosing-bugs, domain-modeling, find-skills, grilling, grill-me, ponytail, setup-matt-pocock-skills, tdd | 11 |
| `project/` | frontend-design, grill-with-docs, handoff, improve-codebase-architecture, react-best-practices, to-spec, ui-ux-pro-max, web-design-guidelines | 8 |

同名技能只装一份；不要把仓库根目录当成单个 Skill 导入。**技能按 `SKILL.md` 的 `name:` 注册，不按目录名**——两处不一致属正常，不要改：

- `permanent/agent-browser/` → `name: core`
- `project/react-best-practices/` → `name: vercel-react-best-practices`

`permanent/` 里 `grilling`、`domain-modeling`、`codebase-design`、`setup-matt-pocock-skills` 是**依赖技能**：它们被常驻技能按名字调用，必须和调用者放在**同一个搜索路径**、保持独立目录（详见 `INSTALL.md` §3.1，四个 harness 做法相同）。`setup-matt-pocock-skills` 每个仓库跑一次，**不进常驻**。

---

## 上游拉取地址（维护 Agent 的比对基准）

比对新版本时，请对照下列**仓库 + 路径**（不要只看仓库最近提交时间，也要看该路径的提交历史）。

### office/

| 技能 | 上游仓库 | 上游路径 | 目录历史 |
|---|---|---|---|
| `docx` | https://github.com/anthropics/skills | `skills/docx` | https://github.com/anthropics/skills/commits/main/skills/docx |
| `pdf` | https://github.com/anthropics/skills | `skills/pdf` | https://github.com/anthropics/skills/commits/main/skills/pdf |
| `pptx` | https://github.com/anthropics/skills | `skills/pptx` | https://github.com/anthropics/skills/commits/main/skills/pptx |
| `xlsx` | https://github.com/anthropics/skills | `skills/xlsx` | https://github.com/anthropics/skills/commits/main/skills/xlsx |

入口文件直链：`https://raw.githubusercontent.com/anthropics/skills/main/<上游路径>/SKILL.md`
例：https://raw.githubusercontent.com/anthropics/skills/main/skills/docx/SKILL.md

### permanent/

| 技能 | 上游仓库 | 上游路径 | 目录历史 |
|---|---|---|---|
| `tdd` | https://github.com/mattpocock/skills | `skills/engineering/tdd` | https://github.com/mattpocock/skills/commits/main/skills/engineering/tdd |
| `grill-me` | https://github.com/mattpocock/skills | `skills/productivity/grill-me` | https://github.com/mattpocock/skills/commits/main/skills/productivity/grill-me |
| `code-review` | https://github.com/mattpocock/skills | `skills/engineering/code-review` | https://github.com/mattpocock/skills/commits/main/skills/engineering/code-review |
| `diagnosing-bugs` | https://github.com/mattpocock/skills | `skills/engineering/diagnosing-bugs` | https://github.com/mattpocock/skills/commits/main/skills/engineering/diagnosing-bugs |
| `find-skills` | https://github.com/vercel-labs/skills | `skills/find-skills` | https://github.com/vercel-labs/skills/commits/main/skills/find-skills |
| `agent-browser` | https://github.com/vercel-labs/agent-browser | `skill-data/core` | https://github.com/vercel-labs/agent-browser/commits/main/skill-data/core |
| `ponytail` | https://github.com/DietrichGebert/ponytail | `skills/ponytail` | https://github.com/DietrichGebert/ponytail/commits/main/skills/ponytail |
| `grilling` ※依赖 | https://github.com/mattpocock/skills | `skills/productivity/grilling` | https://github.com/mattpocock/skills/commits/main/skills/productivity/grilling |
| `domain-modeling` ※依赖 | https://github.com/mattpocock/skills | `skills/engineering/domain-modeling` | https://github.com/mattpocock/skills/commits/main/skills/engineering/domain-modeling |
| `codebase-design` ※依赖 | https://github.com/mattpocock/skills | `skills/engineering/codebase-design` | https://github.com/mattpocock/skills/commits/main/skills/engineering/codebase-design |
| `setup-matt-pocock-skills` ※依赖 | https://github.com/mattpocock/skills | `skills/engineering/setup-matt-pocock-skills` | https://github.com/mattpocock/skills/commits/main/skills/engineering/setup-matt-pocock-skills |

依赖关系的调用方（四个 harness 相同）：

| 依赖技能 | 被谁调用 |
|---|---|
| `grilling` | `grill-me`、`grill-with-docs`、`improve-codebase-architecture` |
| `domain-modeling` | `grill-with-docs`、`improve-codebase-architecture` |
| `codebase-design` | `tdd`、`improve-codebase-architecture` |
| `setup-matt-pocock-skills` | `code-review`、`to-spec` |

`grill-me` 自身正文只有一句 "Call the Skill tool with \"grilling\""，`grill-with-docs` 同样只做转发；不放这些依赖，它们无法工作。

### project/

| 技能 | 上游仓库 | 上游路径 | 目录历史 |
|---|---|---|---|
| `frontend-design` | https://github.com/anthropics/skills | `skills/frontend-design` | https://github.com/anthropics/skills/commits/main/skills/frontend-design |
| `ui-ux-pro-max` | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | `.claude/skills/ui-ux-pro-max` | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/commits/main/.claude/skills/ui-ux-pro-max |
| `web-design-guidelines` | https://github.com/vercel-labs/agent-skills | `skills/web-design-guidelines` | https://github.com/vercel-labs/agent-skills/commits/main/skills/web-design-guidelines |
| `react-best-practices` | https://github.com/vercel-labs/agent-skills | `skills/react-best-practices` | https://github.com/vercel-labs/agent-skills/commits/main/skills/react-best-practices |
| `grill-with-docs` | https://github.com/mattpocock/skills | `skills/engineering/grill-with-docs` | https://github.com/mattpocock/skills/commits/main/skills/engineering/grill-with-docs |
| `to-spec` | https://github.com/mattpocock/skills | `skills/engineering/to-spec` | https://github.com/mattpocock/skills/commits/main/skills/engineering/to-spec |
| `improve-codebase-architecture` | https://github.com/mattpocock/skills | `skills/engineering/improve-codebase-architecture` | https://github.com/mattpocock/skills/commits/main/skills/engineering/improve-codebase-architecture |
| `handoff` | https://github.com/mattpocock/skills | `skills/productivity/handoff` | https://github.com/mattpocock/skills/commits/main/skills/productivity/handoff |

---

## 环境适配速览

完整说明见 **`INSTALL.md`**（harness 判定 → 安装 → 三项整改 → 自检 → 回滚）。要点：

**判 harness，只取第一个命中：** 有 `CLAUDE_PLUGIN_ROOT` 或装在 `.claude/skills/` → Claude Code；有 `CODEX_HOME` 或装在 `~/.codex/skills/` → Codex；进程/配置出现 Hermes → Hermes；其余 → Pi。

| 项 | 处理 |
|---|---|
| grill 一组 | 四个依赖与调用者同搜索路径、各自独立目录，**不要塞进 `grill-me/`**；四 harness 相同。若发现逐个问而非一轮问完，先加载 `grilling` |
| `ui-ux-pro-max` | 上游写死 `${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py`；**只改副本**为 `python "<本库>/project/ui-ux-pro-max/scripts/search.py"`。Claude Code 中该变量已设置且路径存在则不改。需 Python 3 |
| `agent-browser` | 入口名 `core`（**不要改**），正文要求 `agent-browser skills get core`；四 harness 都先 `npm i -g agent-browser && agent-browser install`。无 CLI 时只读 `permanent/agent-browser/SKILL.md` 并**说明浏览器命令不可用** |
| Anthropic 五个 | 按 `licenses/` 与技能目录内 `LICENSE.txt` 原文再分发。`frontend-design` 直接读；`docx`/`pdf`/`pptx`/`xlsx` 离开 Claude Code 时只当**版式规范**，用当前 harness 的写文件工具产出 |

自动整改：

```bash
node scripts/adapt.mjs --list                                        # 打印真实注册名
node scripts/adapt.mjs --check --dest <安装路径> --repo-root "$PWD"   # 预览
node scripts/adapt.mjs --apply --dest <安装路径> --repo-root "$PWD"   # 应用（写 patches/ 备份）
node scripts/adapt.mjs --revert --dest <安装路径> --skill <目录名>     # 回滚
```

**分类目录永远保持上游原文。** 脚本不会写它们，适配只落在安装副本与 `patches/`。

---

## 版本基线（本次拉取的上游提交）

| 上游仓库 | 提交 | 提交时间 |
|---|---|---|
| anthropics/skills | `8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4` | 2026-09-28T19:20:03-07:00 |
| mattpocock/skills | `d81f3a183412e71a5b1e84ca21bc1a35eea03a60` | 2026-09-29T13:37:40+01:00 |
| vercel-labs/skills | `18f96ea131dab3b0fcc9b27cf7c6f6cbb6174680` | 2026-10-02T09:25:54-07:00 |
| vercel-labs/agent-browser | `526157cfd4ec64f45939f9ba0f10d5936aa7ac33` | 2026-10-03T03:28:26-03:00 |
| vercel-labs/agent-skills | `063bee94c3f4df8453406c830b0a7df0f2860278` | 2026-08-28T15:36:07+02:00 |
| DietrichGebert/ponytail | `c982cd411abb53323c4baa1baa3c2f020b8d0b08` | 2026-10-03T07:12:55+02:00 |
| nextlevelbuilder/ui-ux-pro-max-skill | `477bcb28c9812b385cb51a4605ddf30d7b2266e2` | 2026-10-03T23:05:26+07:00 |

`upstream.json` 以机器可读形式记录同一批数据（含每个技能的上游仓库、路径、提交、许可证、`required_by` 依赖关系与本次收录日期）。

---

## 维护 Agent 的更新流程

1. 读取 `upstream.json`，对每个技能取 `repo` + `path`。
2. 用 GitHub API 比较该路径在上游的**最新提交**与记录中的 `commit`：
   `GET /repos/{repo}/commits?path={path}&per_page=1`
3. 若提交不同 → 用 `GET /repos/{repo}/git/trees/{branch}?recursive=1` 取该路径下文件清单，下载差异文件到对应目录（保留原目录结构，不要扁平化）。
4. 更新 `upstream.json` 里该条目的 `commit`、`commit_date`、`checked_on`。
5. **不要只看 `SKILL.md`**：`scripts/`、`references/`、`data/`、`agents/` 的变化同样要同步。
6. 同步后更新本 README 的「版本基线」表与「最后核对日期」。
7. 移除上游已删除的文件；不要保留遗留副本。
8. **不要把环境适配回写进分类目录**。适配只存在于安装副本与 `patches/`；更新上游后重新跑 `scripts/adapt.mjs --apply` 即可。

注意：

- **`ui-ux-pro-max` 的脚本路径**（见上表）在每个使用它的 harness 里都要按 §3.2 处理，`CLAUDE_PLUGIN_ROOT` 不能作为唯一方式。
- **`agent-browser` 对应上游 `skill-data/core`，目录已改名为 `agent-browser`**，其 `SKILL.md` 中 `name:` 仍是 `core`；`references/` 与 `templates/` 相对路径不变。
- **Anthropic 的 `docx`/`pdf`/`pptx`/`xlsx` 与 `frontend-design` 不是开源许可**：各技能目录内 `LICENSE.txt` 写明使用受 Anthropic 服务条款约束。不要再分发。
- `vercel-labs/agent-skills` 仓库没有 `LICENSE` 文件，README 声明为 MIT；`licenses/` 中未收录该仓库许可证原文，以 README 声明为准。

---

## 许可证

| 上游 | 许可证 | 原文 |
|---|---|---|
| anthropics/skills | 专有（Anthropic 服务条款） | 各技能目录内 `LICENSE.txt` |
| mattpocock/skills | MIT | `licenses/mattpocock-skills-MIT.txt` |
| vercel-labs/skills | MIT | `licenses/vercel-labs-skills-MIT.txt` |
| vercel-labs/agent-browser | Apache-2.0 | `licenses/vercel-labs-agent-browser-Apache-2.0.txt` |
| vercel-labs/agent-skills | MIT（README 声明） | — |
| DietrichGebert/ponytail | MIT | `licenses/DietrichGebert-ponytail-MIT.txt` |
| nextlevelbuilder/ui-ux-pro-max-skill | MIT | `licenses/nextlevelbuilder-ui-ux-pro-max-MIT.txt` |

---

## 本次未收录的相邻技能

这些技能有时与你清单里的技能同名或高度相关，但**未纳入**，避免歧义记录在此：

- `ponytail-review`（DietrichGebert/ponytail 同仓库）：只做「过度设计」审查，你确认要的是 `ponytail` 本体。
- `systematic-debugging`、`verification-before-completion`、`writing-plans`、`requesting-code-review`、`receiving-code-review`（obra/superpowers 及旧库）：与 `code-review`、`diagnosing-bugs` 功能重叠。
- `agent-browser` 仓库 `skill-data/` 下的 `electron`、`slack`、`dogfood`、`vercel-sandbox`、`derive-client`、`agentcore`、`protected-vercel-deployments` 等子技能：不属于浏览器核心操作。
- `mattpocock/skills` 的 `implement`、`implement-spec`、`prototype`、`research`、`pr`、`retro`、`triage`、`wayfinder`、`to-tickets`、`wizard`、`ask-matt` 等其余技能。
