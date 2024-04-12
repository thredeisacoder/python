def check(value):
    if value[-3:] == ".py" or value[-3:] == ".Py" or value[-3:] == ".pY" or value[-3:] == ".PY":
        print("yes")
    else:
        print("no")

u = str(input())
check(u)