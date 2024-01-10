import settings
import menu
import bomb
import turtle as trtl

def keySetup(wn):  # Key actions go here
    wn.onkeypress(easy, "1")
    wn.onkeypress(medium, "2")
    wn.onkeypress(hard, "3")
    wn.onkeypress(quitGame, "9")
    wn.listen()

def runCurrScreen(args=None):
    if args is None:
        settings.screenInfo.currScreen()
    else:
        settings.screenInfo.currScreen(args)

def easy():
    if settings.screenInfo.currScreen == menu.menu:
        menu.cleanup()
        settings.screenInfo.currScreen = bomb.bomb
        runCurrScreen([1, "EASY", 1, 45])

def medium():
    if settings.screenInfo.currScreen == menu.menu:
        menu.cleanup()
        settings.screenInfo.currScreen = bomb.bomb
        runCurrScreen([3, "MEDIUM", 3, 60])

def hard():
    if settings.screenInfo.currScreen == menu.menu:
        menu.cleanup()
        settings.screenInfo.currScreen = bomb.bomb
        runCurrScreen([1, "HARD", 3, 60])

def quitGame():
    if settings.screenInfo.currScreen == menu.menu:
        exit()
    