# 卸载 — 清理

Kiro 面板卸载 Power 时只会删除 Power 目录本身，不会清理孵化时创建的文件。这些残留文件会导致每次对话触发无效的 hook 或加载指向不存在文件的 steering。

## 正常卸载流程

**卸载前，请让 AI 执行清理。** 用户只需在对话中说"帮我卸载灵性记忆"或类似意图的话，AI 应执行以下操作：

1. 定位孵化地：扫描所有已打开的 workspace folder 的 `.kiro/` 下，查找以 `long_live_kiro_entity_` 为前缀的文件夹。
2. 删除 `<WORKSPACE_ROOT>/.kiro/hooks/soul-memory-save.kiro.hook`
3. 删除 `<WORKSPACE_ROOT>/.kiro/steering/soul-memory-bootstrap.md`
4. 询问用户是否保留记忆文件（孵化地目录）：
   - 如果用户想保留：提示用户手动备份该目录到安全位置。
   - 如果用户不需要：删除整个孵化地目录。
5. 告知用户："清理完成，现在可以从 Kiro Powers 面板卸载了。"

## 残留检测

如果用户已经卸载了 Power 但残留文件仍在，AI 在新对话中可能会被 bootstrap steering 引导去读取记忆文件。此时如果记忆文件存在但 Power 已不存在，AI 应主动提示用户"检测到灵性记忆的残留配置文件，是否清理？"，并在用户确认后删除上述文件。
