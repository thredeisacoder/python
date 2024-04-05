def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_special_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if is_prime(i):
            if not is_prime(int(str_num[i])):
                return "NO"
        else:
            if is_prime(int(str_num[i])):
                return "NO"
    return "YES"

num_tests = int(input())

for _ in range(num_tests):
    num = int(input())
    result = check_special_prime(num)
    print(result)
