quiz_questions = {
    "who is developed python programming language?": {
        "A": "Wiwk Van Rossum",
        "B": "Rasmus Lerdorf",
        "C": "Guido Van Rossum",
        "D": "Niene Stom",
        "Answer": "C"
    },
    "Which of the following is the correct extension of python files?": {
        "A": ".python",
        "B": ".pl",
        "C": ".p",
        "D": ".py",
        "Answer": "D"
    },
    "Which type of programming does python support?": {
        "A": "Object Oriented Programmings",
        "B": "Structured Programming",
        "C": "Unstructured Programming",
        "D": "Functional Programming",
        "Answer": "A"
    }
}
print(type(quiz_questions))
score = 0
quz=0
tot_marks=4
extra_mark=2
for question, options in quiz_questions.items(): #0
    print(question)
    for option, value in options.items():
        if option != "Answer":
            print(f"{option}: {value}")
    answer = input("Choose your answer (A/B/C/D): ")
    quz+=1
    if answer.upper() == options["Answer"] and quz==2 :
        print("Correct answer!\n")
        score += extra_mark
    elif answer.upper() == options["Answer"] :
        print("Correct answer!\n")
        score += 1
    else:
        print(f"Incorrect answer. The correct answer was {options['Answer']}.\n")
print(f"Quiz finished! Your final score is {score} out of {tot_marks}")