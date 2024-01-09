import helper
import turtle as trtl
import settings
import menu

settings.init(menu.menu)

wn = trtl.Screen()
helper.keySetup(wn)
wn.mainloop()