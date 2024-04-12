def splitValue(value):
    return value.split()

def total(num):
    str_num = str(num)
    total = 0
    for digit in str_num:
        total += int(digit)
    return total

def swap(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

def arrange(value):
    lst = [int(x) for x in splitValue(value)]
    length = len(lst)
    for i in range(length):
        for j in range(length - 1):
            if total(lst[j]) > total(lst[j + 1]):
                swap(lst, j, j + 1)
            elif total(lst[j]) == total(lst[j + 1]):
                if lst[j] > lst[j + 1]:
                    swap(lst, j, j + 1)
    return lst

n = int(input())
length = int(input())
value = input()
result = arrange(value)
print(' '.join(map(str, result)))