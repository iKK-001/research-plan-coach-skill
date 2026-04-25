# Research Plan Coach Skill

面向中文学生的研究计划书思维教练，重点服务日本经营学/商学大学院申请场景。

它不是研究计划书代写器，而是帮助学生把模糊兴趣整理成可研究问题：

- 把“感兴趣的现象”变成“研究问题”
- 缩小过大的研究范围
- 提取论文、草稿、课件中的有用信息
- 整理既存研究并寻找研究缺口
- 判断变量能不能作为合理创新加入模型
- 检查研究方法能不能支撑结论
- 根据学生基础调整解释方式

## Skill Features

### 1. 看人下菜的前置诊断

首次使用时，skill 会先用 30 秒问卷判断学生状态：

- 是否已经有主题或草稿
- 是否理解变量、中介变量、调节变量
- 是否读过论文
- 是否有统计或研究方法基础
- 当前最卡在哪一步

然后再决定输出方式。小白先讲人话，进阶学生再讲模型、变量和方法。

### 2. 不直接代写

这个 skill 的默认产出是：

- 诊断
- 表格
- 追问
- 修改建议
- 提纲
- 示例句式
- 下一步任务

如果需要段落示例，会明确标注为 `示例写法`，避免把 AI 文字伪装成学生终稿。

### 3. 论文与材料提取脚本

内置脚本支持提取：

- PDF
- DOCX
- PPTX
- TXT
- MD

推荐使用 Codex bundled Python：

```bash
$CODEX_BUNDLED_PYTHON scripts/extract_source_notes.py SOURCE.pdf
```

常用参数：

```bash
--max-pages 30
--sections-only
--keywords "limitations,future research,method"
```

如果系统 Python 缺少依赖，脚本会提示使用 bundled Python 或安装对应库。

## Installation

复制本目录到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R research-plan-coach ~/.codex/skills/
```

重新打开 Codex 后即可在可用 skills 中看到它。

## No Agent? Web LLM Usage

如果用户只有 ChatGPT、Gemini、Kimi、DeepSeek、豆包等网页版，也能使用这套逻辑。

区别是：

- Agent 版可以自动读取本地 PDF/DOCX/PPTX 并调用脚本
- 网页版需要手动上传文件，或复制论文摘要、草稿、关键段落

网页版提示词：

```text
请你扮演“研究计划书思维教练”，不要直接帮我代写完整研究计划书。

请先用5个问题判断我现在的阶段：
1. 我现在是只有兴趣、有题目、有草稿，还是已有文献和模型？
2. 我是否理解变量、中介变量、调节变量？
3. 我读论文是只能总结，还是能提取研究问题、变量、方法和结论？
4. 我有没有统计或研究方法基础？
5. 我现在最卡的是选题、问题意识、既存研究、变量模型，还是研究方法？

然后根据我的水平，用我能听懂的语言帮我：
- 把感兴趣的现象变成研究问题
- 缩小研究范围
- 整理既存研究
- 找研究缺口
- 判断变量能不能加
- 推荐可行研究方法

请不要一上来使用复杂术语。如果必须使用，请先用白话解释。
```

## Structure

```text
research-plan-coach/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── onboarding_diagnostic.md
│   ├── learner_adaptation.md
│   ├── proposal_rubric.md
│   ├── literature_extraction_template.md
│   ├── gap_patterns.md
│   ├── variable_ideation.md
│   ├── method_matching.md
│   ├── japanese_business_school_style.md
│   └── toolkit.md
└── scripts/
    ├── extract_source_notes.py
    └── extract_pdf_notes.py
```

## Notes

- 默认面向中文学生输出
- 研究计划书场景以日本经营学/商学大学院为主
- 参考资料强调问题意识、既存研究、研究缺口、变量逻辑和方法适配
- 这个项目不包含申请成功保证，也不替代导师指导

