# Variables
lowestMark = 0
maxCourseworkMark = 60
maxPrelimMark = 90
tableOfStudents = []

# Read student data from file
def readStudentData(fileName):
    with open(fileName, "r") as file:
        return file.readlines()

# Calculate grade
def calculateGrade(gradePercentage):
    if gradePercentage >= 70:
        return "A"
    elif gradePercentage >= 60:
        return "B"
    elif gradePercentage >= 50:
        return "C"
    elif gradePercentage >= 45:
        return "D"
    else:
        return "No Grade"

# Calculate percentage
def calculatePercentage(courseworkMark, prelimMark):
    totalMark = courseworkMark + prelimMark
    percentage = (totalMark * 100) / 150
    return percentage

# Get grade count
def getGradeCount():
    gradeCount = {"A": 0, "B": 0, "C": 0, "D": 0, "No Grade": 0}
    for student in tableOfStudents:
        gradeCount[student[4]] += 1
    for grade in gradeCount:
        print(f"{grade}: {gradeCount[grade]}")

# Find best student via percentage
def findBestStudent():
    bestStudent = tableOfStudents[0]
    for student in tableOfStudents:
        if student[3] > bestStudent[3]:
            bestStudent = student
    return bestStudent

# Main function
def main():
    while True:
        print("1. Print Student Data")
        print("2. How many students got each grade")
        print("3. What student had the best percentage")
        print("4. Exit")
        choice = input("Please enter your choice: ")
        if choice == "1":
            for student in tableOfStudents:
                print(f"Student: {student[0]}")
                print(f"Percentage: {student[3]}%")
                print(f"Grade: {calculateGrade(calculatePercentage(student[1], student[2]))}")
                print()
        elif choice == "2":
            getGradeCount()
        elif choice == "3":
            bestStudent = findBestStudent()
            print(f"{bestStudent[0]} had the best percentage with {bestStudent[3]}% and a grade of {bestStudent[4]}")
        elif choice == "4":
            break

def init():
    studentNames = readStudentData("data/studentNames.txt")
    studentCourseworkMarks = readStudentData("data/studentCourseworkMarks.txt")
    studentPrelimMarks = readStudentData("data/studentPrelimMarks.txt")
    for i in range(len(studentNames)):
        studentName = studentNames[i].strip()
        courseWorkMark = int(studentCourseworkMarks[i].strip())
        prelimMark = int(studentPrelimMarks[i].strip())
        studentPercentage = int(calculatePercentage(courseWorkMark, prelimMark))
        studentGrade = calculateGrade(studentPercentage)
        if not (courseWorkMark >= 0 and courseWorkMark <= maxCourseworkMark) or not (prelimMark >= 0 and prelimMark <= maxPrelimMark):
            print(f"{studentName} has invalid marks")
            continue
        tableOfStudents.append([studentName, courseWorkMark, prelimMark, studentPercentage, studentGrade])
    main()


init()