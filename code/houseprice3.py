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







