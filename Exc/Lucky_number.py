def Counter(num):
    count = 0
    while num != 0:
        tmp = num % 10
        if tmp == 4 or tmp == 7:
            count += 1
        num //= 10
    return count

num = int(input())
res = Counter(num)

if res == 4 or res == 7:
    print("YES")
else:
    print("NO")