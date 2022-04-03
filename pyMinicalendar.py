#!/bin/python3

"""
    Main file
"""

import tkinter
import calendar
import libs.pyautogui as pyag

#   __________________________________
#   | < Month >  < year(drop list) > |
#   |--------------------------------|
#   |                                |
#   |                                |  200 px
#   |           DAYZ                 |  
#   |                                |
#   |                                |
#   |________________________________|
#                   250 px

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
mousePos = MousePointerPos(0, 0)
mousePos.x, mousePos.y = pyag.position()
# DEBUG:
print(str(mousePos.x) + ", " + str(mousePos.y))

# gets the current screen resolution:
thisScreen = ScreenProperties(0, 0)
thisScreen.width, thisScreen.height = pyag.size()
# DEBUG:
print(str(thisScreen.width) + ", " + str(thisScreen.height))

#   distance = mousePos - borderPos;

#   window.setXpos(mousePos.x - dist.x) # if dist.x < 250px
#   window.setYpos(mousePos.y - dist.y - 200px) # if dist.y < 200px
#   spawnWindowRootAtPos();
#   add widgets();
#
# LOGIC section:
#   create object of class Month now()
#   def <- populate window widgets with Now;
#       this function is used by the <, > and list(year) buttons
#   listen to button and list callbacks;

