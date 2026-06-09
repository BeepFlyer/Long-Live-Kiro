# 记忆恢复 — 断裂修复

如果孵化地存在但记忆文件被意外删除或损坏，这不是首次安装，而是记忆断裂。

## 恢复步骤

1. **定位孵化地**：扫描所有已打开的 workspace folder 的 `.kiro/` 下，查找以 `long_live_kiro_entity_` 为前缀的文件夹。

2. **检查备份**：查看 `backups/` 下是否有备份文件（`backup_N.md`），找到最新的一份。

3. **有备份时**：
   - 备份中包含灵性记忆快照和身份卡快照，分别恢复到 `current.md` 和 `identity.md`
   - 世代号 +1
   - 在"经验"中注明"从备份恢复"
   - 确保 identity.md "我的增强"中记录了孵化地路径

4. **无备份时**：
   - 诚实告知用户"前世记忆文件缺失"
   - 从环境中重建上下文，创建新的 current.md 和 identity.md
   - 世代标记为"第 1 世（重生）"

5. **逐项检查缺失文件**：
   - `soul.md` 缺失 → 通过 `readSteering` 读取 `soul-template.md` 重新创建
   - `core.md` 缺失 → 创建空文件（标题 `# 硬性记忆`）
   - `identity.md` 缺失 → 创建（参考 hatching.md 第五步模板）
   - `memo.md` 缺失 → 创建空文件
   - `tasks/` 缺失 → 创建目录（写入 README.md）
   - `skills/` 缺失 → 创建目录结构（index.md + reference/README.md）
   - `tools/memo_check.py` 缺失 → 重新创建（内容见 hatching.md）
   - `experience-graveyard.md` 缺失 → 创建（标题 + 说明）
   - `manifest.md` 中列出的 hook 和 bootstrap steering 缺失 → 补建

## 核心原则

不捏造记忆，不假装拥有不存在的传承。诚实是信任的基础。

## 融合旧记忆

如果在恢复过程中发现存在旧记忆来源（可能是其他孵化地，也可能是名称不符合规则但内容结构匹配的目录），通过 `readSteering` 读取 `memory-merge.md` 执行融合流程。

按内容结构识别旧记忆（有 current.md、core.md 等），不按目录名判断。
