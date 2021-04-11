class HomeScreen():
    
    def __init__(self, x):
        self.x = x
    
    def render(self):
        print('Rendering home screen')

    def scrollX(self, offset):
        self.x += offset