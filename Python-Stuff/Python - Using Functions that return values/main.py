def getName():
    return input("Enter your name: ")

def getAge():
    return int(input("Enter your age: "))

name = getName()
age = getAge()

if age >= 18:
    print(f"Welcome, {name}!")
else:
    print(f"Sorry {name}, you are too young.")