from __future__ import annotations
import pygame_menu

import Campaign
from GameStateEnum import GameStateEnum
from GridDraw import Tetris
from typing import TYPE_CHECKING, Union
from Window import Window


class PauseMenu:
    if TYPE_CHECKING:
        from Campaign import Campaign
        from Endless import Endless

    hudsDefaultColors = (255, 255, 255)
    pause_menu = None

    def quit(self):
        self.pause_menu.disable()
        self.pause_menu.clear()

    def open(self, game: Union[Campaign, Endless]):
        print("def pauseMenu")
        # Create a pause menu
        self.pause_menu = pygame_menu.Menu('Pause Menu', game.w.vduDimensions[0], game.w.vduDimensions[1], theme=game.w.mainTheme)

        # Add items to the pause menu (e.g., resume and quit options)
        self.pause_menu.add.button('Resume', self.resume, game.tetris)
        self.pause_menu.add.button('Restart', self.restart, game, True)
        self.pause_menu.add.button('Quit', self.quit)
        # Run the pause menu
        self.pause_menu.mainloop(game.w.surface)

    def restart(self, game: Union[Campaign, Endless], resetLives=False):
        if self.pause_menu != None:
            self.pause_menu.disable()
            self.pause_menu.clear()
        game.tetris.state = GameStateEnum.STARTED
        game.tetris.__init__(10, 20)
        game.tetris.newFigure()
        game.upcomingFiguresDisplay.fill(self.hudsDefaultColors)
        game.heldFigureLocked = False
        game.heldFigureContainer.fill(self.hudsDefaultColors)
        game.timeLeft = game.defaultTimerDuration
        if isinstance(game, Campaign.Campaign):
            game.targetScore = 30
            game.level = 1
            Window.refreshLivesLeftDisplay(game, resetLives=resetLives)
        global gameRunning
        gameRunning = False
        return game.tetris

    def resume(self, tetris: Tetris):
        global gameRunning
        gameRunning = True
        tetris.state = GameStateEnum.STARTED
        self.pause_menu.disable()
        self.pause_menu.clear()