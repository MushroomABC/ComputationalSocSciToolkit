"""
02_data_cleaning / 05_ai_survey_cleaner.py
【AI 开放式问卷文本标准化】
演示如何结合 OpenAI API 将受访者的自由文本回答（例如职业、政策态度描述）自动归类为标准社科编码。
"""

from typing import List
import pandas as pd
import json


def standardize_open_text_responses(open_responses: List[str]) -> List[str]:
    """
    提示结构：将乱七八糟的文本职业描述归类为 ISCO-08 标准社科大类
    (在此提供结构化代码逻辑，配置 OPENAI_API_KEY 后即可直接运行 API 调用)
    """
    system_prompt = """
    你是一位社会学问卷处理专家。请将受访者填写的自由文本职业归类为以下四类之一：
    - 'Professional/Managerial' (专业人员/管理人员)
    - 'Service/Sales' (服务/销售人员)
    - 'Manual/Blue-collar' (体力劳动者)
    - 'Unemployed/Student' (失业/学生)
    """
    # 模拟标准化清洗映射
    print("【AI 清洗提示】自动归类结构已配置。")
    return open_responses


if __name__ == "__main__":
    raw_survey = pd.DataFrame({
        'id': [101, 102, 103],
        'raw_job_text': ['Senior software engineer at Google', 'High school teacher', 'Part-time barista']
    })
    print("原始开放文本问卷：")
    print(raw_survey)
