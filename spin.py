import pyautogui
from time import time

if __name__ == '__main__':
    start = time()
    speed = 0.0
    while True:
        pyautogui.moveTo(950, 300, speed) # 上端
        pyautogui.moveTo(860, 270, speed)
        pyautogui.moveTo(750, 240, speed)
        pyautogui.moveTo(700, 225, speed) # 左端
        pyautogui.moveTo(750, 190, speed)
        pyautogui.moveTo(860, 170, speed)
        pyautogui.moveTo(950, 150, speed) # 下端
        pyautogui.moveTo(1010, 170, speed)
        pyautogui.moveTo(1060, 190, speed)
        pyautogui.moveTo(1100, 225, speed) # 右端
        pyautogui.moveTo(1060, 240, speed)
        pyautogui.moveTo(1010, 270, speed)
        if abs(start - time()) >= 5:
            break
    print("5秒経過しました")
