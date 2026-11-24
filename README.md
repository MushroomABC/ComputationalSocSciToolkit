# 🏛️ ComputationalSocialScience Toolkit

> **Empowering Social Scientists with Open-Source Python & OpenAI LLM Workflows**  
> A zero-barrier Python / OpenAI API computational toolkit built specifically for students and researchers in the social sciences (Political Science, Sociology, Economics, Public Administration).

---

## 🌟 Project Mission & Public Benefit

Most Python / R programming tutorials use biological genetics, flower measurements (Iris Dataset), or physics simulation data, making it difficult for beginners with social science backgrounds to apply what they learn in practice.

**SocialScienceCodingFoundation** leaves behind obscure computer science jargon and adopts a **modular, small-file, multi-step** approach to provide the most commonly used real-world code in social science research (survey data cleaning, Likert scale conversion, survey weighting calculation, regression analysis, and academic journal-style plotting). It also deeply integrates the **OpenAI API and Codex workflows** to help social science researchers empower both quantitative and qualitative research with AI.

---

## 🗺️ Project Roadmap

- [x] **Phase 1: Core Toolkit Development (Foundation)**
  - Provide modular code for data cleaning (survey weighting, Likert scales, missing value handling).
  - Provide standardized tools for linear regression (OLS with HC1 robust standard errors) and logistic regression (Logit).
  - Provide academic journal-style (ASR, APSR) chart plotting and Markdown table export tools.

- [ ] **Phase 2: Deep Integration with OpenAI API & LLMs (OpenAI Grant Powered)**
  - **Synthetic Social Science Data Generation**: Automatically generate synthetic survey data with realistic demographic distributions using the OpenAI API for teaching and privacy-preserving research.
  - **Automated Qualitative Coding**: Zero-shot topic classification and sentiment coding tools for social science texts (political speeches, interview transcripts) based on GPT-4o / Codex architectures.
  - **Intelligent Codebook Parsing**: One-click parsing of large-scale social science databases such as ANES / GSS via the OpenAI interactive interface, with automatic generation of Python data preprocessing scripts.

- [ ] **Phase 3: Open-Source Community & Education**
  - Launch zero-barrier interactive Jupyter Notebook tutorials.
  - Organize open-source computational workshops for social science students.

---

## 🗂️ Directory Overview (Beginner-Friendly Folder Map)

The code is organized numerically by learning stage and functionality, with each file focused on a single small feature:

```text
ComputationalSocSciToolkit/
├── 🚀 01_getting_started/                  # Beginner's start: What is computational social science & Python basics
│   ├── 01_welcome_to_css.md             #    - Introduction to Computational Social Science and AI-powered research
│   ├── 02_python_basics_for_socsci.py    #    - Essential Python basic data types for social science students
│   └── 03_load_social_data.py           #    - How to load survey and statistical yearbook data (CSV/Excel)
├── 🧹 02_data_cleaning/                    # Survey and polling data preprocessing
│   ├── 01_likert_scale_encoder.py       #    - Convert Likert scale (1-5) text responses to numeric values
│   ├── 02_handle_missing_responses.py   #    - Handle missing values (-99, "Refused", "Don't know")
│   ├── 03_survey_weighting_basics.py    #    - Survey sampling weight calculation (Survey Weighting)
│   ├── 04_recode_demographics.py        #    - Recode demographic variables (age groups, income brackets)
│   └── 05_ai_survey_cleaner.py          #    - AI-driven automatic standardization of open-ended survey text
├── 📊 03_statistical_analysis/             # Common quantitative regression models in social science
│   ├── 01_ols_regression.py             #    - OLS linear regression (with HC1 robust standard errors)
│   ├── 02_logistic_regression.py        #    - Logistic regression (binary choice models, e.g., voting behavior)
│   ├── 03_summary_table_exporter.py     #    - Export regression results to academic paper tables (Markdown/HTML)
│   └── 04_ai_model_interpreter.py       #    - Automated natural language interpretation of regression results via AI
├── 🎨 04_data_visualization/               # Plotting for academic journals and policy reports
│   ├── 01_publication_style.py          #    - One-click setup for academic journal color palettes and font styles
│   ├── 02_coefficient_plots.py          #    - Plot regression coefficients and 95% confidence intervals (Coefficient Plot)
│   └── 03_demographic_charts.py         #    - Grouped bar charts and distribution plots by demographics
├── 📁 05_real_world_case_studies/          # Practical case studies: complete research code templates
│   ├── case_01_public_opinion_survey.py #    - Case 1: End-to-end public opinion survey data analysis
│   ├── case_02_policy_eval_report.py    #    - Case 2: Public policy evaluation data analysis pipeline
│   └── case_03_ai_augmented_research.py #    - Case 3: AI-augmented academic social science research pipeline
├── 🤖 06_openai_integration/               # OpenAI API, LLM, Prompt & Terminal integration
│   ├── 01_welcome_to_openai_llms.md     #    - Guide to empowering social science research with OpenAI and LLMs
│   ├── 01_openai_api_quickstart.py      #    - Basic OpenAI Python SDK setup and secure API calls
│   ├── 02_prompt_engineering_for_socsci.py #  - Structured prompt coding for political speeches and social science texts
│   ├── 03_llm_synthetic_data_generator.py #  - Generate synthetic polling datasets using OpenAI
│   └── 04_terminal_codex_workflow.md    #    - Boost productivity in the terminal command line with Codex
├── 🧪 tests/                               # Automated unit tests
│   ├── test_data_cleaning.py
│   └── test_openai_integration.py
├── CONTRIBUTING.md                      # 🤝 How to contribute your social science code
├── LICENSE                              # 📄 MIT License
└── requirements.txt                     # 📦 Project dependencies
```

---

## ⚡ Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Try Interacting with the OpenAI API
```bash
export OPENAI_API_KEY="your_openai_api_key"
python 06_openai_integration/01_openai_api_quickstart.py
```

---

## 📄 License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.
