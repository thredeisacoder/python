def encode(string):
    res = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            res += str(count) + string[i - 1]
            count = 1
    res += str(count) + string[-1]
    return res

lst = []
tc_num = int(input())
for i in range(tc_num):
    n = str(input())
    lst.append(n)

for i in lst:
    print(encode(i))