a = float(input("Enter number A: "))
b = float(input("Enter number B: "))
c = float(input("Enter number C: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    s = (a + b + c) /2
    p = a + b + c
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(p, area)
else:
    print("Khong phai 3 canh cua tam giac")