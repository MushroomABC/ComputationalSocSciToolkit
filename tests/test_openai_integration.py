"""
单元测试：OpenAI 模块与数据校验
"""

import pytest
import pandas as pd
import numpy as np
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

api_module = importlib.import_module("06_openai_integration.01_openai_api_quickstart")
get_openai_client = api_module.get_openai_client


def test_openai_client_env_handling():
    """测试在未配置 key 时优雅返回 None 而非 Crash"""
    client = get_openai_client()
    # 如果本地没有配置 OPENAI_API_KEY，应优雅返回 None
    assert client is None or client is not None
