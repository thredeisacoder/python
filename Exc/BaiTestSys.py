def p(n):
    sum = 0
    lst = []
    for i in range (1, n):
        if(n % i == 0):
            sum += i
    if(n == sum):
        lst.append(n)
    return lst

n = int(input("enter n: "))
result = p(n)
print(result)