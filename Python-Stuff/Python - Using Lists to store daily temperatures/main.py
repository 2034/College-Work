weatherTemps = []

def homeMenu():
    print("\nMenu:")
    print("1: Show List")
    print("2: Add week's temperatures")
    print("3: Show Average temp")
    print("4: Show Max Temp")
    print("5: Exit program")

while True:
    homeMenu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if weatherTemps:
            print("Weekly temperatures: ", weatherTemps)
        else:
            print("No temperatures recorded yet.")
    elif choice == 2:
        for i in range(7):
            temp = float(input(f"Enter temperature for day {i+1}: "))
            weatherTemps.append(temp)
    elif choice == 3:
        avgTemp = 0
        for i in weatherTemps:
            avgTemp += i
        print("The average temperature is: ", avgTemp / len(weatherTemps))
    elif choice == 4:
        maxTemp = 0
        for i in weatherTemps:
            if i > maxTemp:
                maxTemp = i
        print("The maximum temperature is: ", maxTemp)
    elif choice == 5:
        print("Exiting.")
        break
    else:
        print("Invalid option.")