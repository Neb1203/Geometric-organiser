import pygame
import pygame_menu
from MainGameplay import MainGameplay
from Window import Window

subTheme = pygame_menu.themes.THEME_SOLARIZED

mainTheme = pygame_menu.themes.THEME_ORANGE
window = Window()
# subWindow = (300,200)

def setDifficulty(value, difficulty):
    # Do the job here
    # Window(50)
    pass

def screenSize(screenSize):
    Window.newScreenSize = screenSize

def userName(userName):
    print(userName)
def email(email):
    pass
def pickGameMode(value, gameMode):
    global gameModeSelected
    gameModeSelected = gameMode
def startGame():
    # Do the job here !
    if gameModeSelected == False:
        MainGameplay()
    elif gameModeSelected == True:
        print("cum")
surface = window.surface

startScreen = pygame_menu.Menu('Start Screen',
                               window.vduDimensions[0],
                               window.vduDimensions[1],
                            theme=mainTheme)
playMenu = pygame_menu.Menu('Play',
                            window.vduDimensions[0],
                            window.vduDimensions[1],
                            theme=mainTheme)
settings = pygame_menu.Menu('settings',
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
# profileCreation = pygame_menu.Menu('Create a profile',
#                                    subWindow[0],
#                                    subWindow[1],
#                                    theme=subTheme)

#create buttons for startScreen
startScreen.add.label("Geometric Organiser")
startScreen.add.button('Go to main menu', mainMenu)
startScreen.add.button('Change player profile', playerProfile)
startScreen.add.button('Quit', pygame_menu.events.EXIT)

#create buttons for mainMenu
mainMenu.add.button('Play', playMenu)
mainMenu.add.button('Settings', settings)
mainMenu.add.button('Back', pygame_menu.events.BACK)

#settings
settings.add.range_slider('Set screen size',
                          range_values=[1,2,3,4,5],
                          default=3,
                          onchange=screenSize)

#Create buttons for playMenu
playMenu.add.selector('Gamemode : ', [('Campaign', True), ('Endless', False)], onchange = pickGameMode)
playMenu.add.selector('Difficulty :', [('Hard', 1), ('Normal', 2), ('Easy', 3)], onchange = setDifficulty)
playMenu.add.button('Start Game', startGame)
playMenu.add.button('back', pygame_menu.events.BACK)

#buttons for player profiles
# playerProfile.add.button('Create a profile', profileCreation)
playerProfile.add.button('back', pygame_menu.events.BACK)

#buttons for profile creation
# profileCreation.add.text_input('User Name :', onchange=userName)
# profileCreation.add.text_input('Email :', onchange=email)

#world map


if startScreen.is_enabled():
    startScreen.mainloop(surface)