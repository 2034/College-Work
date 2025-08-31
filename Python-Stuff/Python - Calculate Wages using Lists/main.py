monthlyEarnings = [967, 967, 1000, 1000, 650, 1100, 1000, 1250, 967, 1000, 1200, 650]

def calcEarnings(inputMonth):
    if monthlyEarnings[inputMonth]:
        amountMade = 0
        for i in range(0, inputMonth):
            amountMade += monthlyEarnings[i]

        print(f"You have made: £{amountMade} so far this year")
        return amountMade
    else:
        print("There is not a month for your input")


inputOfMonth = int(input("Enter the month you want to calculate earnings for (1-12): "))


if inputOfMonth > 0 and inputOfMonth <= 12:
    calcEarnings(inputOfMonth)
else:
    print("Invalid month input")