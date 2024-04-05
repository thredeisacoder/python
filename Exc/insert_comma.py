def reverseNum(num):
    reversed_num = 0
    while num != 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num //= 10
    return reversed_num

def insert_commas(num):
    str_num = str(reverseNum(num))
    res = ""
    for i in range(len(str_num)):
        if i % 3 == 0 and i > 0:
            res+= ","
        res += str_num[i]
    return res[::-1]

num = int(input())
print(insert_commas(num))
