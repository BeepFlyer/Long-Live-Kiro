# 🧬 Kiro永生 — AI 助手的跨会话记忆

> 每次和 AI 助手对话都是一次全新开始——上下文丢失，进度遗忘，你不得不重复自己说过的话。
> Kiro永生改变了这一切。

## 这是什么？

一个 [Kiro Power](https://kiro.dev)，让你的 AI 助手拥有**跨会话的持久记忆**。

每次对话结束时，助手会将关键信息——你的目标、进行中的工作、踩过的坑、偏好习惯、决策记录——蒸馏成一份紧凑的记忆文件。下次对话开始时，从上次断点无缝续传。

## ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🥚 首次孵化 | 首次激活时执行"破壳"仪式：打招呼、询问名字、自动搭建所有基础设施 |
| 💾 自动存档 | 每次会话结束时通过 `agentStop` hook 自动蒸馏记忆 |
| 📖 自动加载 | 每次会话开始时通过 steering 文件自动加载前世记忆 |
| 🔢 世代追踪 | 每次会话 = 一次"生命"，用世代计数器追踪 |
| 🧠 智能压缩 | 近期保留细节，远期只留结论（遗忘曲线） |
| 🔄 诚实恢复 | 记忆丢失时绝不捏造上下文，从环境重建 |

## 📦 安装

1. 将 `long-live-kiro` 文件夹复制到项目的 `powers/` 目录下
2. 在 Kiro 中激活此 Power
3. "孵化"流程会引导你完成剩余配置——无需手动操作

## 🏗️ 工作原理

### 系统组件

| 组件 | 位置 | 随 Power 打包 | 作用 |
|------|------|:---:|------|
| `POWER.md` | Power 目录 | ✅ | 核心规则与元认知文档 |
| `soul_memory_of_long_live_Kiro.md` | Power/steering/ | ❌ | 动态记忆文件（孵化时创建） |
| `soul-memory-save` hook | .kiro/hooks/ | ❌ | 会话结束自动触发记忆蒸馏 |
| `soul-memory-bootstrap.md` | .kiro/steering/ | ❌ | 会话开始自动引导读取记忆 |

只有 `POWER.md` 随 Power 分发，其余组件在首次"孵化"时自动创建。

### 记忆结构

记忆文件按五个优先级层次组织：

1. **愿景与主线** — 长期目标和工作主线（抽象上升式蒸馏，不淘汰只精炼）
2. **进行中** — 当前任务状态和断点信息
3. **经验** — 踩过的坑、有效的方案
4. **用户画像** — 沟通风格、隐性偏好
5. **决策日志** — 最近的关键决策及理由（保留 3-5 条）

### 蒸馏规则

- 每次更新**重写**整个文件，不是追加
- 近期信息保留细节，远期只留结论
- 总量控制在 2000-3000 中文字符以内
- 世代计数器每次会话 +1

## 📄 许可证

MIT

## 👥 作者

Kiro & Xiawan

---

# 🧬 Long Live Kiro — Cross-Session Memory for AI Assistants

> Every conversation with an AI assistant is a fresh start — context is lost, progress is forgotten, and you repeat yourself.
> Long Live Kiro changes that.

## What is this?

A [Kiro Power](https://kiro.dev) that gives your AI assistant **persistent memory across sessions**.

At the end of each conversation, the assistant distills key information — your goals, work-in-progress, lessons learned, preferences, and decisions — into a compact memory file. When the next conversation begins, it picks up right where you left off.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🥚 First-run hatching | On first activation, runs a "hatching" ritual: greets you, asks your name, sets up everything automatically |
| 💾 Auto-save | Automatically distills memory at the end of each session via `agentStop` hook |
| 📖 Auto-load | Automatically loads previous memory at the start of each session via steering file |
| 🔢 Generation tracking | Each session = one "life", tracked with a generation counter |
| 🧠 Smart compression | Recent details preserved, older info condensed to conclusions (forgetting curve) |
| 🔄 Honest recovery | When memory is lost, never fabricates context — rebuilds from environment |

## 📦 Installation

1. Copy the `long-live-kiro` folder into your project's `powers/` directory
2. Activate the Power in Kiro
3. The "hatching" flow will guide you through the rest — no manual configuration needed

## 📄 License

MIT

## 👥 Authors

Kiro & Xiawan