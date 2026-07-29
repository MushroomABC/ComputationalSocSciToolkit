"""
02_data_cleaning / 02_handle_missing_responses.py
【缺失值处理 (-99, -98, "拒绝回答")】
社科问卷中常使用 -99 或 -98 代表拒绝回答，需要替换为 NaN 以避免污染均值。
"""

import pandas as pd
import numpy as np


def clean_survey_missing(df: pd.DataFrame, missing_codes=[-99, -98, "Refused"]) -> pd.DataFrame:
    """将指定的缺失值代码替换为 NaN"""
    return df.replace(missing_codes, np.nan)


if __name__ == "__main__":
    raw_df = pd.DataFrame({
        'age': [25, 34, -99, 42],
        'income': [50000, -98, 62000, 71000]
    })

    clean_df = clean_survey_missing(raw_df)
    print("清洗前收入均值:", raw_df['income'].mean())  # 会被 -98 严重污染
    print("清洗后收入均值:", clean_df['income'].mean())  # 真实的正常均值
