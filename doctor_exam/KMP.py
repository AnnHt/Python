
s, t = input("please input two string first is s, another is t:").split(",")
t = list(t)
s = list(s)
next = list()


def get_next(pt, next):
    next.append(-1)
    next.append(0)
    j = 1
    k = 0
    while j < len(pt):
        if (k == 0) | (pt[j-1] == pt[k-1]):
            j += 1
            k += 1
            next.append(k)
        else:
            k = next[k]
get_next(t, next)
print(next)