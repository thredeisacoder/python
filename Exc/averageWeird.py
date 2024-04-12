def splitString(value):
    return value.split()

def calAverage(length, value):
    lst = [float(x) for x in splitString(value)]  
    minimum = min(lst)
    maximum = max(lst)
    total = sum(lst)
    
    min_count = lst.count(minimum)
    max_count = lst.count(maximum)
    
    total -= minimum * min_count
    total -= maximum * max_count
    
    return total / (length - min_count - max_count)

length = int(input())
value = input()

res = round(calAverage(length, value), 2) 
print(res)
