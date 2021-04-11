import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch8
from PIL import Image,ImageDraw,ImageFont
import screenFactory

welcomeStr = """
  ___      ___         _         __   _ 
 | _ \_  _| _ \___  __| |  __ __/  \ / |
 |  _/ || |  _/ _ \/ _` |  \ V / () || |
 |_|  \_, |_| \___/\__,_|   \_/ \__(_)_|
      |__/                              
"""

# screen variables
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0
disp = LCD_1inch8.LCD_1inch8()
Lcd_ScanDir = LCD_1inch8.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
refreshRate = 20

headerHeight = 20

states = {
    0: "Welcome",
    1: "Home"
}
welcomeTimer = 0

def setState(stateId):
    global disp, currentState, currentScreenRef

    print("Setting state to " + states[stateId])
    currentState = stateId
    currentScreenRef = screenFactory.getScreenRef(currentState, disp.width, disp.height-headerHeight)

def main_loop():
    global currentScreenRef, welcomeTimer, refreshRate

    render()
    
    if(currentState == 0):
        if (welcomeTimer >= refreshRate):
            setState(1)
            welcomeTimer = 0
    
    welcomeTimer += 1

    time.sleep(1/refreshRate)
    main_loop()

def render():
    global disp, currentScreenRef

    screen = Image.new("RGB", (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(screen)
    font18 = ImageFont.truetype("./Assets/Chicago.ttf",12)

    draw.text((1, 1), states[currentState], fill = "BLACK",font=font18)

    screenImg = currentScreenRef.render()
    if(currentState == 0):
        screen.paste(screenImg, (0, 0))
    else:
        screen.paste(screenImg, (0, headerHeight))

    disp.ShowImage(screen)

if __name__ == '__main__':
    print(welcomeStr)
    disp.Init()
    disp.clear()
    setState(0)
    main_loop()