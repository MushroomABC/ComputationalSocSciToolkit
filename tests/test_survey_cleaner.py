"""
Unit tests for Survey Data Cleaning module.
"""

import sys
import os

# Add parent directory to sys.path to enable imports when executing pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
import numpy as np
from src.data_processing.survey_cleaner import clean_likert_scale, recode_missing_codes


def test_clean_likert_scale():
    df = pd.DataFrame({
        'trust': ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree', 'Refused']
    })
    cleaned = clean_likert_scale(df, 'trust')
    assert 'trust_numeric' in cleaned.columns
    assert cleaned['trust_numeric'].iloc[0] == 1.0
    assert cleaned['trust_numeric'].iloc[4] == 5.0
    assert np.isnan(cleaned['trust_numeric'].iloc[5])


def test_recode_missing_codes():
    df = pd.DataFrame({'age': [25, 30, -99, 45]})
    cleaned = recode_missing_codes(df, ['age'], missing_values=[-99])
    assert np.isnan(cleaned['age'].iloc[2])
    assert cleaned['age'].iloc[0] == 25
