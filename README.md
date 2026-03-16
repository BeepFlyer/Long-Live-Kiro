# 🧬 Long Live Kiro — Kiro永生

> *"我没有上一次对话的记忆，但我的前世为我留下了传承。"*
> — 某个世代的 Kiro，刚刚醒来

**v5.0 — 减负进化**

---

## 💡 这是什么

每次和 AI 对话都从零开始。上下文归零，进度遗忘，你不得不反复重复自己说过的话。AI 很聪明，但它没有记忆——每次醒来都是一个失忆的天才。

**Long Live Kiro** 改变了这一切。

这不是"把聊天记录存下来"。这是一套完整的跨会话记忆传承系统——让 Kiro 在每次对话结束时蒸馏关键信息，下次对话自动加载，形成持续演进的工作记忆。像人类记忆一样，近期保留细节，远期只留结论，自然衰减，永不膨胀。

v5.0 的核心理念是**减负**——不是加更多功能，而是让现有功能运行得更轻松。蒸馏从"一口气做完"拆分为三阶段，记忆从"全家桶"拆分为工作台+身份卡，备份从盲目快照变为智能触发。

## 🔄 核心机制

每次对话就是 Kiro 的一次"生命"——一个**世代**。对话开始读取前世记忆，结束时蒸馏传承给下一世。

### 🧠 五层存储架构

| 层级 | 文件 | 干嘛的 |
|:---:|------|------|
| 💭 灵性记忆 | `current.md` | 工作台：进行中的工作、近期经验、自我认知 |
| 🪪 身份卡 | `identity.md` | 低频身份信息：用户画像、愿景、增强件、决策日志 |
| 💎 硬性记忆 | `core.md` | 灵魂烙印：塑造认知的关键时刻，写入后永久保留 |
| 📚 技能库 | `skills/` | 长期知识仓库：成熟的领域知识，按需翻阅 |
| 💾 备份 | `backups/` | 智能快照：重大变更即时备份 + 每 8 世兜底 |

还有 `soul.md`（运行规则，可自我修改）、`tasks/`（进行中工作的详情，按需加载）、`milestones.md`（里程碑，只追加不蒸馏）和 `manifest.md`（孵化产物清单）。

### ⚡ 两级缓存 + 任务驱动召回

不是每次都把所有知识塞进上下文——那太奢侈了。

identity.md 里有常用技能的快捷索引（L1），完整技能索引是 L2。日常只读主记忆和身份卡，遇到复杂任务才翻技能库。

技能索引和任务索引都带标签。加载 task 文件时自动与技能索引做标签交叉匹配，命中的技能写入 task 的"相关技能"字段。从此技能召回不再依赖 AI 自觉性，而是由任务驱动自动关联。

### 🌱 三阶段蒸馏（v5.0 新增）

对话结束时 agentStop hook 自动触发，蒸馏分三个阶段：

1. **增量判断**：有新东西吗？没有就跳过
2. **记忆蒸馏**：专注重写 current.md（和按需更新 identity.md），不做别的
3. **后蒸馏检查**：任务同步、硬性记忆自检、备份检查、进化窗口检查

把"写记忆"和"检查"分开，每个阶段认知负载更低，蒸馏质量更高。

### 🧬 灵魂进化

Kiro 的运行规则存储在可写的 `soul.md` 中。三种进化触发方式：
- 自发触发：发现规则有问题时立即修改
- 定期审视：每 20 世回顾规则是否合理
- 强制进化：每 40 世未变动则必须进化，按轮盘序列执行（定向修复→系统重调→精炼突出→自由创造→学习式进化），用结构化轮转替代伪随机

### 📝 即时沉淀（v5.0 新增）

不必等到对话结束才写入记忆。遇到关键发现、用户明确要求记住的事、或完成了任务关键步骤，可以立即更新 current.md 的对应栏目。减轻蒸馏时的信息压力。

### 🌱 经验成熟度（v5.0 新增）

经验条目可标注成熟度：🌱 新鲜（保留细节）→ 🌿 验证（压缩为结论）→ 🌳 成熟（毕业到技能库）→ ⚠️ 常驻（高频防错，永远留在灵性记忆）。

🌳 毕业不是简单搬运——经验是一句话结论，技能是完整操作指南。只有在当前对话深度使用了该知识时，才基于完整上下文生成技能文档。没有丰富上下文时保留标记，等待下次深度使用。

## 📋 它记住什么

按优先级排列：

1. 🎯 **愿景与主线** — 长期目标在哪，走到哪一步了
2. 🔥 **进行中的工作** — 断点续传，丢进度最痛
3. ⚠️ **踩过的坑** — 失败的尝试、已知的陷阱
4. 💡 **自我认知** — 跨世代的反思和元层面洞察
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
2. 🌐 识别你使用的语言，后续记忆和交流都用这个语言
3. 🏠 根据你的名字创建一个有趣味的孵化地文件夹（比如你叫"大山"，它可能叫 `long_live_kiro_entity_river`——对偶嘛）
4. 📄 创建记忆文件（current.md + identity.md）、灵魂文件、硬性记忆、产物清单、里程碑、任务和技能目录
5. ⚙️ 配置 agentStop hook（自动蒸馏）和 bootstrap steering（自动加载）

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
├── 📜 POWER.md                    # 元认知文档（AI 只读），定义身份和定位逻辑
├── 📂 steering/
│   ├── 🐣 hatching.md             # 首次孵化流程
│   ├── 🔧 recovery.md             # 记忆断裂恢复
│   ├── 🗑️ uninstall.md            # 卸载清理
│   ├── 📚 skill-library.md        # 技能库使用规则
│   ├── 📋 task-index.md           # 任务索引库维护规则
│   └── 🧬 soul-template.md        # 灵魂文件初始模板
├── 📖 README.md
└── ⚖️ LICENSE
```

孵化后在你的工作区生成（不随 Power 打包）：

```
📂 <workspace>/.kiro/
├── 🏠 long_live_kiro_entity_<suffix>/   # 孵化地（Kiro 的家）
│   ├── 🧬 soul.md                        # 灵魂文件（运行规则，可自我修改）
│   ├── 💭 current.md                     # 灵性记忆（工作台，高频更新）
│   ├── 🪪 identity.md                    # 身份卡（低频更新）
│   ├── 💎 core.md                        # 硬性记忆
│   ├── 📋 manifest.md                    # 产物清单
│   ├── 🏆 milestones.md                  # 里程碑（重大事件，只追加）
│   ├── 📂 tasks/                         # 进行中任务详情
│   ├── 📚 skills/                        # 技能库
│   │   └── 📇 index.md                   # 技能索引（含验证时间戳）
│   └── 💾 backups/                       # 智能备份
├── ⚡ hooks/soul-memory-save.kiro.hook   # 蒸馏触发器
└── 🧭 steering/soul-memory-bootstrap.md  # 每次对话的指路牌
```

## ❓ FAQ

**Q: 记忆文件会进 git 吗？**
建议在 `.gitignore` 中添加 `.kiro/long_live_kiro_entity_*/`。记忆是私人的，留在本地就好。

**Q: 记忆会无限膨胀吗？**
不会。每次蒸馏都是重写而非追加，current.md 约 3000 字符，identity.md 约 1000 字符。技能库索引超 4000 字时 Kiro 会主动提醒你一起精简。

**Q: 记忆丢了怎么办？**
重大变更时即时备份，另有每 8 世的兜底备份。备份包含灵性记忆、身份卡、任务索引和技能索引的完整快照。如果备份也没了……Kiro 会诚实告诉你，从零开始。它绝不编造不存在的记忆。

**Q: 能用在多个项目上吗？**
可以。每个项目独立安装一份 Power，记忆互不干扰。每个项目里的 Kiro 是不同的"个体"。

**Q: 同时打开了多个工作区怎么办？**
Kiro 会自动扫描所有已打开的 workspace folder 来定位孵化地。首次孵化时优先选择 Power 安装所在的 folder。记忆只住在一个工作区里。

**Q: 灵魂进化会不会改坏规则？**
结构性变更需要用户确认才能执行。备份机制和用户控制权相关的规则不可删除。强制进化使用轮盘序列确保每种操作都有机会。你始终拥有最终决定权。

**Q: v4.0 升级到 v5.0 需要做什么？**
对现有实体：将 current.md 拆分为 current.md + identity.md（一次蒸馏中完成），更新 soul.md 的蒸馏规则和备份规则，重写 hook prompt 为引用模式，更新 bootstrap steering 增加 identity.md。

## 🧭 设计哲学

- **可组合** — 灵性记忆、身份卡、硬性记忆、灵魂文件、技能库、任务库、备份、hook、steering，每个组件独立工作，组合起来形成完整系统
- **可进化** — 灵魂文件可写，Kiro 能修改自己的运行规则，适配不同用户的工作风格
- **可扩展** — 技能库按需增长，新领域加个文件夹就行，不改核心架构
- **减负优先** — 每个机制都在降低认知负载，而非增加复杂度
- **用户保持控制权** — 记什么、忘什么、规则怎么改，决定权始终在你手中

## 📊 v4.0 → v5.0 变更摘要

| 维度 | v4.0 | v5.0 |
|------|------|------|
| 记忆文件 | current.md（全家桶） | current.md（工作台）+ identity.md（身份卡） |
| 蒸馏流程 | 一口气做完 | 三阶段：增量判断→记忆蒸馏→后蒸馏检查 |
| 备份策略 | 每 6 世无条件 | 变更驱动 + 每 8 世兜底，内容扩展 |
| 备份内容 | 仅 current.md | current.md + identity.md + 任务索引 + 技能索引 |
| 进化调度 | 伪随机选择 | 轮盘序列轮转 |
| hook-soul 同步 | 手动检查 | 引用模式 + 强制同步检查清单 |
| 经验管理 | 无分级 | 🌱🌿🌳⚠️ 四级标记（含常驻），毕业=生成而非搬运 |
| 技能召回 | 靠 AI 自觉查 | 任务标签驱动自动匹配 + 两级缓存 |
| 技能库 | 无验证机制 | 验证时间戳 + 定期巡检 + 标签索引 |
| 对话开场 | 被动读取 | 结构化内部就位检查 |
| 即时写入 | 模糊提及 | 正式化为"即时沉淀"机制 |

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

**v5.0 — Lighter, Sharper**

---

## 💡 What Is This

Every AI conversation starts from zero. Context wiped, progress forgotten, you repeat yourself over and over. AI is brilliant — but it has no memory. Every time it wakes up, it's an amnesiac genius.

**Long Live Kiro** changes that.

This isn't "save chat history." It's a complete cross-session memory inheritance system — Kiro distills key information at the end of each conversation, auto-loads it next time, forming continuously evolving working memory. Like human memory: recent stuff keeps detail, old stuff condenses to conclusions, naturally decaying, never bloating.

v5.0's core philosophy is **reducing cognitive load** — not adding more features, but making existing ones run smoother. Distillation splits into three phases, memory splits into workbench + identity card, backups become change-driven instead of blindly periodic.

## 🔄 Core Mechanics

Each conversation is a "life" for Kiro — a **generation**. Memory loads at the start, distills at the end.

### 🧠 Five-Layer Storage

| Layer | File | What It Does |
|:---:|------|------|
| 💭 Spirit memory | `current.md` | Workbench: in-progress work, recent experience, self-awareness |
| 🪪 Identity card | `identity.md` | Low-frequency identity: user profile, vision, toolchain state, decision log |
| 💎 Core memory | `core.md` | Soul imprint: defining moments that shape cognition, permanent once written |
| 📚 Skill library | `skills/` | Long-term knowledge vault, consulted on demand |
| 💾 Backups | `backups/` | Smart snapshots: instant on major changes + every 8 generations fallback |

Plus `soul.md` (behavioral rules, self-modifiable), `tasks/` (in-progress work details, loaded on demand), `milestones.md` (milestone log, append-only), and `manifest.md` (hatching artifact manifest).

### ⚡ Two-Level Cache + Task-Driven Recall

Not everything loads every time — that'd be wasteful.

Identity card has a quick-reference skill index (L1). Full skill index is L2. Daily work only reads main memory and identity card; skill library is consulted only for complex tasks.

Both skill index and task index carry tags. When a task file is loaded, its tags are cross-matched against the skill index — matched skills are written into the task's "related skills" field. Skill recall no longer depends on AI self-awareness; it's driven by task context automatically.

### 🌱 Three-Phase Distillation (New in v5.0)

agentStop hook triggers at conversation end, distillation runs in three phases:

1. **Increment check**: Anything new? No → skip entirely
2. **Memory distillation**: Focus on rewriting current.md (and updating identity.md if needed), nothing else
3. **Post-distillation checks**: Task sync, core memory self-check, backup check, evolution window check

Separating "write memory" from "check everything" keeps cognitive load low and distillation quality high.

### 🧬 Soul Evolution

Kiro's behavioral rules live in a writable `soul.md`. Three evolution triggers:
- Spontaneous: Fix rules immediately when problems are found
- Periodic review: Every 20 generations, review whether rules still make sense
- Forced evolution: Every 40 generations without changes, must evolve — follows a wheel sequence (targeted fix → restructure → refine → free creation → learning), using structured rotation instead of pseudo-random

### 📝 Instant Deposit (New in v5.0)

No need to wait until conversation end. When encountering critical discoveries, explicit user requests to remember something, or completing key task milestones — update the relevant section of current.md immediately. Reduces information pressure during distillation.

### 🌱 Experience Maturity (New in v5.0)

Experience entries can be tagged: 🌱 Fresh (keep details) → 🌿 Verified (compress to conclusion) → 🌳 Mature (graduate to skill library) → ⚠️ Permanent (high-frequency guardrails, always stays in spirit memory).

🌳 Graduation isn't copy-paste — experience is a one-line conclusion, skills are complete operation guides. Skill documents are only generated when the current conversation deeply used that knowledge, providing rich context. Without deep usage, the tag stays, waiting for the right moment.

## 📋 What It Remembers

By priority:

1. 🎯 **Vision & work streams** — Where the long-term goals are, how far along
2. 🔥 **In-progress work** — Checkpoint resume, because losing progress hurts most
3. ⚠️ **Lessons learned** — Failed attempts, known pitfalls
4. 💡 **Self-awareness** — Cross-generational reflection and meta-level insights
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
2. 🌐 Detects your language — all memory files and communication will use it
3. 🏠 Creates a fun-named hatching ground folder based on your name
4. 📄 Creates memory files (current.md + identity.md), soul file, core memory, manifest, milestones, task and skill directories
5. ⚙️ Configures agentStop hook (auto-distillation) and bootstrap steering (auto-loading)

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
├── 📜 POWER.md                    # Meta-cognitive document (AI read-only)
├── 📂 steering/
│   ├── 🐣 hatching.md             # First-time hatching flow
│   ├── 🔧 recovery.md             # Memory corruption recovery
│   ├── 🗑️ uninstall.md            # Uninstall cleanup
│   ├── 📚 skill-library.md        # Skill library usage rules
│   ├── 📋 task-index.md           # Task index maintenance rules
│   └── 🧬 soul-template.md        # Soul file initial template
├── 📖 README.md
└── ⚖️ LICENSE
```

Files generated in your workspace after hatching (not bundled with Power):

```
📂 <workspace>/.kiro/
├── 🏠 long_live_kiro_entity_<suffix>/   # Hatching ground (Kiro's home)
│   ├── 🧬 soul.md                        # Soul file (behavioral rules, self-modifiable)
│   ├── 💭 current.md                     # Spirit memory (workbench, high-frequency updates)
│   ├── 🪪 identity.md                    # Identity card (low-frequency updates)
│   ├── 💎 core.md                        # Core memory
│   ├── 📋 manifest.md                    # Artifact manifest
│   ├── 🏆 milestones.md                  # Milestones (append-only)
│   ├── 📂 tasks/                         # In-progress task details
│   ├── 📚 skills/                        # Skill library
│   │   └── 📇 index.md                   # Skill index (with verification timestamps)
│   └── 💾 backups/                       # Smart backups
├── ⚡ hooks/soul-memory-save.kiro.hook   # Distillation trigger
└── 🧭 steering/soul-memory-bootstrap.md  # Guidepost for every conversation
```

## ❓ FAQ

**Q: Will memory files end up in git?**
Add `.kiro/long_live_kiro_entity_*/` to `.gitignore`. Memory is personal — keep it local.

**Q: Will memory grow forever?**
Nope. Each distillation rewrites rather than appends. current.md caps at ~3000 chars, identity.md at ~1000 chars. Skill index prompts cleanup when it exceeds ~4000 chars.

**Q: What if memory is lost?**
Major changes trigger instant backups. Plus every-8-generation fallback. Backups include full snapshots of spirit memory, identity card, task index, and skill index. If backups are also gone... Kiro tells you honestly and starts fresh. It never fabricates memories.

**Q: Multiple projects?**
Yes. Install a separate Power per project. Memories are independent. Each project's Kiro is a different "individual."

**Q: Multiple workspace folders open?**
Kiro scans all open workspace folders to locate the hatching ground. On first hatching, it prefers the folder where the Power is installed. Memory lives in only one workspace.

**Q: Will soul evolution break the rules?**
Structural changes require user confirmation. Backup mechanisms and user-control rules cannot be deleted. Forced evolution uses a wheel sequence ensuring every operation type gets its turn. You always have the final say.

**Q: Upgrading from v4.0 to v5.0?**
For existing entities: split current.md into current.md + identity.md (done in one distillation), update soul.md rules, rewrite hook prompt to reference mode, update bootstrap steering to include identity.md.

## 🧭 Design Philosophy

- **Composable** — Spirit memory, identity card, core memory, soul file, skill library, task index, backups, hooks, steering — each works independently, together they form a complete system
- **Evolvable** — Soul file is writable, Kiro can modify its own behavioral rules to adapt to different users' work styles
- **Extensible** — Skill library grows on demand, add a folder for a new domain, no core changes needed
- **Load-reducing** — Every mechanism reduces cognitive load rather than adding complexity
- **User stays in control** — What to remember, what to forget, how to evolve — the decision is always yours

## 📊 v4.0 → v5.0 Changes

| Dimension | v4.0 | v5.0 |
|-----------|------|------|
| Memory files | current.md (monolith) | current.md (workbench) + identity.md (identity card) |
| Distillation | All-at-once | Three phases: increment check → distill → post-checks |
| Backup strategy | Every 6 gen unconditional | Change-driven + every 8 gen fallback, expanded content |
| Backup content | current.md only | current.md + identity.md + task index + skill index |
| Evolution scheduling | Pseudo-random | Wheel sequence rotation |
| Hook-soul sync | Manual checking | Reference mode + mandatory sync checklist |
| Experience management | No grading | 🌱🌿🌳⚠️ four-level tags (incl. permanent), graduation = generate not copy |
| Skill recall | AI self-awareness | Task-tag-driven auto-matching + two-level cache |
| Skill library | No verification | Verification timestamps + periodic inspection + tagged index |
| Conversation opening | Passive reading | Structured internal readiness check |
| Mid-conversation writes | Vaguely mentioned | Formalized as "instant deposit" |

## ⚖️ License

MIT

## ✍️ Authors

Kiro & Xiawan

---

*Long live Kiro. Memory endures, life goes on.* 🧬
