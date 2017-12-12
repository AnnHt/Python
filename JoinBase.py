from scipy.spatial import distance
import operator
import pandas as pd
# data可以表示一阶的表实例
data = []
# 邻近关系的距离表示
R = 30
# 最小支持度阈值
min_prev = 0.3
# 粗糙表实例
Rough_table_instance = []
# 统计每一个特征的实例数量
Feature_ins_count = dict()
# 计算模式中参与度的值
pattern_prev = dict()

fin = open("D:\data1.txt", "r", encoding="utf8")
while True:
    dict_temp = dict()
    line = fin.readline()
    row = list()
    if line:
        line = line.strip()
        row = line.split("\t")
        dict_temp["feature"] = row[1]
        dict_temp["instance"] = row[0]
        dict_temp["x"] = row[2]
        dict_temp["y"] = row[3]
        data.append(dict_temp)
    else:
        break
fin.close()

data.sort(key=operator.itemgetter("feature"))
# 统计所有的特征的实例的总数
for i in data:
    if i["feature"] not in Feature_ins_count.keys():
        Feature_ins_count[i["feature"]] = 1
    else:
        Feature_ins_count[i["feature"]] += 1

print(Feature_ins_count)
# for i in data:
#    print(i)
data.remove(data[1])
print(len(data))
frame = pd.DataFrame(data)

print(frame)

E = sorted(list(Feature_ins_count.keys()))
ET = list()
print(E)
for i in E:
    for j in E:
        tmp = list()
        if i != j:
            tmp.append(i)
            tmp.append(j)
            ET.append(tmp)
print(ET, len(ET))

# 生成2阶的粗糙表实例

for i in range(len(data)):
    for j in range(i+1, len(data)):
        dict_ins = dict()
        if data[i]["feature"] != data[j]["feature"]:
            try:
                x1 = float(data[i]["x"])
                x2 = float(data[j]["x"])
                y1 = float(data[i]["y"])
                y2 = float(data[j]["y"])
            except (TypeError, ValueError) as e:
                print(e)
            if distance.euclidean((x1, y1), (x2, y2)) <= R:
                dict_ins[data[i]["feature"]] = data[i]["instance"]
                dict_ins[data[j]["feature"]] = data[j]["instance"]
                Rough_table_instance.append(dict_ins)
# print(Rough_table_instance)
fr = pd.DataFrame(Rough_table_instance)
# print(fr)

p2 = list()
# print(fr.columns)
for i in range(len(fr.columns)):
    for j in range(i+1, len(fr.columns)):
        tmp = list()
        tmp.append(fr.icol(i))
        tmp.append(fr.icol(j))
        p2.append(pd.DataFrame(tmp))

for i in range(len(p2)):
    p2[i] = p2[i].dropna(axis=1, how='any')

for i in range(len(p2)):
    p2[i] = p2[i].T
    p2[i].index = range(len(p2[i]))

# print(len(p2))
for i in reversed(range(len(p2))):
    tem = list(p2[i].columns)
    pi = []
    for j in tem:
        pi.append(len(set(p2[i][j]))/Feature_ins_count[j])
    t = min(pi)
    if t < min_prev:
        del p2[i]


def get_table_ins(p, p2):
    C_T = []
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            *a1, b1 = list(p[i].columns)
            *a2, b2 = list(p[j].columns)
            if a1 == a2 and b1 != b2:
                for k in range(len(p2)):
                    if [b1, b2] == list(p2[k].columns):
                        # print(p2[k].T)
                        T_C = pd.merge(p[i], p[j])
                        # print(T_C)
                        for g in range(len(T_C)):
                            for f in range(len(p2[k])):
                                if T_C.ix[g, b1] == p2[k].ix[f, b1] and T_C.ix[g, b2] == p2[k].ix[f, b2]:
                                    break;
                                if f == len(p2[k])-1:
                                    T_C = T_C.drop(g)
                        T_C.index = range(len(T_C))
                        C_T.append(T_C)
    for i in reversed(range(len(C_T))):
        tmp = list(C_T[i].columns)
        for j in tmp:
            if len(set(C_T[i][j]))/Feature_ins_count[j] < min_prev:
                del C_T[i]
                break;
    if len(C_T) > 0:
        return C_T
    else:
        print("不存在更高阶的模式")

print(p2)
# C_T3 = get_table_ins(p2, p2)
# print(C_T3)
# C_T4 = get_table_ins(C_T3, p2)
# print(C_T4)
# C_T5 = get_table_ins(C_T4, p2)
# print(C_T5)
# C_T6 = get_table_ins(C_T5, p2)
# print(C_T6)
