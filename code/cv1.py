import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import uniform
from sklearn.linear_model import LinearRegression

# 20차 모델 성능을 알아보자
np.random.seed(2024)
x = uniform.rvs(size=30, loc=-4, scale=8)
y = np.sin(x) + norm.rvs(size=30, loc=0, scale=0.3)

import pandas as pd
df = pd.DataFrame({
    "y" : y,
    "x" : x
})
df

for i in range(2, 21):
    df[f"x{i}"] = df["x"] ** i

df

myindex=np.random.choice(30, 30, replace=False)

myindex[0:10]
myindex[10:20]
myindex[20:30]

df.loc[myindex[0:10]]
df.drop(myindex[0:10])

fold_num=0
fold_num=1
def make_tr_val(fold_num, df, cv_num=3):
    np.random.seed(2024)
    myindex=np.random.choice(30, 30, replace=False)

    # valid index
    val_index=myindex[(10*fold_num):(10*fold_num+10)]

    # valid set, train set
    valid_set=df.loc[val_index]
    train_set=df.drop(val_index)

    train_X=train_set.iloc[:,1:]
    train_y=train_set.iloc[:,0]

    valid_X=valid_set.iloc[:,1:]
    valid_y=valid_set.iloc[:,0]

    return (train_X, train_y, valid_X, valid_y)

train_X, train_y, valid_X, valid_y = make_tr_val(fold_num=0, df=df)
train_X
train_y
valid_X
valid_y

from sklearn.linear_model import Lasso

# 결과 받기 위한 벡터 만들기
val_result=np.repeat(0.0, 100)
tr_result=np.repeat(0.0, 100)

for i in np.arange(0, 100):
    model= Lasso(alpha=i*0.01)
    model.fit(train_X, train_y)

    # 모델 성능
    y_hat_train = model.predict(train_X)
    y_hat_val = model.predict(valid_X)

    perf_train=sum((train_y - y_hat_train)**2)
    perf_val=sum((valid_y - y_hat_val)**2)
    tr_result[i]=perf_train
    val_result[i]=perf_val

tr_result
val_result





















