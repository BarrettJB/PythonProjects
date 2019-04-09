import pyautogui
try:
  while True:
    x, y = pyautogui.position()
    posStr = 'X: ' + str(x).rjust(6) + 'Y: ' + str(y).rjust(6)
    print(posStr, end='')
    print('\b' * len(posStr), end='', flush=True)
except KeyboardInterrupt:
  print('\n')