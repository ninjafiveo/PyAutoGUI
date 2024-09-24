import pyautogui
import time

# Move the Mouse
pyautogui.moveTo(919, 1056, 1)
pyautogui.click(919, 1056)
pyautogui.moveTo(253, 61, .01)
pyautogui.click(253, 61)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('www.github.com/ninjafiveo')
time.sleep(.1)
pyautogui.press('enter')
time.sleep(1)
screenshot = pyautogui.screenshot("screenshot.png")




while True:
    current_mouse_position = pyautogui.position()
    time.sleep(1)
    print(current_mouse_position)
