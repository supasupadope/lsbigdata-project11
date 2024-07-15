import numpy as np

# 벡터 슬라이싱 예제, a를 랜덤하게 채움
np.random.seed(2024)

a = np.random.randint(1, 21, 10)
print(a)

# 두 번째 값 추출
print(a[1])

a[::2]
a[-2] # 맨 끝에서 두번째
a[0:6:2]

# 1에서부터 1000사이 3의 배수의 합은?
sum(np.arange(3, 1001, 3))
x = np.arange(3, 1001)
sum(x[::3])
