"""
03_statistical_analysis / 04_ai_model_interpreter.py
【AI 回归分析结果自然语言自动解读】
演示如何将 Statsmodels 回归摘要通过 OpenAI API 转为政策简报与学术论文可用的自然语言解读段落。
"""

from typing import Dict
from openai import OpenAI
import pandas as pd


def generate_ai_executive_summary(client: OpenAI, regression_summary_str: str) -> str:
    """利用 OpenAI 模型为复杂的回归分析表格编写学术简报摘要"""
    system_prompt = """
    你是一位量化社会科学与公共政策研究专家。
    请阅读输入的统计回归分析摘要，用平实的语言撰写一段 150 字以内的政策简报结论：
    - 说明哪些自变量在统计上显著 (p < 0.05)
    - 解释其效应方向（正向影响还是负向影响）及其实际社科含义
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Regression Summary:\n{regression_summary_str}"}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("【AI 统计解读器】已配置回归表格解读模版。")
