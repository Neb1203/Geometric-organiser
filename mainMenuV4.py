import pygame
import pygame_menu
from Window import Window
# import MainGameplay
from pygame_menu.examples import create_example_window

from typing import Tuple, Any, Optional, List


mainTheme = pygame_menu.themes.THEME_BLUE
window = Window()

def set_difficulty(value, difficulty):
    # Do the job here !
    print(difficulty)

def startGame():
    # Do the job here !
    # MainGameplay()
    pass
surface: Optional['pygame.Surface'] = None
surface = create_example_window('Example - Game Selector', window.vduDimensions)

startScreen = pygame_menu.Menu('Start Screen', 400, 300,
                            theme=mainTheme)
playMenu = pygame_menu.Menu('Play', 400, 300,
                            theme=mainTheme)

#create buttons for startScreen
startScreen.add.text_input('Name :', default='Insert Name here')
startScreen.add.button('Go to main menu', playMenu)
startScreen.add.button('Quit', pygame_menu.events.EXIT)

#Create buttons for playMenu
playMenu.add.selector('Difficulty :', [('Hard', 1), ('Normal', 2), ('Easy', 3)], onchange=set_difficulty)
playMenu.add.button('Start Game', startGame())
# playMenu.add.button('back; #go back a menu


if startScreen.is_enabled():
    startScreen.mainloop(surface)
if playMenu.is_enabled():
    playMenu.mainloop(surface)