month = int(input("Enter month: "))
year = int(input("Enter year: "))
if (year % 4 == 0) and (year % 100 != 0):
    checkYear = False
else:
    checkYear = True

if month in [1, 3, 5, 7, 8, 10, 12]:
    day = 31
    print(day)
elif month in [4, 6, 9, 11]:
    day = 30
    print(day)
else:
    if checkYear == True:
        day = 28
        print(day)
    else:
        day = 29
        print(day)