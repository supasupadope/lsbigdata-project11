import pandas as pd
import numpy as np

old_seat=np.arange(1, 29)


np.random.seed(20240729)
# 1~28 숫자 중에서 중복 없이 28개 숫자를 뽑는 방법
new_seat=np.random.choice(old_seat, 28, replace=False)

result=pd.DataFrame(
    {"old_seat": old_seat,
     "new_seat": new_seat}
)

result.to_csv(result, "result.csv")


# y=2x 그래프 그리기
# 점을 직선으로 이어서 표현
import matplotlib.pyplot as plt

x = np.linspace(0, 8, 2)
y = 2 * x
# plt.scatter(x, y, s=3)
plt.plot(x, y, color="black")
plt.show()
plt.clf()

# y = x^2 를 점 3개 사용해서 그리기
x = np.linspace(-8, 8, 100)
y = x**2
# plt.scatter(x, y, s=3)
plt.plot(x, y, color="black")

# x, y 축 범위 설정
plt.xlim(-10, 10)
plt.ylim(0, 40)
# 비율 맞추기
# plt.axis('equal')는 xlim, ylim과 같이 사용 x
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
plt.clf()



