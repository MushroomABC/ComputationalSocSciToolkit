"""
06_openai_integration / 03_llm_synthetic_data_generator.py
【基于 OpenAI 生成社科合成数据 (Synthetic Survey Data)】
演示利用 LLM 生成具备现实分布特征的假民调数据，保护受访者隐私或用于教学演示。
"""

from typing import List, Dict
import pandas as pd
from openai import OpenAI
import json


def generate_synthetic_survey_responses(client: OpenAI, num_samples: int = 5) -> pd.DataFrame:
    """利用 OpenAI API 生成指定数量的模拟民调受访者数据框"""
    prompt = f"""
    请生成 {num_samples} 条模拟社会科学问卷受访者数据，返回 JSON 数组格式，包含字段：
    - respondent_id: 整数 ID
    - age: 18-75 之间整数
    - education: High School / Bachelor / Master / PhD
    - trust_in_ai: 1 到 5 分的李克特得分
    - primary_news_source: Social Media / TV / Newspapers / Academic Journals
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You output JSON arrays of synthetic survey responses."},
            {"role": "user", "content": prompt}
        ]
    )

    data = json.loads(response.choices[0].message.content)
    # 提取数组
    records = data.get("responses", data.get("data", list(data.values())[0]))
    return pd.DataFrame(records)


if __name__ == "__main__":
    print("【合成社科数据生成器】请接入 OpenAI API 以实时生成测试数据集。")
