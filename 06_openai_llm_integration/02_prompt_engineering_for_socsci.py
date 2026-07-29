"""
06_openai_integration / 02_prompt_engineering_for_socsci.py
【社科 Prompt 工程：政治演讲与文本自动分类】
演示利用 Structured System Prompt 让 LLM 输出 JSON 格式的定性编码结果。
"""

from typing import Dict
from openai import OpenAI
import json


def classify_political_speech(client: OpenAI, speech_text: str) -> Dict:
    """利用 OpenAI 模型进行社科文本结构化分类与情感/立场判定"""
    system_prompt = """
    你是一位政治学与社会学研究分析专家。
    请对提供的文本进行定性编码，严格返回以下 JSON 格式：
    {
      "topic": "经济 / 外交 / 环保 / 医疗 / 其他",
      "stance": "支持 / 中立 / 反对",
      "policy_proposal_mentioned": true/false,
      "summary_zh": "一句话中文总结"
    }
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": speech_text}
        ]
    )

    result_json = json.loads(response.choices[0].message.content)
    return result_json


if __name__ == "__main__":
    sample_text = "We must immediately invest in renewable solar energy and phase out coal to achieve net-zero emissions by 2040."
    print("【样例政治文本】:", sample_text)
    print("【模拟测试提示】请设置 OPENAI_API_KEY 运行完整 API 调用。")
