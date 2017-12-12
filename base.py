import pandas as pd
from scipy.spatial import distance
# 最小邻近距离
R = 30
# 参与度
min_prev = 0.3
two_prev = []
F_I_count = {}

data = pd.read_table("D:\data1.txt", header=None)
df = pd.DataFrame(data)
df.columns = ["Instance", "Feature", "X", "Y"]

# 统计特征的数量


def get_count(dt):
    for i in range(len(dt)):
        if dt.ix[i, "Feature"] in F_I_count.keys():
            F_I_count[df.ix[i, "Feature"]] += 1
        else:
            F_I_count[df.ix[i, "Feature"]] = 1
    return F_I_count
print(get_count(df))

# 生成2阶的频繁模式


def two_pattern(dt):
    near = []
    for i in range(len(dt)):
        for j in range(i+1, len(dt)):
            dict_near = {}
            if dt.ix[i, "Feature"] != dt.ix[j, "Feature"]:
                try:
                    x1 = float(dt.ix[i, "X"])
                    y1 = float(dt.ix[i, "Y"])
                    x2 = float(dt.ix[j, "X"])
                    y2 = float(dt.ix[j, "Y"])
                except (TypeError, ValueError) as e:
                    print(e)
                if distance.euclidean((x1, y1), (x2, y2)) <= R:
                    dict_near[dt.ix[i, "Feature"]] = dt.ix[i, "Instance"]
                    dict_near[dt.ix[j, "Feature"]] = dt.ix[j, "Instance"]
                    near.append(dict_near)
    dt2 = pd.DataFrame(near)
    p2 = []
    for i in range(len(dt2.columns)):
        for j in range(i + 1, len(dt2.columns)):
            tmp = list()
            tmp.append(dt2.icol(i))
            tmp.append(dt2.icol(j))
            p2.append(pd.DataFrame(tmp))

    for i in range(len(p2)):
        p2[i] = p2[i].dropna(axis=1, how='any')

    for i in range(len(p2)):
        p2[i] = p2[i].T
        p2[i].index = range(len(p2[i]))

    for i in reversed(range(len(p2))):
        dict_pi = {}
        tem = list(p2[i].columns)
        pi = []
        for j in tem:
            dict_pi[j] = len(set(p2[i][j])) / F_I_count[j]
            pi.append(len(set(p2[i][j])) / F_I_count[j])
        t = min(pi)
        if t < min_prev:
            del p2[i]
        else:
            two_prev.append(dict_pi)
    return p2

print(two_pattern(df))
