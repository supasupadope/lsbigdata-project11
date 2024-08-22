import numpy as np
import matplotlib.pyplot as plt

# y = ax^2 + bx + c 그래프 그리기
a=1
b=0
c=-10
d=0
e=10
x = np.linspace(-4, 4, 1000)
# y = a * x**3 + b*x**2 + c*x + d
y = a * x**4 + b*x**3 + c*x**2 + d*x + e

plt.plot(x, y, color="black")