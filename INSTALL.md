# 多 harness 安装与整改

> **给拉取本仓库的 Agent 看的第一份文件。** 拉库后先读完本节，再按当前环境整改。要改的地方全部集中在 `scripts/adapt.mjs`，正常使用不需要手改。

核心原则：**不改上游原文。** 三个分类目录里的文件是上游快照，逐字节与上游一致；任何环境适配只写进 `patches/`，或写到安装副本（复制出去的那份）。

---

## 1. 先判断当前 harness

**只取第一个命中的**，不叠加：

| 顺序 | 判据 | harness |
|---:|---|---|
| 1 | 环境变量有 `CLAUDE_PLUGIN_ROOT`，或技能装在 `.claude/skills/` | Claude Code |
| 2 | 环境变量有 `CODEX_HOME`，或技能装在 `~/.codex/skills/` | Codex |
| 3 | 进程名或配置文件出现 `Hermes` | Hermes |
| 4 | 以上都不命中 | Pi |

```bash
# 一行判断（可直接执行）
if [ -n "$CLAUDE_PLUGIN_ROOT" ] || [ -d .claude/skills ]; then echo claude-code
elif [ -n "$CODEX_HOME" ] || [ -d ~/.codex/skills ]; then echo codex
elif pgrep -qi hermes || grep -rqsi hermes ~/.config 2>/dev/null; then echo hermes
else echo pi; fi
```

**技能按 `SKILL.md` 里的 `name:` 注册，不按目录名。** 本仓库有两处目录名与 `name:` 不一致，属正常，不要"改正"：

- `permanent/agent-browser/` → `name: core`
- `project/react-best-practices/` → `name: vercel-react-best-practices`

用 `scripts/adapt.mjs --list` 可以打印每个目录的真实注册名。

---

## 2. 安装

`permanent/` 与 `project/` 里的技能目录**彼此独立、平铺**：把每个技能目录直接放进 harness 的 skills 搜索路径，不要把 `permanent/` 或 `project/` 整个目录当成一个技能塞进去，也不要嵌套。

| harness | 常见搜索路径（按实际改） |
|---|---|
| Claude Code | `<项目>/.claude/skills/` 或 `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Hermes | Hermes 自己的技能目录 |
| Pi | `~/.pi/agent/skills/` |

```bash
# 平铺复制（目标路径按上表替换）
DEST=~/.pi/agent/skills
mkdir -p "$DEST"
for d in permanent/* project/*; do [ -d "$d" ] && cp -a "$d" "$DEST/"; done   # 复制，不是软链；随后按 §3 改副本
```

`office/` 只装当前任务需要的，不是常驻。

---

## 3. 环境整改（三项）

全部是**改安装副本**，不要回写本仓库的分类目录。

### 3.1 grill 一组：四个依赖必须在同一搜索路径

依赖关系：

| 技能 | 调用 |
|---|---|
| `grill-me` | 只调用 `grilling` |
| `grill-with-docs` | 调用 `grilling` + `domain-modeling` |
| `tdd` | 调用 `codebase-design` |
| `improve-codebase-architecture` | 调用 `grilling` + `domain-modeling` + `codebase-design` |
| `code-review` | 调用 `setup-matt-pocock-skills` |
| `to-spec` | 调用 `setup-matt-pocock-skills` |

四个依赖 **`grilling`、`domain-modeling`、`codebase-design`、`setup-matt-pocock-skills` 都在 `permanent/`**，与调用者同一层。安装时把它们复制到**与 `permanent/`、`project/` 技能同一个搜索路径**，保持四个独立目录。

- **不要**塞进 `grill-me/` 里面。
- **四个 harness 做法相同**，没有差异。
- `grilling` 的一轮问法：**一次把整条前沿的问题问完**（编号 + 给出推荐答案），不是逐个问。若发现自己在逐个问、没走一轮问完，先确认 `grilling` 已加载。
- `grill-me` 正文只有一句转发，`grill-with-docs` 同理。它们本身没有实质内容，缺依赖就完全不可用。
- `domain-modeling` 在**项目里**随 `grill-with-docs` 一起加载，不需要额外动作。
- `setup-matt-pocock-skills` **每个仓库跑一次**（原本在新项目首次使用工程技能前跑），**不进常驻**：装到搜索路径后按需调用，不要让它常驻生效。它被 `code-review`、`to-spec` 引用。

### 3.2 ui-ux-pro-max：脚本绝对路径

上游正文把路径写死为：

```bash
python "${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py" "<query>" --domain <domain>
```

**只改副本**，换成：

```bash
python "<本库>/project/ui-ux-pro-max/scripts/search.py" "<query>" --domain <domain>
```

`<本库>` 是本仓库克隆的绝对路径。脚本有大量调用点（`--domain`、`--design-system`、`--stack`、`--persist` 等），全部换掉。

- **Claude Code**：若 `CLAUDE_PLUGIN_ROOT` 已设置**且该变量拼出的路径确实存在**，则不改，保持原样。
- 需要 **Python 3**。
- 自动改写：`node scripts/adapt.mjs --apply --dest <安装路径> --repo-root "$PWD"`

### 3.3 agent-browser：CLI 优先，说明书兜底

- 入口技能目录是 `permanent/agent-browser/`，但正文 `name:` 是 **`core`**，**不要改这个名字**。
- 正文要求执行 `agent-browser skills get core` 取完整用法（`--full` 取全文）。

**先装 CLI（四个 harness 都一样）：**

```bash
npm i -g agent-browser && agent-browser install
```

- **有 CLI**：走 `agent-browser skills get core`。
- **没有 CLI**：只读本库 `permanent/agent-browser/SKILL.md`（及 `references/`、`templates/`），并**明确说明浏览器命令不可用**，不要假装能开浏览器。
- 自检：`agent-browser --version` 有输出才算有 CLI。

### 3.4 Anthropic 五个

`frontend-design`、`docx`、`pdf`、`pptx`、`xlsx` **按 `licenses/` 与各技能目录内 `LICENSE.txt` 原文再分发**（这是 Anthropic 服务条款下的专有许可，不是开源）。

- `frontend-design`：直接读，无脚本依赖。
- `docx`、`pdf`、`pptx`、`xlsx`：脚本（`scripts/` 下的 Python、`office/` 校验器与 XSD schema）若依赖 Claude 的文件接口，**离开 Claude Code 就只当版式规范用**：读取其 `SKILL.md` 的排版/版式要求，改用**当前 harness 的写文件工具**产出文件，不要硬跑这些脚本。

---

## 4. 自检

整改后逐条确认：

```bash
# 1) 四个依赖能按名字找到（注册名，不是目录名）
for n in grilling domain-modeling codebase-design setup-matt-pocock-skills; do
  printf "%-26s " "$n"; ls -d "$DEST/$n" >/dev/null 2>&1 && grep -q "^name: $n" "$DEST/$n/SKILL.md" && echo ok || echo MISSING
done

# 2) search.py 绝对路径能跑
python "<本库>/project/ui-ux-pro-max/scripts/search.py" "dashboard" --domain ux | head -3

# 3) agent-browser CLI
agent-browser --version || echo "无 CLI：仅说明书模式，浏览器命令不可用"

# 4) 调用名与 name: 一致
node scripts/adapt.mjs --list
```

- 四个依赖：能按名字找到 ✔
- `search.py`：用绝对路径能跑 ✔（Claude Code 保留原变量且路径存在时不改）
- `agent-browser --version`：有输出；没有就标明"只有说明书" ✔
- 调用名与 `name:` 一致；浏览器用法用 `core` ✔

---

## 5. 安装副本的校验与回滚

`scripts/adapt.mjs` 每改写一个文件，都会在 `patches/` 下留一份原始副本与说明：

```
patches/
└── <技能目录名>/
    ├── MANIFEST.md        # 改了什么、为什么、harness
    └── <原文件>            # 改写前的原文（可直接覆盖回去回滚）
```

```bash
# 预览将要做的改写，不落盘
node scripts/adapt.mjs --check --dest <安装路径> --repo-root "$PWD"

# 应用（会写 patches/ 备份）
node scripts/adapt.mjs --apply --dest <安装路径> --repo-root "$PWD"

# 回滚某个技能
node scripts/adapt.mjs --revert --dest <安装路径> --skill ui-ux-pro-max
```

分类目录（`office/`、`permanent/`、`project/`）**永远保持上游原文**。脚本不会写它们；`--repo-root` 只用于拼 `search.py` 的绝对路径。更新上游（见 `README.md` 的维护流程）时不会与适配冲突，因为适配只存在于安装副本与 `patches/`。
