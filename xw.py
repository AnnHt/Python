import pandas as pd
import math

df = pd.read_csv("D:/tianchi_fresh_comp_train_user.csv", header=None)
fr = pd.DataFrame(df)
dict_p_usr = {}
dict_pi = {}
print(fr)
print(len(set(fr[1])))
print(len(set(fr[0])))
for i in range(len(fr)):
    if fr.ix[i, 1] in dict_p_usr.keys():
        dict_p_usr[fr.ix[i, 1]].append(fr.ix[i, 0])
    else:
        temp = list()
        temp.append(fr.ix[i, 0])
        dict_p_usr[fr.ix[i, 1]] = temp

print(dict_p_usr)
for i in dict_p_usr.keys():
    for j in dict_p_usr.keys():
        if i != j:
            tmp = [str(i), str(j)]
            tmp = sorted(tmp)
            key = "_".join(str(tmp))
            if key in dict_pi.keys():
                break
            else:
                tmp_i = set(dict_p_usr[i])
                tmp_j = set(dict_p_usr[j])
                tmp_i_j = tmp_i & tmp_j
                if len(tmp_i_j) != 0:
                    t = len(tmp_i_j)/(len(tmp_i)*len(tmp_j))
                    dict_pi[key] = math.log2(t)

print(dict_pi)