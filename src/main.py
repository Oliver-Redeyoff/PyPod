import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch8
from PIL import Image,ImageDraw,ImageFont

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

states = {
    0: "Welcome",
    1: "Home"
}
currentState = 0

def main_loop():
    render()

def render():
    print('Rendering to PyPod')
    print('Rendering ' + states[currentState])
    
    # Clear display.
    disp.clear()

    image = Image.new("RGB", (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image)
    font18 = ImageFont.truetype("./Assets/Chicago.ttf",12) 

    draw.text((5, 5), states[currentState], fill = "BLACK",font=font18)

    disp.ShowImage(image)

    disp.module_exit()

if __name__ == '__main__':
    print(welcomeStr)
    disp.Init()
    main_loop()