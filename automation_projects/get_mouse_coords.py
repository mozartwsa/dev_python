#! python3
# mouseNow.py - Displays the mouse cursor's current position.

#install pyauto gui: 'pip install pyautogui'
import pyautogui
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = '(' + str(x).rjust(4) + ', ' + str(y).rjust(4) + ')'
        print(positionStr)
        print('\b' * len(positionStr), end='', flush='True')
except KeyboardInterrupt:
    print('\nDone.')