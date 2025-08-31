# Config to adjust max and minimum marks
lowestMark = 0
maxCourseworkMark = 60
maxPrelimMark = 90

def calculateGrade(gradePercentage): # func to calculate grade
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

def calculatePercentage(courseworkMark, prelimMark): # func to calculate percentage
    totalMark = courseworkMark + prelimMark
    percentage = (totalMark * 100) / 150
    return int(percentage)

def main():
    # Initialising variables from user input
    inputName = input("Please Enter student's name: ")
    inputCourseworkMark = None
    inputPrelimMark = None

    # Checks if input is valid
    def getValidMark(prompt, maxMark):
        while True:
            try:
                mark = int(input(prompt))
                if lowestMark <= mark <= maxMark:
                    return mark
                else:
                    print(f"Please enter a valid mark between {lowestMark} and {maxMark}")
            except ValueError:
                print(f"Please enter a valid mark between {lowestMark} and {maxMark}")

    inputCourseworkMark = getValidMark("Please Enter student's coursework mark: ", maxCourseworkMark)
    inputPrelimMark = getValidMark("Please Enter student's prelim mark: ", maxPrelimMark)

    # Calculating percentage and grade
    percentage = calculatePercentage(inputCourseworkMark, inputPrelimMark)
    grade = calculateGrade(percentage)

    print(f"{inputName}'s Percentage: {percentage}%")
    print(f"{inputName}'s Grade: {grade}")

main()