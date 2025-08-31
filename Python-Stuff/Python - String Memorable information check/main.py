import random

secret="This is my secret password shhh"
length=len(secret)

num= random.randint(1,length)

answer=input("Guess the " +str(num)+ " character of the password ")

if (answer == secret[num]):
    print("Logged in now")
else:
    print("You are locked out now!")