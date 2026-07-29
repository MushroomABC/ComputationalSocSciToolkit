"""
01_getting_started / 02_python_basics_for_socsci.py
【社科生必懂的 Python 基础数据类型】
用社会科学的概念解释 Python 基础变量。
"""

# 1. 文本变量 (String) - 例如：受访者回答、政党名称
respondent_party = "Democratic Party"
print(f"受访者政党倾向: {respondent_party}")

# 2. 数值变量 (Integer / Float) - 例如：年龄、家庭年收入
respondent_age = 28
household_income = 65000.50
print(f"受访者年龄: {respondent_age}, 家庭收入: ${household_income}")

# 3. 字典 (Dictionary) - 例如：问卷代码对照表 (Codebook)
gender_codebook = {
    1: "Male",
    2: "Female",
    9: "Refused/Missing"
}
print(f"问卷代码 1 代表: {gender_codebook[1]}")

# 4. 列表 (List) - 例如：一组变量名列表
survey_variables = ["age", "gender", "education", "income", "trust_in_gov"]
print(f"本次调查包含的变量数量: {len(survey_variables)}")
