import pandas as pd
import numpy as np
from palmerpenguins import load_penguins

penguins = load_penguins()
penguins.head()

# 펭귄 분류 문제
# y: 펭귄의 종류
# x1: bill_length_mm (부리 길이)
# x2: bill_depth_mm (부리 깊이)

df=penguins.dropna()
df=df[["species", "bill_length_mm", "bill_depth_mm"]]
df=df.rename(columns={
    'species': 'y',
    'bill_length_mm': 'x1',
    'bill_depth_mm': 'x2'})
df

# x1, x2 산점도를 그리되, 점 색깔은 펭귄 종별 다르게 그리기!
import seaborn as sns

sns.scatterplot(data=df, x="x1", y="x2", hue='y')
plt.axvline(x=42.4)

# Q. 나누기 전 현재의 엔트로피?
# Q. 45로 나눴을때, 엔트로피 평균은 얼마인가요?
# 입력값이 벡터 -> 엔트로피!
p_i=df['y'].value_counts() / len(df['y'])
entropy_curr=-sum(p_i * np.log2(p_i))

# x1=45 기준으로 나눈 후, 평균 엔트로피 구하기!
# x1=45 기준으로 나눴을때, 데이터포인트가 몇개 씩 나뉘나요?
np.sort(df['x1'].unique())
n1=df.query("x1 < 42.4").shape[0]  # 1번 그룹
n2=df.query("x1 >= 42.4").shape[0] # 2번 그룹

def entropy(col):
    entropy_i = []
    for i in range(len(df[col].unique())):
        df_left = df[df[col]< df[col].unique()[i]]
        df_right = df[df[col]>= df[col].unique()[i]]
        info_df_left = df_left[['y']].value_counts() / len(df_left)
        info_df_right = df_right[['y']].value_counts() / len(df_right)
        after_e_left = -sum(info_df_left*np.log2(info_df_left))
        after_e_right = -sum(info_df_right*np.log2(info_df_right))
        entropy_i.append(after_e_left * len(df_left)/len(df) + after_e_right * len(df_right)/len(df))
    return entropy_i

entropy_df = pd.DataFrame({
    'standard': df['x1'].unique(),
    'entropy' : entropy('x1')
    })

entropy_df.iloc[np.argmin(entropy_df['entropy']),:]

# standard    16.400000
# entropy      0.834074

# standard    42.400000
# entropy      0.804269
# x1, 42.4 선택: 엔트로피가 더 낮음!