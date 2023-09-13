import pygame_menu

from GameStateEnum import GameStateEnum
from GridDraw import Tetris
from Window import Window


class PauseMenu:

    hudsDefaultColors = (255, 255, 255)


    def quit(self):
        self.pause_menu.disable()
        self.pause_menu.clear()

    def open(self, w: Window, mainGameplay):
        print("def pauseMenu")
        # Create a pause menu
        self.pause_menu = pygame_menu.Menu('Pause Menu', w.vduDimensions[0], w.vduDimensions[1], theme=w.mainTheme)

        # Add items to the pause menu (e.g., resume and quit options)
        self.pause_menu.add.button('Resume', self.resume, mainGameplay.tetris)
        self.pause_menu.add.button('Restart', self.restart, mainGameplay)
        self.pause_menu.add.button('Quit', self.quit)
        # Run the pause menu
        self.pause_menu.mainloop(w.surface)

    def restart(self, mainGameplay):
        self.pause_menu.disable()
        self.pause_menu.clear()
        mainGameplay.tetris.state = GameStateEnum.STARTED
        mainGameplay.tetris.__init__(10, 20)
        mainGameplay.tetris.newFigure()
        mainGameplay.upcomingFiguresDisplay.fill(self.hudsDefaultColors)
        global gameRunning
        gameRunning = False
        return mainGameplay.tetris

    def resume(self, tetris: Tetris):
        global gameRunning
        gameRunning = True
        tetris.state = GameStateEnum.STARTED
        self.pause_menu.disable()
        self.pause_menu.clear()