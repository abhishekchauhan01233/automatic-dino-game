import pyautogui
from PIL import Image,ImageGrab
import time

pyautogui.moveTo(145,751,duration=1)
pyautogui.click(145,751,duration=0.5)
pyautogui.press('up')

def Collision(data):
    for i in range(460,520):
        for j in range(157, 190):
            if data[i, j] < 171:
                pyautogui.press('down')
                print('down')
                return 
                
    for i in range(460,540):
        for j in range(205,229):
            if data[i, j] < 100:
                pyautogui.press('up')
                print('up')
                return
    return 
        
while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    Collision(data)

