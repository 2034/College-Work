# Jonathan (17/12/24)

# Input Name
student_name = input("Enter the student's name: ")
# Input Mark
exam_mark = int(input(f"Enter the exam mark for {student_name}: "))


string="failed"
# Check exam score
if exam_mark >= 70:
    string = "got an A"
elif exam_mark >= 60:
    string = "got an B"
elif exam_mark >= 50:
    string = "got an C"

print(f"{student_name} {string}")