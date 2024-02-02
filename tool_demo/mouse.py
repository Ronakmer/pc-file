import pyautogui

for i in range(1000):
    print(i)
    pyautogui.moveTo(100, 100, duration = 1)
    pyautogui.moveTo(200, 200, duration = 2)
    pyautogui.moveTo(300, 300, duration = 3)
    pyautogui.moveTo(400, 400, duration = 4)
    