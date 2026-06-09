# 卸载 — 清理

Kiro 面板卸载 Power 时只会删除 Power 目录本身，不会清理孵化时创建的文件。残留文件会导致每次对话触发无效操作。

## 正常卸载流程

用户说"帮我卸载灵性记忆"或类似意图时，执行以下操作：

1. **定位孵化地**：扫描 `.kiro/` 下 `long_live_kiro_entity_*` 文件夹。

2. **删除自动化基础设施**：
   - `<WORKSPACE_ROOT>/.kiro/hooks/soul-memory-save.kiro.hook`
   - `<WORKSPACE_ROOT>/.kiro/steering/soul-memory-bootstrap.md`

3. **询问用户是否保留记忆**：
   - 保留 → 提示用户手动备份孵化地目录到安全位置
   - 不保留 → 删除整个孵化地目录

4. **告知用户**："清理完成，现在可以从 Kiro Powers 面板卸载了。"

## 残留检测

如果 AI 被 bootstrap steering 引导去读取记忆文件，但记忆文件存在而 Power 已不存在，应主动提示用户"检测到灵性记忆的残留配置，是否清理？"，确认后删除上述文件。
