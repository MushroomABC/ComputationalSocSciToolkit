"""
03_statistical_analysis / 02_logistic_regression.py
【Logistic 逻辑回归 (二元选择模型)】
用于分析二分变量（如：是否投票、是否参与抗议、是否买房）。
"""

import pandas as pd
import statsmodels.formula.api as smf


def run_logit_model(df: pd.DataFrame, formula: str):
    """运行逻辑回归模型"""
    model = smf.logit(formula, data=df)
    results = model.fit(disp=False)
    return results


if __name__ == "__main__":
    voter_data = pd.DataFrame({
        'voted': [1, 0, 1, 1, 0, 1],
        'political_interest': [5, 2, 4, 5, 1, 3],
        'age': [45, 20, 35, 50, 19, 62]
    })

    logit_res = run_logit_model(voter_data, 'voted ~ political_interest + age')
    print("逻辑回归结果摘要：")
    print(logit_res.summary())
