import helper
import turtle as trtl
import settings
import menu

settings.init(menu.menu) # landing page

wn = trtl.Screen()
helper.keySetup(wn)
wn.mainloop()
