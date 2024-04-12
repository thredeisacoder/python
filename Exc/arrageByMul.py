def splitValue(value):
    return value.split()

def mul(num):
    str_num = str(num)
    mul = 1
    for digit in str_num:
        mul *= int(digit)
    return mul

def swap(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

def arrange(value):
    lst = [int(x) for x in splitValue(value)]
    length = len(lst)
    for i in range(length):
        for j in range(length - 1):
            if mul(lst[j]) > mul(lst[j + 1]):
                swap(lst, j, j + 1)
            elif mul(lst[j]) == mul(lst[j + 1]):
                if lst[j] > lst[j + 1]:
                    swap(lst, j, j + 1)
    return lst

n = int(input())
length = int(input())
value = input()
result = arrange(value)
print(' '.join(map(str, result)))