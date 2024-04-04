def decode(sequence):
    res = ""
    flag = 0
    while flag < len(sequence):
        if sequence[flag].isdigit():
            res += sequence[flag - 1] * (int(sequence[flag]) - 1)
            flag += 1
        else:
            res += sequence[flag]
            flag += 1
    return res

lst = []
for i in range(int(input())):
    n = str(input())
    lst.append(n)

for i in lst:
    print(decode(i))