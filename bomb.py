import turtle as trtl
import random
import settings
from time import sleep

col = None  # entire solution column that was randomly selected
options = None  # randomized 4 symbols chosen
ordered = None  # ordered 4 symbols chosen
clickedDots = None  # All turtles for the indicator dots
chances = 1  # number of times you can get it wrong before it explodes
difficulty = ""  # Difficulty mode
puzzlesLeft = 1  # Number of puzzles left for this difficulty mode
timerSpeed = 1  # Rate at which timer decreases (increases after getting it wrong)
timeLeft = 100  # Time left in seconds on the countdown
timerTurtle = None  # Turtle object for the timer
pl = None  # Holds the turtle for the puzzles left text
turtleBin = []  # Holds all the turtles for easy disposal

def init():
    global col, options, ordered

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

def bomb(data=None):
    # Pre-setup
    if data is not None:
        global chances, difficulty, puzzlesLeft, timeLeft
        chances = data[0]
        difficulty = data[1]
        puzzlesLeft = data[2]
        timeLeft = data[3]

    init()  # Setup game instance

    global clickedDots, timerTurtle, pl, turtleBin

    # Draw the back border
    frame = settings.newTurtle()
    frame.hideturtle()
    frame.pensize(0)
    frame.fillcolor(0.05, 0.05, 0.25)
    frame.begin_fill()
    settings.drawSquare(frame, -150, -150, 300, 300)
    frame.end_fill()
    turtleBin.append(frame)

    # Turtle setup
    symbolButtons: [trtl.Turtle] = []  # Left to right, top to bottom
    clickedDots = []
    for i in range(len(options)):
        settings.screenInfo.wn.addshape(f"{options[i]}.gif")
        button = settings.newTurtle(shape=f"{options[i]}.gif")
        button.onclick(lambda x, y, n = i: onButtonClick(x, y, n))  # Worlds sexiest lambda function Approved by Thomas :)
        symbolButtons.append(button)
        turtleBin.append(button)

        # Makes an indicator circle
        miniCircle = settings.newTurtle(shape="circle")
        miniCircle.color("gray")
        miniCircle.resizemode("user")
        miniCircle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        clickedDots.append(miniCircle)
        turtleBin.append(miniCircle)

    # Arranges the symbols
    symbolButtons[0].goto(-62.5, 62.5)
    symbolButtons[1].goto(62.5, 62.5)
    symbolButtons[2].goto(-62.5, -62.5)
    symbolButtons[3].goto(62.5, -62.5)

    # Aranges the indicator circles
    offset = 55
    clickedDots[0].goto(-62.5, 62.5 + offset)
    clickedDots[1].goto(62.5, 62.5 + offset)
    clickedDots[2].goto(-62.5, -62.5 + offset)
    clickedDots[3].goto(62.5, -62.5 + offset)

    # Set up timer turtle
    timerTurtle = settings.newTurtle()
    timerTurtle.hideturtle()
    timerTurtle.up()
    timerTurtle.goto(150, 200)
    timerTurtle.color("red")
    handleCountdown()
    turtleBin.append(timerTurtle)

    # Puzzles left
    pl = settings.newTurtle()
    pl.hideturtle()
    pl.up()
    pl.goto(150, 170)
    pl.color("white")
    pl.write(f"Puzzles left: {puzzlesLeft}", font=("Arial", 20, "normal"))
    turtleBin.append(pl)

def onButtonClick(x, y, num):
    global clickedDots, ordered, options
    if ordered[0] == options[num]:  # If the button just clicked is in order
        clickedDots[num].color("lime green")
        ordered.pop(0)  # remove the button just clicked from the order

        if len(ordered) == 0:  # Check that all buttons have been pressed
            defused()

    else:
        wrong()

def wrong():
    global clickedDots, chances, timerSpeed

    # Indicate incorrect order
    for i in clickedDots:
        i.color("red")
    sleep(1)
    for i in clickedDots:
        i.color("gray")

    calculateOrder()  # Resets order checker

    chances -= 1
    timerSpeed *= 2
    if chances == 0:
        explode()

def explode():  # Too many failed attempts
    print("explode")

def defused():  # Correct order fully entered
    global pl, puzzlesLeft, timerSpeed

    # Update puzzles left
    puzzlesLeft -= 1
    pl.clear()
    pl.write(f"Puzzles left: {puzzlesLeft}", font=("Arial", 20, "normal"))

    if puzzlesLeft <= 0:
        timerSpeed = 0  # get timer to stop ticking
        print("Complete")
    else:  # Start next puzzle
        cleanup()
        bomb()


def calculateOrder():  # Calculates what the order the buttons should be pressed in
    global ordered, options, col

    ordered = []
    for i in col:
        if i in options:
            ordered.append(i)

def handleCountdown():
    global timerSpeed, timeLeft, timerTurtle
    wn = settings.screenInfo.wn  # Get window

    if timerSpeed == 0:  # timerSpeed will be 0 if the user finishes the game early
        return

    timerTurtle.clear()
    if timeLeft <= 0:  # If the user runs out of time
        timerTurtle.write(f"TIME LEFT: 0 s", font=("Arial", 20, "bold"))
        explode()
    else:
        timerTurtle.write(f"TIME LEFT: {timeLeft} s", font=("Arial", 20, "bold"))
        timeLeft -= timerSpeed
        wn.ontimer(handleCountdown, 1000)

def cleanup():
    global turtleBin

    for i in turtleBin:
        i.hideturtle()
        i.clear()

    turtleBin = []
