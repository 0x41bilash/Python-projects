'''This fun python program is to creat an AFK bot which moves the cursor every 2 seconds to random coordinates
Credits to @b001ean from Tiktok'''

# install pyautogui using pip if this is the first time using pyautogui library

import pyautogui as pag
import random
import time

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)
    time.sleep(2)
