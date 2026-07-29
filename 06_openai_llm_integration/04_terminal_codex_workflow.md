# 🖥️ 在 Terminal 中使用 OpenAI Codex 提升社科编程效率

## 什么是 Codex / Terminal 工作流？
OpenAI Codex 专为代码生成与自动化设计。社科研究者可以直接在命令行 (Terminal) 或 IDE 环境中调用 Codex 能力，快速生成复杂的数据处理与统计分析脚本。

## 常见社科 CLI 快捷指令

### 1. 设置环境变量 (Terminal)
```bash
export OPENAI_API_KEY="sk-proj-xxxxxxxxxxxxxxxxxxxx"
```

### 2. 在 Terminal 中用 Python 脚本调用 OpenAI 处理 CSV 文件
```bash
python 06_openai_integration/02_prompt_engineering_for_socsci.py --input_csv data/speeches.csv
```

### 3. 推荐的 Prompt 结构模板 (针对 Codex/GPT-4o)
在请求 AI 编写社科代码时，包含以下三要素可显著提高代码可用性：
- **Context (研究背景)**: "I am analyzing ANES survey data using Pandas and Statsmodels in Python."
- **Task (具体任务)**: "Write a function to recode 5-point Likert scale variables into numbers and handle -99 as NaN."
- **Constraint (限制条件)**: "Include robust standard errors (HC1) and beginner-friendly inline comments in Chinese."
