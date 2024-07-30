# !pip install pyreadstat
import pandas as pd
import numpy as np
import seaborn as sns

raw_welfare=pd.read_spss("./data/koweps/Koweps_hpwc14_2019_beta2.sav")
raw_welfare

welfare=raw_welfare.copy()
welfare.shape
welfare.describe()

welfare=welfare.rename(
    columns = {
        "h14_g3": "sex",
        "h14_g4": "birth",
        "h14_g10": "marriage_type",
        "h14_g11": "religion",
        "p1402_8aq1": "income",
        "h14_eco9": "code_job",
        "h14_reg7": "code_region"
    }
)

welfare=welfare[["sex", "birth", "marriage_type",
                "religion", "income", "code_job", "code_region"]]
welfare.shape

welfare["sex"].dtypes
welfare["sex"].value_counts()
# welfare["sex"].isna().sum()

welfare["sex"] = np.where(welfare["sex"] == 1,'male', 'female')
welfare["sex"].value_counts()


welfare["income"].describe()
welfare["income"].isna().sum()

sex_income=welfare.dropna(subset="income") \
                  .groupby("sex", as_index=False) \
                  .agg(mean_income = ("income", "mean"))

sex_income

import seaborn as sns

sns.barplot(data=sex_income, x="sex", y="mean_income",
            hue="sex")
plt.show()
plt.clf()

# 숙제: 위 그래프에서 각 성별 95% 신뢰구간 계산후 그리기
# 위 아래 검정색 막대기로 표시

welfare["birth"].describe()
sns.histplot(data=welfare, x="birth")
plt.show()
plt.clf()

welfare["birth"].isna().sum()

welfare=welfare.assign(age = 2019 - welfare["birth"] + 1)
welfare["age"]
sns.histplot(data=welfare, x="age")
plt.show()
plt.clf()

age_income=welfare.dropna(subset="income") \
                    .groupby("age", as_index=False) \
                    .agg(mean_income = ("income", "mean"))

sns.lineplot(data=age_income, x="age", y="mean_income")
plt.show()
plt.clf()

# 나이별 income 칼럼 na 개수 세기!
welfare["income"].isna().sum()

welfare["income"].isna()
my_df=welfare.assign(income_na=welfare["income"].isna()) \
                        .groupby("age", as_index=False) \
                        .agg(n = ("income_na", "sum"))


sns.barplot(data = my_df, x="age", y="n")
plt.show()
plt.clf()

# 나이대별 수입 분석
# cut
bin_cut=np.array([0, 9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119])
welfare=welfare.assign(age_group = pd.cut(welfare["age"], 
                bins=bin_cut, 
                labels=(np.arange(12) * 10).astype(str) + "대"))

age_income=welfare.dropna(subset="income") \
                    .groupby("age_group", as_index=False) \
                    .agg(mean_income = ("income", "mean"))

age_income
sns.barplot(data=age_income, x="age_group", y="mean_income")
plt.show()
plt.clf()

welfare
sex_age_income = \
    welfare.dropna(subset="income") \
    .groupby(["age_group", "sex"], as_index=False) \
    .agg(mean_income=("income", "mean"))
    
    
