import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x, y의 값을 정의합니다 (-1에서 7까지)
x = np.linspace(-1, 7, 400)
y = np.linspace(-1, 7, 400)
x, y = np.meshgrid(x, y)

# 함수 f(x, y)를 계산합니다.
z = (x - 3)**2 + (y - 4)**2 + 3

# 그래프를 그리기 위한 설정
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 표면 그래프를 그립니다.
ax.plot_surface(x, y, z, cmap='viridis')

# 레이블 및 타이틀 설정
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.set_title('Graph of f(x, y) = (x-3)^2 + (y-4)^2 + 3')

# 그래프 표시
plt.show()
