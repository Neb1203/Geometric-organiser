import pygame
import pygame_menu
from Window import Window
from MainGameplay import MainGameplay


mainTheme = pygame_menu.themes.THEME_BLUE
window = Window()
def set_difficulty(value, difficulty):
    # Do the job here
    print(difficulty)

def startGame():
    # Do the job here !
    # MainGameplay()
    pass

surface = window.setMode

startScreen = pygame_menu.Menu('Start Screen',
                               window.vduDimensions[0],
                               window.vduDimensions[1],
                            theme=mainTheme)
playMenu = pygame_menu.Menu('Play',
                            window.vduDimensions[0],
                            window.vduDimensions[1],
                            theme=mainTheme)
playerProfile = pygame_menu.Menu('Change player Profiles',
                            window.vduDimensions[0],
                            window.vduDimensions[1],
                            theme=mainTheme)
mainMenu = pygame_menu.Menu('Main Menu',
                            window.vduDimensions[0],
                            window.vduDimensions[1],
                            theme=mainTheme)

#create buttons for startScreen
startScreen.add.label("Geometric Organiser")
startScreen.add.button('Go to main menu', mainMenu)
startScreen.add.button('Change player profile', playerProfile)
startScreen.add.button('Quit', pygame_menu.events.EXIT)

#create buttons for mainMenu
mainMenu.add.button('Play', playMenu)
mainMenu.add.button('Back', pygame_menu.events.BACK)

#Create buttons for playMenu
playMenu.add.selector('Difficulty :', [('Hard', 1), ('Normal', 2), ('Easy', 3)], onchange=set_difficulty)
playMenu.add.button('Start Game', startGame())
playMenu.add.button('back', pygame_menu.events.BACK)

#buttons for player profiles
playerProfile.add.text_input('Name :', default='Insert Name here')
playerProfile.add.button('back', pygame_menu.events.BACK)

if startScreen.is_enabled():
    startScreen.mainloop(surface)