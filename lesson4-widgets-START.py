'''
Project Title: Quizzup
Author: Mohammed Farzaan Fahim
Date: 8 | 9 | 2024

[insert description of project and instructions for use]

'''


'''
TODO:
- fill out titleblock
- create at least 5 questions
    - each question requires:
        - it's own frame
        - a label to ask the question (in this frame)
        - a widget to get input (in this frame) ex. Button, Entry, RadioButton

- each question must use a different type of widget for input - Get creative!
- stylize the test to show off what you know! Use background and foreground
colours, alignment settings, images, frame padding etc. to make it appealing

'''


from tkinter import *
root = Tk()

# These lists will hold each of your StringVars (1 per question)
# and expected answers (1 per question)
# As you create your questions, append to these lists so that stringvars[i]
# is considered correct if it's value is equal to answers[i]
stringvars = []
answers = []

result = StringVar()


def check_answers():
    points = 0
    if answer1.get() == "1":
        points += 1
    if answer2.get() == "25":
        points += 1
    if answer3.get() == False:
        points += 1
    if answer4.get() == "6":
        points += 1
    if answer5.get() == "3":
        points += 1
    if points == 5:
        result.set("Bingo! You got everything correct!")
    elif points == 0:
        result.set("Womp! Womp! You got everything wrong ")
    else:
        result.set("Points = " + str(points))
# Add all your questions and widgets here
T = Label(root, text= "QUIZZUP!", font=("Helvetica", 18, "bold"))
T.pack(expand = True)

Q1 = Label(root, text='What ingrident would you not use in a cake ?', font=("Helvetica", 14))
Q1.pack(expand = True)
answer1 = StringVar(value=-1)
a1 = Radiobutton(root, text="Flour",variable=answer1, font=("Helvetica", 14), value=0)
a2 = Radiobutton(root, text="Oninions",variable=answer1, font=("Helvetica", 14), value=1)
a3 = Radiobutton(root, text="Sugar",variable=answer1, font=("Helvetica", 14), value=2)
a4 = Radiobutton(root, text="Frosting",variable=answer1, font=("Helvetica", 14), value=3)
a1.pack(expand = True)
a2.pack(expand = True)
a3.pack(expand = True)
a4.pack(expand = True)


Q2 = Label(root, text='How many prime numbers are there in between 1 to a 100 ?', font=("Helvetica", 14))
Q2.pack(expand = True)
answer2 = (StringVar)
answer2 = StringVar()
entrybox = Entry(root, textvariable= answer2,font=("Helvetica", 14))
entrybox.pack(expand = True)


Q3 = Label(root, text='Does Mars have three moons?', font=("Helvetica", 14))
answer3 = BooleanVar(value=False)
Q3.pack(expand = True)
q3 = Checkbutton(root, text='True', font=("Helvetica", 14), variable=answer3)
q3.pack(expand = True)


Q4 = Label(root, text='How many points is a touchdown worth in american football', font=("Helvetica", 14))
Q4.pack(expand = True)
answer4 = StringVar()
entrybox = Entry(root, textvariable= answer4,font=("Helvetica", 14))
entrybox.pack(expand = True)

Q5 = Label(root, text="Which planet has the most gravity in the solar system", font=("Helvetica",14))
Q5.pack(expand = True)
answer5 = StringVar(value=-1)
q5a1 = Radiobutton(root, text="Earth", variable=answer5, font=("Helvetica",14), value=0)
q5a2 = Radiobutton(root, text="Mercury", variable=answer5, font=("Helvetica",14), value=1)
q5a3 = Radiobutton(root, text="Neptune", variable=answer5, font=("Helvetica",14), value=2)
q5a4 = Radiobutton(root, text="Jupiter", variable=answer5, font=("Helvetica",14), value=3)
q5a1.pack(expand = True)
q5a2.pack(expand = True)
q5a3.pack(expand = True)
q5a4.pack(expand = True)

# This submit button should be at the end of your test
# It is meant to be clicked once the user has answered all questions
submitButton = Button(root, text='Submit Answers', font=("Helvetica", 14),
                      bg='white', command=check_answers)
submitButton.pack(expand = True)

# This results label will display the number of questions answered correctly
# Feel free to change up the code for submitButton and results to make
# the test prettier and individualized!
results = Label(root, textvariable=result)
results.pack(expand = True)

root.mainloop()
