import turtle as trtl
import random
import settings
from time import sleep

col = None  # entire solution column that was randomly selected
options = None  # randomized 4 symbols chosen
ordered = None  # ordered 4 symbols chosen
clickedDots = None  # All turtles for the indicator dots

def init():
    global symbols, col, options, ordered

    # According to rules.png
    symbols = [
        [1, 2, 3, 4, 5, 6, 7],
        [8, 1, 7, 9, 10, 6, 11],
        [12, 13, 9, 14, 15, 3, 10],
        [16, 17, 18, 5, 14, 11, 19],
        [20, 19, 18, 21, 17, 22, 23],
        [16, 8, 24, 25, 20, 26, 27]
    ]

    # Pick one of the columns from rules.png aka rows from symbols
    col = random.choice(symbols)

    # Randomly generate 4 images without repeating from col
    options = []
    while len(options) < 4:
        temp = random.choice(col)
        if temp not in options:
            options.append(temp)

    # Calculates order for checking
    calculateOrder()

def bomb():
    init()  # Setup game instance

    global clickedDots

    # Turtle setup
    symbolButtons: [trtl.Turtle] = []  # Left to right, top to bottom
    clickedDots = []
    for i in range(len(options)):
        settings.screenInfo.wn.addshape(f"{options[i]}.gif")
        button = settings.newTurtle(shape=f"{options[i]}.gif")
        button.onclick(lambda x, y, n = i: onButtonClick(x, y, n))  # Worlds sexiest lambda function Approved by Thomas :)
        symbolButtons.append(button)

        # Makes an indicator circle
        miniCircle = settings.newTurtle(shape="circle")
        miniCircle.color("gray")
        miniCircle.resizemode("user")
        miniCircle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        clickedDots.append(miniCircle)

    symbolButtons[0].goto(-62.5, 62.5)
    symbolButtons[1].goto(62.5, 62.5)
    symbolButtons[2].goto(-62.5, -62.5)
    symbolButtons[3].goto(62.5, -62.5)

    offset = 50
    clickedDots[0].goto(-62.5, 62.5 + offset)
    clickedDots[1].goto(62.5, 62.5 + offset)
    clickedDots[2].goto(-62.5, -62.5 + offset)
    clickedDots[3].goto(62.5, -62.5 + offset)

    painter = settings.newTurtle()
    painter.hideturtle()

def onButtonClick(x, y, num):
    global clickedDots, ordered, options
    if ordered[0] == options[num]:  # If the button just clicked is in order
        clickedDots[num].color("lime green")
        ordered.pop(0)  # remove the button just clicked from the order
    else:
        wrong()

def wrong():
    # Indicate incorrect order
    for i in clickedDots:
        i.color("red")
    sleep(1)
    for i in clickedDots:
        i.color("gray")

    calculateOrder()  # Resets order checker

def explode():
    pass

def calculateOrder():
    global ordered, options, col

    ordered = []
    for i in col:
        if i in options:
            ordered.append(i)
