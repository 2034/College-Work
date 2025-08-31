tblOfRates = []
tblOfNames = []
tblOfWages = []
userName = "user"
userPass = "pass"
userAttempts = 3

def init():
    nameFile = open("names.txt", "r")
    rateFile = open("rates.txt", "r")
    wageFile = open("wages.txt", "r")

    for line in rateFile:
        tblOfRates.append(float(line.strip()))
   
    for line in nameFile:
        tblOfNames.append(line.strip())

    for line in wageFile:
        tblOfWages.append(line.strip())

    rateFile.close()
    nameFile.close()
    wageFile.close()

def mainMenu():
    while True:
        print("\nMenu:")
        print("1. Calculate Wages")
        print("2. Print Wages")
        print("3. Find Max Wage")
        print("4. Find Min Wage")
        print("5. Count Wages Under £100")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            hours_worked = int(input("Enter hours worked: "))
            for rate in tblOfRates:
                tblOfWages.append(rate * hours_worked)
           
            wageFile = open("wages.txt", "w")
            for wage in tblOfWages:
                wageFile.write(f"{wage}\n")
            wageFile.close()
        elif choice == "2":
            for i in range(len(tblOfNames)):
                print(f"{tblOfNames[i]} gets paid £{tblOfWages[i]} per hour")
        elif choice == "3":
            maxWage = max(tblOfWages)
            print(f"Max wage is £{maxWage}")
        elif choice == "4":
            minWage = min(tblOfWages)
            print(f"Min wage is £{minWage}")
        elif choice == "5":
            for wage in tblOfWages:
                if wage < 100:
                    count += 1
            print(f"Number of wages under £100: {count}")
        elif choice == "6":
            break
        else:
            print("Invalid choice")

while userAttempts > 0:
    userInput = input("Enter username: ")
    passInput = input("Enter password: ")
    if userInput == userName and passInput == userPass:
        break
    else:
        userAttempts -= 1
        print("Wrong Login")

init()
mainMenu()