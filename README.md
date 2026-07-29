# 🏛️ ComputationalSocialScience Toolkit (社科计算方法工具箱)

> 专为社会科学（政治学、社会学、经济学、公共管理）学生与研究者打造的零门槛 Python/R 计算工具箱。

---

## 💡 为什么建立这个项目？ (The Problem)

大多数 Python / R 编程教程使用的都是生物基因、花卉测量（Iris Dataset）或物理仿真数据，社会科学背景的初学者往往觉得难以学以致用。

**本工具箱** 抛弃晦涩的计算机术语，以**模块化、小文件、多步骤**的方式，提供社会科学研究中最常用的真实场景代码（问卷数据清洗、李克特量表转换、调查权重计算、回归分析与学术期刊风格绘图）。

---

## 🗂️ 目录导览 (Beginner-Friendly Folder Map)

我们将代码拆分为按学习顺序编号的文件夹，每个文件只专注一个简单的具体功能：

```text
ComputationalSocSciToolkit/
├── 01_getting_started/                 # 🚀 01_入门指南：什么是社科计算与 Python 基础
│   ├── 01_welcome_to_css.md            #    - 计算社会科学简介与学习路线图
│   ├── 02_python_basics_for_socsci.py   #    - 社科生必懂的 Python 基础数据类型
│   └── 03_load_social_data.py          #    - 如何读取问卷与统计年鉴数据 (CSV/Excel)
├── 02_data_cleaning/                   # 🧹 02_数据清洗：问卷与民调数据预处理
│   ├── __init__.py
│   ├── 01_likert_scale_encoder.py      #    - 李克特量表 (1-5分) 文本转数值
│   ├── 02_handle_missing_responses.py  #    - 缺失值处理 (-99, "拒绝回答", "不知道")
│   ├── 03_survey_weighting_basics.py   #    - 问卷抽样权重 (Survey Weighting) 计算
│   └── 04_recode_demographics.py       #    - 人口统计变量重新编码 (年龄段、收入分组)
├── 03_statistical_analysis/            # 📊 03_统计建模：社科常用的量化回归模型
│   ├── __init__.py
│   ├── 01_ols_regression.py            #    - OLS 线性回归 (带稳健标准误 HC1)
│   ├── 02_logistic_regression.py       #    - Logistic 逻辑回归 (二元选择模型，如投票行为)
│   └── 03_summary_table_exporter.py    #    - 将回归结果导出为学术论文表格 (Markdown/HTML)
├── 04_data_visualization/              # 🎨 04_数据可视化：期刊与政策报告绘图
│   ├── __init__.py
│   ├── 01_publication_style.py         #    - 一键设置学术期刊配色与字体风格
│   ├── 02_coefficient_plots.py         #    - 绘制回归系数与 95% 置信区间图 (Coefficient Plot)
│   └── 03_demographic_charts.py        #    - 人口特征分组柱状图与分布图
├── 05_real_world_case_studies/         # 📁 05_实战案例：完整的研究代码模板
│   ├── case_01_public_opinion_survey.py #    - 案例1：民意调查数据全流程分析
│   └── case_02_policy_eval_report.py   #    - 案例2：公共政策评估数据分析流水线
├── tests/                               # 🧪 自动单元测试
│   └── test_data_cleaning.py
├── CONTRIBUTING.md                     # 🤝 如何贡献你的社科代码
├── LICENSE                             # 📄 MIT 开源协议
└── requirements.txt                    # 📦 项目依赖库
```

---

## ⚡ 快速开始 (Quick Start)

### 1. 安装依赖库
```bash
pip install -r requirements.txt
```

### 2. 运行入门示例
```bash
# 运行问卷清洗示例
python 02_data_cleaning/01_likert_scale_encoder.py

# 运行完整实战案例
python 05_real_world_case_studies/case_01_public_opinion_survey.py
```

---

## 📄 开源协议 (License)

本项目采用 MIT 许可证，详情请参阅 [`LICENSE`](LICENSE) 文件。
