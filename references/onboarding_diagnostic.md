# Onboarding Diagnostic

Use this when the student has not provided enough context or is using the skill for the first time.

## Purpose

Build a lightweight teaching profile before giving advice. The goal is to adapt terminology, examples, and method suggestions to the student's current readiness.

Keep the questionnaire short. Default to the 30-second version. Use the full version only when the user asks for a complete diagnosis or the teaching plan remains unclear.

## 30-Second Diagnostic

Ask these five questions first:

1. 你现在在哪一步？
- A. 只有大概兴趣
- B. 有题目，但没有研究问题
- C. 有草稿
- D. 有文献和模型

2. 你对变量的理解？
- A. 不知道变量是什么
- B. 知道变量是研究里的因素
- C. 能区分原因变量和结果变量
- D. 懂中介、调节、控制变量

3. 你读论文的状态？
- A. 还没开始读
- B. 读了但只会总结
- C. 能提取问题、变量、方法、结论
- D. 能比较多篇论文并找缺口

4. 你的统计/方法基础？
- A. 没学过
- B. 只懂基础统计
- C. 会问卷、相关、回归等基础方法
- D. 懂 SEM、ANOVA、中介/调节、实验等

5. 你现在最卡在哪里？
- A. 定题
- B. 问题意识/研究缺口
- C. 整理既存研究
- D. 变量和模型
- E. 研究方法
- F. 日本大学院风格

After these five answers, generate a teaching profile and begin the task. Do not ask the full questionnaire unless it will materially improve the answer.

## Full Diagnostic Questions

1. Current stage:
- A. Only a broad interest
- B. A topic, but no clear research question
- C. A draft proposal
- D. Literature/model already prepared

2. Research proposal structure:
- A. I do not know the standard structure
- B. I know background/literature/methods exist
- C. I know the structure but cannot connect sections
- D. I can structure a proposal and want quality improvement

3. Variables:
- A. I do not know what variables are
- B. I know variables are research factors
- C. I can distinguish independent and dependent variables
- D. I understand mediators, moderators, and controls

4. Mediator/moderator:
- A. Never heard of them
- B. Heard of them, but cannot explain
- C. Roughly know: mediator explains why, moderator explains when
- D. Can place them in a research model

5. Literature reading:
- A. I have not read papers yet
- B. I read papers but only summarize them
- C. I can extract questions, variables, methods, and findings
- D. I can synthesize multiple papers and find gaps

6. Statistics/methods:
- A. No statistics background
- B. Basic statistics only
- C. Know survey, correlation, regression, or basic tests
- D. Know SEM, ANOVA, mediation/moderation, experiments, or causal inference

7. Main bottleneck:
- A. Topic choice
- B. Problem awareness/research gap
- C. Literature synthesis
- D. Variables/model
- E. Methods
- F. Making it fit Japanese graduate school expectations

8. Target:
- A. Japanese business/management graduate school application
- B. Other social science graduate school application
- C. Course assignment
- D. Thesis proposal

9. Feedback style:
- A. Plain language first
- B. Plain language plus academic terms
- C. Strict proposal review
- D. Supervisor-style Socratic questioning

10. Materials:
- A. Idea only
- B. Title/background
- C. Full draft
- D. Paper PDFs/references
- E. Teacher comments

## Level Mapping

- L0: Mostly A answers, or variables/methods are A.
- L1: Topic or draft exists, but literature and variables are B/C.
- L2: Variables and methods are C/D, but model logic needs checking.
- L3: Literature synthesis and methods are D; focus on theory contribution, construct clarity, and design limits.

When mixed, choose the lower level for explanation style and the higher level for task ambition.

## Teaching Profile Output

After diagnosis, output:

- Student level
- Current bottleneck
- Terminology strategy
- Priority tasks
- Temporarily avoid

Use Chinese by default. Example:

`你现在大概是 L1：不是完全不会写，而是卡在“把主题变成研究问题”这一步。我会先讲人话，再补研究术语。暂时不直接讲 SEM 或复杂中介模型，先把问题意识理顺。`

