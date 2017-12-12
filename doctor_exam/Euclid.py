m, n = eval(input("please input two number:"))


def gcd(large, small):
    r = large % small
    while r != 0:
        large = small
        small = r
        r = large % small
    print(small)


def gcd_old(large, small):
    r = large - small
    while r > 0:
        large = small
        small = r
        r = large - small
    print(small)
gcd_old(m, n)
