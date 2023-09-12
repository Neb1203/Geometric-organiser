import pygame
import pygame_menu

from GameStateEnum import GameStateEnum
from GridDraw import Tetris
from Window import Window


class Menus:

    # game = Tetris(10, 20)
    upcomingFiguresDisplay = pygame.Surface((150, 450))

    hudsDefaultColors = (255, 255, 255)

    def __init__(self):
        self.upcomingFiguresDisplay.fill(Menus.hudsDefaultColors)
        self.tetris = Tetris(10, 20)

    def quit(self):
        self.pause_menu.disable()
        self.pause_menu.clear()

    def open(self, w: Window):
        print("def pauseMenu")
        # Create a pause menu
        self.pause_menu = pygame_menu.Menu('Pause Menu', w.vduDimensions[0], w.vduDimensions[1], theme=w.mainTheme)

        # Add items to the pause menu (e.g., resume and quit options)
        self.pause_menu.add.button('Resume', self.resume)
        self.pause_menu.add.button('Restart', self.restart)
        self.pause_menu.add.button('Quit', self.quit)
        # Run the pause menu
        self.pause_menu.mainloop(w.surface)

    def restart(self):
        self.pause_menu.disable()
        self.pause_menu.clear()
        self.tetris.state = GameStateEnum.STARTED
        self.tetris.__init__(10, 20)
        self.tetris.newFigure()
        self.upcomingFiguresDisplay.fill(self.hudsDefaultColors)
        global gameRunning
        gameRunning = False

    def resume(self):
        global gameRunning
        gameRunning = True
        self.tetris.state = GameStateEnum.STARTED
        self.pause_menu.disable()
        self.pause_menu.clear()