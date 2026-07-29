"""
05_real_world_case_studies / case_03_ai_augmented_research.py
【实战案例3：AI 赋能的计算社会科学全流程】
演示由 OpenAI LLMs 参与的数据生成 -> 清洗 -> 统计建模 -> 自动化成果生成全流水线。
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf


def run_ai_augmented_pipeline():
    print("=== 开始 AI 赋能的社科学术研究流水线案例 ===")

    # 1. 模拟受访者数据集
    df = pd.DataFrame({
        'respondent_id': range(1, 10),
        'trust_in_ai': [5, 4, 2, 1, 5, 3, 4, 2, 5],
        'education_years': [16, 18, 12, 14, 20, 16, 14, 12, 18],
        'age': [28, 42, 65, 50, 31, 39, 45, 58, 26]
    })

    print("\n--- 1. 社科调查数据集预览 ---")
    print(df.head())

    # 2. 统计建模
    model = smf.ols('trust_in_ai ~ education_years + age', data=df).fit()

    print("\n--- 2. 回归模型分析摘要 ---")
    print(model.summary())

    print("\n--- 3. 提示：下一步可调用 06_openai_integration 模块生成学术分析报告段落。 ---")


if __name__ == "__main__":
    run_ai_augmented_pipeline()
