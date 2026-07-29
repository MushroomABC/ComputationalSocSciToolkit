"""
02_data_cleaning / 04_recode_demographics.py
【人口统计变量重新编码 (年龄段与收入分组)】
将连续的年龄转为年龄段分组 (Youth, Middle, Senior)。
"""

import pandas as pd


def create_age_groups(age_series: pd.Series) -> pd.Series:
    """将连续年龄分组"""
    bins = [0, 30, 60, 100]
    labels = ['Youth (<30)', 'Middle-aged (30-60)', 'Senior (>60)']
    return pd.cut(age_series, bins=bins, labels=labels)


if __name__ == "__main__":
    people = pd.DataFrame({'age': [21, 45, 68, 29, 52]})
    people['age_group'] = create_age_groups(people['age'])
    print(people)
