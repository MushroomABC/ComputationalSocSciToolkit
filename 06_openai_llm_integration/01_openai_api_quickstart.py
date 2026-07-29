"""
06_openai_integration / 01_openai_api_quickstart.py
【OpenAI API 基础调用与环境变量配置】
演示社科研究者如何在 Python 中安全调用 OpenAI API (避免硬编码 Key)。
"""

import os
from openai import OpenAI


def get_openai_client() -> OpenAI:
    """
    初始化 OpenAI 客户端。
    推荐在 Terminal 中运行 `export OPENAI_API_KEY="your_api_key"`
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("[提示] 未检测到 OPENAI_API_KEY 环境变量，请在 Terminal 中设置 export OPENAI_API_KEY='your_key'")
        return None
    return OpenAI(api_key=api_key)


def test_openai_connection(client: OpenAI):
    """测试 API 连通性"""
    if client is None:
        return
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for social science researchers."},
            {"role": "user", "content": "Explain 'computational social science' in one simple sentence."}
        ],
        max_tokens=50
    )
    print("OpenAI 回复：", response.choices[0].message.content)


if __name__ == "__main__":
    client = get_openai_client()
    if client:
        test_openai_connection(client)
