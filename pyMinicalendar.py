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

""" Main """

class MousePointerPos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# GUI section:
#   mousePos = GetMousePos()
mousePos = MousePointerPos(0, 0)
mousePos.x, mousePos.y = pyag.position()
print(str(mousePos.x) + ", " + str(mousePos.y))
#   GetDisplayResolution() # with Tk.winfo_screen{height,width}()
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

