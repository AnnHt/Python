import operator
import itertools
# 距离阈值
from scipy.spatial import distance
r_dist = 100
# 存贮读入的数据
data = list()
# 存贮星行实例
sn = dict()
list_sn = list()
dict_sn = dict()
# 存储模式和实例
dict_pattern = dict()
# 存贮特征
feature = set()
# 读入的数据文件
fin = open("D:\data2.txt", "r", encoding="utf8")


class f_i:

    def __init__(self, fu, ins):
        if fu != "" and ins != "":
            self.fu = fu
            self.ins = ins

while True:
    dict_temp = dict()
    line = fin.readline()
    row = list()
    if line:
        line = line.strip()
        row = line.split("\t")
        dict_temp["feature"] = row[0]
        dict_temp["instance"] = row[1]
        dict_temp["x"] = row[2]
        dict_temp["y"] = row[3]
        data.append(dict_temp)
    else:
        break
fin.close()

# 将列表中的字典按照特征的字典序来排列
data.sort(key=operator.itemgetter("feature"))


# 定义求距离的公式


def dist(x1, y1, x2, y2):
    return distance.euclidean((x1, y1), (x2, y2))

# 星行函数


def star_neighbor(list_data, value_dist, data_sn):
    for data_i in range(len(list_data)):
        temp = list()
        temp.append(data_i) 
        for data_j in range(len(list_data)):
            if (data_j > data_i) and (
                        list_data[data_j]["feature"] != list_data[data_i]["feature"]) and (
                        dist(float(list_data[data_i]["x"]), float(list_data[data_i]["y"]),
                             float(list_data[data_j]["x"]),
                             float(list_data[data_j]["y"])) <= value_dist):
                temp.append(data_j)
        if len(temp) > 1:
            data_sn.append(temp)


star_neighbor(data, r_dist, list_sn)
print(list_sn)


# 转换成字典结构


for sn_row in list_sn:
    # print(data[sn_row[0]]["feature"])
    feature_str = data[sn_row[0]]["feature"]
    instance_int = data[sn_row[0]]["instance"]
    del sn_row[0]
    if feature_str in dict_sn:
        dict_n = dict()
        dict_instance = dict()
        dict_instance = dict_sn[feature_str]
        for sn_col in sn_row:
            dict_n[data[sn_col]["feature"]] = data[sn_col]["instance"]
            # tp = f_i(data[sn_col]["feature"], data[sn_col]["instance"])
            # set_instance.add(tp)
            # set_instance.add(dict_n)
        dict_instance[instance_int] = dict_n
        dict_sn[feature_str] = dict_instance
    else:
        dict_instance = dict()
        dict_n = dict()
        for sn_col in sn_row:
            dict_n[data[sn_col]["feature"]] = data[sn_col]["instance"]
            # tp = f_i(data[sn_col]["feature"], data[sn_col]["instance"])
            # set_instance.add(tp)
            # set_instance.add(data[sn_col]["feature"]+data[sn_col]["instance"])
            # set_instance.add(dict_n)
        dict_instance[instance_int] = dict_n
        dict_sn[feature_str] = dict_instance

print(dict_sn)

f_i = dict()

# 得到特征


def get_feature(set_feature, list_data):
    for two in list_data:
        if two["feature"] in set_feature:
            f_i[two["feature"]] += 1
        else:
            f_i.setdefault(two["feature"], 1)
            set_feature.add(two["feature"])


get_feature(feature, data)
print(f_i)
feature = list(feature)
feature.sort()
print(feature)

# 生成2阶的候选模式
two_colocation = list()
for i in itertools.combinations(feature, 2):
    two_colocation.append(i)
print(two_colocation)

# 提取出二阶的实例
pattern_instance = dict()
for pattern in two_colocation:
    # 模式集合
    pattern = list(pattern)
    str_pattern = ('').join(pattern)
    if pattern[0] in dict_sn.keys():
        # print(dict_sn[pattern[0]])
        for keys in dict_sn[pattern[0]].keys():
            if pattern[1] in dict_sn[pattern[0]][keys]:
                dict_tmp = dict()
                dict_tmp[pattern[1]] = dict_sn[pattern[0]][keys][pattern[1]]
                dict_two = dict()
                dict_two[keys] = dict_tmp
    pattern_instance[str_pattern] = dict_two
print(pattern_instance)
