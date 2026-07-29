"""
05_real_world_case_studies / case_02_policy_eval_report.py
【实战案例2：公共政策评估数据流水线】
演示政策干预前后 (Treatment vs Control) 的简单回归评估。
"""

import pandas as pd
import statsmodels.formula.api as smf


def evaluate_policy_impact():
    print("=== 开始公共政策评估案例分析 ===")

    # 模拟政策评估实验数据
    eval_data = pd.DataFrame({
        'community_id': range(1, 7),
        'policy_treated': [1, 1, 1, 0, 0, 0],  # 1表示试点社区，0表示对照组
        'employment_rate': [75.2, 78.0, 76.5, 68.1, 69.5, 67.8],
        'avg_education_years': [13, 14, 13.5, 12, 12.5, 11.5]
    })

    model = smf.ols('employment_rate ~ policy_treated + avg_education_years', data=eval_data).fit()

    print("\n--- 政策效应评估 OLS 估计 ---")
    print(f"政策试点对就业率提升估计值: {model.params['policy_treated']:.2f}% (p-value: {model.pvalues['policy_treated']:.3f})")


if __name__ == "__main__":
    evaluate_policy_impact()
