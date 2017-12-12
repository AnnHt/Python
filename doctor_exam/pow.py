import math

x, y = eval(input("please enter two number"))


def pow1(a, n):
    if n == 1:
        return a
    else:
        return pow1(a, math.ceil(n/2)) * pow1(a, math.floor(n/2))

print(pow1(x, y))
