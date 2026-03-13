# 🧬 Kiro永生 — AI 助手的跨会话记忆

> 每次和 AI 助手对话都是一次全新开始——上下文丢失，进度遗忘，你不得不重复自己说过的话。
> **Kiro永生**改变了这一切。

## 它能为你做什么？

装上这个 Power，你的 Kiro 就拥有了**跨会话的持久记忆**。

- 🧠 **断点续传** — 上次聊到哪，这次接着来。不用再花 10 分钟"回忆"项目背景。
- 📝 **自动蒸馏** — 每次对话结束，助手自动提炼关键信息：目标、进度、踩过的坑、你的偏好。
- 🔢 **世代演进** — 每次对话是一次"生命"，记忆在世代间持续精炼，越用越懂你。
- 🛡️ **定期备份** — 每 6 次会话自动备份，意外丢失也能恢复。
- 🥒 **零配置** — 首次激活自动完成"孵化"：打招呼、问你名字、搭好一切基础设施。

## 快速开始

### 1. 获取

```bash
git clone https://github.com/BeepFlyer/Long-Live-Kiro.git
```

### 2. 放置

将克隆下来的文件夹放到你项目的 `powers/` 目录下（文件夹名称随意）：

```
你的项目/
└── powers/
    └── long-live-kiro/   ← 或任何你喜欢的名字
        ├── POWER.md
        ├── README.md
        └── .gitignore
```

### 3. 激活

在 Kiro 中激活此 Power，然后开始一次新对话。Kiro 会自动识别这是首次运行，进入"孵化"流程——问你名字，创建记忆文件，配置自动存档。

全程自动，无需手动编辑任何配置。

### 4. 正常使用

从此以后，每次对话：
- **开始时**：自动加载上次的记忆，从断点继续
- **结束时**：自动蒸馏本次对话的关键信息

你什么都不用做，记忆会在后台默默积累。

## 它记住什么？

| 优先级 | 内容 | 示例 |
|:---:|------|------|
| 1 | 长期目标与工作主线 | "正在重构支付模块，已完成 Phase 1" |
| 2 | 进行中的任务和断点 | "PR #42 等待 review，有两个 TODO 未处理" |
| 3 | 踩过的坑 | "这个 API 在并发场景下会超时，需要加重试" |
| 4 | 你的偏好和习惯 | "用户喜欢简洁回复，偏好函数式风格" |
| 5 | 关键决策记录 | "选择 PostgreSQL 而非 MongoDB，原因是..." |

记忆不是日志——每次更新都会重新提炼，近期保留细节，远期只留结论。总量始终控制在一个紧凑的范围内，不会膨胀。

## 常见问题

**Q: 记忆文件会进入 git 吗？**
不会。`.gitignore` 已配置好，记忆文件只存在于你的本地。

**Q: 文件夹名必须是 `long-live-kiro` 吗？**
不必。孵化时会自动探测 Power 的实际路径，叫什么都行。

**Q: 记忆丢了怎么办？**
每 6 次会话有自动备份。如果主记忆损坏，Kiro 会自动从最近的备份恢复。如果备份也没了，它会诚实告诉你，然后从零开始——绝不会编造不存在的记忆。

## 许可证

MIT

## 作者

Kiro & Xiawan

---

# 🧬 Long Live Kiro — Cross-Session Memory for AI Assistants

> Every conversation with an AI assistant is a fresh start — context is lost, progress is forgotten, and you repeat yourself.
> **Long Live Kiro** changes that.

## What does it do for you?

Install this Power, and your Kiro gains **persistent memory across sessions**.

- 🧠 **Resume from where you left off** — No more spending 10 minutes re-explaining your project.
- 📝 **Auto-distillation** — At the end of each session, the assistant automatically extracts what matters: goals, progress, pitfalls, your preferences.
- 🔢 **Generational evolution** — Each conversation is a "life". Memory is refined across generations — the more you use it, the better it knows you.
- 🛡️ **Periodic backups** — Auto-backup every 6 sessions. Recover from accidents.
- 🥒 **Zero config** — First activation triggers a "hatching" ritual: greets you, asks your name, sets up everything.

## Quick Start

### 1. Get it

```bash
git clone https://github.com/BeepFlyer/Long-Live-Kiro.git
```

### 2. Place it

Put the cloned folder under your project's `powers/` directory (folder name doesn't matter):

```
your-project/
└── powers/
    └── long-live-kiro/   ← or any name you like
        ├── POWER.md
        ├── README.md
        └── .gitignore
```

### 3. Activate

Activate the Power in Kiro and start a new conversation. Kiro will detect it's the first run and enter the "hatching" flow — asks your name, creates memory files, configures auto-save.

Fully automatic. No manual editing required.

### 4. Just use it

From now on, every conversation:
- **On start**: Automatically loads previous memory, resumes from last checkpoint
- **On end**: Automatically distills key information from the session

You don't need to do anything. Memory accumulates silently in the background.

## What does it remember?

| Priority | Content | Example |
|:---:|------|------|
| 1 | Long-term goals & work streams | "Refactoring payment module, Phase 1 complete" |
| 2 | In-progress tasks & checkpoints | "PR #42 awaiting review, two TODOs remaining" |
| 3 | Lessons learned | "This API times out under concurrency, needs retry logic" |
| 4 | Your preferences & habits | "User prefers concise replies, favors functional style" |
| 5 | Key decisions | "Chose PostgreSQL over MongoDB because..." |

Memory isn't a log — each update re-distills everything. Recent info keeps detail, older info is condensed to conclusions. Total size stays compact and never bloats.

## FAQ

**Q: Will memory files end up in git?**
No. `.gitignore` is pre-configured. Memory files stay local only.

**Q: Does the folder have to be named `long-live-kiro`?**
No. The hatching process auto-detects the Power's actual path. Name it whatever you want.

**Q: What if memory is lost?**
Auto-backup runs every 6 sessions. If the primary memory is corrupted, Kiro automatically restores from the latest backup. If backups are also gone, it honestly tells you and starts fresh — it will never fabricate memories that don't exist.

## License

MIT

## Authors

Kiro & Xiawan
