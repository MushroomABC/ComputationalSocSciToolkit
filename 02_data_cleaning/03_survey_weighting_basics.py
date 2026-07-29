"""
02_data_cleaning / 03_survey_weighting_basics.py
【问卷抽样权重 (Survey Weighting) 计算】
演示如何用抽样权重计算全人口的加权平均值。
"""

import pandas as pd


def calculate_weighted_mean(df: pd.DataFrame, value_col: str, weight_col: str) -> float:
    """计算加权平均数"""
    weighted_sum = (df[value_col] * df[weight_col]).sum()
    total_weights = df[weight_col].sum()
    return weighted_sum / total_weights


if __name__ == "__main__":
    survey_sample = pd.DataFrame({
        'support_policy': [1, 1, 0, 0, 1],  # 1支持, 0反对
        'sample_weight': [1.2, 0.8, 1.5, 0.9, 1.1]  # 抽样权重
    })

    unweighted = survey_sample['support_policy'].mean()
    weighted = calculate_weighted_mean(survey_sample, 'support_policy', 'sample_weight')

    print(f"未加权支持率: {unweighted:.1%}")
    print(f"加权后总体估计支持率: {weighted:.1%}")
