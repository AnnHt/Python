import pandas as pd
import numpy as np
# import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.datasets import load_boston
# from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
data = pd.read_csv("D:\POI_dis1.csv")
df = pd.DataFrame(data)
df.columns = range(len(df.columns))
print(df)

sp_dict = {'F': 17, 'C': 17, 'Q': 1, 'L': 51, 'D': 3, 'H': 10, 'G': 15, 'B': 23, 'J': 7, 'N': 10,
           'A': 43, 'R': 4, 'I': 16, 'O': 5, 'K': 67, 'M': 10, 'P': 26, 'E': 50}


def dis_count(dt):
    # 用来存距离的数组
    dis = dict()
    m = max(dt.icol(5))/1000
    for i in range(len(dt)):
        t = round(dt.ix[i, 5] / m)
        if t == 0:
            t = 1
        if m*t in dis.keys():
            dis[m*t].append(dt.ix[i, 5])
        else:
            tmp = list()
            tmp.append(dt.ix[i, 5])
            dis[m*t] = tmp
    return dis
dis = dict()
dis = dis_count(df)
print(dis)

X = []
Y = []

for key in sorted(dis.keys()):
    X.append(key)
for i in range(len(X)):
    Y.append(len(dis[X[i]]))
print(X)
print(Y)

fig = plt.figure()
plt.bar(X, Y, 20, color="red")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("count")
plt.show()

fig2 = plt.figure()
X = np.array(X)
X = [[x] for x in X]
y = np.array(Y)
# rng = np.random.RandomState(1)
# X = np.linspace(0, 6, 100)[:, np.newaxis]
# y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
print(len(X), len(y))
print(X)
print(y)
regr_1 = DecisionTreeRegressor(max_depth=10)
m = regr_1.fit(X, y)
print(m)
y_1 = regr_1.predict(X)
plt.figure()
plt.scatter(X, y, c="k", label="training samples")
plt.plot(X, y_1, c="g", label="n_estimators=1", linewidth=2)
plt.legend()
plt.show()

xmax = max(df.icol(5))

# 计算曲线的面积
s = 0
dx = 0
while dx <= xmax:
    s += 100 * m.predict([[dx]])
    dx += 100

print(s)

# 计算特征损失率的函数


def loss_feature(d1, d2):
    loss_dict = {}
    for i in range(len(df)):
        if (float(df.ix[i, 5]) >= d1) and (float(df.ix[i, 5]) <= d2):
            if df.ix[i, 2] in loss_dict.keys():
                loss_dict[df.ix[i, 2]].add(df.ix[i, 1])
            else:
                tmp = set()
                tmp.add(df.ix[i, 1])
                loss_dict[df.ix[i, 2]] = tmp
            if df.ix[i, 4] in loss_dict.keys():
                loss_dict[df.ix[i, 4]].add(df.ix[i, 3])
            else:
                tmp = set()
                tmp.add(df.ix[i, 3])
                loss_dict[df.ix[i, 4]] = tmp
    ls = 0
    for i in loss_dict.keys():
        ls += len(loss_dict[i])/float(sp_dict[i])
    return ls

# 定义p
p = 0.3
ds = 0
pi = 0
dt = 0
while pi <= p:
    ds += 100 * m.predict([[dt]])
    pi = ds/s
    dt += 100

dx1 = dt

ds = 0
pi = 0
dt = xmax
while pi <= p:
    ds += 100 * m.predict([[dt]])
    pi = ds/s
    dt -= 100

dx2 = dt
print(dx2)
pi = 1 - 2*p
while (pi <= 1 - p) & (dx1 > 0):
    if loss_feature(dx1-100, dx1) > loss_feature(dx2, dx2+100):
        dx1 -= 100
        pi += 100 * m.predict([[dx1-100]])/s
    else:
        dx2 += 100
        pi += 100 * m.predict([[dx2+100]])/s

print(dx1, dx2, xmax)