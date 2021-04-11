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

        draw.rectangle(xy=[(5, 10 + 20*self.scrollValue-5), (self.width-10, 10 + 20*self.scrollValue+15)], fill="BLUE", width= 5)

        draw.text((10, 10), 'Spotify', fill = "WHITE",font=font18)
        draw.text((10, 30), 'Photos', fill = "WHITE",font=font18)
        draw.text((10, 50), 'Settings', fill = "WHITE",font=font18)

        return screen

    def scroll(self, offset):
        self.scrollValue += offset