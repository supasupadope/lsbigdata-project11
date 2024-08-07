import numpy as np
import matplotlib.pyplot as plt
import json

geo_seoul = json.load(open("./data/SIG_Seoul.geojson", encoding="UTF-8"))

# 데이터 탐색
type(geo_seoul)
len(geo_seoul)
geo_seoul.keys()
geo_seoul["features"][0]
len(geo_seoul["features"])
len(geo_seoul["features"][0])
geo_seoul["features"][0].keys()

# 숫자가 바뀌면 "구"가 바뀌는구나!
geo_seoul["features"][2]["properties"]
geo_seoul["features"][0]["geometry"]

# 리스트로 정보 빼오기
coordinate_list=geo_seoul["features"][2]["geometry"]["coordinates"]
len(coordinate_list[0][0])
coordinate_list[0][0]

coordinate_array=np.array(coordinate_list[0][0])
x=coordinate_array[:,0]
y=coordinate_array[:,1]

plt.plot(x, y)
plt.show()
plt.clf()

# 함수로 만들기
def draw_seoul(num):
    gu_name=geo_seoul["features"][num]["properties"]["SIG_KOR_NM"]
    coordinate_list=geo_seoul["features"][num]["geometry"]["coordinates"]
    coordinate_array=np.array(coordinate_list[0][0])
    x=coordinate_array[:,0]
    y=coordinate_array[:,1]

    plt.rcParams.update({"font.family": "Malgun Gothic"})
    plt.plot(x, y)
    plt.title(gu_name)
    plt.show()
    plt.clf()
    
    return None

draw_seoul(12)


# 서울시 전체 지도 그리기
gu_name | x | y
===============
종로구  | 126 | 36
종로구  | 126 | 36
종로구  | 126 | 36
......
종로구  | 126 | 36
종로구  | 126 | 36
중구  | 126 | 36
중구  | 126 | 36
......
중구  | 126 | 36

plt.plot(x, y, hue="gu_name")
