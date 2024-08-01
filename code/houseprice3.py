# 직선의 방정식
# y = ax + b
# y=x+2
# 예: y = 2x + 3 의 그래프를 그려보세요!
a = 1
b = 0

x = np.linspace(-5, 5, 100)
y = a * x + b

import numpy as np
import matplotlib.pyplot as plt

plt.plot(x, y, color="blue")
plt.axvline(0, color="black")
plt.axhline(0, color="black")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
plt.clf()

import pandas as pd

a = 80
b = 5

x = np.linspace(0, 5, 100)
y = a * x + b

house_train=pd.read_csv("./data/houseprice/train.csv")
my_df=house_train[["BedroomAbvGr", "SalePrice"]].head(10)
my_df["SalePrice"]=my_df["SalePrice"] /1000
plt.scatter(x=my_df["BedroomAbvGr"], y=my_df["SalePrice"])
plt.plot(x, y, color="blue")
plt.show()
plt.clf()

y = 70 * x + 10
방 1개 집값: 8천만
방 2개 집값: 1억 5천
방 3개 집값: 2억 2천
방 4개 집값: 2억 9천
방 5개 집값: 3억 6천
# 1조: (70, 10) - 0.52186
# 2조: (12, 170) - 0.46138
# 3조: (53, 45) - 0.40613
# 4조: (36, 68) - 0.42609
# 5조: (80, -30) - 0.69897
# 6조: (47, 63) - 0.46078
# 7조: (63, 100) - 1.376

# 테스트 집 정보 가져오기
house_test=pd.read_csv("./data/houseprice/test.csv")
a=70; b=10
(a * house_test["BedroomAbvGr"] + b) * 1000

# sub 데이터 불러오기
sub_df=pd.read_csv("./data/houseprice/sample_submission.csv")
sub_df

# SalePrice 바꿔치기
sub_df["SalePrice"] = (a * house_test["BedroomAbvGr"] + b) * 1000
sub_df


# 직선을 구하는 방법


sub_df.to_csv("./data/houseprice/sample_submission3.csv", index=False)






