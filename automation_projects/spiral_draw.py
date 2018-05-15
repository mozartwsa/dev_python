#using the mouse to draw a spiral on paint

import pyautogui, time

pyautogui.FAILSAFE = True

time.sleep(3)
pyautogui.click()

distance = 200
try:

    while distance > 100:
        pyautogui.dragRel(distance, 0, duration=1) #move right
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=1) #move down
        pyautogui.dragRel(-distance, 0, duration=1) #move left
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=1) #move up

except KeyboardInterrupt:
    print('\nDone.')


