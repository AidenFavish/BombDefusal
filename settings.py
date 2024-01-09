import turtle as trtl

class ScreenInfo():
    # Module that stores important screen changing info and can be passed by reference
    def __init__(self, first, wn):
        self.isPlaying = True
        self.currScreen = first
        self.wn = wn

def init(first, wn):
    global screenInfo
    screenInfo = ScreenInfo(first, wn)
    first()

def newTurtle(shape=None) -> trtl.Turtle:
    # Create fresh turtle
    if shape is None:
        t = trtl.Turtle()
    else:
        t = trtl.Turtle(shape=shape)
    t.speed(0)
    t.pensize(5)
    t.penup()
    t.hideturtle()
    return t

def drawSquare(painter: trtl.Turtle, bottomLeftX, bottomLeftY, width, height):
    old = [painter.xcor(), painter.ycor()]

    painter.up()
    painter.goto(bottomLeftX, bottomLeftY)
    painter.down()
    painter.setheading(90)
    for _ in range(2):
        painter.forward(height)
        painter.right(90)
        painter.forward(width)
        painter.right(90)

    painter.up()
    painter.goto(old[0], old[1])
