import settings
import menu
import bomb
import turtle as trtl

def keySetup(wn):  # Key actions go here
    wn.onkeypress(play, "1")
    wn.onkeypress(quitGame, "2")
    wn.listen()

def runCurrScreen():
    settings.screenInfo.currScreen()

def play():
    if settings.screenInfo.currScreen == menu.menu:
        menu.cleanup()
        settings.screenInfo.currScreen = bomb.bomb
        runCurrScreen()

def quitGame():
    exit()
    