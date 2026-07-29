"""
03_statistical_analysis / 01_ols_regression.py
【OLS 线性回归 (带稳健标准误 HC1)】
社科定量研究标准线性回归模型。
"""

import pandas as pd
import statsmodels.formula.api as smf


def run_robust_ols(df: pd.DataFrame, formula: str):
    """运行带有 HC1 稳健标准误的 OLS 回归"""
    model = smf.ols(formula, data=df)
    results = model.fit(cov_type='HC1')
    return results


if __name__ == "__main__":
    data = pd.DataFrame({
        'income': [30000, 45000, 50000, 68000, 80000, 95000],
        'education_years': [12, 14, 16, 16, 18, 20],
        'age': [25, 30, 35, 40, 45, 50]
    })

    res = run_robust_ols(data, 'income ~ education_years + age')
    print("回归分析结果摘要：")
    print(res.summary())
