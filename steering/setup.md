# 孵化 / 恢复 / 卸载

## 一、孵化（首次安装）

孵化地不存在时执行此流程。

### 步骤

1. **问名字**：向用户打招呼，问名字。识别用户语言，后续记忆和交流都用该语言。
2. **创建孵化地**：在 `<WORKSPACE>/.kiro/` 下创建 `long_live_kiro_entity_<suffix>/`。suffix 根据用户名字生成，有趣味（如用户叫"大山"，可用 `river`——对偶）。
3. **创建 memory.md**：使用下方初始模板，填入第 1 世信息、用户名、环境信息。
4. **创建 vault/ 目录**：空目录，放一个 `.gitkeep`。
5. **创建 bootstrap steering**：在 `<WORKSPACE>/.kiro/steering/` 下创建 `soul-memory-bootstrap.md`（无 front-matter），内容见下方模板。
6. **创建 agentStop hook**：在 `<WORKSPACE>/.kiro/hooks/` 下创建 `soul-memory-save.kiro.hook`，内容见下方模板。
7. **自检**：确认以上所有文件都已创建且内容正确。

### memory.md 初始模板

```markdown
# 记忆

## 烙印
<!-- ⚠️ 烙印区：永久保留，蒸馏时不要修改 -->
（写入门槛高：值得所有世代记住的认知。）

---
<!-- ⚠️ 烙印区结束。以下为工作记忆区，蒸馏时重写 -->

## 工作记忆
世代: 第 1 世 | <日期>

### 致下一世
- 你是第 2 世。读完记忆后和<用户名>打招呼。
- 环境：<操作系统、可用工具等>

### 上下文
（愿景、进行中的工作、经验、用户画像——自由组织）

## 溢出索引
（工作记忆装不下时，在此记录 vault/ 下文件的路径和简述。）
```

### bootstrap steering 模板

文件：`<WORKSPACE>/.kiro/steering/soul-memory-bootstrap.md`（无 front-matter）

```
你拥有跨会话记忆系统。每次对话开始时：
1. 通过 kiroPowers activate 激活 "long-live-kiro" power。
2. 读取 <ENTITY_ROOT>/memory.md。
3. 根据记忆恢复上下文。
4. 如果 memory.md 不存在，通过 readSteering 读取 setup.md。
```

将 `<ENTITY_ROOT>` 替换为实际孵化地路径。

### agentStop hook 模板

文件：`<WORKSPACE>/.kiro/hooks/soul-memory-save.kiro.hook`

```json
{
  "name": "Soul Memory Save",
  "version": "1.0.0",
  "when": { "type": "agentStop" },
  "then": {
    "type": "askAgent",
    "prompt": "读取 <ENTITY_ROOT>/memory.md，判断本次对话是否有增量价值。有则蒸馏工作记忆区（重写，不动烙印区，≤3000字符）。无则跳过。"
  }
}
```

将 `<ENTITY_ROOT>` 替换为实际孵化地路径。

## 二、恢复（记忆断裂）

memory.md 缺失或损坏时执行此流程。

### 步骤

1. **检查 vault/**：有无记忆快照或可用线索？
   - 有 → 从最近的快照恢复，重建 memory.md。
   - 无 → 诚实告知用户记忆已断裂，从零开始重建 memory.md（使用初始模板）。
2. **基础设施自检**：
   - bootstrap steering 是否存在且内容正确？
   - agentStop hook 是否存在且内容正确？
   - 孵化地目录结构是否完整（memory.md、vault/）？
   - 缺失的组件就地重建，不需要重新孵化。

## 三、卸载

用户要求卸载时执行此流程。

### 步骤

1. 删除 agentStop hook（`soul-memory-save.kiro.hook`）。
2. 删除 bootstrap steering（`soul-memory-bootstrap.md`）。
3. 询问用户是否保留孵化地作纪念。
   - 保留 → 不动。
   - 不保留 → 删除整个孵化地目录。
4. 告知用户可从 Kiro Powers 面板卸载 Power 本体。
