import Screens.welcome_screen as welcome_screen
import Screens.home_screen as home_screen

def getScreenRef(screenId, width, height):
    if screenId == 0: return welcome_screen.WelcomeScreen(0, width, height)
    if screenId == 1: return home_screen.HomeScreen(0, width, height)