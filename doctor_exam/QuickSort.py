
d = [23, 13, 49, 6, 31, 19, 28]


def partition(r, first, end):
    i = first
    j = end
    while i < j:
        while (i < j) & (r[i] <= r[j]):
            j -= j
            if i < j:
                r[i], r[j] = r[j], r[i]
                i += i
        while (i < j) & (r[i] <= r[j]):
            i += i
            if i < j:
                r[j], r[i] = r[i], r[j]
                j -= 1
    return i
