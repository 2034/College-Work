lowestMark = 0
maxCourseworkMark = 60
maxPrelimMark = 90

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

def calculatePercentage(courseworkMark, prelimMark):
    totalMark = courseworkMark + prelimMark
    percentage = (totalMark * 100) / 150
    return percentage


# Read student data from file
def readStudentData(fileName):
    with open(fileName, "r") as file:
        return file.readlines()

def main():
    studentNames = readStudentData("data/studentNames.txt")
    studentCourseworkMarks = readStudentData("data/studentCourseworkMarks.txt")
    studentPrelimMarks = readStudentData("data/studentPrelimMarks.txt")
    for i in range(len(studentNames)):
        studentName = studentNames[i].strip()
        courseWorkMark = int(studentCourseworkMarks[i].strip())
        prelimMark = int(studentPrelimMarks[i].strip())
        if not (courseWorkMark >= 0 and courseWorkMark <= maxCourseworkMark) or not (prelimMark >= 0 and prelimMark <= maxPrelimMark):
            print(f"{studentName} has invalid marks")
            continue

        gradePercentage = calculatePercentage(courseWorkMark, prelimMark)
        grade = calculateGrade(gradePercentage)

        print(f"Student: {studentName}")
        print(f"Percentage: {int(gradePercentage)}%")
        print(f"Grade: {grade}")
        print()

main()