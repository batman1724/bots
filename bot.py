from pyautogui import *
import pyautogui
import win32api,win32con
import time
import keyboard
import random


#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#x:438, y:604- LEFT TILE
#555,603- LEFT CENTRE TILE
#678,623  - RIGHT CENTRE TILE
#792,617 - RIGHT TILE



#link for game that it it works on.(played on large screen but not ingame full screen.
#https://www.agame.com/game/magic-piano-tiles
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('q')==False:
    if pyautogui.pixel(438,604)[0]==0:
        click(438,609)
    if pyautogui.pixel(555,603)[0]==0:
        click(555,608)
    if pyautogui.pixel(678,623)[0]==0:
        click(678,623)
    if pyautogui.pixel(792,617)[0]==0:
        click(792,617)
