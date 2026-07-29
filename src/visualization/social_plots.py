"""
Social Science Data Visualization Module
Provides clean, publication-ready visualization helpers for academic papers and policy briefs.
"""

from typing import Optional
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def set_social_science_style():
    """Configures global matplotlib and seaborn styles for social science publishing."""
    sns.set_theme(style="whitegrid", font="sans-serif")
    plt.rcParams.update({
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.titlesize': 16
    })


def plot_coefficient_effect(
    coef_df: pd.DataFrame,
    title: str = "Regression Coefficients (95% CI)",
    save_path: Optional[str] = None
):
    """
    Plots coefficient point estimates and confidence intervals for regression models.

    Args:
        coef_df: DataFrame with columns ['variable', 'coef', 'ci_lower', 'ci_upper'].
        title: Plot title.
        save_path: Optional path to save the generated plot.
    """
    set_social_science_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    y_pos = range(len(coef_df))
    ax.errorbar(
        coef_df['coef'], y_pos,
        xerr=[coef_df['coef'] - coef_df['ci_lower'], coef_df['ci_upper'] - coef_df['coef']],
        fmt='o', color='#1f77b4', ecolor='#1f77b4', elinewidth=2, capsize=4
    )

    ax.axvline(0, color='red', linestyle='--', linewidth=1)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(coef_df['variable'])
    ax.set_xlabel("Estimate (95% Confidence Interval)")
    ax.set_title(title)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300)

    return fig, ax
