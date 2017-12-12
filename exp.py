import numpy as np
from numpy import *
import matplotlib.pyplot as plt

# 实例的总数
Num = 9
# 特征的范围
F_count = 4
# 坐标的范围
Max_dis = 100

data = []
for i in range(Num):
    dict_tmp = {}
    f = random.randint(0, 4)
    dict_tmp["Feature"] = chr(65+f)
    dict_tmp["X"] = random.randint(0, 100)
    dict_tmp["Y"] = random.randint(0, 100)
    data.append(dict_tmp)

g1 = plt.figure(1)
for dt in data:
    if dt["Feature"] == "A":
        plt.scatter(int(dt["X"]), int(dt["Y"]), label="A", marker="s", color="b", s=30)
    if dt["Feature"] == "B":
        plt.scatter(int(dt["X"]), int(dt["Y"]), label="B", marker="^", color="r", s=30)
    if dt["Feature"] == "C":
        plt.scatter(int(dt["X"]), int(dt["Y"]), label="C", marker="v", color="c", s=30)
    if dt["Feature"] == "D":
        plt.scatter(int(dt["X"]), int(dt["Y"]), label="D", marker=">", color="m", s=30)
plt.legend()
plt.show()


# x1 = np.random.randn(1, 2)
# x2 = np.random.randn(1, 2)
# x = np.random.randn(4, 4)
# y = np.random.randn(4, 4)
# mark = ['s', 'o', '^', 'v', '>', '<', 'd', 'p', 'h', '8', '+', '*']
# for i in range(0, 4):
#     plt.scatter(x[i], y[i], marker=mark[i], color=(np.random.rand(1, 3)), s=50, label=chr(i+65))
# plt.legend()
# plt.show()
