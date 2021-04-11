class WelcomeScreen():

    def __init__(self, x):
        self.x = x
    
    def render(self):
        print('Rendering welcome screen')

    def scrollX(self, offset):
        self.x += offset