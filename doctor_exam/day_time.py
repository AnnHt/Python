year = eval(input("please enter the year:"))
days = 0
if year > 1900:
    for i in range(1900, year):
        if i % 400 == 0:
            # 判断是闰年
            days += 31 * 7 + 30 * 4 + 29
        elif (i % 100 != 0) & (i % 4 == 0):
            days += 31 * 7 + 30 * 4 + 29
        else:
            days += 31 * 7 + 30 * 4 + 28
print(days)
t = (days+1) % 7
print(str(year)+".01.01 is "+"星期"+""+str(t))
