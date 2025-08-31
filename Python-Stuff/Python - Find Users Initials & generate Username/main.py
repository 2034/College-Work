# Jonathan
# 13:28 08/01/25
import random

name=input("What is your full name? ")
# Find Split
postion=name.find(" ")

# Fetch Initials
initName=name[0]+name[postion+1]

# Gen random num
randomNum = random.randint(1,100)

# Print
print("Username: ",initName+str(randomNum))