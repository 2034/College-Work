for attempt in range(3):
    password = input("Enter the password: ")
    if password != "password":
        print("Incorrect password. Try again.")
    else:
        while True:
            studentName = input("Enter the student's name: ")
            studentMark = int(input("Enter the student's mark: "))
           
            if studentMark >= 70:
                print(f"{studentName} got an A")
            elif studentMark >= 60:
                print(f"{studentName} got a B")
            elif studentMark >= 50:
                print(f"{studentName} got a C")
            else:
                print(f"{studentName} failed")

            checkRun = input("Do you want to enter another student's details? (yes/no): ").lower()
            if checkRun != "yes":
                break
        break
else:
    print("You have tried to many times.")