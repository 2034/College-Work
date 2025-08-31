def getInfo(option):
    return input(f"Please enter your {option}: ")

name = getInfo("name")
age = int(getInfo("age"))
address = getInfo("address")

if age >= 21:
    print(f"Welcome {name}")
    print(f"Address: {address}")
else:
    print("You are too young")