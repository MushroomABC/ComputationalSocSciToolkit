"""
05_real_world_case_studies / case_01_public_opinion_survey.py
【实战案例1：民意调查数据全流程分析】
从问卷数据清洗 -> 变量转化 -> 逻辑回归模型 -> 结果输出的全流程演示。
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf


def run_opinion_survey_pipeline():
    print("=== 开始民意调查全流程分析案例 ===")

    # 1. 模拟收集到的原始问卷数据
    raw_survey = pd.DataFrame({
        'respondent_id': [1, 2, 3, 4, 5, 6],
        'trust_in_media': ['Strongly Agree', 'Agree', 'Disagree', 'Refused', 'Strongly Agree', 'Neutral'],
        'age': [24, 45, 62, -99, 38, 51],
        'voted_last_election': [1, 1, 0, 1, 1, 0]
    })

    # 2. 清洗数据：处理缺失值与量表转换
    cleaned = raw_survey.replace([-99, 'Refused'], np.nan).copy()
    likert_map = {
        'Strongly Disagree': 1, 'Disagree': 2, 'Neutral': 3, 'Agree': 4, 'Strongly Agree': 5
    }
    cleaned['media_trust_num'] = cleaned['trust_in_media'].map(likert_map)

    print("\n--- 清洗后的问卷数据集 ---")
    print(cleaned[['respondent_id', 'media_trust_num', 'age', 'voted_last_election']])

    # 3. 拟合模型分析：媒体信任度与年龄对投票行为的影响
    valid_data = cleaned.dropna()
    logit_model = smf.logit('voted_last_election ~ media_trust_num + age', data=valid_data).fit(disp=False)

    print("\n--- 统计分析模型结果 ---")
    print(logit_model.summary())


if __name__ == "__main__":
    run_opinion_survey_pipeline()
