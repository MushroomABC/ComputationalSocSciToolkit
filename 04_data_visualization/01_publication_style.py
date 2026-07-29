"""
04_data_visualization / 01_publication_style.py
【一键设置学术期刊配色与字体风格】
设定适合社科学术期刊排版（如 ASR, APSR, AJPS）的 Plot 样式。
"""

import matplotlib.pyplot as plt
import seaborn as sns


def apply_academic_style():
    """应用简洁清晰的学术可视化风格"""
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 13,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.titlesize': 14,
        'figure.dpi': 300
    })
    print("已成功加载社科学术绘图风格！")


if __name__ == "__main__":
    apply_academic_style()
