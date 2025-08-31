marks = [20, 78, 50, 52, 12, 34, 88, 90, 3, 52]

def homeMenu():
    print("\nMenu:")
    print("1. Display List")
    print("2. Find Highest Value")
    print("3. Find Lowest Value")
    print("4. Count number of values under 50")
    print("5. Add Value")
    print("6. Exit")

while True:
    homeMenu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Marks List:", marks)
    elif choice == 2:
        highestValue = 0
        for i in marks:
            if i > highestValue:
                highestValue = i
        print("Highest Value:", highestValue)
    elif choice == 3:
        lowestValue = 100
        for i in marks:
            if i < lowestValue:
                lowestValue = i
        print("Lowest Value:", lowestValue)
    elif choice == 4:
        amtOfValues = 0
        for i in marks:
            if i < 50:
                print(f"Number {i} is under 50.")
                amtOfValues += 1
        print("Number's under 50:", amtOfValues)
    elif choice == 5:
        inputValue = int(input("Enter a value to add (0-100): "))
        if inputValue < 0 or inputValue > 100:
            print("Invalid value.")
        else:
            marks.append(inputValue)
            print("Successfully added value.")
    elif choice == 6:
        print("Exiting")
        break
    else:
        print("Error: Invalid choice. Please select a valid option.")