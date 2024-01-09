import settings
import menu

def keySetup(wn):  # Key actions go here
    wn.onkeypress(menu.menu, "a")
    wn.onkeypress(runCurrScreen, "b")
    wn.listen()

def runCurrScreen():
    settings.screenInfo.currScreen()
    