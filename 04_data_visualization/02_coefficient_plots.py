"""
04_data_visualization / 02_coefficient_plots.py
【绘制回归系数与 95% 置信区间图 (Coefficient Plot)】
社科学术论文中非常流行的回归效果可视化方法。
"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_regression_coefficients(coef_data: pd.DataFrame, title="Regression Coefficients"):
    """
    绘制系数点图与置信区间
    coef_data 需包含列: ['var_name', 'coef', 'ci_lower', 'ci_upper']
    """
    fig, ax = plt.subplots(figsize=(7, 4))
    y_pos = range(len(coef_data))

    ax.errorbar(
        coef_data['coef'], y_pos,
        xerr=[coef_data['coef'] - coef_data['ci_lower'], coef_data['ci_upper'] - coef_data['coef']],
        fmt='o', color='#2b5c8f', ecolor='#2b5c8f', elinewidth=2, capsize=4
    )

    ax.axvline(0, color='red', linestyle='--', alpha=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(coef_data['var_name'])
    ax.set_xlabel("Estimate (95% CI)")
    ax.set_title(title)
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    sample_coefs = pd.DataFrame({
        'var_name': ['Education', 'Age', 'Income (log)', 'Urban Resident'],
        'coef': [0.45, 0.12, 0.85, -0.20],
        'ci_lower': [0.20, 0.02, 0.50, -0.45],
        'ci_upper': [0.70, 0.22, 1.20, 0.05]
    })
    fig = plot_regression_coefficients(sample_coefs, "Determinants of Civic Participation")
    print("系数图生成成功！")
