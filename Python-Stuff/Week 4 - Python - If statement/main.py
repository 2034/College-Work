gradeInput =  int(input("Enter your grade: "))

gradeResult = ""
if gradeInput >= 90:
    gradeResult = "A"
elif gradeInput >= 70:
    gradeResult = "B"
elif gradeInput >= 50:
    gradeResult = "C"
elif gradeInput >= 40:
    gradeResult = "D"
elif gradeInput >= 0:
    gradeResult = "Fail"
else:
    gradeResult = "Invalid grade"

print(f"Your grade is {gradeResult}")