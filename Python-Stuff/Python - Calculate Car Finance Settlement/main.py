balance = 2500
carPayments = [160, 160, 150, 150, 150, 150, 160, 155, 150, 160, 150, 150]

def calcPayments(month):
    if month < 1 or month > 12:
        print("Invalid month. Enter a month between 1 and 12.")
        return

    totalPayment = 0
    for i in range(month):
        totalPayment += carPayments[i]

    print(f"Total payments up to month {month}: £{totalPayment}")
    print(f"Settlement figure: £{balance - totalPayment}")


month = int(input("Enter a month as an integer (1-12): "))
calcPayments(month)