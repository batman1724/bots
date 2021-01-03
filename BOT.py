from pyautogui import *
import win32api
import win32con
import time
import pyautogui
import random
import keyboard
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(3)

click(618,856)

while keyboard.is_pressed('q')==False:
    
    pic=pyautogui.screenshot(region=(489,308,930,660))

    
    width,height=pic.size
    
    for i in range(0,width,5):
        
        for j in range(0,height,5):
            
            r,g,b= pic.getpixel((i,j))
            
            if b==195:
                click(i+489,j+308)
                time.sleep(0.05)
                break

