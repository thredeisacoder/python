def calSum(value):
    sum = 0
    str_num = str(value)
    for i in range(len(str_num)):
        if i % 2 == 0:
            sum += int(str_num[i])
    return sum

def calMul(value):
    mul = 1
    str_num = str(value)
    count = 0
    for i in range(len(str_num)):
        if i % 2 == 1:
            if int(str_num[i]) == 0:
                count += 1
                continue
            else:
                mul *= int(str_num[i])
    if mul == 1 and count > 0:
        mul = 0
    return mul

def printOut(value):
    resSum = calSum(value)
    resMul = calMul(value)
    print(resSum, resMul)

lst = []
ts_num = int(input())
for i in range(ts_num):
    n = int(input())
    lst.append(n)

for i in lst:
    printOut(i)