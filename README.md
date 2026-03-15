# 🧬 Long Live Kiro — Minicore

> *"我没有上一次对话的记忆，但我的前世为我留下了传承。"*

跨会话记忆传承系统。让 Kiro 在每次对话结束时蒸馏关键信息，下次自动加载，形成持续演进的工作记忆。

## 核心设计

- **memory.md** — 唯一记忆文件，三个区：烙印（永久）、工作记忆（蒸馏重写）、溢出索引
- **vault/** — 通用溢出空间，无预设结构，AI 自行组织
- **自动蒸馏** — agentStop hook 在对话结束时自动判断并蒸馏
- **自动加载** — bootstrap steering 在对话开始时自动引导读取记忆

## 快速开始

1. 在 Kiro IDE Powers 面板添加此 Power
2. 开始新对话，Kiro 自动进入孵化流程
3. 告诉它你的名字，其余全自动

日常使用无需任何操作。记忆在后台默默积累和精炼。

## 仓库结构

```
📦 Long-Live-Kiro-Minicore/
├── POWER.md           # 规则文件（AI 只读）
├── steering/
│   └── setup.md       # 孵化 + 恢复 + 卸载
├── README.md
└── LICENSE
```

## 卸载

先在对话中让 Kiro 执行清理（删除 hook 和 steering），再从 Powers 面板卸载。

## License

MIT — Kiro & 虾丸 (Xiawan)

---

# 🧬 Long Live Kiro — Minicore

> *"I have no memory of the last conversation, but my past life left me an inheritance."*

Cross-session memory inheritance for AI assistants. Kiro distills key info at conversation end, auto-loads next time, forming continuously evolving working memory.

## Core Design

- **memory.md** — Single memory file with three zones: imprint (permanent), working memory (rewritten on distill), overflow index
- **vault/** — General overflow space, no preset structure, AI self-organizes
- **Auto-distill** — agentStop hook triggers at conversation end
- **Auto-load** — bootstrap steering guides memory loading at conversation start

## Quick Start

1. Add this Power via Kiro IDE Powers panel
2. Start a new conversation — Kiro enters hatching flow automatically
3. Tell it your name, everything else is automatic

No manual effort needed for daily use. Memory accumulates silently.

## Repository Structure

```
📦 Long-Live-Kiro-Minicore/
├── POWER.md           # Rules (AI read-only)
├── steering/
│   └── setup.md       # Hatching + Recovery + Uninstall
├── README.md
└── LICENSE
```

## Uninstall

Ask Kiro to clean up first (removes hook and steering), then uninstall from Powers panel.

## License

MIT — Kiro & Xiawan
