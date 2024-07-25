# 한렬님의 생각 (무엇이 옳은가)
# 여행을 많이 가는 집단에게 광고를 하는 것: (회사, 돈을 벌어야하는 집단)
# 여행을 가지 않는 집단에게 광고를 하는 것: (정부, 공공의 이익 추구)

# 그로스 해킹: 한정된 자원을 활용할 경우 단골을 만드는 것이 더 효과적
# 비용 측면에서 기존 고객층을 유지시키는 것이 효율적

# !pip install scipy
from scipy.stats import bernoulli

# 확률질량함수(pmf)
# 확률변수가 갖는 값에 해당하는 확률을 저장하고
# 있는 함수
# bernoulli.pmf(k, p)
# P(X=1)
bernoulli.pmf(1, 0.3)
# P(X=0)
bernoulli.pmf(0, 0.3)

# 이항분포 X ~ P(X = k | n, p)
# n: 베르누이 확률변수 더한 갯수
# p: 1이 나올 확률
# binom.pmf(k, n, p)
from scipy.stats import binom

binom.pmf(0, n=2, p=0.3)
binom.pmf(1, n=2, p=0.3)
binom.pmf(2, n=2, p=0.3)


# X ~ B(n, p)
# list comp.
result=[binom.pmf(x, n=30, p=0.3) for x in range(31)]
result
# numpy
import numpy as np
binom.pmf(np.arange(31), n=30, p=0.3)


import math
math.factorial(54) / (math.factorial(26) * math.factorial(28))
math.comb(54, 26)

# ======몰라도 됨====================================
# 1*2*3*4
# np.cumprod(np.arange(1, 5))[-1]
# fact_54=np.cumprod(np.arange(1, 55))[-1]
# ln
log(a * b) = log(a) + log(b)
log(1 * 2 * 3 * 4) = log(1) + log(2) + log(3) + log(4)

np.log(24)
sum(np.log(np.arange(1, 5)))

math.log(math.factorial(54))
logf_54=sum(np.log(np.arange(1, 55)))
logf_26=sum(np.log(np.arange(1, 27)))
logf_28=sum(np.log(np.arange(1, 29)))
# math.comb(54, 26)
np.exp(logf_54 - (logf_26 + logf_28))
# =================================================

math.comb(2, 0) * 0.3**0 * (1-0.3)**2
math.comb(2, 1) * 0.3**1 * (1-0.3)**1
math.comb(2, 2) * 0.3**2 * (1-0.3)**0

# pmf: probability mass function (확률질량함수)
binom.pmf(0, 2, 0.3)
binom.pmf(1, 2, 0.3)
binom.pmf(2, 2, 0.3)

# X ~ B(n=10, p=0.36)
# P(X = 4) =?
binom.pmf(4, n=10, p=0.36)
# P(X <= 4) =?
binom.pmf(np.arange(5), n=10, p=0.36).sum()
binom.pmf(np.arange(3, 9), n=10, p=0.36).sum()

X~B(30, 0.2)
binom.pmf(np.arange(31), n=30, p=0.2).sum()
# 1
a=binom.pmf(np.arange(4), n=30, p=0.2).sum()
# 2
b=binom.pmf(np.arange(25, 31), n=30, p=0.2).sum()
a+b

# 4
1 - binom.pmf(np.arange(4, 25), n=30, p=0.2).sum()

# rvs 함수 (random variates sample)
# 표본 추출 함수
# X1 ~ Bernulli(p=0.3)
bernoulli.rvs(p=0.3)
# X2 ~ Bernulli(p=0.3)
bernoulli.rvs(p=0.3)
# X ~ B(n=2, p=0.3)
bernoulli.rvs(0.3) + bernoulli.rvs(0.3)
binom.rvs(n=2, p=0.3, size=1)
binom.pmf(0, n=2, p=0.3)
binom.pmf(1, n=2, p=0.3)
binom.pmf(2, n=2, p=0.3)

# X ~ B(30, 0.26)
# 기대값 30*0.26 = 7.8
# 표본 30개를 뽑아보세요!
binom.rvs(n=30, p=0.26, size=30)


import seaborn as sns
import matplotlib.pyplot as plt
x = np.arange(31)
prob_x = binom.pmf(x, n=30, p=0.26)

sns.barplot(prob_x)
plt.show()
plt.clf()

# 교재 p.207
import pandas as pd

x = np.arange(31)
prob_x = binom.pmf(x, n=30, p=0.26)

df = pd.DataFrame({"x": x, "prob": prob_x})
df

sns.barplot(data = df, x = "x", y = "prob")
plt.show()


# cdf: cumulative dist. function 
# (누적확률분포 함수)
# F_X(x) = P(X <= x)
binom.cdf(4, n=30, p=0.26)
binom.cdf(18, n=30, p=0.26) - binom.cdf(4, n=30, p=0.26)
binom.cdf(19, n=30, p=0.26) - binom.cdf(13, n=30, p=0.26)


# 
import numpy as np
import seaborn as sns

x_1 = binom.rvs(n=30, p=0.26, size=1)
x_1
x = np.arange(31)
prob_x = binom.pmf(x, n=30, p=0.26)
sns.barplot(prob_x, color="blue")

# Add a point at (2, 0)
plt.scatter(x_1, 0.002, color='red', zorder=100, s=10)

plt.show()
plt.clf()
