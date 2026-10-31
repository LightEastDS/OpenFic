# OpenFic Fork (LightEastDS Edition) 与原版差异对比文档

> **代码仓库**：[LightEastDS/OpenFic](https://github.com/LightEastDS/OpenFic)  
> **上游仓库（Upstream）**：[syrizelink/OpenFic](https://github.com/syrizelink/OpenFic)  
> **当前基线**：已完全合并上游最新 `v0.12.1` 版本，并在其基础上持续优化。

---

## 概述与核心定位转变

原版 OpenFic 是一个面向网络小说自动生成的优秀多 Agent 协作系统。但在原版设定下，由于角色定位局限于“网文写手”、提示词充斥反向禁令以及死板的字数卡点，模型在实际创作时极易陷入**“半新不旧、北方方言味、说书腔、零碎动作短句断行（电报体）”**的低质语域。

本 Fork 版（LightEastDS Edition）的核心目标是**将创作质感从“快餐网文”彻底拔升至“严肃文学与高质量出版物”级别**，通过系统级的提示词重构、粉色大象效应根除、全量内置技能脱敏、死板字数规则松绑，并新增了全栈中文字数精确统计工具。

---

## 详细差异对比

### 一、 文风体系重塑与提示词深度净化（Core Style Overhaul）

| 维度 | 原版 OpenFic | 本 Fork 版 (LightEastDS Edition) | 改进意义与机制 |
| :--- | :--- | :--- | :--- |
| **Agent 角色身份** | `你是专业的网络小说写手...` | `你是专业的资深出版物作家与文学创作者...` | 彻底切断 LLM 对网络快餐小说、低质语料的潜意识调用，将其全局语域拉升至出版级严肃文学范畴。 |
| **负面约束与禁词表** | 维护了一张死板且容易误伤的 `<banned_words>` 禁词表（粗暴禁用“沙哑”、“一丝”、“不是...而是”等文学基础词），并在提示词中提及“避免生硬说书腔与突兀方言”。 | **完全移除机械禁词表**，删除所有提及“方言/说书”的负面指令；改用**正向审美锚点**。 | **根除“粉色大象效应”**：原版越是强调“不要用方言/说书腔”，模型注意力越聚焦在方言特征上；本版本改为“采用典雅、洗练的高级出版物文风，标准规范的现代汉语”。 |
| **断句与段落示范** | 在提示词中提供了“一寸 / 两寸 / 三寸”一惊一乍式的短句断行示范。 | **彻底删除破碎断句示范**，明确要求“使用连贯、完整的复合长句，保持语气的沉稳与文学性”。 | 根除网文手机阅读常见的单句成段、抽搐断行问题，恢复汉语复合句的叙事韵律。 |
| **对白与人物设计** | 要求对白“尽量随意口语化”、“像自然口语交流”，容易退化为水词碎话。 | 要求“角色对话贴合身份、真实生动，展现角色的知性与独特气质，使用规范的现代通用语”。 | 杜绝无意义的低俗口头禅与俚语，让人物对白具备文学智性与潜台词深度。 |

---

### 二、 解除死板的章节与字数机械限制（Narrative Flexibility）

| 维度 | 原版 OpenFic | 本 Fork 版 (LightEastDS Edition) | 改进意义 |
| :--- | :--- | :--- | :--- |
| **字数硬性卡点** | 规定每章必须严格在 1800~2200 字之间，“过多或过少都会导致审查不通过”。 | **取消机械字数卡点**，章节划分顺应场景转换与悬念高潮，字数交由叙事自然完整度决定。 | 避免剧情写到一半因为“到了 2000 字”被生硬腰斩，或者剧情已结束却为了凑字数而强行注水。 |
| **章节节奏控制** | 强制按预设字数卡章。 | 若用户指定了字数要求，则严格执行用户指示；未指定时，以自然叙事和情节节拍推进为主。 | 真正契合长篇或中篇小说的呼吸节奏。 |

---

### 三、 内置技能库（Skills）全面脱敏与默认禁用

| 维度 | 原版 OpenFic | 本 Fork 版 (LightEastDS Edition) | 改进意义 |
| :--- | :--- | :--- | :--- |
| **技能默认开关** | 多个包含网文套路的技能处于启用或半启用状态。 | 全部 16 个内置技能统一设置为 **`is_enabled: false`（默认禁用）**。 | 防止冗长复杂的预设套路膨胀 Context 窗口，将控制权完全留给核心撰写 Agent。 |
| **技能内容净化** | `deslop-writing`、`character-design`、`dialogue-design`、`story-deconstruction` 等技能内部充斥大量“白话化”、“改为口语化”、“纯短句换气”等反向劣化指令。 | **深度清洗全部 16 个技能 YAML**，将所有“网文”、“口语化”、“自然白话”、“白描”全部重构为“高质量小说”、“生动具体的微动作”、“现代通用语”。 | 即使未来用户主动开启某个技能（如角色关系设计），也不会再带偏整体文学文风。 |

---

### 四、 新增功能：高精度中文字数统计与结构分析工具（Fullstack Feature）

LLM 普遍存在无法准确感知汉字字数的天然短板（通常基于 Token 估算，偏差极大），原版无法由 Agent 真实诊断字数。

本 Fork 版新增了 **全栈级精确中文字数统计工具**：

1. **后端实现 (`count_chinese_words`)**：
   - 文件路径：[`backend/app/agent_runtime/tools/impls/text/count_words.py`](file:///F:/Project/OpenFic/backend/app/agent_runtime/tools/impls/text/count_words.py)
   - 支持统计 **含标点字数** 与 **纯中文字符数（不含标点与空白）**。
   - 支持智能文本分句：可按小句（`clause`，逗号、分号切分）或整句（`sentence`，句号、感叹号切分）进行微观诊断。
   - 支持通过 `min_length` 与 `max_length` 条件筛选，方便模型自检出“过于零碎的短句（电报体）”或“失控的超长句”。
2. **智能体赋能**：
   - 将 `text` 工具类目赋予 `build`, `plan`, `writer`, `reviewer` 四大核心 Agent。
   - Agent 在撰写与审查时，可通过调用真实代码工具获取精确字数，杜绝模型幻觉。
3. **前端 UI 交互可视化**：
   - 文件路径：[`web/src/components/agent/message-blocks/tools/text/count-words-tool-message.tsx`](file:///F:/Project/OpenFic/web/src/components/agent/message-blocks/tools/text/count-words-tool-message.tsx)
   - 在前端聊天会话界面，模型调用字数统计时会渲染出专用的 **卡片式统计视图**，直观展示统计结果与分句情况。

---

### 五、 上游同步与工程维护（Upstream Sync）

- 持续跟进官方主线更新，已成功变基合并上游最新 `v0.12.1` 发布版。
- 修复了前端工具组件导入路径类型检查错误（`isRecord`, `asString` 路径修复）。
- 保持 Docker 容器化部署与本地运行的最佳兼容性。

---

## 变更文件清单

```text
30 files changed, 413 insertions(+), 290 deletions(-)

[全栈工具]
- backend/app/agent_runtime/tools/impls/text/count_words.py
- backend/app/agent_runtime/tools/impls/text/__init__.py
- backend/app/agent_runtime/tools/impls/__init__.py
- backend/app/agent_runtime/agents/definitions.py
- backend/app/agent_runtime/agents/tool_categories.py
- web/src/components/agent/message-blocks/tools/text/count-words-tool-message.tsx
- web/src/components/agent/message-blocks/tools/text/count-words-tool-message.css
- web/src/components/agent/message-blocks/tools/shared/tool-message-catalog.ts
- web/src/components/agent/message-blocks/tools/shared/tool-message-registry.tsx

[核心提示词]
- backend/app/prompts/builtin-agents/writer.yaml
- backend/app/prompts/builtin-agents/build.yaml
- backend/app/prompts/builtin-agents/composer.yaml
- backend/app/prompts/builtin-agents/plan.yaml
- backend/app/prompts/builtin-agents/reviewer.yaml

[技能库脱敏与禁用]
- backend/app/skills/*.yaml (共 16 个技能全部置为 is_enabled: false，并全量文本脱敏)
```
