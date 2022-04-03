#!/bin/python3

"""
    Main file
"""

import tkinter as tk
import calendar
import libs.pyautogui as pyag

#   ,_________________________________
#   | < Month >  < year(drop list) > |
#   |--------------------------------|
#   |                                |
#   |                                |  200 px
#   |           DAYZ                 |  
#   |                                |
#   |                                |
#   |________________________________|
#                   250 px
#   .  # this point roughly indicates the cursor position,
#      # whereas the comma indicates the window Root coordinate.

""" Classes """

class MousePointerPos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ScreenProperties:
    def __init__(self, x, y):
        self.width  = x
        self.height = y


""" START OF MAIN """


""" GUI section: """

# Gets the current ABSOLUTE mouse coordinates:
cursorPos = MousePointerPos(0, 0)
cursorPos.x, cursorPos.y = pyag.position()
# DEBUG:
print(str(cursorPos.x) + ", " + str(cursorPos.y))

# gets the current screen resolution:
thisScreen = ScreenProperties(0, 0)
thisScreen.width, thisScreen.height = pyag.size()
# DEBUG:
print(str(thisScreen.width) + ", " + str(thisScreen.height))

# computes how much the cursor is distant from the screen border.
# In most cases the clock is in the lower right corner, so the root
# needs to be moved to the left by a certain amount. In other cases
# this is not needed (e.g.: when the clock is in the upper right corner).
cursorDistance_X = cursorPos.x - thisScreen.width
cursorDistance_Y = cursorPos.y - thisScreen.height
# DEBUG:
print(str(cursorDistance_X) + ", " + str(cursorDistance_Y))

# create a root window
root = tk.Tk()
root.wm_title("MiniCalendar")
root.geometry("250x200")
frame = tk.Frame(root)
root.config(bg="#000000")
frame.pack()

#from tkinter import * 
# TkForm = Tk()
#
#  #Set Height and Width of Window
#   TkForm.geometry("350x150") 
#
#    #Set the Title according to desire
#     TkForm.title("TK Size in Python")
#
#      TkForm.mainloop()

#   window.setXpos(cursorPos.x - dist.x) # if dist.x < 250px
#   window.setYpos(cursorPos.y - dist.y - 200px) # if dist.y < 200px
#   spawnWindowRootAtPos();
#   add widgets();
#
# LOGIC section:
#   create object of class Month now()
#   def <- populate window widgets with Now;
#       this function is used by the <, > and list(year) buttons
#   listen to button and list callbacks;

root.mainloop()
