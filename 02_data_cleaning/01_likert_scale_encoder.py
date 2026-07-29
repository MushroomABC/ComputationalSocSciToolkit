"""
02_data_cleaning / 01_likert_scale_encoder.py
【李克特量表 (1-5分) 文本转数值】
将问卷中的 "非常同意"、"不同意" 等文字转为可用于回归分析的数字。
"""

import pandas as pd
import numpy as np


def convert_likert_5point(data_series: pd.Series) -> pd.Series:
    """将5点李克特量表转化为 1-5 分的数值"""
    mapping = {
        'Strongly Disagree': 1.0,
        'Disagree': 2.0,
        'Neutral': 3.0,
        'Agree': 4.0,
        'Strongly Agree': 5.0,
        'Don\'t Know': np.nan,
        'Refused': np.nan
    }
    return data_series.map(mapping)


if __name__ == "__main__":
    # 示例数据
    survey = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'gov_trust': ['Strongly Agree', 'Agree', 'Disagree', 'Refused']
    })

    survey['gov_trust_num'] = convert_likert_5point(survey['gov_trust'])
    print("转换结果：")
    print(survey[['id', 'gov_trust', 'gov_trust_num']])
