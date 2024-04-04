from math import*
def isPrime(x):
    if x<2: return False
    for i in range(2,int(sqrt(x)+1)):
        if x % i==0: return False
    return True

def reverseNum(num):
    return int(str(num)[::-1])
def Res(n):
    save = ''
    for i in range(12, n + 1):
        if isPrime(i) and isPrime(reverseNum(i)) and reverseNum(i) <= n and str(i) not in save and str(reverseNum(i)) not in save and i != reverseNum(i):    
            save += f"{i} {reverseNum(i)} "
    print(save)

num = int(input())
lst=[]
for i in range (num):
    lst.append(int(input())) 
for i in lst:
    Res(i)  