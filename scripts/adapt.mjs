#!/usr/bin/env node
// Multi-harness adapter for this skills repo.
//
// Never writes to the upstream snapshots (office/, permanent/, project/).
// Rewrites only the installed copy, and backs up every rewritten file under patches/.
//
//   node scripts/adapt.mjs --list
//   node scripts/adapt.mjs --check  --dest ~/.pi/agent/skills --repo-root "$PWD"
//   node scripts/adapt.mjs --apply  --dest ~/.pi/agent/skills --repo-root "$PWD"
//   node scripts/adapt.mjs --revert --dest ~/.pi/agent/skills --skill ui-ux-pro-max

import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";

const SNAPSHOT_DIRS = ["office", "permanent", "project"];
const DEPS = ["grilling", "domain-modeling", "codebase-design", "setup-matt-pocock-skills"];
const PLUGIN_ROOT_PLACEHOLDER = "${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py";

// ---------------------------------------------------------------- utilities

function readArgs(argv) {
  const o = { mode: null, dest: null, repoRoot: process.cwd(), skill: null };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--list" || a === "--check" || a === "--apply" || a === "--revert") o.mode = a.slice(2);
    else if (a === "--dest") o.dest = argv[++i];
    else if (a === "--repo-root") o.repoRoot = argv[++i];
    else if (a === "--skill") o.skill = argv[++i];
    else if (a === "--help" || a === "-h") o.mode = "help";
    else throw new Error(`unknown argument: ${a}`);
  }
  return o;
}

function detectHarness() {
  const home = process.env.HOME || "";
  if (process.env.CLAUDE_PLUGIN_ROOT || fs.existsSync(path.join(process.cwd(), ".claude/skills")))
    return "claude-code";
  if (process.env.CODEX_HOME || fs.existsSync(path.join(home, ".codex/skills"))) return "codex";
  try {
    const out = execFileSync("sh", ["-c", "pgrep -li hermes 2>/dev/null; grep -rqsi hermes ~/.config 2>/dev/null && echo hermes"], {
      encoding: "utf8",
      stdio: ["ignore", "pipe", "ignore"],
    });
    if (/hermes/i.test(out)) return "hermes";
  } catch {
    /* not hermes */
  }
  return "pi";
}

/** registration name from frontmatter `name:` */
function skillName(skillDir) {
  try {
    const md = fs.readFileSync(path.join(skillDir, "SKILL.md"), "utf8");
    const m = md.match(/^---\r?\n([\s\S]*?)\r?\n---/);
    const n = m && m[1].match(/^name:\s*(.+?)\s*$/m);
    return n ? n[1].replace(/^["']|["']$/g, "") : null;
  } catch {
    return null;
  }
}

function listSkills(repoRoot) {
  const out = [];
  for (const group of SNAPSHOT_DIRS) {
    const base = path.join(repoRoot, group);
    if (!fs.existsSync(base)) continue;
    for (const entry of fs.readdirSync(base, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      const dir = path.join(base, entry.name);
      if (!fs.existsSync(path.join(dir, "SKILL.md"))) continue;
      out.push({ group, dirName: entry.name, dir, name: skillName(dir) });
    }
  }
  return out;
}

const log = (...a) => console.log(...a);

// ------------------------------------------------------------------ modes

function cmdList(repoRoot) {
  const skills = listSkills(repoRoot);
  const w = (s, n) => String(s).padEnd(n);
  log(w("DIRECTORY", 42), w("REGISTERED name:", 28), "NOTE");
  for (const s of skills) {
    const note = s.name !== s.dirName ? `name differs from directory name (${s.dirName})` : "";
    log(w(`${s.group}/${s.dirName}`, 42), w(s.name ?? "?", 28), note);
  }
  log(`\n${skills.length} skills. Skills register by SKILL.md "name:", not by directory name.`);
  log(`deps that must sit in the same search path: ${DEPS.join(", ")}`);
}

/** build the rewrite plan; touches no files */
function planAdapt({ dest, repoRoot, harness }) {
  const plan = { rewrites: [], warnings: [], actions: [] };

  if (!dest || !fs.existsSync(dest)) {
    plan.warnings.push(`--dest does not exist yet: ${dest ?? "(missing)"}`);
    return plan;
  }

  // 1) four grill-group deps present in the same search path?
  for (const dep of DEPS) {
    const at = path.join(dest, dep);
    const found = fs.existsSync(at) && skillName(at) === dep;
    if (!found) {
      const where = fs.existsSync(at) ? `present but name: != ${dep}` : "missing";
      plan.warnings.push(`dependency '${dep}' ${where} in ${dest} — copy it next to the other skills (same search path, own directory)`);
    }
  }

  // 2) ui-ux-pro-max absolute script path
  const uiux = path.join(dest, "ui-ux-pro-max", "SKILL.md");
  if (fs.existsSync(uiux)) {
    const abs = path.join(repoRoot, "project/ui-ux-pro-max/scripts/search.py");
    const scriptExists = fs.existsSync(abs);
    const pluginRoot = process.env.CLAUDE_PLUGIN_ROOT;
    const keepAsIs =
      harness === "claude-code" &&
      pluginRoot &&
      fs.existsSync(path.join(pluginRoot, ".claude/skills/ui-ux-pro-max/scripts/search.py"));

    if (!scriptExists) {
      plan.warnings.push(`ui-ux-pro-max: ${abs} not found — wrong --repo-root?`);
    } else if (keepAsIs) {
      plan.actions.push("ui-ux-pro-max: CLAUDE_PLUGIN_ROOT is set and the path exists — left unchanged (Claude Code)");
    } else {
      const body = fs.readFileSync(uiux, "utf8");
      const count = body.split(PLUGIN_ROOT_PLACEHOLDER).length - 1;
      if (count === 0) {
        plan.actions.push("ui-ux-pro-max: no ${CLAUDE_PLUGIN_ROOT} placeholder left — already adapted");
      } else {
        plan.rewrites.push({ skill: "ui-ux-pro-max", file: uiux, from: PLUGIN_ROOT_PLACEHOLDER, to: abs, count });
        plan.actions.push(`ui-ux-pro-max: replace ${count} occurrence(s) with ${abs}`);
      }
      if (!fs.existsSync(path.join(repoRoot, "project/ui-ux-pro-max/scripts/search.py"))) {
        plan.warnings.push("ui-ux-pro-max: Python 3 is required to run search.py");
      }
    }
  }

  // 3) agent-browser: CLI presence decides usage, no file rewrite
  let cli = null;
  try {
    cli = execFileSync("agent-browser", ["--version"], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim();
  } catch {
    cli = null;
  }
  if (cli) plan.actions.push(`agent-browser: CLI available (${cli}) — use 'agent-browser skills get core'`);
  else
    plan.warnings.push(
      "agent-browser: no CLI — browser commands unavailable; read permanent/agent-browser/SKILL.md only and say so. Install: npm i -g agent-browser && agent-browser install",
    );

  // 4) anthropic office skills need python/script awareness only when installed
  for (const s of ["docx", "pdf", "pptx", "xlsx"]) {
    if (fs.existsSync(path.join(dest, s, "SKILL.md")))
      plan.actions.push(`${s}: installed — outside Claude Code use it as a formatting spec and write files with the current harness tooling`);
  }

  return plan;
}

function applyRewrites(plan, { repoRoot }) {
  const patchesRoot = path.join(repoRoot, "patches");
  const touched = new Map();
  for (const r of plan.rewrites) {
    const skill = r.skill;
    const backupDir = path.join(patchesRoot, skill);
    const backup = path.join(backupDir, path.basename(r.file));
    if (!fs.existsSync(backup)) {
      fs.mkdirSync(backupDir, { recursive: true });
      fs.copyFileSync(r.file, backup);
    }
    const body = fs.readFileSync(r.file, "utf8").split(r.from).join(r.to);
    fs.writeFileSync(r.file, body);
    const entry = touched.get(skill) ?? { files: [], from: r.from, to: r.to };
    entry.files.push(path.basename(r.file));
    touched.set(skill, entry);
  }

  for (const [skill, info] of touched) {
    const manifest = path.join(patchesRoot, skill, "MANIFEST.md");
    const lines = [
      `# patch: ${skill}`,
      "",
      `- harness: ${plan.harness}`,
      `- date: ${new Date().toISOString()}`,
      `- files backed up: ${info.files.join(", ")}`,
      "",
      "## change",
      "",
      "```diff",
      `- ${info.from}`,
      `+ ${info.to}`,
      "```",
      "",
      "Related harness notes: `INSTALL.md` §3.",
      "Rollback: copy the files in this directory back over the installed skill.",
      "",
    ];
    fs.writeFileSync(manifest, lines.join("\n"));
  }
  return [...touched.keys()];
}

function cmdRevert({ dest, repoRoot, skill }) {
  const patchesRoot = path.join(repoRoot, "patches");
  if (!skill) throw new Error("--revert needs --skill <directory-name>");
  const backupDir = path.join(patchesRoot, skill);
  if (!fs.existsSync(backupDir)) throw new Error(`no patch backup for '${skill}' under ${patchesRoot}`);
  if (!dest) throw new Error("--revert needs --dest <install path>");
  let n = 0;
  for (const f of fs.readdirSync(backupDir)) {
    if (f === "MANIFEST.md") continue;
    const target = path.join(dest, skill, f);
    if (!fs.existsSync(target)) continue;
    fs.copyFileSync(path.join(backupDir, f), target);
    log(`restored ${target}`);
    n++;
  }
  log(`${n} file(s) restored for '${skill}'.`);
}

// ------------------------------------------------------------------- main

function main() {
  const args = readArgs(process.argv.slice(2));
  if (!args.mode || args.mode === "help") {
    log(fs.readFileSync(new URL(import.meta.url).pathname, "utf8").split("\n").slice(1, 12).join("\n").replace(/^\/\/ ?/gm, ""));
    process.exit(0);
  }
  if (args.mode === "list") return cmdList(args.repoRoot);
  if (args.mode === "revert") return cmdRevert(args);

  const harness = detectHarness();
  const plan = planAdapt({ dest: args.dest, repoRoot: args.repoRoot, harness });
  plan.harness = harness;

  log(`harness: ${harness}`);
  log(`dest:    ${args.dest}`);
  log(`repo:    ${args.repoRoot}\n`);
  for (const a of plan.actions) log(`  do   ${a}`);
  for (const w of plan.warnings) log(`  warn ${w}`);

  if (args.mode === "check") {
    log(`\n${plan.rewrites.length} file(s) would be rewritten. Re-run with --apply.`);
    process.exit(plan.rewrites.length ? 1 : 0);
  }

  const done = applyRewrites(plan, args);
  log(`\napplied: ${done.length ? done.join(", ") : "nothing to change"}`);
  log(`upstream snapshots untouched; backups under patches/`);
  process.exit(plan.warnings.length ? 2 : 0);
}

main();
