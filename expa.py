from random import choice
import pandas as pd
from scipy.spatial import distance

# 统计抽样比率
SI = 0.001
data = pd.read_csv("D:\POI.csv", header=None)
df = pd.DataFrame(data)
df.columns = ["Instance", "Feature", "X", "Y"]
# df.to_csv("D:\POI1.csv")


def sample(dt):
    # 统计特征中的实例的数量
    f_count = {}
    for i in range(len(dt)):
        if dt.ix[i, "Feature"] in f_count.keys():
            f_count[dt.ix[i, "Feature"]] += 1
        else:
            f_count[dt.ix[i, "Feature"]] = 1
    # 抽样数据集
    st = list()
    for i in f_count.keys():
        m = int(f_count[i]*SI)
        j = 0
        while j < m:
            t = choice(range(len(dt)))
            if i == dt.ix[t, "Feature"]:
                st.append(dt.irow(t))
                j += 1
    sp = pd.DataFrame(st)
    sp.index = range(len(sp))
    return sp
sp = sample(df)
print(sp)
# 统计样本中的特征数量
sp_dict = {}
for i in range(len(sp)):
    if sp.ix[i, "Feature"] in sp_dict.keys():
        sp_dict[sp.ix[i, "Feature"]] += 1
    else:
        sp_dict[sp.ix[i, "Feature"]] = 1
print(sp_dict)

def get_distance(df):
    dis = pd.DataFrame(columns=range(5))
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            if df.ix[i, "Feature"] != df.ix[j, "Feature"]:
                x1 = df.ix[i, "X"]
                y1 = df.ix[i, "Y"]
                x2 = df.ix[j, "X"]
                y2 = df.ix[j, "Y"]
                dt = distance.euclidean((x1, y1), (x2, y2))
                tem = pd.Series(
                    [df.ix[i, "Instance"], df.ix[i, "Feature"], df.ix[j, "Instance"], df.ix[j, "Feature"], dt])
                dis = dis.append(tem, ignore_index=True)
    return dis
dis = get_distance(sp)

dis.to_csv("D:\POI_dis1.csv")
