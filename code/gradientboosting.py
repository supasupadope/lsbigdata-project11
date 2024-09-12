# GBRT

import numpy as np
from sklearn.tree import DecisionTreeRegressor

np.random.seed(42)
X = np.random.rand(100) - 0.5
y = 3 * X**2 + 0.05*np.random.randn(100)
X=X.reshape(100,1)

tree_model1=DecisionTreeRegressor(max_depth=2)
tree_model1.fit(X, y)

y2=y-tree_model1.predict(X)
tree_model2=DecisionTreeRegressor(max_depth=2)
tree_model2.fit(X, y2)

y3=y-tree_model1.predict(X)
tree_model3=DecisionTreeRegressor(max_depth=2)
tree_model3.fit(X, y3)

# 새로운 데이터
X_new=np.array([[0.5], [-0.7], [0.2]])
