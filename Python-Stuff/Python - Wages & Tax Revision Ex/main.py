# Jonathan (17/12/24)

# Input First Name
Name=input("Please enter your first name: ")
# Input Hours
Hours=input("Please enter how many hours you worked? ")
# Input Rates
Rate=input("Please enter the rate you get paid: ")
# Calculate Wage
Wages=float(Hours)*float(Rate)
# Calculate Tax
Tax=Wages*0.2
# Calculate the pay
Pay=Wages-Tax
# Print out message
print(f"Your take home pay is £{Pay}")