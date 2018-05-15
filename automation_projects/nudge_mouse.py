import pyautogui, time

pyautogui.FAILSAFE = False

print('Press Ctrl-C to quit.')
try:
    while True:
        #x, y = pyautogui.position()

        pyautogui.press('ctrlright')

        time.sleep(10)
        #print(str(time.clock()))

        #pyautogui.moveRel(100, 100, duration=0.2) #hundred pixels right/down
        #time.sleep(1)
        #pyautogui.moveRel(-100, -100, duration=0.2) #hundred pixels left/up
        pyautogui.press('ctrlleft')

except KeyboardInterrupt:
    print('\nDone.')