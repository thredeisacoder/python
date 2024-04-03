choice1 = input("Is it raining? ").lower()
if choice1 == "yes":
    choice2 = input("Is it windy? ").lower()
    if choice2 == "yes":
        print("Troi qua gio de mang o")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
