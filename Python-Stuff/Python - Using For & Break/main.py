# Jonathan (17/12/24)
# Config
max_attempts = 4

# Data
correct_username = "yourname"
correct_password = "city"
attempts = 0  # Counter for attempts

# Loop to check max attempts
while attempts < max_attempts:
    # Input
    username = input("Enter your username: ")
    password = input("Enter your password: ")
   
    # Input Check
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break #Break Loop
    else:
        print("Incorrect username or password. Please try again.")
        attempts += 1  # Failed attempt

# Max attempts
if attempts == max_attempts:
    print("You have exceeded the maximum number of attempts.")