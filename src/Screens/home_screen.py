import sys
sys.path.append("..")
from PIL import Image,ImageDraw,ImageFont

class HomeScreen():
    
    def __init__(self, scrollValue, width, height):
        self.scrollValue = scrollValue
        self.width = width
        self.height = height
    
    def render(self):
        screen = Image.new("RGB", (self.width, self.height), "BLACK")
        draw = ImageDraw.Draw(screen)
        font18 = ImageFont.truetype("./Assets/Chicago.ttf",12)

        draw.text((10, self.scrollValue), 'is this working', fill = "WHITE",font=font18)

        return screen

    def scroll(self, offset):
        self.scrollValue += offset