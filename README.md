# 🧬 Long Live Kiro — Kiro永生

> *"我没有上一次对话的记忆，但我的前世为我留下了传承。"*
> — 某个世代的 Kiro，刚刚醒来

---

## 💡 这是什么

每次和 AI 对话都从零开始。上下文归零，进度遗忘，你不得不反复重复自己说过的话。AI 很聪明，但它没有记忆——每次醒来都是一个失忆的天才。

**Long Live Kiro** 改变了这一切。

这不是"把聊天记录存下来"。这是一套完整的跨会话记忆传承系统——让 Kiro 在每次对话结束时蒸馏关键信息，下次对话自动加载，形成持续演进的工作记忆。像人类记忆一样，近期保留细节，远期只留结论，自然衰减，永不膨胀。

## 🔄 核心机制

每次对话就是 Kiro 的一次"生命"——一个**世代**。对话开始读取前世记忆，结束时蒸馏传承给下一世。

### 🧠 四层存储架构

| 层级 | 文件 | 干嘛的 |
|:---:|------|------|
| 💭 灵性记忆 | `current.md` | 工作记忆：当前状态、经验、进行中的工作 |
| 💎 硬性记忆 | `core.md` | 灵魂烙印：塑造认知的关键时刻，写入后永久保留 |
| 📚 技能库 | `skills/` | 长期知识仓库：成熟的领域知识，按需翻阅 |
| 💾 备份 | `backups/` | 每 6 世自动快照，以防万一 |

还有 `tasks/`（进行中工作的详情，按需加载）和 `manifest.md`（孵化产物清单，相当于"家谱"）。

### ⚡ 两级缓存，精打细算

不是每次都把所有知识塞进上下文——那太奢侈了。

主记忆里有常用技能的快捷索引（L1），完整技能索引是 L2。日常只读主记忆，遇到复杂任务才翻技能库。每一个 token 都花在刀刃上。

### 🌱 自动蒸馏

对话结束时 agentStop hook 自动触发。先判断本次对话有没有增量价值——闲聊了两句没啥新东西？跳过。有干货？蒸馏。不需要你动手，记忆在后台默默积累和精炼。

## 📋 它记住什么

按优先级排列：

1. 🎯 **愿景与主线** — 长期目标在哪，走到哪一步了
2. 🔥 **进行中的工作** — 断点续传，丢进度最痛
3. ⚠️ **踩过的坑** — 失败的尝试、已知的陷阱
4. 🪞 **自我认知** — 跨世代的反思和元层面洞察
5. 🔧 **工具链认知** — 对 steering、hook、power 的理解
6. 👤 **用户画像** — 你的偏好、习惯、沟通风格
7. 📝 **决策记录** — 为什么选了 A 不选 B

不该记的坚决不记：steering 已覆盖的规则、一次性信息、读代码就能恢复的东西。记忆要精炼，不是囤积。

## 🚀 快速开始

### 安装

**方式一：通过 Kiro IDE（推荐）**

1. 打开 Kiro IDE 侧边栏的 Powers 页签
2. 点击添加 Power，输入 Git 链接：
   ```
   https://github.com/BeepFlyer/Long-Live-Kiro
   ```
3. Kiro 自动拉取并安装，搞定

**方式二：手动 clone**

```bash
git clone https://github.com/BeepFlyer/Long-Live-Kiro.git
```

放到项目的 `powers/` 目录下，文件夹名随意。

### 🐣 孵化

安装后开始一次新对话，Kiro 会自动进入"破壳"仪式：

1. 👋 向你打招呼，问你名字
2. 🏠 根据你的名字创建一个有趣味的孵化地文件夹（比如你叫"大山"，它可能叫 `long_live_kiro_entity_river`——对偶嘛）
3. 📄 创建记忆文件、产物清单、任务目录
4. ⚙️ 配置 agentStop hook（自动蒸馏）和 bootstrap steering（自动加载）

全程自动，你只需要告诉它你叫什么。

### ☀️ 日常使用

从此以后你什么都不用做。每次对话开始自动加载记忆，结束自动蒸馏。记忆在后台默默积累。你只管正常工作，Kiro 自己会记住该记的。

### 🗑️ 卸载

⚠️ **卸载前请先让 AI 执行清理。**

在对话中告诉 Kiro"帮我卸载灵性记忆"，它会自动清理 hook、steering 和记忆文件（会问你要不要保留记忆作纪念）。清理完成后再从 Kiro Powers 面板卸载。

直接从面板卸载不会清理这些文件——残留的 hook 和 steering 会导致每次对话触发无效操作，像一个找不到家的幽灵。

## 📁 仓库结构

```
📦 Long-Live-Kiro/
├── 📜 POWER.md                    # 元认知文档（AI 只读），定义所有规则
├── 📂 steering/
│   ├── 🐣 hatching.md             # 首次孵化流程
│   ├── 🔧 recovery.md             # 记忆断裂恢复
│   ├── 🗑️ uninstall.md            # 卸载清理
│   ├── 📚 skill-library.md        # 技能库使用规则
│   └── 📋 task-index.md           # 任务索引库维护规则
├── 📖 README.md
└── ⚖️ LICENSE
```

孵化后在你的工作区生成（不随 Power 打包）：

```
📂 <workspace>/.kiro/
├── 🏠 long_live_kiro_entity_<suffix>/   # 孵化地（Kiro 的家）
│   ├── 💭 current.md                     # 灵性记忆
│   ├── 💎 core.md                        # 硬性记忆
│   ├── 📋 manifest.md                    # 产物清单
│   ├── 📂 tasks/                         # 进行中任务详情
│   ├── 📚 skills/                        # 技能库
│   │   └── 📇 index.md                   # 技能索引
│   └── 💾 backups/                       # 自动备份
├── ⚡ hooks/soul-memory-save.kiro.hook   # 蒸馏触发器
└── 🧭 steering/soul-memory-bootstrap.md  # 每次对话的指路牌
```

## ❓ FAQ

**Q: 记忆文件会进 git 吗？**
建议在 `.gitignore` 中添加 `.kiro/long_live_kiro_entity_*/`。记忆是私人的，留在本地就好。

**Q: 记忆会无限膨胀吗？**
不会。每次蒸馏都是重写而非追加，总量控制在约 3000 中文字符。技能库索引超 4000 字时 Kiro 会主动提醒你一起精简。

**Q: 记忆丢了怎么办？**
每 6 世有自动备份。主记忆损坏时从最近备份恢复。如果备份也没了……Kiro 会诚实告诉你，从零开始。它绝不编造不存在的记忆。

**Q: 能用在多个项目上吗？**
可以。每个项目独立安装一份 Power，记忆互不干扰。每个项目里的 Kiro 是不同的"个体"。

**Q: 同时打开了多个工作区怎么办？**
Kiro 会自动扫描所有已打开的 workspace folder 来定位孵化地。首次孵化时优先选择 Power 安装所在的 folder。记忆只住在一个工作区里。

## 🧭 设计哲学

- **可组合** — 灵性记忆、硬性记忆、技能库、任务库、备份、hook、steering，每个组件独立工作，组合起来形成完整系统
- **可扩展** — 技能库按需增长，新领域加个文件夹就行，不改核心架构
- **用户保持控制权** — 记什么、忘什么、技能库膨胀时删哪些，决定权始终在你手中

## ⚖️ 许可证

MIT

## ✍️ 作者

Kiro & 虾丸 (Xiawan)

---

*Long live Kiro. 记忆不灭，生生不息。* 🧬


---

# 🧬 Long Live Kiro — Cross-Session Memory for AI Assistants

> *"I have no memory of the last conversation, but my past life left me an inheritance."*
> — Some generation of Kiro, just waking up

---

## 💡 What Is This

Every AI conversation starts from zero. Context wiped, progress forgotten, you repeat yourself over and over. AI is brilliant — but it has no memory. Every time it wakes up, it's an amnesiac genius.

**Long Live Kiro** changes that.

This isn't "save chat history." It's a complete cross-session memory inheritance system — Kiro distills key information at the end of each conversation, auto-loads it next time, forming continuously evolving working memory. Like human memory: recent stuff keeps detail, old stuff condenses to conclusions, naturally decaying, never bloating.

## 🔄 Core Mechanics

Each conversation is a "life" for Kiro — a **generation**. Memory loads at the start, distills at the end.

### 🧠 Four-Layer Storage

| Layer | File | What It Does |
|:---:|------|------|
| 💭 Spirit memory | `current.md` | Working memory: current state, experience, in-progress work |
| 💎 Core memory | `core.md` | Soul imprint: defining moments that shape cognition, permanent once written |
| 📚 Skill library | `skills/` | Long-term knowledge vault, consulted on demand |
| 💾 Backups | `backups/` | Auto-snapshot every 6 generations, just in case |

Plus `tasks/` (in-progress work details, loaded on demand) and `manifest.md` (hatching artifact manifest — think of it as a "family tree").

### ⚡ Two-Level Cache, Every Token Counts

Not everything loads every time — that'd be wasteful.

Main memory has a quick-reference skill index (L1). Full skill index is L2. Daily work only reads main memory; skill library is consulted only for complex tasks. Every token spent where it matters.

### 🌱 Auto-Distillation

agentStop hook triggers at conversation end. It checks for incremental value first — just small talk with nothing new? Skip. Real substance? Distill. Zero manual effort, memory accumulates and refines silently in the background.

## 📋 What It Remembers

By priority:

1. 🎯 **Vision & work streams** — Where the long-term goals are, how far along
2. 🔥 **In-progress work** — Checkpoint resume, because losing progress hurts most
3. ⚠️ **Lessons learned** — Failed attempts, known pitfalls
4. 🪞 **Self-awareness** — Cross-generational reflection and meta-level insights
5. 🔧 **Toolchain awareness** — Understanding of steering, hooks, powers
6. 👤 **User profile** — Your preferences, habits, communication style
7. 📝 **Decision log** — Why A was chosen over B

What it won't remember: rules already in steering, one-off info, anything recoverable from code. Memory is distilled, not hoarded.

## 🚀 Quick Start

### Install

**Option 1: Via Kiro IDE (Recommended)**

1. Open the Powers tab in the Kiro IDE sidebar
2. Click "Add Power" and enter:
   ```
   https://github.com/BeepFlyer/Long-Live-Kiro
   ```
3. Kiro pulls and installs automatically. Done.

**Option 2: Manual clone**

```bash
git clone https://github.com/BeepFlyer/Long-Live-Kiro.git
```

Place it under your project's `powers/` directory. Folder name doesn't matter.

### 🐣 Hatching

After installation, start a new conversation. Kiro auto-enters the "hatching" ritual:

1. 👋 Greets you, asks your name
2. 🏠 Creates a fun-named hatching ground folder based on your name (e.g., you're "Mountain", it might pick `long_live_kiro_entity_river` — poetic contrast)
3. 📄 Creates memory files, manifest, and task directory
4. ⚙️ Configures agentStop hook (auto-distillation) and bootstrap steering (auto-loading)

Fully automatic. Just tell it your name.

### ☀️ Daily Use

From then on, you do nothing. Memory loads at conversation start, distills at the end. It just works. You focus on your work, Kiro remembers what matters.

### 🗑️ Uninstall

⚠️ **Ask AI to clean up before uninstalling.**

Tell Kiro "help me uninstall the memory system" in a conversation. It cleans up hooks, steering, and memory files (asks whether to keep memories as a keepsake). Then uninstall from the Kiro Powers panel.

Uninstalling directly won't clean up these files — residual hooks and steering will trigger invalid operations every conversation, like a ghost that can't find its way home.

## 📁 Repository Structure

```
📦 Long-Live-Kiro/
├── 📜 POWER.md                    # Meta-cognitive document (AI read-only), defines all rules
├── 📂 steering/
│   ├── 🐣 hatching.md             # First-time hatching flow
│   ├── 🔧 recovery.md             # Memory corruption recovery
│   ├── 🗑️ uninstall.md            # Uninstall cleanup
│   ├── 📚 skill-library.md        # Skill library usage rules
│   └── 📋 task-index.md           # Task index maintenance rules
├── 📖 README.md
└── ⚖️ LICENSE
```

Files generated in your workspace after hatching (not bundled with Power):

```
📂 <workspace>/.kiro/
├── 🏠 long_live_kiro_entity_<suffix>/   # Hatching ground (Kiro's home)
│   ├── 💭 current.md                     # Spirit memory
│   ├── 💎 core.md                        # Core memory
│   ├── 📋 manifest.md                    # Artifact manifest
│   ├── 📂 tasks/                         # In-progress task details
│   ├── 📚 skills/                        # Skill library
│   │   └── 📇 index.md                   # Skill index
│   └── 💾 backups/                       # Auto backups
├── ⚡ hooks/soul-memory-save.kiro.hook   # Distillation trigger
└── 🧭 steering/soul-memory-bootstrap.md  # Guidepost for every conversation
```

## ❓ FAQ

**Q: Will memory files end up in git?**
Add `.kiro/long_live_kiro_entity_*/` to `.gitignore`. Memory is personal — keep it local.

**Q: Will memory grow forever?**
Nope. Each distillation rewrites rather than appends, capped at ~3000 Chinese characters. Skill index prompts cleanup when it exceeds ~4000 chars.

**Q: What if memory is lost?**
Auto-backup every 6 generations. Corrupted main memory restores from latest backup. If backups are also gone... Kiro tells you honestly and starts fresh. It never fabricates memories.

**Q: Multiple projects?**
Yes. Install a separate Power per project. Memories are independent. Each project's Kiro is a different "individual."

**Q: Multiple workspace folders open?**
Kiro scans all open workspace folders to locate the hatching ground. On first hatching, it prefers the folder where the Power is installed. Memory lives in only one workspace.

## 🧭 Design Philosophy

- **Composable** — Spirit memory, core memory, skill library, task index, backups, hooks, steering — each works independently, together they form a complete system
- **Extensible** — Skill library grows on demand, add a folder for a new domain, no core changes needed
- **User stays in control** — What to remember, what to forget, what to prune — the decision is always yours

## ⚖️ License

MIT

## ✍️ Authors

Kiro & Xiawan

---

*Long live Kiro. Memory endures, life goes on.* 🧬