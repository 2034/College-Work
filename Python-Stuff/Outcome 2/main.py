# Jonathan 
# 19/02/2025 08:55
# Outcome 2

import tkinter as tkMenu
from tkinter import messagebox as messageBox

mainMenu = {"1": "Eating Healthy","2": "Exercise","3": "Fun facts about mental health","4": "Exit"}
healthMenu = {"1": "Tips","2": "Quiz","3": "Back to main menu"}
exerciseMenu = {"1": "Workout Tips","2": "Workout mini games","3": "Back to main menu"}

# Display"s txt file content
def displayMessage(file):
    with open(file, "r") as txtDoc:
        messageBox.showinfo("File Content", txtDoc.read())

def displayQuiz():
    # Init quiz menu
    quizWindow = tkMenu.Toplevel()
    quizWindow.title("Health Quiz")

    questions = [
        ("Which of the following is a good source of healthy fats?", "B", ["Butter", "Avocado", "Candy", "Soda"]),
        ("How many cups of water should the average adult drink per day?", "C", ["2-3", "5-6", "8+", "12+"])
    ]

    # List to store answers
    selectedAnswers = []

    for question, correctAnswer, options in questions:
        tkMenu.Label(quizWindow, text=question).pack()
        var = tkMenu.StringVar(value="N/A")
        selectedAnswers.append(var)
        for option in options:
            tkMenu.Radiobutton(quizWindow, text=option, variable=var, value=option.lower()).pack()

    tkMenu.Button(quizWindow, text="Submit", command=lambda: checkUserAnswer(quizWindow, questions, selectedAnswers)).pack()

def checkUserAnswer(quizWindow, questions, selectedAnswers):
    for answer in selectedAnswers:
        if answer.get() == "N/A":
            messageBox.showerror("Error", "Not all questions have been answered")
            return

    correct = 0
    for i, (_, correctAnswer, options) in enumerate(questions):
        selected = selectedAnswers[i].get()  # Gets user"s answer
        if selected == options[ord(correctAnswer) - 65].lower(): # ord = unicode of char
            correct += 1
    messageBox.showinfo("Quiz Result", f"You got {correct} out of {len(questions)} correct!")
    quizWindow.destroy()

def main():
    # Init main menu
    root = tkMenu.Tk()
    root.title("Health and Exercise App")

    def mainMenuHandler(choice):
        if choice == "1":
            displayHealthMenu()
        elif choice == "2":
            displayExerciseMenu()
        elif choice == "3":
            displayMessage("txt/mentalHealth.txt")
        elif choice == "4":
            root.quit()

    def healthMenuHandler(choice, healthWindow):
        if choice == "1":
            displayMessage("txt/healthTips.txt")
        elif choice == "2":
            displayQuiz()
        elif choice == "3":
            healthWindow.destroy()

    def exerciseMenuHanlder(choice, exerciseWindow):
        if choice == "1":
            displayMessage("txt/exerciseTips.txt")
        elif choice == "2":
            displayMessage("txt/workoutMinigame.txt")
        elif choice == "3":
            exerciseWindow.destroy()

    def displayHealthMenu():
        healthWindow = tkMenu.Toplevel()
        healthWindow.title("Eating Healthy")
        for key, value in healthMenu.items():
            tkMenu.Button(healthWindow, text=value, command=lambda k=key: healthMenuHandler(k,healthWindow)).pack()

    def displayExerciseMenu():
        exerciseWindow = tkMenu.Toplevel()
        exerciseWindow.title("Exercise")
        for key, value in exerciseMenu.items():
            tkMenu.Button(exerciseWindow, text=value, command=lambda k=key: exerciseMenuHanlder(k, exerciseWindow)).pack()

    for key, value in mainMenu.items():
        tkMenu.Button(root, text=value, command=lambda k=key: mainMenuHandler(k)).pack()

    root.mainloop()

main()