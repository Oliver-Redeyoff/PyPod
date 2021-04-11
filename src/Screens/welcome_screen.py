import sys
sys.path.append("..")
from PIL import Image,ImageDraw,ImageFont

class WelcomeScreen():

    def __init__(self, scrollValue, width, height):
        self.scrollValue = scrollValue
        self.width = width
        self.height = height
    
    def render(self):
        screen = Image.open('./Assets/welcomeImg.jpg')
        return screen

    def scroll(self, offset):
        self.scrollValue += offset