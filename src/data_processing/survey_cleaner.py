"""
Survey Data Cleaner Module
Tailored for social science datasets (e.g., ANES, GSS, World Values Survey).
"""

from typing import Dict, List, Optional
import numpy as np
import pandas as pd


def clean_likert_scale(
    df: pd.DataFrame,
    column_name: str,
    mapping: Optional[Dict[str, float]] = None
) -> pd.DataFrame:
    """
    Converts text-based Likert scale responses into numeric values for regression analysis.

    Args:
        df: Pandas DataFrame containing the survey data.
        column_name: The name of the column to clean.
        mapping: Optional custom dictionary mapping (e.g., {'Strongly Agree': 5}).
                 Defaults to a standard 5-point scale.

    Returns:
        DataFrame with a new numeric column added (<column_name>_numeric).
    """
    if mapping is None:
        mapping = {
            'Strongly Disagree': 1.0,
            'Disagree': 2.0,
            'Neutral': 3.0,
            'Agree': 4.0,
            'Strongly Agree': 5.0,
            'Don\'t Know': np.nan,
            'Refused': np.nan
        }

    clean_col_name = f"{column_name}_numeric"
    df_copy = df.copy()
    df_copy[clean_col_name] = df_copy[column_name].map(mapping)
    return df_copy


def recode_missing_codes(
    df: pd.DataFrame,
    columns: List[str],
    missing_values: List[object] = [-99, -98, -97, "Don't Know", "Refused"]
) -> pd.DataFrame:
    """
    Recodes common survey missing response codes (-99, -98, Refused, etc.) into NaN values.

    Args:
        df: Pandas DataFrame containing survey data.
        columns: List of column names to recode missing values in.
        missing_values: List of values indicating missing/refused answers.

    Returns:
        DataFrame with specified values replaced by NaN.
    """
    df_copy = df.copy()
    for col in columns:
        if col in df_copy.columns:
            df_copy[col] = df_copy[col].replace(missing_values, np.nan)
    return df_copy


if __name__ == "__main__":
    # Simulated survey data
    data = pd.DataFrame({
        'respondent_id': [1, 2, 3, 4],
        'trust_in_gov': ['Strongly Agree', 'Disagree', 'Refused', 'Neutral']
    })

    cleaned_data = clean_likert_scale(data, 'trust_in_gov')
    print("Cleaned Survey Data:")
    print(cleaned_data)
