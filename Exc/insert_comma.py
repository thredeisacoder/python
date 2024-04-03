def insert_commas(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    res = ""
    for i in range(len(reversed_str)):
        if i % 3 == 0:
            res += "," + reversed_str[i]
        res += reversed_str
    return reversed_str[::-1]

num = int(input())
print(insert_commas(num))
