#using the mouse to draw a spiral on paint

import pyautogui, time

time.sleep(3)
pyautogui.click()

distance = 2000

while distance > 2000:
    pyautogui.dragRel(distance, 0, duration=0.2) #move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2) #move down
    pyautogui.dragRel(-distance, 0, duration=0.2) #move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2) #move up


