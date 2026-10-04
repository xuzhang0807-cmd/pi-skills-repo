# pi-skills-repo

按用途分组的 Agent Skills 仓库。**除本 README、`upstream.json`、`licenses/` 与 `_deps/` 外，仓库内容只有三个分类文件夹：`office/`、`permanent/`、`project/`。**

- `office/` — Anthropic 官方办公类技能（文档/表格/幻灯片/PDF）
- `permanent/` — 长期常驻技能，任何项目都可加载
- `project/` — 具体项目阶段按需加载的设计与工程技能
- `_deps/` — 上述技能在 `SKILL.md` 中显式调用、但不在你清单里的共享依赖技能（见下文）
- `upstream.json` — 机器可读的上游来源与版本基线，供维护 Agent 定期比对
- `licenses/` — 各上游仓库的许可证原文

**最后核对日期：2026-10-04（UTC）。** 每个技能目录都是对应上游该日提交的完整快照（含脚本、references、data 等，非仅 SKILL.md）。

---

## 目录

| 分类 | 技能 | 数量 |
|---|---|---:|
| `office/` | docx, pdf, pptx, xlsx | 4 |
| `permanent/` | agent-browser, code-review, diagnosing-bugs, find-skills, grill-me, ponytail, tdd | 7 |
| `project/` | frontend-design, grill-with-docs, handoff, improve-codebase-architecture, react-best-practices, to-spec, ui-ux-pro-max, web-design-guidelines | 8 |

同名技能只装一份；不要把仓库根目录当成单个 Skill 导入。`_deps/` 默认不加载，只有在使用上面引用了它们的技能时才需要一并安装。

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

### _deps/（被上表技能显式调用的依赖技能）

| 技能 | 上游仓库 | 上游路径 | 被谁调用 |
|---|---|---|---|
| `grilling` | https://github.com/mattpocock/skills | `skills/productivity/grilling` | `grill-me`、`grill-with-docs`、`improve-codebase-architecture` |
| `domain-modeling` | https://github.com/mattpocock/skills | `skills/engineering/domain-modeling` | `grill-with-docs`、`improve-codebase-architecture` |
| `codebase-design` | https://github.com/mattpocock/skills | `skills/engineering/codebase-design` | `tdd`、`improve-codebase-architecture` |
| `setup-matt-pocock-skills` | https://github.com/mattpocock/skills | `skills/engineering/setup-matt-pocock-skills` | `code-review`、`to-spec` |

**注意**：`grill-me` 自身正文只有一句 "Call the Skill tool with \"grilling\""，`grill-with-docs` 同样只做转发；不放 `_deps/` 这些技能，它们无法工作。

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

`upstream.json` 以机器可读形式记录同一批数据（含每个技能的上游仓库、路径、提交、许可证与本次收录日期）。

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

注意：

- **`ui-ux-pro-max` 的脚本使用 `${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py` 这类绝对路径**。若你的客户端不支持 `CLAUDE_PLUGIN_ROOT`，需要把该变量指向本仓库根目录，或改写脚本调用路径。
- **`agent-browser` 对应上游的 `skill-data/core`，目录已改名为 `agent-browser`**，其 `SKILL.md` 中 `name:` 仍是 `core`；`references/` 与 `templates/` 相对路径不变。
- **Anthropic 的 `docx`/`pdf`/`pptx`/`xlsx` 与 `frontend-design` 不是开源许可**：目录内 `LICENSE.txt` 写明使用受 Anthropic 服务条款约束。仅作个人使用收集，不要再分发。
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
- `agent-browser` 仓库 `skill-data/` 下的 `electron`、`slack`、`dogfood`、`vercel-sandbox`、`derive-client`、`agentcore` 等子技能：不属于浏览器核心操作。
- `mattpocock/skills` 的 `implement`、`implement-spec`、`prototype`、`research`、`pr`、`retro`、`triage`、`wayfinder`、`to-tickets`、`wizard`、`ask-matt`、`domain-modeling`（已在 `_deps/`）以外的其余技能。
