"""
04_data_visualization / 03_demographic_charts.py
【人口特征分组柱状图】
社会科学报告中常用的人口结构与比例展示图。
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_group_proportions(df: pd.DataFrame, group_col: str, category_col: str):
    """绘制分组百分比柱状图"""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    sns.barplot(data=df, x=group_col, y=category_col, palette="Set2", ax=ax)
    ax.set_ylabel("Proportion (%)")
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    df = pd.DataFrame({
        'Region': ['East', 'West', 'North', 'South'],
        'Voter Turnout %': [68.5, 62.1, 71.0, 59.4]
    })
    fig = plot_group_proportions(df, 'Region', 'Voter Turnout %')
    print("分组比例柱状图生成成功！")
