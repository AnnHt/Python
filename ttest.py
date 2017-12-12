

dict1 = {"A": "31", "B": "14", "D": "23"}
dict2 = {"A": "3", "C": "3", "D": "3"}
dict3 = {"B": "4", "C": "3", "D": "3"}
data = list()
data.append(dict1)
data.append(dict2)
data.append(dict3)

print(data)
# 并集
def dict_union(dict1, dict2, k):
    pattern_tmp = list()
    key1 = dict1.keys()
    key2 = dict2.keys()
    t = key1 & key2
    m = dict()
    n = dict()
    # key相同
    if len(t) == k - 1:
        for s in t:
            if dict1[s] == dict2[s]:
                m[s] = dict1[s]
    # value相同
    if len(m) == k - 1:
        n = dict(dict1, **dict2)
    print(n)
    print(m)
# dict_union(dict1, dict2, 3)
set1 = list(dict1.keys())
set2 = list(dict1.values())
print(set1)
print(set2)


