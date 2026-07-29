"""
Quickstart Demo: Computational Social Science Workflow
Demonstrates data cleaning, modeling, and plotting using the ComputationalSocSciToolkit.
"""

import sys
import os

# Add parent directory to sys.path to enable imports when executing standalone script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
from src.data_processing.survey_cleaner import clean_likert_scale, recode_missing_codes
from src.modeling.regression_models import fit_ols_model


def main():
    print("=== Computational Social Science Toolkit Demo ===")

    # 1. Simulate survey response data
    raw_data = pd.DataFrame({
        'respondent_id': range(1, 6),
        'trust_in_media': ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Refused'],
        'income': [50000, 62000, 48000, -99, 71000],
        'civic_engagement': [4, 5, 3, 2, 5]
    })

    print("\n--- 1. Raw Survey Data ---")
    print(raw_data)

    # 2. Clean Likert scales and missing codes
    cleaned_df = clean_likert_scale(raw_data, 'trust_in_media')
    cleaned_df = recode_missing_codes(cleaned_df, ['income'], missing_values=[-99])

    print("\n--- 2. Cleaned Survey Data ---")
    print(cleaned_df[['respondent_id', 'trust_in_media_numeric', 'income', 'civic_engagement']])

    # 3. Fit regression model
    valid_df = cleaned_df.dropna(subset=['trust_in_media_numeric', 'income', 'civic_engagement'])
    results = fit_ols_model(valid_df, 'civic_engagement ~ trust_in_media_numeric + income')

    print("\n--- 3. Regression Results Summary ---")
    print(results.summary())


if __name__ == "__main__":
    main()
