# 🏛️ ComputationalSocialScience Toolkit (社科计算方法工具箱)

> **Empowering Social Scientists with Open-Source Python & OpenAI LLM Workflows**  
> 专为社会科学（政治学、社会学、经济学、公共管理）学生与研究者打造的零门槛 Python / OpenAI API 计算工具箱。

---

## 🌟 项目使命与公共价值 (Public Benefit)

大多数 Python / R 编程教程使用的都是生物基因、花卉测量（Iris Dataset）或物理仿真数据，社会科学背景的初学者往往觉得难以学以致用。

**SocialScienceCodingFoundation** 抛弃晦涩的计算机术语，以**模块化、小文件、多步骤**的方式，提供社会科学研究中最常用的真实场景代码（问卷数据清洗、李克特量表转换、调查权重计算、回归分析与学术期刊风格绘图），并深度整合 **OpenAI API 与 Codex 工作流**，帮助社科研究者用 AI 赋能量化与定性研究。

---

## 🗺️ 项目路线图 (Project Roadmap)

- [x] **Phase 1: 基础工具箱建设 (Foundation)**
  - 提供模块化的数据清洗（问卷权重、李克特量表、缺失值处理）代码。
  - 提供线性回归（OLS HC1 稳健标准误）与逻辑回归（Logit）标准化工具。
  - 提供学术期刊风格（ASR, APSR）图表绘制与 Markdown 表格导出工具。

- [ ] **Phase 2: OpenAI API 与 LLM 深度赋能 (OpenAI Grant Powered)**
  - **合成社科数据生成 (Synthetic Social Science Data Generation)**：利用 OpenAI API 自动生成具备人口统计分布特征的假问卷数据，用于教学与隐私保护研究。
  - **自动定性编码 (Automated Qualitative Coding)**：基于 GPT-4o / Codex 架构的社科文本（政治演讲、访谈记录）零样本主题分类与情绪编码工具。
  - **智能 Codebook 解析**：通过 OpenAI 交互接口一键解析 ANES / GSS 等大型社科数据库并自动生成 Python 数据预处理脚本。

- [ ] **Phase 3: 开源社区建设与教育推广 (Community & Education)**
  - 推出零门槛 Jupyter Notebook 交互教程。
  - 组织面向社科院系学生的开源计算工作坊。

---

## 🗂️ 目录导览 (Beginner-Friendly Folder Map)

代码按学习与功能编号拆分，每个文件专注单个小功能：

```text
ComputationalSocSciToolkit/
├── 🚀 01_getting_started/                  # 初学者入门：什么是社科计算与 Python 基础
│   ├── 01_welcome_to_css.md             #    - 计算社会科学与 AI 赋能研究简介
│   ├── 02_python_basics_for_socsci.py    #    - 社科生必懂的 Python 基础数据类型
│   └── 03_load_social_data.py           #    - 如何读取问卷与统计年鉴数据 (CSV/Excel)
├── 🧹 02_data_cleaning/                    # 问卷与民调数据预处理
│   ├── 01_likert_scale_encoder.py       #    - 李克特量表 (1-5分) 文本转数值
│   ├── 02_handle_missing_responses.py   #    - 缺失值处理 (-99, "拒绝回答", "不知道")
│   ├── 03_survey_weighting_basics.py    #    - 问卷抽样权重 (Survey Weighting) 计算
│   ├── 04_recode_demographics.py        #    - 人口统计变量重新编码 (年龄段、收入分组)
│   └── 05_ai_survey_cleaner.py          #    - AI 驱动的开放式文本问卷自动标准化
├── 📊 03_statistical_analysis/             # 社科常用的量化回归模型
│   ├── 01_ols_regression.py             #    - OLS 线性回归 (带稳健标准误 HC1)
│   ├── 02_logistic_regression.py        #    - Logistic 逻辑回归 (二元选择模型，如投票行为)
│   ├── 03_summary_table_exporter.py     #    - 将回归结果导出为学术论文表格 (Markdown/HTML)
│   └── 04_ai_model_interpreter.py       #    - AI 回归分析结果自然语言自动解读
├── 🎨 04_data_visualization/               # 期刊与政策报告绘图
│   ├── 01_publication_style.py          #    - 一键设置学术期刊配色与字体风格
│   ├── 02_coefficient_plots.py          #    - 绘制回归系数与 95% 置信区间图 (Coefficient Plot)
│   └── 03_demographic_charts.py         #    - 人口特征分组柱状图与分布图
├── 📁 05_real_world_case_studies/          # 实战案例：完整的研究代码模板
│   ├── case_01_public_opinion_survey.py #    - 案例1：民意调查数据全流程分析
│   ├── case_02_policy_eval_report.py    #    - 案例2：公共政策评估数据分析流水线
│   └── case_03_ai_augmented_research.py #    - 案例3：AI 赋能的社科学术研究流水线
├── 🤖 06_openai_integration/               # OpenAI API, LLM, Prompt & Terminal 集成
│   ├── 01_welcome_to_openai_llms.md     #    - OpenAI 与 LLM 赋能社科研究指南
│   ├── 01_openai_api_quickstart.py      #    - OpenAI Python SDK 基础配置与安全调用
│   ├── 02_prompt_engineering_for_socsci.py #  - 政治演讲与社科文本 Prompt 结构化编码
│   ├── 03_llm_synthetic_data_generator.py #  - 利用 OpenAI 生成合成民调数据集
│   └── 04_terminal_codex_workflow.md    #    - 在 Terminal 命令行中结合 Codex 提高效率
├── 🧪 tests/                               # 自动单元测试
│   ├── test_data_cleaning.py
│   └── test_openai_integration.py
├── CONTRIBUTING.md                      # 🤝 如何贡献你的社科代码
├── LICENSE                              # 📄 MIT 开源协议
└── requirements.txt                     # 📦 项目依赖库
```

---

## ⚡ 快速开始 (Quick Start)

### 1. 安装依赖库
```bash
pip install -r requirements.txt
```

### 2. 尝试 OpenAI API 交互
```bash
export OPENAI_API_KEY="your_openai_api_key"
python 06_openai_integration/01_openai_api_quickstart.py
```

---

## 📄 开源协议 (License)

本项目采用 MIT 许可证，详情请参阅 [`LICENSE`](LICENSE) 文件。
