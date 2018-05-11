import pyautogui, time

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()

        time.sleep(30)

        pyautogui.moveRel(10, 10, duration=0.2) #ten pixels right/down
        time.sleep(1)
        pyautogui.moveRel(-10, -10, duration=0.2) #ten pixels left/up

except KeyboardInterrupt:
    print('\nDone.')