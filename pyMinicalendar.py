#!/bin/python3

"""
    Main file
"""

import Tk, calendar

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

# GUI section:
#   mousePos = GetMousePos()
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

