import pyautogui
from random import randint
import keyboard
import sys

def kb():
    while True:
        if keyboard.is_pressed("a"):
            for n in range(90):
                L=["q","w","e","r","t","y","u","i","o","p","o","s","d"]
                ch=""
                for i in range(8):
                    ch=L[randint(0,12)]+ch
                pyautogui.write(ch, interval=0.001)
                pyautogui.press('enter')
                pyautogui.click()

screenWidth, screenHeight = pyautogui.size()
kb()