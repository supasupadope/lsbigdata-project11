import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# X ~ 균일분포 U(a, b)
# loc: a, scale: b-a
uniform.rvs(loc=2, scale=4, size=1)
uniform.pdf(3, loc=2, scale=4)
uniform.pdf(7, loc=2, scale=4)

k = np.linspace(0, 8, 100)
y = uniform.pdf(k, loc=2, scale=4)
plt.plot(k, y, color="black")
plt.show()
plt.clf()

uniform.cdf(6, loc=2, scale=4) - uniform.cdf(5, loc=2, scale=4)
uniform.ppf(0.93, loc=2, scale=4)

# 표본 20개 뽑고 표본평균 계산

x=uniform.rvs(loc=2, scale=4, size=20*1000,
              random_state=42)
x=x.reshape(-1, 20)
x.shape
blue_x=x.mean(axis=1)
blue_x
