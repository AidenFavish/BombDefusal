import turtle as trtl

class ScreenInfo():
    # Module that stores important screen changing info and can be passed by reference
    def __init__(self, first):
        self.isPlaying = True
        self.currScreen = first

def newTurtle() -> trtl.Turtle:
    # Create fresh turtle
    t = trtl.Turtle()
    t.speed(0)
    t.pensize(5)
    t.hideturtle()
    return t

def init(first):
    global screenInfo
    screenInfo = ScreenInfo(first)