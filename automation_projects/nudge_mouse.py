import pyautogui, time

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()

        time.sleep(5)

        pyautogui.moveRel(x+0.1, y+0.1, duration=0.2)
        time.sleep(1)
        pyautogui.moveRel(x-0.1, y-0.1, duration=0.2)

except KeyboardInterrupt:
    print('\nDone.')