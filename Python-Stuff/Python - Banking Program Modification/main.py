balance = 1010 # Total Balance on the account
choice = 0

def mainMenu():
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    return int(input("Choose an option: "))

def deposit(amount):
    global balance
    balance += amount
    return "Amount deposited successfully, new balance is: " + str(balance)


def withdraw(amount):
    global balance
    if balance < amount:
        return "Insufficient funds"
    balance -= amount
    return "Amount withdrawn successfully, new balance is: " + str(balance)


def checkBalance():
    global balance
    return "Your balance is: " + str(balance)


while (choice !=5):
    choice = mainMenu()
    if choice == 1:
        print(checkBalance())
    elif choice == 2:
        print(deposit(int(input("Enter amount to deposit: "))))
    elif choice == 3:
        print(withdraw(int(input("Enter amount to withdraw: "))))
    elif choice == 4:
        print("Exiting...")
    else:
        print("Invalid choice")