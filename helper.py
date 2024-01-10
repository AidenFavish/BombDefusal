import settings
import menu
import bomb
import turtle as trtl
import summary

def keySetup(wn):  # Key actions go here
    wn.onkeypress(one, "1")
    wn.onkeypress(two, "2")
    wn.onkeypress(three, "3")
    wn.onkeypress(quitGame, "9")
    wn.listen()

def runCurrScreen(args=None):
    if args is None:
        settings.screenInfo.currScreen()
    else:
        settings.screenInfo.currScreen(args)

def one():
    if settings.screenInfo.currScreen == menu.menu:  # Play easy mode
        menu.cleanup()
        settings.screenInfo.currScreen = bomb.bomb
        runCurrScreen([1, "EASY", 1, 45])
    elif settings.screenInfo.currScreen == summary.summarize:  # Play again
        summary.cleanup()
        settings.screenInfo.currScreen = bomb.bomb

        # Locate correct difficulty and run new game
        if summary.diff == "EASY":
            runCurrScreen([1, "EASY", 1, 45])
        elif summary.diff == "MEDIUM":
            runCurrScreen([3, "MEDIUM", 3, 60])
        else:
            runCurrScreen([1, "HARD", 3, 60])

def two():
    if settings.screenInfo.currScreen == menu.menu:  # Play medium mode
        menu.cleanup()
        settings.screenInfo.currScreen = bomb.bomb
        runCurrScreen([3, "MEDIUM", 3, 60])
    elif settings.screenInfo.currScreen == summary.summarize:  # Go to main menu
        summary.cleanup()
        settings.screenInfo.currScreen = menu.menu
        runCurrScreen()

def three():
    if settings.screenInfo.currScreen == menu.menu:  # Play hard mode
        menu.cleanup()
        settings.screenInfo.currScreen = bomb.bomb
        runCurrScreen([1, "HARD", 3, 60])

def quitGame():
    if settings.screenInfo.currScreen == menu.menu:  # Quit application
        exit()
    