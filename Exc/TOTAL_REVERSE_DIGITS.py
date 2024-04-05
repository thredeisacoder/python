def sumOfEachElement(num):
    sum = 0
    while num != 0:
        remain = num % 10
        sum += remain
        num //= 10
    return sum

def reverseNum(num):
    reversed_num = 0
    while num != 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num //= 10
    return reversed_num

def main(num):
    if (sumOfEachElement(num) == reverseNum(sumOfEachElement(num))) and sumOfEachElement(num) > 9:
        print("YES")
    else:
        print("NO")

lst = []
tc_num = int(input())
for i in range(tc_num):
    n = int(input())
    lst.append(n)

for i in lst:
    main(i)