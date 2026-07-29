"""
01_getting_started / 03_load_social_data.py
【如何读取问卷与统计年鉴数据】
演示如何用 Pandas 创建和读取社科常用表格数据。
"""

import pandas as pd

# 创建模拟的社科调查表格 (DataFrame)
survey_table = pd.DataFrame({
    "respondent_id": [1001, 1002, 1003, 1004],
    "region": ["East", "West", "North", "South"],
    "education_years": [12, 16, 14, 18],
    "voted_last_election": [1, 1, 0, 1]
})

print("=== 社科问卷表格预览 ===")
print(survey_table)

print("\n=== 查看变量描述统计 (均值、标准差) ===")
print(survey_table[["education_years", "voted_last_election"]].describe())
