import turtle as trtl
import random
import settings

symbols = None
col = None
options = None

def init():
    global symbols, col, options

    # According to rules.png
    symbols = [
        [1, 2, 3, 4, 5, 6, 7],
        [8, 1, 7, 9, 10, 6, 11],
        [12, 13, 9, 14, 15, 3, 10],
        [16, 17, 18, 5, 14, 11, 19],
        [20, 19, 18, 21, 17, 22, 23],
        [16, 8, 24, 25, 20, 26, 27]
    ]

    # Pick one of the columns from rules.png
    col = random.choice(symbols)

    # Randomly generate 4 images without repeating from col
    options = []
    while len(options) < 4:
        temp = random.choice(col)
        if temp not in options:
            options.append(temp)

def bomb():
    init()  # Setup game instance

    # Turtle setup
    symbolButtons = []  # Left to right, top to bottom
    for i in options:
        settings.screenInfo.wn.addshape(f"{i}.gif")
        symbolButtons.append(settings.newTurtle(shape=f"{i}.gif"))

    painter = settings.newTurtle()
    painter.hideturtle()

    
