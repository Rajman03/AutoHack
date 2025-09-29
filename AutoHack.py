import pyautogui
import time
import getpass

aktualny_uzytkownik = getpass.getuser()

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('cmd')
time.sleep(0.2)
pyautogui.press('enter')
time.sleep(0.2)
pyautogui.typewrite(f'net user ')
time.sleep(0.2)
pyautogui.press('enter')
time.sleep(0.2)