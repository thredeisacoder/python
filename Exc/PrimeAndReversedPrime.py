
def reverseNum(num):
    reversed_num = 0
    while num != 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num //= 10
    return reversed_num

def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);

def main(num):
    if uscln(num, reverseNum(num)) == 1:
        print("YES")
    else:
        print("NO")

tc_num = int(input())
lst = []
for i in range(tc_num):
    n = int(input())
    lst.append(n)

for i in lst:
    main(i)
