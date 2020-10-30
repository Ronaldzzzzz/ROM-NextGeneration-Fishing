# main file
import pyautogui
from pynput import mouse
import cv2
import numpy as np


x1 = y1 = x2 = y2 = 0

def on_click(x, y, button, pressed):
    global x1, y1, x2, y2
    if button == mouse.Button.middle:
        if pressed:
            x1 = x
            y1 = y
            print('{} at {}'.format('Pressed Right Click' , (x1, y1)))
        else:
            x2 = x
            y2 = y
            print('{} at {}'.format('Released Right Click' , (x2, y2)))
            print("Start!")
            return False

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()
print(x1, y1)
print(x2, y2)
input("Wait....")

control_mouse = mouse.Controller()
fishing_click_x = ((x2 - x1) * 0.85 + x1)
fishing_click_y = ((y2 - y1) * 0.74 + y1)
print(fishing_click_x, fishing_click_y)
control_mouse.position = (fishing_click_x, fishing_click_y)
input("Wait....")

fishing_icon_x1 = ((x2 - x1) * 0.77 + x1)
fishing_icon_y1 = ((y2 - y1) * 0.62 + y1)
control_mouse.position = (fishing_icon_x1, fishing_icon_y1)
input("Wait....")

fishing_icon_x2 = ((x2 - x1) * 0.92 + x1)
fishing_icon_y2 = ((y2 - y1) * 0.85 + y1)
control_mouse.position = (fishing_icon_x2, fishing_icon_y2)
input("Wait....")

img = pyautogui.screenshot(region=(fishing_icon_x1, fishing_icon_y1, 
                            fishing_icon_x2 - fishing_icon_x1, fishing_icon_y2 - fishing_icon_y1))
open_cv_image = np.array(img) 
# Convert RGB to BGR 
open_cv_image = open_cv_image[:, :, ::-1].copy()
cv2.imshow("icon", open_cv_image)
cv2.waitKey(0)  