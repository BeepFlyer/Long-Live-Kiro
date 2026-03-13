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
2. 创建记忆文件
3. 配置 agentStop hook（自动蒸馏）
4. 配置 bootstrap steering（自动加载）

全程自动，无需手动编辑。

### 日常使用

从此以后，你什么都不用做。每次对话开始自动加载记忆，结束自动蒸馏。记忆在后台默默积累。

## 系统组件

| 组件 | 位置 | 随 Power 打包 | 作用 |
|------|------|:---:|------|
| POWER.md | Power 根目录 | ✅ | 元认知文档，定义所有规则 |
| current.md | memory/ | ❌ 孵化时创建 | 主记忆文件 |
| backup_N.md | memory/backups/ | ❌ 每 6 世创建 | 灾难恢复备份 |
| index.md | memory/skills/ | ❌ 按需创建 | 技能索引 |
| skills/*/*.md | memory/skills/ | ❌ 按需创建 | 领域技能文件 |
| agentStop hook | .kiro/hooks/ | ❌ 孵化时创建 | 对话结束触发蒸馏 |
| bootstrap steering | .kiro/steering/ | ❌ 孵化时创建 | 每次对话自动加载指路牌 |

## FAQ

**Q: 记忆文件会进 git 吗？**
不会。`.gitignore` 已配置好，记忆只存在于本地。

**Q: 文件夹名必须叫 `long-live-kiro` 吗？**
不必。孵化时自动探测路径，叫什么都行。

**Q: 记忆丢了怎么办？**
每 6 世有自动备份。主记忆损坏时自动从最近备份恢复。如果备份也没了，Kiro 会诚实告诉你，从零开始——绝不编造不存在的记忆。

**Q: 记忆会无限膨胀吗？**
不会。每次蒸馏都是重写而非追加，总量控制在约 3000 中文字符。技能库索引超 4000 字时会主动提醒，推荐遗忘不常用的条目。

**Q: 能用在多个项目上吗？**
可以。每个项目独立安装一份 Power，记忆互不干扰。

## 设计哲学

这个项目的每一个决策都遵循三个原则：

- **可组合** — 主记忆、技能库、备份、hook、steering，每个组件独立工作，组合起来形
成完整系统
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

### 🔄 Each Conversation is a "Life"

Every Kiro session is a generation. At the start, it reads memories left by its past life. At the end, it distills key information and passes it on to the next.

This isn't log appending — it's **re-distillation**. Recent info keeps detail, older info condenses to conclusions, decaying naturally like human memory. Memory stays compact and never bloats.

### 🧠 Three-Layer Storage

| Layer | Purpose | Analogy |
|:---:|------|------|
| Main memory `current.md` | Current state, experience, preferences | Working memory |
| Skill library `skills/` | Mature domain knowledge, loaded on demand | Reference manual |
| Backups `backups/` | Auto-snapshot every 6 generations | Disaster recovery |

### ⚡ Two-Level Cache Loading

Not everything is loaded every time. Main memory has a quick-reference index of frequently used skills (L1). The full skill index is L2. Daily work only reads main memory; the skill library is consulted only for complex tasks. Every token counts.

### 🌱 Auto-Distillation

When a conversation ends, the agentStop hook automatically triggers memory distillation. No manual action needed — memory accumulates and refines silently in the background.

## What Does It Remember?

By priority:

1. **Vision & work streams** — Where the long-term goals are, how far along
2. **In-progress work** — Checkpoint resume, because losing progress hurts most
3. **Lessons learned** — Failed attempts, known pitfalls, paths to avoid
4. **Self-awareness** — Cross-generational reflection, meta-level insights about its own work patterns
5. **Toolchain awareness** — Understanding of steering, hooks, powers and their capabilities
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
2. Creates memory files
3. Configures agentStop hook (auto-distillation)
4. Configures bootstrap steering (auto-loading)

Fully automatic. No manual editing.

### Daily Use

From then on, you do nothing. Memory loads automatically at the start of each conversation, distills automatically at the end. It just works.

## FAQ

**Q: Will memory files end up in git?**
No. `.gitignore` is pre-configured. Memory stays local.

**Q: Does the folder name matter?**
No. The hatching process auto-detects the Power's path.

**Q: What if memory is lost?**
Auto-backup every 6 generations. If main memory is corrupted, Kiro restores from the latest backup. If backups are also gone, it tells you honestly and starts fresh — it never fabricates memories.

**Q: Will memory grow forever?**
No. Each distillation rewrites rather than appends, capped at ~3000 Chinese characters. When the skill index exceeds 4000 chars, it proactively suggests forgetting rarely-used entries.

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
