# y=2x+3 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# x 값의 범위 설정
x = np.linspace(0, 100, 400)

# y 값 계산
y = 2 * x + 3

np.random.seed(20240805)
obs_x=np.random.choice(np.arange(100), 20)
epsilon_i=norm.rvs(loc=0, scale=20, size=20)
obs_y = 2*obs_x+3 + epsilon_i


# 그래프 그리기
plt.plot(x, y, label='y = 2x + 3', color="black")
plt.scatter(obs_x, obs_y, color="blue", s=3)
plt.show()
plt.clf()
