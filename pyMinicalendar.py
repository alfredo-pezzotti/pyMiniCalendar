#!/bin/python3

"""
    Main file

    pyMiniCalendar is a basic calendar designed to be used with ultra 
    lightweight Desktop Environments/Window Managers requiring only
    python3 and tkinter to be run: everything else is self-contained.
    
    This file is invoked by the the other python script, the Handler,
    and creates the calendar window, populating it with the correct Month
    object.
"""

import tkinter as tk
import calendar, datetime
import libs.pyautogui as pyag

#   ,_________________________________
#   | < Month >o < year(drop list) > |
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
#      # The character "o" is a button to set time to now

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

# DEBUG:
debug_ON = True

""" GUI section: """

# defines the basic window geometry:
windowSize_X = 250
windowSize_Y = 200

# Gets the current ABSOLUTE mouse coordinates:
cursorPos = MousePointerPos(0, 0)
cursorPos.x, cursorPos.y = pyag.position()

# DEBUG:
if debug_ON:
    print("1 " + str(cursorPos.x) + ", " + str(cursorPos.y))

# gets the current screen resolution:
thisScreen = ScreenProperties(0, 0)
thisScreen.width, thisScreen.height = pyag.size()

# DEBUG:
if debug_ON:
    print("2 "+ str(thisScreen.width) + ", " + str(thisScreen.height))

# computes how much the cursor is distant from the screen border.
# In most cases the clock is in the lower right corner, so the root
# needs to be moved to the left by a certain amount. In other cases
# this is not needed (e.g.: when the clock is in the upper right corner).
cursorDistance_X = abs(cursorPos.x - thisScreen.width)
cursorDistance_Y = abs(cursorPos.y - thisScreen.height)

# DEBUG:
if debug_ON:
    print("3 " + str(cursorDistance_X) + ", " + str(cursorDistance_Y))

# create a root window
root = tk.Tk()
root.wm_title("MiniCalendar")
root.geometry(str(windowSize_X) + "x" + str(windowSize_Y))


# set the window position

# the offset is used to skip over/under the tray:
offset_Y = 40
if cursorDistance_X < windowSize_X:
    # we're here if we are near the right edge of the screen
    windowPos_X = cursorPos.x - cursorDistance_X - (windowSize_X - cursorDistance_X)
else:
    windowPos_X = cursorPos.x
if cursorDistance_Y < windowSize_Y:
    # we're here if we are near the bottom edge of the screen
    windowPos_Y = cursorPos.y - cursorDistance_Y - (windowSize_Y + offset_Y - cursorDistance_Y)
else:
    windowPos_Y = cursorPos.y + offset_Y

# DEBUG:
if debug_ON:
    print("4 " + str(windowPos_X) + ", " + str(windowPos_Y))

root.geometry("+" + str(windowPos_X) + "+" + str(windowPos_Y))
# adds a frame
frame = tk.Frame(root)
root.config(bg="#000000")
frame.pack()
# adds the top frame. It will contain the Month and Year items:
topFrame = tk.Frame(root)
topFrame.pack(side="top")
#adds the bottom frame, it will contain the Dayz items:
bottomFrame = tk.Frame(root)
bottomFrame.pack(side="bottom")

# creates an object of class datetime.Date now()
rightNowDate = datetime.datetime.now()
currDay   = rightNowDate.day
currMonth = rightNowDate.month
currYear  = rightNowDate.year

# creates a calendar object:
currCalendar = calendar.Calendar(firstweekday = 0)  # first weekday is Monday

# returns an iterator for the month month (1–12) in the year year. 
# This iterator will return all days (as datetime.date objects) for the month 
# and all days before the start of the month or after the end of the month that 
# are required to get a complete week:
currMonthIterator = currCalendar.itermonthdates(currYear, currMonth)

# DEBUG:
# this will print a horrible, unformatted calendar on the terminal:
if debug_ON:
    print(str(rightNowDate.now()) + ", " + str(currMonthIterator))
    i = 0
    for day in currMonthIterator:
        print(str(day.day) + " ", end="")
        i += 1
        if i == 7:
            print("\n")
            i = 0


#   add widgets();
#
# LOGIC section:
#   
#   def <- populate window widgets with Now;
#       this function is used by the <, > and list(year) buttons
#   listen to button and list callbacks;

root.mainloop()
