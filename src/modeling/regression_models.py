"""
Statistical Modeling Module for Computational Social Science
Provides helper functions for common statistical models in social science (OLS, Logit, Fixed Effects).
"""

from typing import List, Optional
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


def fit_ols_model(
    df: pd.DataFrame,
    formula: str,
    cov_type: str = 'HC1'
) -> sm.regression.linear_model.RegressionResultsWrapper:
    """
    Fits an Ordinary Least Squares (OLS) regression with robust standard errors.

    Args:
        df: Pandas DataFrame containing data.
        formula: Statsmodels formula string (e.g., 'income ~ education + age').
        cov_type: Covariance estimator (default 'HC1' for heteroskedasticity-robust standard errors).

    Returns:
        Fitted Statsmodels regression result object.
    """
    model = smf.ols(formula, data=df)
    results = model.fit(cov_type=cov_type)
    return results


def fit_logit_model(
    df: pd.DataFrame,
    formula: str
) -> sm.discrete.discrete_model.BinaryResultsWrapper:
    """
    Fits a Logistic Regression model for binary outcomes (e.g., voter turnout, survey participation).

    Args:
        df: Pandas DataFrame.
        formula: Statsmodels formula string (e.g., 'voted ~ income + education').

    Returns:
        Fitted Logistic regression result object.
    """
    model = smf.logit(formula, data=df)
    results = model.fit(disp=False)
    return results
