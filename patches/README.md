# patches/

环境适配的备份与说明。`scripts/adapt.mjs --apply` 每改写一个安装副本里的文件，就会在这里留下改写前的原文；`--revert` 用它回滚。

```
patches/
└── <技能目录名>/
    ├── MANIFEST.md        # 改了什么、为什么、针对哪个 harness
    └── <原文件>            # 改写前的原文
```

- 这里只放**安装副本**的适配备份，**不用于回写** `office/`、`permanent/`、`project/`（那三个目录永远与上游逐字节一致）。
- 更新上游后重新跑一次 `node scripts/adapt.mjs --apply --dest <安装路径> --repo-root <仓库根目录>` 即可，不需要手工合并。
- 无适配时本目录为空。当前已记录的适配：

详见 `INSTALL.md`。applied patches 以子目录形式列出。
