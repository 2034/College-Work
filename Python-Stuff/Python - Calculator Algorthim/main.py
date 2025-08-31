choice = 0

def calculateMenu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    return input("Enter your choice: ")


def fetchNumbers():
    firstNum = int(input("Enter first number: "))
    secondNum = int(input("Enter second number: "))
    return firstNum, secondNum


while choice != "5":
    choice = calculateMenu()
    if choice != "5":
        firstNum, secondNum = fetchNumbers()
        sumNum = 0
        if choice == "1": # Addition
            sumNum = firstNum + secondNum
        elif choice == "2": # Subtraction
            sumNum = firstNum - secondNum
        elif choice == "3": # Multiplication
            sumNum = firstNum * secondNum
        elif choice == "4": # Division
            sumNum = firstNum / secondNum

        # Print the result
        print(f"Result: {sumNum}")
    else:
        # Exit the program
        print("Exiting...")