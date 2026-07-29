"""
03_statistical_analysis / 03_summary_table_exporter.py
【将回归结果导出为学术论文表格】
帮助社科生将 Python 回归结果直接转为 Markdown 表格放入论文中。
"""

import importlib
import pandas as pd


def export_coefficients_table(model_results) -> pd.DataFrame:
    """提取回归系数、标准误、t值与p值生成简洁表格"""
    summary_df = pd.DataFrame({
        'Coefficient': model_results.params,
        'Std Err': model_results.bse,
        'p-value': model_results.pvalues
    })
    summary_df['Significance'] = summary_df['p-value'].apply(
        lambda p: '***' if p < 0.001 else ('**' if p < 0.01 else ('*' if p < 0.05 else ''))
    )
    return summary_df


if __name__ == "__main__":
    ols_module = importlib.import_module("03_statistical_analysis.01_ols_regression")
    run_robust_ols = ols_module.run_robust_ols

    data = pd.DataFrame({
        'y': [10, 20, 25, 30, 42, 50],
        'x': [1, 2, 3, 4, 5, 6]
    })
    res = run_robust_ols(data, 'y ~ x')
    table = export_coefficients_table(res)
    print("Markdown 格式论文表格：")
    print(table.to_markdown())
