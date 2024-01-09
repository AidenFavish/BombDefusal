import helper
import turtle as trtl
import settings
import menu

wn = trtl.Screen()

settings.init(menu.menu, wn) # landing page

helper.keySetup(wn)

wn.bgcolor("black")

wn.mainloop()
