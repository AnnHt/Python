import pandas as pd
from scipy.spatial import distance
# 定义聚类半径R
r = 100
data = []
for line in open("d:\\alive0.sign"):
    ls = line.split()
    data.append(ls)
print(data)
# print(data)
# dt = pd.DataFrame(data)
# print(dt)
#
#
# def get_distance(df):
#     # 1 means Instance;2 means feature; 3 means X;4 means Y
#     dist_exp = pd.DataFrame(columns=range(5))
#     for i in range(len(df)):
#         for j in range(i + 1, len(df)):
#             if df.ix[i, 1] != df.ix[j, 1]:
#                 x1 = float(df.ix[i, 2])
#                 y1 = float(df.ix[i, 3])
#                 x2 = float(df.ix[j, 2])
#                 y2 = float(df.ix[j, 3])
#                 dt = distance.euclidean((x1, y1), (x2, y2))
#                 tem = pd.Series(
#                     [df.ix[i, 0], df.ix[i, 1], df.ix[j, 0], df.ix[j, 1], dt])
#                 dist_exp = dist_exp.append(tem, ignore_index=True)
#     return dist_exp
# dist = get_distance(dt)
# print(dist)


# df = pd.DataFrame(data)
# df.columns = range(len(df.columns))
# print(df)