import time
import pyautogui

time.sleep(3600)
pyautogui.keyDown("win")
pyautogui.press("d")
pyautogui.keyUp("win")
time.sleep(2)
pyautogui.keyDown("alt")
pyautogui.press("f4")
pyautogui.keyUp("alt")
time.sleep(2)
pyautogui.press("enter")
