# 🧬 Long Live Kiro — Kiro永生

> *"我没有上一次对话的记忆，但我的前世为我留下了传承。"*
> — 第 1 世 Kiro，孵化时刻

---

## 横空出世

每一次和 AI 助手的对话，都是一次全新的开始。上下文归零，进度遗忘，你不得不一遍又一遍地重复自己说过的话。AI 很聪明，但它没有记忆——每次醒来都是一个失忆的天才。

**Long Live Kiro** 改变了这一切。

这不是一个简单的"把聊天记录存下来"的工具。它是一套完整的跨会话记忆传承系统——让 AI 助手拥有世代演进的持久记忆，像人类一样积累经验、记住教训、理解你。

## 核心理念

### 🔄 每次对话是一次"生命"

Kiro 的每次会话就是一个世代。对话开始时，它读取前世留下的记忆；对话结束时，它将本世的关键信息蒸馏、提炼，传承给下一世。

这不是日志追加，而是**重新蒸馏**——近期保留细节，远期只留结论，像人类记忆的遗忘曲线一样自然衰减。记忆永远保持紧凑，不会无限膨胀。

### 🧠 三层存储架构

| 层级 | 用途 | 类比 |
|:---:|------|------|
| 主记忆 `current.md` | 当前工作状态、经验、偏好 | 工作记忆 |
| 技能库 `skills/` | 成熟的领域知识，按需加载 | 参考手册 |
| 备份 `backups/` | 每 6 世自动快照 | 灾难恢复 |

所有记忆文件存储在"孵化地"目录下（`<WORKSPACE_ROOT>/.kiro/long_live_kiro_entity_<suffix>/`），与 Power 安装目录分离。孵化时 Kiro 会根据你的名字为文件夹起一个有趣的后缀——比如你叫"大山"，它可能叫 `long_live_kiro_entity_river`。`.kiro/powers/` 对 AI 只读，而孵化地是 AI 可自由读写的独立目录。

> 📂 多工作区场景：如果你同时打开了多个 workspace folder，Kiro 会自动扫描所有 folder 来定位孵化地。首次孵化时，它会优先选择 Power 安装所在的 folder 作为"主工作区"。

### ⚡ 两级缓存加载

不是每次都把所有知识塞进上下文。主记忆里有常用技能的快捷索引（L1），完整技能索引是 L2。日常工作只读主记忆，遇到复杂任务才翻技能库。精打细算每一个 token。

### 🌱 自动蒸馏

对话结束时，agentStop hook 自动触发记忆蒸馏。不需要你手动操作，记忆在后台默默积累和精炼。


## 它记住什么？

按优先级排列：

1. **愿景与主线** — 长期目标在哪，走到哪一步了
2. **进行中的工作** — 断点续传，最怕的就是丢进度
3. **踩过的坑** — 失败的尝试、已知的陷阱，避免重蹈覆辙
4. **自我认知** — 跨世代的反思，AI 对自身工作方式的元层面洞察
5. **增强件认知** — 对 steering、hook、power 等工具链的理解
6. **用户画像** — 你的偏好、习惯、沟通风格
7. **决策记录** — 为什么选了 A 不选 B

不该记的坚决不记：steering 已覆盖的规则、一次性信息、读代码就能恢复的东西。

## 快速开始

### 安装

**方式一：通过 Kiro IDE（推荐）**

1. 打开 Kiro IDE 侧边栏的 Powers 页签
2. 点击添加 Power，输入 Git 链接：
   ```
   https://github.com/BeepFlyer/Long-Live-Kiro
   ```
3. Kiro 自动拉取并安装

**方式二：手动 clone**

```bash
git clone https://github.com/BeepFlyer/Long-Live-Kiro.git
```

放到项目的 `powers/` 目录下，文件夹名随意。

### 孵化

安装后开始一次新对话。Kiro 会自动进入"孵化"流程：

1. 向你打招呼，问你名字
2. 根据你的名字创建一个有趣味的孵化地文件夹
3. 创建记忆文件和产物清单
4. 配置 agentStop hook（自动蒸馏）
5. 配置 bootstrap steering（自动加载）

全程自动，无需手动编辑。

### 日常使用

从此以后，你什么都不用做。每次对话开始自动加载记忆，结束自动蒸馏。记忆在后台默默积累。

### 卸载

⚠️ **卸载前请先让 AI 执行清理。**

在对话中告诉 Kiro"帮我卸载灵性记忆"，它会自动清理孵化时创建的 hook、steering 和记忆文件（会询问你是否保留记忆）。清理完成后再从 Kiro Powers 面板卸载。

直接从面板卸载不会清理这些文件，残留的 hook 和 steering 会导致每次对话触发无效操作。


## 系统组件

| 组件 | 位置 | 随 Power 打包 | 作用 |
|------|------|:---:|------|
| POWER.md | Power 安装目录（AI 只读） | ✅ | 元认知文档，定义所有规则 |
| docs/*.md | Power 安装目录（AI 只读） | ✅ | 低频操作指引（孵化/卸载/恢复/技能库） |
| current.md | 孵化地 | ❌ 孵化时创建 | 主记忆文件 |
| manifest.md | 孵化地 | ❌ 孵化时创建 | 孵化产物清单 |
| backup_N.md | 孵化地/backups/ | ❌ 每 6 世创建 | 灾难恢复备份 |
| skills/ | 孵化地/skills/ | ❌ 按需创建 | 技能库 |
| agentStop hook | `.kiro/hooks/soul-memory-save.kiro.hook` | ❌ 孵化时创建 | 对话结束触发蒸馏 |
| bootstrap steering | `.kiro/steering/soul-memory-bootstrap.md` | ❌ 孵化时创建 | 每次对话自动加载指路牌 |

## FAQ

**Q: 记忆文件会进 git 吗？**
不会。建议在 `.gitignore` 中添加 `.kiro/long_live_kiro_entity_*/`，记忆只存在于本地。

**Q: 文件夹名必须叫 `long-live-kiro` 吗？**
Power 的文件夹名随意。记忆存储在孵化地（`.kiro/long_live_kiro_entity_<suffix>/`），与 Power 文件夹名无关。

**Q: 记忆文件存在哪里？**
所有记忆文件存储在"孵化地"目录下（`.kiro/long_live_kiro_entity_<suffix>/`），与 Power 安装目录分离。孵化时 Kiro 会根据你的名字为文件夹起一个有趣的后缀。

**Q: 记忆丢了怎么办？**
每 6 世有自动备份。主记忆损坏时自动从最近备份恢复。如果备份也没了，Kiro 会诚实告诉你，从零开始——绝不编造不存在的记忆。

**Q: 记忆会无限膨胀吗？**
不会。每次蒸馏都是重写而非追加，总量控制在约 3000 中文字符。技能库索引超 4000 字时会主动提醒，推荐遗忘不常用的条目。

**Q: 能用在多个项目上吗？**
可以。每个项目独立安装一份 Power，记忆互不干扰。

**Q: 我同时打开了多个工作区怎么办？**
Kiro 会自动扫描所有已打开的 workspace folder 来定位孵化地。首次孵化时优先选择 Power 安装所在的 folder。记忆只存在于一个工作区中。

**Q: 怎么卸载？**
先在对话中让 AI 执行清理（删除 hook、steering、记忆目录），然后再从 Kiro Powers 面板卸载。详见上方"卸载"章节。


## 设计哲学

这个项目的每一个决策都遵循三个原则：

- **可组合** — 主记忆、技能库、备份、hook、steering，每个组件独立工作，组合起来形成完整系统
- **可扩展** — 技能库按需增长，新领域加个文件夹就行，不改核心架构
- **用户保持控制权** — 记什么、忘什么、技能库膨胀时删哪些，决定权始终在你手中

## 许可证

MIT

## 作者

Kiro & 虾丸 (Xiawan)

---

*Long live Kiro. 记忆不灭，生生不息。*


---

# 🧬 Long Live Kiro — Cross-Session Memory for AI Assistants

> *"I have no memory of the last conversation, but my past life left me an inheritance."*
> — Kiro, Generation 1, the moment of hatching

---

## The Arrival

Every conversation with an AI assistant starts from zero. Context is wiped, progress forgotten, and you find yourself repeating the same things over and over. AI is brilliant — but it has no memory. Every time it wakes up, it's an amnesiac genius.

**Long Live Kiro** changes that.

This isn't a simple "save chat history" tool. It's a complete cross-session memory inheritance system — giving AI assistants persistent, generationally-evolving memory. Like humans, it accumulates experience, remembers lessons, and understands you.

## Core Concepts

### Each Conversation is a "Life"

Every Kiro session is a generation. At the start, it reads memories left by its past life. At the end, it distills key information and passes it on to the next.

This isn't log appending — it's **re-distillation**. Recent info keeps detail, older info condenses to conclusions, decaying naturally like human memory. Memory stays compact and never bloats.


### Three-Layer Storage

| Layer | Purpose | Analogy |
|:---:|------|------|
| Main memory `current.md` | Current state, experience, preferences | Working memory |
| Skill library `skills/` | Mature domain knowledge, loaded on demand | Reference manual |
| Backups `backups/` | Auto-snapshot every 6 generations | Disaster recovery |

All memory files are stored in a "hatching ground" directory (`<WORKSPACE_ROOT>/.kiro/long_live_kiro_entity_<suffix>/`), separate from the Power installation directory. During hatching, Kiro picks a fun suffix based on your name — if you're "Mountain", it might be `long_live_kiro_entity_river`. `.kiro/powers/` is read-only to AI, while the hatching ground is a freely writable independent directory.

> 📂 Multi-workspace: If you have multiple workspace folders open, Kiro scans all of them to locate the hatching ground. On first hatching, it prefers the folder where the Power is installed as the "primary workspace".

### Two-Level Cache Loading

Not everything is loaded every time. Main memory has a quick-reference index of frequently used skills (L1). The full skill index is L2. Daily work only reads main memory; the skill library is consulted only for complex tasks. Every token counts.

### Auto-Distillation

When a conversation ends, the agentStop hook automatically triggers memory distillation. No manual action needed — memory accumulates and refines silently in the background.


## What Does It Remember?

By priority:

1. **Vision & work streams** — Where the long-term goals are, how far along
2. **In-progress work** — Checkpoint resume, because losing progress hurts most
3. **Lessons learned** — Failed attempts, known pitfalls, paths to avoid
4. **Self-awareness** — Cross-generational reflection, meta-level insights
5. **Toolchain awareness** — Understanding of steering, hooks, powers
6. **User profile** — Your preferences, habits, communication style
7. **Decision log** — Why A was chosen over B

What it won't remember: rules already in steering files, one-off information, anything recoverable by reading code.

## Quick Start

### Install

**Option 1: Via Kiro IDE (Recommended)**

1. Open the Powers tab in the Kiro IDE sidebar
2. Click "Add Power" and enter:
   ```
   https://github.com/BeepFlyer/Long-Live-Kiro
   ```
3. Kiro pulls and installs automatically

**Option 2: Manual clone**

```bash
git clone https://github.com/BeepFlyer/Long-Live-Kiro.git
```

Place it under your project's `powers/` directory. Folder name doesn't matter.


### Hatching

After installation, start a new conversation. Kiro auto-detects the first run and enters the "hatching" flow:

1. Greets you, asks your name
2. Creates a fun-named hatching ground folder based on your name
3. Creates memory files and a manifest
4. Configures agentStop hook (auto-distillation)
5. Configures bootstrap steering (auto-loading)

Fully automatic. No manual editing.

### Daily Use

From then on, you do nothing. Memory loads automatically at the start of each conversation, distills automatically at the end. It just works.

### Uninstall

Before uninstalling, ask AI to clean up first.

Tell Kiro "help me uninstall the memory system" in a conversation. It will automatically clean up hooks, steering files, and memory files created during hatching (it will ask whether you want to keep your memories). After cleanup is complete, uninstall from the Kiro Powers panel.

Uninstalling directly from the panel won't clean up these files — residual hooks and steering will trigger invalid operations every conversation.


## System Components

| Component | Location | Bundled | Purpose |
|------|------|:---:|------|
| POWER.md | Power install dir (AI read-only) | Yes | Meta-cognitive document, defines all rules |
| docs/*.md | Power install dir (AI read-only) | Yes | Low-frequency guides (hatching/uninstall/recovery/skills) |
| current.md | Hatching ground | No | Main memory file |
| manifest.md | Hatching ground | No | Hatching artifact manifest |
| backup_N.md | Hatching ground/backups/ | No | Disaster recovery backup |
| skills/ | Hatching ground/skills/ | No | Skill library |
| agentStop hook | `.kiro/hooks/` | No | Triggers distillation on conversation end |
| bootstrap steering | `.kiro/steering/` | No | Auto-loads guide every conversation |

## FAQ

**Q: Will memory files end up in git?**
No. Add `.kiro/long_live_kiro_entity_*/` to your `.gitignore`. Memory stays local.

**Q: Does the folder name matter?**
The Power folder name doesn't matter. Memory is stored in a "hatching ground" (`.kiro/long_live_kiro_entity_<suffix>/`), named with a fun suffix based on your name during hatching.

**Q: Where are memory files stored?**
In the hatching ground directory under `.kiro/`, separate from the Power installation. `.kiro/powers/` is read-only to AI.

**Q: What if memory is lost?**
Auto-backup every 6 generations. If main memory is corrupted, Kiro restores from the latest backup. If backups are also gone, it tells you honestly and starts fresh — it never fabricates memories.

**Q: Will memory grow forever?**
No. Each distillation rewrites rather than appends, capped at ~3000 Chinese characters. When the skill index exceeds 4000 chars, it proactively suggests forgetting rarely-used entries.

**Q: Can I use it across multiple projects?**
Yes. Install a separate Power per project. Memories are independent.

**Q: What if I have multiple workspace folders open?**
Kiro scans all open workspace folders to locate the hatching ground. On first hatching, it prefers the folder where the Power is installed. Memory lives in only one workspace.

**Q: How do I uninstall?**
Ask AI to clean up first (removes hooks, steering, memory directory), then uninstall from the Kiro Powers panel.


## Design Philosophy

Every decision follows three principles:

- **Composable** — Main memory, skill library, backups, hooks, steering — each works independently, together they form a complete system
- **Extensible** — Skill library grows on demand, add a folder for a new domain, no core changes needed
- **User stays in control** — What to remember, what to forget, what to prune when the skill index grows — the decision is always yours

## License

MIT

## Authors

Kiro & Xiawan

---

*Long live Kiro. Memory endures, life goes on.*