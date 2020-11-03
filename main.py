# main file
import pyautogui
import time
import os
from pynput import mouse, keyboard

x1 = y1 = x2 = y2 = 0

def on_click(x, y, button, pressed):
    global x1, y1, x2, y2
    if button == mouse.Button.middle:
        if pressed:
            x1 = x
            y1 = y
            print('{} at {}'.format('Pressed Middle Click' , (x1, y1)))
        else:
            x2 = x
            y2 = y
            print('{} at {}'.format('Released Middle Click' , (x2, y2)))
            print("Start!")
            return False

def on_press(key):
    try:
        print(key)
        if(key == keyboard.Key.esc):
            print(key)
            print("Good Bye!")
            return False
    except AttributeError:
        print('special key {0} pressed'.format(key))

if os.path.exists("img/temp.png"):
    os.remove("img/temp.png")

print("Welcome to use RO Mobile: Next Gen Auto Fishing!")
print("Press and drag middle button for the screen...")

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()

print(x1, y1)
print(x2, y2)
input("Wait....")

control_mouse = mouse.Controller()
fishing_click_x = int((x2 - x1) * 0.85 + x1)
fishing_click_y = int((y2 - y1) * 0.74 + y1)
control_mouse.position = (fishing_click_x, fishing_click_y)
#input("Wait....")

fishing_icon_x1 = int((x2 - x1) * 0.77 + x1)
fishing_icon_y1 = int((y2 - y1) * 0.62 + y1)
control_mouse.position = (fishing_icon_x1, fishing_icon_y1)
#input("Wait....")

fishing_icon_x2 = int((x2 - x1) * 0.92 + x1)
fishing_icon_y2 = int((y2 - y1) * 0.85 + y1)
control_mouse.position = (fishing_icon_x2, fishing_icon_y2)
#input("Wait....")
listener.stop()

print("Fishing Click at ", fishing_click_x, fishing_click_y)
print("Fishing icon range: ", fishing_icon_x1, fishing_icon_y1, fishing_icon_x2, fishing_icon_y2 )
print(fishing_icon_x1, fishing_icon_y1, fishing_icon_x2 - fishing_icon_x1, fishing_icon_y2 - fishing_icon_y1)
print("Make sure the range is correct! If not, press Ctrl+C to halt the program and re-run it.")
print("The program will start at 3 second, do not using your mouse during the time!")
time.sleep(3)

count = 0
while True :
    if pyautogui.locateOnScreen('img/0.png', region=(fishing_icon_x1, fishing_icon_y1, fishing_icon_x2 - fishing_icon_x1, fishing_icon_y2 - fishing_icon_y1), confidence = 0.7) != None:
        print("Start Fishing!")
        pyautogui.click(fishing_click_x, fishing_click_y)
        start = time.time()
        while True:
            if pyautogui.locateOnScreen('img/1.png', region=(fishing_icon_x1, fishing_icon_y1, fishing_icon_x2 - fishing_icon_x1, fishing_icon_y2 - fishing_icon_y1), confidence = 0.6) != None:
                print("Pull!")
                pyautogui.click(fishing_click_x, fishing_click_y)
                time.sleep(0.01)
                pyautogui.click(fishing_click_x, fishing_click_y)
                break
            else:
                if(time.time() - start > 10):
                    print("Fishing Failed...")
                    break
                print("Not ready....")
                time.sleep(0.1)
    else:
        print("Not ready......")
        count += 1
        if(count == 5):
            im = pyautogui.screenshot(region=(fishing_icon_x1, fishing_icon_y1, fishing_icon_x2 - fishing_icon_x1, fishing_icon_y2 - fishing_icon_y1))
            im.save("img/temp.png")
            print("Save Picture...")
            count = 50
        time.sleep(0.5)