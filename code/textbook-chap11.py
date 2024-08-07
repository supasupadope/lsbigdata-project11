import json

geo_seoul = json.load(open("./data/SIG_Seoul.geojson", encoding="UTF-8"))


type(geo_seoul)
len(geo_seoul)
geo_seoul.keys()
geo_seoul["features"][0]
len(geo_seoul["features"])
len(geo_seoul["features"][0])
geo_seoul["features"][0].keys()
geo_seoul["features"][0]["properties"]
geo_seoul["features"][0]["geometry"]


coordinate_list=geo_seoul["features"][0]["geometry"]["coordinates"]
len(coordinate_list[0][0])
coordinate_list[0][0]


import numpy as np
coordinate_array=np.array(coordinate_list[0][0])
x=coordinate_array[:,0]
y=coordinate_array[:,1]




