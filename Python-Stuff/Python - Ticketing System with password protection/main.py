# Jonathan
# 15/01/25 13:33

# Define Variables
choice = 0
attempts = 0
types = ["Adult","Child","Student","OAP"]
ticketPrices = [19.95,9.95,17.95,9.95]
ticketTypeAmount = len(types)+1
# Define Functions

def homeScreen():
    print("Please Select a option:\n")
    for name in range(len(types)):
        if (ticketPrices[name]):
            print(f"{name+1}: Calculate {types[name]} Tickets")
        else:
            break
    print(f"{ticketTypeAmount}: Exit")

def calculateCost(typeOfTicket):
    ticketAmount = int(input(f"Please enter the amount of {types[typeOfTicket-1]} ticket's you want:"))
    costPerTicket = ticketPrices[typeOfTicket-1] or 0
    print(f"\nThe Cost of your tickets are: {ticketAmount*costPerTicket}")

while (attempts < 3):
    userPassword = input("What is the password\n")
    if (userPassword == "password"):
        print("Welcome")
        break
    else:
        print("\nIncorrect password")
        attempts = attempts + 1

if (attempts < 3):
    while (choice != 5):
        homeScreen()
        choice = int(input("Select a option:\n"))
        if (choice != ticketTypeAmount and choice <= ticketTypeAmount and choice > 0):
            calculateCost(choice)
        elif (choice == ticketTypeAmount):
            break

print("Exiting")