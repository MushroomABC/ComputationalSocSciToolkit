"""单元测试：数据清洗"""

import pytest
import pandas as pd
import numpy as np
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

likert_module = importlib.import_module("02_data_cleaning.01_likert_scale_encoder")
missing_module = importlib.import_module("02_data_cleaning.02_handle_missing_responses")

convert_likert_5point = likert_module.convert_likert_5point
clean_survey_missing = missing_module.clean_survey_missing


def test_convert_likert_5point():
    s = pd.Series(['Strongly Agree', 'Disagree', 'Refused'])
    res = convert_likert_5point(s)
    assert res.iloc[0] == 5.0
    assert res.iloc[1] == 2.0
    assert np.isnan(res.iloc[2])


def test_clean_survey_missing():
    df = pd.DataFrame({'age': [20, -99, 30]})
    res = clean_survey_missing(df, missing_codes=[-99])
    assert np.isnan(res['age'].iloc[1])
    assert res['age'].iloc[0] == 20
