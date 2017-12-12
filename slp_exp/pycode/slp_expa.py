import pandas as pd
import os
import math
from_path = "./data"
to_path = "./to_data"
file_ls = []
file_name_ls = []


def each_file(file_path):
    file_list = []
    path_dir = os.listdir(file_path)
    # print(path_dir)
    for all_file in path_dir:
        file_name = os.path.join(file_path, all_file)
        file_list.append(file_name)
        # print(file_name)
    return file_list, path_dir
file_ls, file_name_ls = each_file(from_path)
print(file_name_ls)


def data_process(file_name="./data/boy0.sign", path="./data/boy0.csv"):
    data = []
    # 第5，6，12,13,14,15 列去掉
    for line in open(file_name):
        ls = line.split(",")
        ls = map(eval, ls)
        data.append(ls)

    df_boy = pd.DataFrame(data)
    df_boy.drop(df_boy.columns[11:15], axis=1, inplace=True)
    df_boy.drop(df_boy.columns[4:6], axis=1, inplace=True)

    df_boy = get_std(df_boy)
    df_boy = dim_change(df_boy)
    df_boy = df_boy.T
    # print(df_boy)
    col = df_boy.columns
    dt = pd.DataFrame()
    # dt.apply(lambda x: x.diff)
    for i in range(len(col)):
        j = i + 1
        if j == len(col):
            break
        else:
            tmp = df_boy[j].astype(float)-df_boy[i].astype(float)
            dt = dt.append(tmp, ignore_index=True)
    dt = dt.T
    print(type(dt.iloc[5, 4]))
    for i in range(len(dt)):
        for j in dt.columns:
            if dt.iloc[i, j] > 0.84:
                dt.iloc[i, j] = "U"
            elif (dt.iloc[i, j] <= 0.84) & (dt.iloc[i, j] > 0.25):
                dt.iloc[i, j] = "u"
            elif (dt.iloc[i, j] <= 0.25) & (dt.iloc[i, j] > -0.25):
                dt.iloc[i, j] = "s"
            elif (dt.iloc[i, j] <= -0.25) & (dt.iloc[i, j] > -0.84):
                dt.iloc[i, j] = "d"
            elif dt.iloc[i, j] <= -0.84:
                dt.iloc[i, j] = "D"
    dt.to_csv(path)


def get_std(dt):
    # dt_temp = pd.DataFrame()
    # dt_temp = dt.applymap()
    # col = dt.columns
    # for i in range(len(col)):
    #     dt_temp = dt.applymap(lambda x: (dt[col[i]] - dt[col[i]].mean())/dt[col[i]].var)
    # print(dt_temp)
    # dk = dt.apply(lambda x: x - x.mean)
    # print(dk)
    ls_mean = list(dt.mean())
    ls_std = list(dt.std())
    # print(ls_std)
    ls_data = []
    for i in range(len(dt)):
        ls_col = []
        for j in range(len(dt.columns)):
            if ls_std[j] != 0:
                ls_col.append((dt.iloc[i, j] - ls_mean[j])/ls_std[j])
            else:
                ls_col.append(0)
        ls_data.append(ls_col)
    # print(pd.DataFrame(ls_data))
    return pd.DataFrame(ls_data)


def dim_change(dt):
    ls_data = []
    for i in dt.columns:
        ls_col = []
        ls_new = []
        ls_col = dt[i]
        n = len(ls_col)
        for j in range(0, 57):
            ls_new.append(sum(ls_col[math.floor(n*j/57): math.ceil(n*j/57)])*57/n)
        ls_data.append(ls_new)
    return pd.DataFrame(ls_data)
#
# dt_col = dt.columns
# for i in dt_col:
#     dt[i] = dt[i].apply(lambda v: )
# print(df_boy)
# s = df_boy.columns()
# print(s)
# print(df_boy[1].astype(float)-df_boy[0].astype(float))
for i in range(len(file_ls)):
    file = file_name_ls[i] + ".csv"
    to_file = os.path.join(to_path, file)
    from_file = file_ls[i]
    data_process(file_ls[i], to_file)
