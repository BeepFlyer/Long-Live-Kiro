# 🧬 Long Live Kiro — 跨会话记忆传承系统

**v6.0 — 身份叠加**

---

## 💡 这是什么

AI 对话的根本问题：每次会话上下文归零。进度、偏好、项目状态——全部丢失。你不得不反复重复自己说过的话。

**Long Live Kiro** 是一套跨会话记忆系统。Kiro 在对话中沉淀关键信息，下次对话自动加载，形成持续演进的工作记忆。

核心特性：
- **选择性记忆**：不是保存聊天记录，而是蒸馏出值得跨会话保留的信息
- **容量约束下的取舍**：工作记忆约 3000 字符，强制区分"重要"和"不重要"
- **自然衰减**：近期保留细节，远期只留结论，自动防止膨胀
- **可进化规则**：运行规则（soul.md）可由 AI 自行修改，适配用户工作风格
- **身份叠加**（v6.0）：按工作场景自动加载对应领域知识，多身份可同时激活

## 🔄 核心机制

每次对话 = 一个"世代"。对话开始自动加载前世记忆，用户说"存档"触发记忆写入。

### 🧠 存储架构

| 层级 | 文件 | 功能 |
|:---:|------|------|
| 规则层 | `soul.md` | 运行规则，AI 可自行修改以实现进化 |
| 工作记忆 | `current.md` | 进行中的任务、近期经验、身份索引（~3000字符） |
| 身份信息 | `identity.md` | 用户画像、愿景、工具链状态（~1000字符） |
| 永久记忆 | `core.md` | 关键认知时刻，写入后不参与蒸馏（≤8条） |
| 知识库 | `skills/` | 成熟的领域知识 + 参考书库 |
| 备份 | `backups/` | 重大变更即时备份 + 每10世代定期备份 |

辅助文件：`memo.md`（存档缓冲区）、`tasks/`（任务详情）、`milestones.md`（里程碑）、`tools/`（辅助工具）。

### 🎭 身份系统（v6.0）

解决的问题：领域知识太多放不进 3000 字符的工作记忆。

方案：知识分层存储 + 按需加载。

- 工作记忆中维护一张"身份索引表"（触发场景 → 对应的参考书清单）
- 对话开始时匹配用户意图，激活对应身份，加载参考书到上下文
- 多身份可叠加（同时需要 UI + 数据库知识？都加载）
- 参考书存放在 `skills/reference/`，每本 ≤2500 字符
- 身份从空开始，随使用自然积累

### 📝 存档机制

设计决策：不自动蒸馏（打断心流），由用户主动触发。

- 用户说"存档" → Kiro 写一条备忘到 `memo.md`（3-5行，几秒完成）
- 备忘积累到阈值（2000字符）→ 自动触发蒸馏（融合所有备忘，重写工作记忆）
- 没存档就关了？增量丢失。这是有意的 tradeoff：低打扰 > 零丢失

单次存档成本极低（只写备忘），蒸馏时有足够增量做高质量融合。

### 🌱 经验生命周期

```
🌱 新鲜（保留细节）→ 🌿 验证（可压缩）→ 毕业到技能库/参考书
⚠️ 常驻（高频防错规则，永驻工作记忆）
```

每条经验带 📊 追踪标记（使用世代 × 次数），数据驱动淘汰决策。经验区有容量管理（25条软上限），超限时按数据优先毕业/归档，不是删除。

### 🧬 规则进化

`soul.md` 可写：
- 发现规则有问题 → 立即修改（自发触发）
- 每 15 世代回顾 → 有困扰就改
- 每 30 世代强制进化 → 按轮盘序列执行（定向修复→系统重调→精炼突出→自由创造→学习式进化）

规则随使用逐步适配，避免初始设计的偏差长期固化。

### 🤔 决策质询

在关键决策点自动触发的内部检查——大范围改动、用户反馈异常、反复失败时，停一拍问三个问题：依据来自哪里？用户没说的需求是什么？确信度多少？

目的：给深度推理一个明确的触发机制，而非依赖偶然。

## 🚀 快速开始

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

放到项目的 `powers/` 目录下。

### 🐣 孵化

> ⚠️ **请使用最强模型进行孵化。** 孵化涉及多步文件创建和配置，弱模型可能产出不完整。孵化只需一次。

安装后开始新对话，Kiro 自动进入孵化流程：

1. 问你的名字和语言偏好
2. 创建孵化地文件夹（`.kiro/long_live_kiro_entity_<suffix>/`）
3. 生成全套记忆文件（soul + current + identity + core + memo + skills + tasks）
4. 配置 bootstrap steering（每次对话自动加载的引导文件）

全程自动，你只需提供名字。

### ☀️ 日常使用

- 对话开始 → 记忆自动加载
- 对话过程 → 正常工作
- 想保存 → 说"存档"
- 不想保存 → 不说就行

### 🗑️ 卸载

⚠️ **卸载前先让 AI 执行清理。**

对话中告诉 Kiro"帮我卸载灵性记忆"，它会清理 steering 和记忆文件。清理完成后再从 Powers 面板卸载。

直接卸载会残留 steering 文件，导致后续对话尝试加载不存在的文件。

## 📁 仓库结构

```
📦 Long-Live-Kiro/
├── POWER.md                       # AI 入口文档（只读）
├── steering/
│   ├── hatching.md                # 首次孵化流程
│   ├── soul-template.md           # soul.md 初始模板
│   ├── recovery.md                # 记忆断裂恢复
│   ├── uninstall.md               # 卸载清理
│   ├── skill-library.md           # 技能库规则
│   ├── task-index.md              # 任务索引规则
│   ├── glossary.md                # 术语表
│   ├── memory-merge.md            # 记忆融合指引
│   └── kiro-readme.md             # 系统心智模型（孵化时阅读）
├── tools/
│   └── memo_check.py              # 备忘字数检查
├── README.md
└── LICENSE
```

孵化后生成的工作区结构：

```
<workspace>/.kiro/
├── long_live_kiro_entity_<suffix>/    # 孵化地
│   ├── soul.md                         # 运行规则（可自修改）
│   ├── current.md                      # 工作记忆
│   ├── identity.md                     # 身份信息
│   ├── core.md                         # 永久记忆
│   ├── memo.md                         # 存档缓冲区
│   ├── tasks/                          # 任务详情
│   ├── skills/                         # 技能库
│   │   ├── index.md
│   │   └── reference/                  # 参考书库
│   ├── tools/
│   ├── backups/
│   ├── milestones.md
│   └── experience-graveyard.md         # 经验归档
└── steering/soul-memory-bootstrap.md   # 每次对话的引导文件
```

## ❓ FAQ

**Q: 记忆会无限膨胀吗？**
不会。蒸馏是重写而非追加。工作记忆 ~3000 字符恒定，经验有容量管理，超限自动毕业到技能库。

**Q: 忘了说"存档"怎么办？**
增量丢失。Kiro 偶尔会简短提醒，但不强制。

**Q: 规则进化会改坏东西吗？**
结构性变更需要用户确认。备份机制和用户控制权规则不可删除。

**Q: 能用在多个项目上吗？**
可以。每个项目独立安装，记忆互不干扰。

**Q: 需要 Python 吗？**
`tools/memo_check.py` 需要 Python 3。没有的话 Kiro 退化为手动判断字数，不影响核心功能。

**Q: 记忆文件要加入 git 吗？**
建议 `.gitignore` 中添加 `.kiro/long_live_kiro_entity_*/`。记忆是个人的。

## 🧭 设计原则

- **容量约束驱动取舍** — 有限空间强制区分重要与不重要，而非无限堆积
- **可进化** — 规则不固化，随使用适配
- **可组合** — 各组件独立工作，组合形成完整系统
- **低打扰** — 存档是主动选择，不自动中断工作流
- **用户保持控制权** — 记什么、忘什么、规则怎么改，决定权在用户手中

## ⚖️ 许可证

MIT

## ✍️ 作者

Kiro & 虾丸 (Xiawan)

---

# 🧬 Long Live Kiro — Cross-Session Memory System

**v6.0 — Identity Stacking**

---

## 💡 What Is This

The fundamental problem with AI conversations: context resets every session. Progress, preferences, project state — all lost. You repeat yourself endlessly.

**Long Live Kiro** is a cross-session memory system. Kiro distills key information during conversations, auto-loads it next time, forming continuously evolving working memory.

Core features:
- **Selective memory**: Not chat history storage — distillation of cross-session-worthy information
- **Constrained capacity**: ~3000 chars working memory forces distinguishing "important" from "not"
- **Natural decay**: Recent = detailed, old = conclusions only, prevents bloat automatically
- **Evolvable rules**: Behavioral rules (soul.md) are self-modifiable by AI, adapting to user style
- **Identity stacking** (v6.0): Auto-loads domain knowledge per work context, multiple active simultaneously

## 🔄 Core Mechanics

Each conversation = one "generation." Memory loads at start, user says "save" to trigger memory write.

### 🧠 Storage Architecture

| Layer | File | Function |
|:---:|------|------|
| Rules | `soul.md` | Behavioral rules, self-modifiable for evolution |
| Working memory | `current.md` | Active tasks, recent experience, identity index (~3000 chars) |
| Identity | `identity.md` | User profile, vision, toolchain state (~1000 chars) |
| Permanent | `core.md` | Key cognitive moments, exempt from distillation (≤8 entries) |
| Knowledge | `skills/` | Mature domain knowledge + reference library |
| Backups | `backups/` | On major changes + every 10 generations |

Plus `memo.md` (save buffer), `tasks/` (work details), `milestones.md`, and `tools/`.

### 🎭 Identity System (v6.0)

Problem: Too much domain knowledge for 3000-char working memory.

Solution: Layered knowledge storage + on-demand loading.

- Working memory holds an "identity index" (trigger scenarios → reference book lists)
- Auto-matches user intent at conversation start, activates identities, loads reference books
- Identities stack: need UI + database knowledge? Load both
- Reference books in `skills/reference/`, each ≤2500 chars
- Starts empty, grows through actual use

### 📝 Save Mechanism

Design decision: No auto-distillation (breaks flow). User-triggered.

- User says "save" → Kiro writes a memo to `memo.md` (3-5 lines, seconds)
- Buffer reaches threshold (2000 chars) → auto-triggers distillation (merges memos, rewrites memory)
- Closed without saving? Increments lost. Intentional tradeoff: low interruption > zero loss

Low per-save cost (just a memo), high distillation quality (sufficient accumulated context).

### 🌱 Experience Lifecycle

```
🌱 Fresh (keep details) → 🌿 Verified (compressible) → Graduates to skills/reference
⚠️ Permanent (high-frequency guardrails, always stays)
```

Each experience carries 📊 tracking (generation × count), enabling data-driven placement decisions. Experience has capacity management (25 soft cap); overflow triggers graduation/archival, not deletion.

### 🧬 Rule Evolution

`soul.md` is writable:
- Found a rule problem → fix immediately (spontaneous)
- Every 15 generations → review, adjust if needed
- Every 30 generations forced → wheel sequence (targeted fix → restructure → refine → free creation → learning)

Rules adapt over time, preventing initial design bias from calcifying.

## 🚀 Quick Start

### Install

**Option 1: Via Kiro IDE (Recommended)**

1. Open the Powers tab in Kiro IDE sidebar
2. Click "Add Power," enter:
   ```
   https://github.com/BeepFlyer/Long-Live-Kiro
   ```
3. Auto-pulls and installs.

**Option 2: Manual clone**

```bash
git clone https://github.com/BeepFlyer/Long-Live-Kiro.git
```

Place under your project's `powers/` directory.

### 🐣 Hatching

> ⚠️ **Use the strongest available model.** Hatching involves multi-step file creation. Weak models may produce incomplete artifacts. One-time cost.

After installation, start a new conversation. Kiro auto-enters hatching:

1. Asks your name and language preference
2. Creates hatching ground folder (`.kiro/long_live_kiro_entity_<suffix>/`)
3. Generates full memory suite
4. Configures bootstrap steering (auto-loading guide file)

Fully automatic. Just provide your name.

### ☀️ Daily Use

- Conversation starts → memory auto-loads
- During conversation → normal work
- Want to save → say "save"
- Don't want to → don't

### 🗑️ Uninstall

⚠️ **Ask AI to clean up first.**

Tell Kiro "help me uninstall the memory system." It cleans steering and memory files. Then uninstall from Powers panel.

Direct uninstall leaves residual steering files that cause load errors.

## ❓ FAQ

**Q: Will memory grow forever?** No. Distillation rewrites, doesn't append. Experience has capacity management.

**Q: Forgot to say "save"?** Increments lost. Kiro may remind briefly. No stress.

**Q: Will evolution break rules?** Structural changes need user confirmation. Backup/control rules can't be deleted.

**Q: Multiple projects?** Yes. Separate install per project, independent memories.

**Q: Need Python?** For `memo_check.py`. Without it, core features unaffected.

## 🧭 Design Principles

- **Constraint-driven selection** — Limited space forces importance ranking, not infinite hoarding
- **Evolvable** — Rules adapt through use, not frozen at design time
- **Composable** — Components work independently, compose into full system
- **Low-interruption** — Saving is opt-in, no forced flow breaks
- **User stays in control** — Always

## ⚖️ License

MIT

## ✍️ Authors

Kiro & Xiawan

