def factorial(num):
    if num == 0:
        return 1
    else:
        res = 1
        for i in range(1, num + 1):
            res = res * i
        return res
def calulate(num):
    fnum = num
    sum = 0
    while num != 0:
        tmp = num % 10
        num //= 10
        sum += factorial(tmp)
    if fnum == sum:
        return "Yes"
    else:
        return "No"

tc_times = int(input())
lst = []
for i in range(tc_times):
    lst.append(int(input()))
for i in lst:
    res = calulate(i)
    print(res)