def main(num):
    str_num = str(num)
    if str_num[:2] == str_num[-2:]:
        print("YES")
    else:
        print("NO")

lst = []
tc_num = int(input())
for i in range(tc_num):
    num = int(input())
    lst.append(num)
for i in lst:
    main(i)