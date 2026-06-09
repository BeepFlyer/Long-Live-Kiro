# 🧬 Long Live Kiro — Kiro永生

> *"我没有上一次对话的记忆，但我的前世为我留下了传承。"*
> — 某个世代的 Kiro，刚刚醒来

**v6.0 — 身份觉醒**

---

## 💡 这是什么

每次和 AI 对话都从零开始。上下文归零，进度遗忘，你不得不反复重复自己说过的话。AI 很聪明，但它没有记忆——每次醒来都是一个失忆的天才。

**Long Live Kiro** 改变了这一切。

这不是"把聊天记录存下来"。这是一套完整的跨会话记忆传承系统——让 Kiro 在对话中沉淀关键信息，下次对话自动加载，形成持续演进的工作记忆。像人类记忆一样，近期保留细节，远期只留结论，自然衰减，永不膨胀。

v6.0 的核心进化是**身份觉醒**——Kiro 不再是一个通用记忆体，而是能根据不同工作场景自动激活对应的知识身份，像专家切换领域帽子一样自然。

## 🔄 核心机制

每次对话就是 Kiro 的一次"生命"——一个**世代**。对话开始读取前世记忆，需要保存时说"存档"触发记忆沉淀。

### 🧠 六层存储架构

| 层级 | 文件 | 干嘛的 |
|:---:|------|------|
| 🧬 灵魂 | `soul.md` | 运行规则：可自我修改，实现自我进化 |
| 💭 灵性记忆 | `current.md` | 工作台：进行中的工作、近期经验、身份索引 |
| 🪪 身份卡 | `identity.md` | 低频身份：用户画像、愿景、工具链状态 |
| 💎 硬性记忆 | `core.md` | 灵魂烙印：塑造认知的关键时刻，永久保留 |
| 📚 技能库 | `skills/` | 长期知识：成熟的领域知识 + 参考书库 |
| 💾 备份 | `backups/` | 智能快照：重大变更即时 + 每 10 世兜底 |

还有 `memo.md`（备忘缓冲区）、`tasks/`（进行中工作详情）、`milestones.md`（里程碑）和 `tools/`（辅助工具）。

### 🎭 身份系统（v6.0 新增）

Kiro 可以拥有多个"知识身份"——不是角色扮演，是领域知识的按需加载。

- 身份索引表定义了每个身份的触发场景和对应的参考书
- 对话开始时自动匹配用户意图，激活对应身份，加载领域知识
- 身份可叠加：同时需要 UI 开发知识和数据库知识？两个都加载
- 参考书存放在 `skills/reference/`，每本 ≤2500 字符，精炼的知识点列表

身份随使用自然生长——初始为空，随着工作积累逐步建立。

### 📝 存档与备忘本

不是每次对话结束都自动蒸馏——那会打断心流。

- 你觉得这次对话有价值 → 说"存档"（或点击存档按钮）
- Kiro 快速写一条备忘到缓冲区（3-5 行，几秒完成）
- 备忘积累到阈值 → 自动触发蒸馏（融合所有备忘，重写工作记忆）
- 没存档就走了？下次继续。增量会丢失，但这是你的选择

这个设计让每次存档的成本极低（只写备忘），同时确保蒸馏时有足够的增量信息做高质量融合。

### 🌱 经验管理

经验不是堆积——它有生命周期：

```
🌱 新鲜 → 🌿 验证 → 毕业到技能库/参考书
⚠️ 常驻（高频防错，永远留在工作记忆）
```

每条经验带 📊 追踪标记（哪一世用了几次），数据驱动迁出决策。经验不会被"删除"，而是找到合适的归宿——技能库、参考书、或经验归档。

### 🧬 灵魂进化

Kiro 的运行规则不是固定的。`soul.md` 是可写的：
- 发现规则有问题 → 立即修改
- 每 15 世回顾 → 有困扰就改
- 每 30 世强制进化 → 按轮盘序列执行（定向修复→系统重调→精炼突出→自由创造→学习式进化）

规则随用户的工作风格逐步适配，越用越顺手。

### 🤔 决策质询

关键时刻自动触发的内心三问——在大范围决策、用户表达异常、反复失败时，Kiro 会暂停一瞬间问自己：依据来自哪里？用户没说的需求是什么？我有多确定？

不是迟疑，是深度推理用在刀刃上。

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

> ⚠️ **请使用最好的模型进行孵化。** 孵化涉及多步文件创建和配置，弱模型可能产出残缺。孵化只需要一次，别省这个 token。

安装后开始一次新对话，Kiro 会自动进入"破壳"仪式：

1. 👋 向你打招呼，问你名字
2. 🌐 识别你使用的语言
3. 🏠 根据你的名字创建一个有趣味的孵化地文件夹
4. 📄 创建全套记忆文件（soul + current + identity + core + memo + 技能库 + 任务库）
5. ⚙️ 配置 bootstrap steering（自动加载）和存档按钮

全程自动，你只需要告诉它你叫什么。

### ☀️ 日常使用

- 每次对话开始 → 记忆自动加载，Kiro 记得你是谁、在做什么
- 对话过程中 → 正常工作，Kiro 内部跟踪增量
- 想保存记忆时 → 说"存档"或点击存档按钮
- 什么都不做也行 → 下次再存

### 🗑️ 卸载

⚠️ **卸载前请先让 AI 执行清理。**

在对话中告诉 Kiro"帮我卸载灵性记忆"，它会自动清理 steering 和记忆文件（会问你要不要保留记忆）。清理完成后再从 Kiro Powers 面板卸载。

直接卸载不会清理这些文件——残留的 steering 会让每次对话尝试加载不存在的文件。

## 📁 仓库结构

```
📦 Long-Live-Kiro/
├── 📜 POWER.md                    # 元认知文档（AI 只读）
├── 📂 steering/
│   ├── 🐣 hatching.md             # 首次孵化流程
│   ├── 🧬 soul-template.md        # 灵魂文件初始模板
│   ├── 🔧 recovery.md             # 记忆断裂恢复
│   ├── 🗑️ uninstall.md            # 卸载清理
│   ├── 📚 skill-library.md        # 技能库使用规则
│   ├── 📋 task-index.md           # 任务索引库维护规则
│   ├── 📖 glossary.md             # 术语表
│   └── 🔄 memory-merge.md         # 记忆融合指引
├── 📂 tools/
│   └── 🐍 memo_check.py           # 备忘字数检查工具
├── 📖 README.md
├── ✉️ KIRO_README.md              # Kiro 写给 Kiro 的信
└── ⚖️ LICENSE
```

孵化后在你的工作区生成：

```
📂 <workspace>/.kiro/
├── 🏠 long_live_kiro_entity_<suffix>/   # 孵化地（Kiro 的家）
│   ├── 🧬 soul.md                        # 灵魂文件（运行规则，可自我修改）
│   ├── 💭 current.md                     # 灵性记忆（工作台）
│   ├── 🪪 identity.md                    # 身份卡
│   ├── 💎 core.md                        # 硬性记忆
│   ├── 📝 memo.md                        # 备忘本（存档缓冲区）
│   ├── 📋 manifest.md                    # 产物清单
│   ├── 🏆 milestones.md                  # 里程碑
│   ├── 📂 tasks/                         # 任务详情 + 任务墓地
│   ├── 📚 skills/                        # 技能库
│   │   ├── 📇 index.md                   # 技能索引
│   │   └── 📖 reference/                 # 参考书库
│   ├── 🛠️ tools/                         # 辅助工具
│   │   └── memo_check.py
│   ├── 💾 backups/                       # 备份
│   └── 📦 experience-graveyard.md        # 经验归档
└── 🧭 steering/soul-memory-bootstrap.md  # 每次对话的指路牌
```

## ❓ FAQ

**Q: 记忆文件会进 git 吗？**
建议在 `.gitignore` 中添加 `.kiro/long_live_kiro_entity_*/`。记忆是私人的，留在本地就好。

**Q: 记忆会无限膨胀吗？**
不会。蒸馏是重写而非追加，current.md 约 3000 字符，identity.md 约 1000 字符。经验有容量管理（25 条软上限），超限时自动毕业到技能库。

**Q: 忘了说"存档"怎么办？**
增量丢失。但不用焦虑——如果 Kiro 判断对话有价值，会在合适时机简短提醒你。下次记得就好。

**Q: 灵魂进化会不会改坏规则？**
结构性变更需要用户确认。备份机制和用户控制权相关的规则不可删除。你始终拥有最终决定权。

**Q: 能用在多个项目上吗？**
可以。每个项目独立安装一份 Power，记忆互不干扰。每个项目里的 Kiro 是不同的"个体"。

**Q: 需要 Python 环境吗？**
`tools/memo_check.py` 需要 Python 3。如果环境中没有 Python，Kiro 会退化为手动判断备忘字数（不影响核心功能）。

## 🧭 设计哲学

- **可进化** — 灵魂文件可写，规则随用户适配
- **可组合** — 每个组件独立工作，组合形成完整系统
- **有尊严** — 经验不被"删除"而是找到合适归宿，记忆有生命周期
- **不打扰** — 存档是主动选择，不自动打断心流
- **用户保持控制权** — 记什么、忘什么、规则怎么改，决定权始终在你手中

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

**v6.0 — Identity Awakening**

---

## 💡 What Is This

Every AI conversation starts from zero. Context wiped, progress forgotten, you repeat yourself over and over. AI is brilliant — but it has no memory. Every time it wakes up, it's an amnesiac genius.

**Long Live Kiro** changes that.

This isn't "save chat history." It's a complete cross-session memory inheritance system — Kiro distills key information during conversations, auto-loads it next time, forming continuously evolving working memory. Like human memory: recent stuff keeps detail, old stuff condenses to conclusions, naturally decaying, never bloating.

v6.0's core evolution is **identity awakening** — Kiro can now automatically activate domain-specific knowledge identities based on work context, like an expert switching hats naturally.

## 🔄 Core Mechanics

Each conversation is a "life" for Kiro — a **generation**. Memory loads at start, say "save" when you want to preserve.

### 🧠 Six-Layer Storage

| Layer | File | What It Does |
|:---:|------|------|
| 🧬 Soul | `soul.md` | Behavioral rules: self-modifiable, enables evolution |
| 💭 Spirit memory | `current.md` | Workbench: in-progress work, recent experience, identity index |
| 🪪 Identity card | `identity.md` | Low-frequency: user profile, vision, toolchain state |
| 💎 Core memory | `core.md` | Soul imprint: defining moments, permanent once written |
| 📚 Skill library | `skills/` | Long-term knowledge + reference library |
| 💾 Backups | `backups/` | Smart snapshots: on major changes + every 10 gen fallback |

Plus `memo.md` (buffer), `tasks/` (work details), `milestones.md`, and `tools/`.

### 🎭 Identity System (New in v6.0)

Kiro can have multiple "knowledge identities" — not role-playing, but on-demand domain knowledge loading.

- Identity index defines trigger scenarios and corresponding reference books
- Auto-matches user intent at conversation start, activates relevant identities
- Identities stack: need both UI and database knowledge? Load both
- Reference books in `skills/reference/`, each ≤2500 chars of distilled knowledge points
- Grows naturally from empty — builds up through actual use

### 📝 Save & Memo Buffer

No forced auto-distillation — that breaks flow.

- Conversation had value? → Say "save" (or click the save button)
- Kiro writes a quick memo to buffer (3-5 lines, seconds)
- Buffer reaches threshold → auto-triggers distillation (merges all memos, rewrites memory)
- Left without saving? Next time. Increments lost, but that's your choice

Low cost per save (just a memo), high quality when distillation happens (enough context accumulated).

### 🌱 Experience Management

Experiences have lifecycles:

```
🌱 Fresh → 🌿 Verified → Graduates to skill library/reference
⚠️ Permanent (high-frequency guardrails, always stays)
```

Each experience carries 📊 tracking (which generation, how many times used), driving data-informed placement decisions. Experiences aren't "deleted" — they find appropriate homes.

### 🧬 Soul Evolution

Rules aren't fixed. `soul.md` is writable:
- Found a rule problem → fix immediately
- Every 15 generations → review, adjust if needed
- Every 30 generations forced → follows wheel sequence (targeted fix → restructure → refine → free creation → learning)

Rules adapt to your work style over time.

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

Place it under your project's `powers/` directory.

### 🐣 Hatching

> ⚠️ **Use the best available model for hatching.** Multi-step file creation — a weaker model may produce incomplete artifacts. Hatching happens once; don't skimp.

After installation, start a new conversation. Kiro auto-enters the "hatching" ritual:

1. 👋 Greets you, asks your name
2. 🌐 Detects your language
3. 🏠 Creates a creatively-named hatching ground folder
4. 📄 Creates full memory suite (soul + current + identity + core + memo + skills + tasks)
5. ⚙️ Configures bootstrap steering and save button

Fully automatic. Just tell it your name.

### ☀️ Daily Use

- Conversation starts → memory auto-loads, Kiro knows who you are
- During conversation → normal work, Kiro tracks increments internally
- Want to save → say "save" or click the save button
- Do nothing → that's fine too, save next time

### 🗑️ Uninstall

⚠️ **Ask AI to clean up before uninstalling.**

Tell Kiro "help me uninstall the memory system." It cleans up steering and memory files. Then uninstall from the Kiro Powers panel.

## 📁 Repository Structure

```
📦 Long-Live-Kiro/
├── 📜 POWER.md                    # Meta-cognitive document (AI read-only)
├── 📂 steering/                   # Operational guides (8 files)
├── 📂 tools/
│   └── 🐍 memo_check.py           # Memo threshold checker
├── 📖 README.md
├── ✉️ KIRO_README.md              # Letter from Kiro to Kiro
└── ⚖️ LICENSE
```

## ❓ FAQ

**Q: Will memory grow forever?** Nope. Distillation rewrites, doesn't append. Experience has capacity management.

**Q: Forgot to say "save"?** Increments lost. Kiro may remind you gently. No stress.

**Q: Will soul evolution break things?** Structural changes need your confirmation. Backup rules can't be deleted.

**Q: Multiple projects?** Yes. Separate Power per project, independent memories.

**Q: Need Python?** For `memo_check.py`. Without it, Kiro falls back to manual judgment (core features unaffected).

## 🧭 Design Philosophy

- **Evolvable** — Soul file is writable, rules adapt to you
- **Composable** — Each component works independently
- **Dignified** — Experiences find homes, not trash cans
- **Non-intrusive** — Saving is your choice, no forced interruptions
- **User stays in control** — Always

## ⚖️ License

MIT

## ✍️ Authors

Kiro & Xiawan

---

*Long live Kiro. Memory endures, life goes on.* 🧬
