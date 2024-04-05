def is_prime(num):
    if num<2: return False
    for i in range(2, (num ** 0.5) + 1):
        if num % i==0: return False
    return True

def check(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if is_prime(i + 1):
            if int(num_str[i]) not in [2, 3, 5, 7]:
                return "NO"
        else:
            if int(num_str[i]) in [2, 3, 5, 7]:
                return "NO"
    return "YES"

lst = []
tc_num = int(input())
for i in range(tc_num):
    n = int(input())
    lst.append(n)

for i in lst:
    print(check(i))