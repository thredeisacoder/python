def splitNumber(string):
    res = []
    saveNumber = ""
    for i in string:
        if i.isdigit():
            saveNumber += i
        elif saveNumber:
            res.append(int(saveNumber))
            saveNumber = ""
    return res

def compare(lst):
    return min(lst)

lst = []
tc_num = int(input())
for i in range(tc_num):
    n = str(input())
    lst.append(n)

for i in lst:
    print(compare(splitNumber(i)))