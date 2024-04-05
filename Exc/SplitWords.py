string = str(input())

res = []
saveString = ""
for i in string:
    if not i.isspace():
        saveString += i
    else:
        res.append(saveString)
        saveString = ""
if saveString:
    res.append(saveString)

for i in res:
    print(i)
