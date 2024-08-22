# 필요한 패키지 불러오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import os
cwd=os.getcwd()
parent_dir = os.path.dirname(cwd)
os.chdir(parent_dir)

## 필요한 데이터 불러오기
house_train=pd.read_csv("./data/houseprice/train.csv")
house_test=pd.read_csv("./data/houseprice/test.csv")
sub_df=pd.read_csv("./data/houseprice/sample_submission.csv")

## 이상치 탐색
house_train=house_train.query("GrLivArea <= 4500")

house_train.shape
house_test.shape
train_n=house_train.shape[0]

df=pd.concat([house_train, house_test],
             ignore_index=True)
df

neighborhood_dummies = pd.get_dummies(
    df["Neighborhood"],
    drop_first=True
    )
neighborhood_dummies

x=pd.concat([df[["GrLivArea", "GarageArea"]], 
            neighborhood_dummies], axis=1)

y=df["SalePrice"]

train_x=x.iloc[:train_n,]
test_x=x.iloc[train_n:,]
train_y=y[:train_n]

# Validation 셋(모의고사 셋) 만들기
np.random.seed(42)
val_index=np.random.choice(np.arange(train_n), size=438, replace=False)
val_index

valid_x=train_x.loc[val_index]  # 30%
train_x=train_x.drop(val_index) # 70%
valid_y=train_y[val_index]      # 30%
train_y=train_y.drop(val_index) # 70%

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(train_x, train_y)  # 자동으로 기울기, 절편 값을 구해줌

# 성능 측정 ()
y_hat=model.predict(valid_x)
np.sqrt(np.mean((valid_y-y_hat)**2))

38986



pred_y=model.predict(test_x) # test 셋에 대한 집값
pred_y

# SalePrice 바꿔치기
sub_df["SalePrice"] = pred_y
sub_df

# csv 파일로 내보내기
sub_df.to_csv("./data/houseprice/sample_submission10.csv", index=False)

