import datetime
import time

import pygame

import controlArray
from CenterButton import CenterButton
from Colours import Colours
from Figure import Figure
from GameDifficultyEnum import GameDifficultyEnum
from GameModeEnum import GameModeEnum
from GameSaves import GameSaves
from GameStateEnum import GameStateEnum
from PauseMenu import PauseMenu
from GridDraw import Tetris
from Window import Window
from tokenModifier import TokenModifier

colours = Colours()
cb = CenterButton()

class Endless:
    w = Window()
    numUpcomingFigures = 3
    hudsBorderColors = (0, 0, 0)
    upcomingFiguresDisplay = pygame.Surface((170, 540))
    heldFigureContainer = pygame.Surface((170, 170))
    heldFigureLocked = False
    defaultTimerDuration = 60

    def __init__(self, difficultyLevel: GameDifficultyEnum):
        self.scaleWVduDimensionsX = (int(self.w.vduDimensions[0]) / 500) * 20
        self.scaleWVduDimensionsY = (int(self.w.vduDimensions[1]) / 400) * 20

        self.tetris = Tetris(10, 20, difficultyLevel.getUpcomingPiecesNumber(), difficultyLevel.getDifficultyLevel(),)

        self.clock = pygame.time.Clock()
        self.fps = 25
        self.counter = 0

        self.interval = 100
        self.delay = 300

        self.pressing_down = False
        self.pressing_right = False
        self.pressing_left = False

    def runGame(self):
        fontOpenSansBig = pygame.font.SysFont('sans', 35)
        fontOpenSans = pygame.font.SysFont('sans', 24)
        fontOpenSansItalic = pygame.font.SysFont('sans', 18)
        fontOpenSansItalic.italic = True

        self.heldFigureContainer.fill(PauseMenu.hudsDefaultColors)

        self.pauseMenu = PauseMenu()
        self.refreshUpcomingDisplay()
        # self.gameplayHelpers.game.state = GameStateEnum.STARTED
        # self.gameplayHelpers.game = Tetris(10, 20)

        game_running = True
        self.timeLeft = self.defaultTimerDuration
        while game_running:
            if self.tetris.figure is None:
                self.tetris.newFigure()
            self.counter += 1
            if self.counter > 100000:
                self.counter = 0

            if self.counter % (self.fps // self.tetris.level // 2) == 0 or self.pressing_down:
                if self.tetris.state.gameStarted():
                    reachedBottom = self.tetris.goDown()
                    if reachedBottom:
                        self.heldFigureLocked = False
                        self.refreshUpcomingDisplay()

            for event in pygame.event.get():
                if event.type == Window.TIMER_END_EVENT:
                    if self.defaultTimerDuration > 0:
                        self.timeLeft -= 1
                    if self.timeLeft <= 0:
                        self.gameEnded()
                if event.type == pygame.QUIT:
                    game_running = False

                if event.type == pygame.KEYDOWN:  # Down keys for rotating
                    if event.key == controlArray.key_mapping['lockPiece'] and not self.heldFigureLocked:
                        newHeldPiece = self.tetris.figure
                        self.refreshUpcomingDisplay()
                        self.tetris.swapHeldFigure()
                        self.tetris.setHeldFigure(newHeldPiece)
                        self.heldFigureContainer.fill(PauseMenu.hudsDefaultColors)

                        for i in range(4):
                            for j in range(4):
                                p = i * 4 + j
                                if p in self.tetris.heldFigure.image():
                                    positionAndSize = pygame.Rect(
                                        (self.tetris.x + self.scaleWVduDimensionsX * (
                                            j + self.tetris.heldFigure.x) + 1) - 365,
                                        (self.tetris.y + self.scaleWVduDimensionsY * (
                                              i + self.tetris.heldFigure.y) + 1) + 15,
                                        (self.scaleWVduDimensionsX - 2),
                                        (self.scaleWVduDimensionsY - 2)
                                    )
                                    pygame.draw.rect(
                                        self.heldFigureContainer,
                                        Figure.colors[self.tetris.heldFigure.color],
                                        positionAndSize
                                    )
                        self.heldFigureLocked = True
                    if event.key == controlArray.key_mapping['rotateRight']:
                        self.tetris.rotateRight()
                    if event.key == controlArray.key_mapping['rotateLeft']:
                        self.tetris.rotateLeft()

                    if event.key == controlArray.key_mapping['softDrop']:
                        self.pressing_down = True

                    if event.key == controlArray.key_mapping['left'] or event.key == pygame.K_LEFT:
                        print("left key pressed")
                        pygame.key.set_repeat(self.delay, self.interval)
                        self.tetris.goSide(-1)

                    if event.key == controlArray.key_mapping['right'] or event.key == pygame.K_RIGHT:
                        pygame.key.set_repeat(self.delay, self.interval)
                        self.tetris.goSide(1)
                    if event.key == controlArray.key_mapping['hardDrop']:
                        self.tetris.goSpace()
                        self.heldFigureLocked = False
                        self.refreshUpcomingDisplay()
                    if event.key == controlArray.key_mapping['pause']:
                        # GameplayHelpers.return_to_main_menu()
                        # self.resume_game()
                        initialState = self.tetris.state
                        if initialState == GameStateEnum.PAUSED:
                            self.pauseMenu.resume()
                            self.tetris.state = GameStateEnum.STARTED
                        elif initialState == GameStateEnum.STARTED:
                            print("RUNNING")
                            self.tetris.state = GameStateEnum.PAUSED
                            self.pauseMenu.open(self)

                        # game.__init__(10, 20)
                if event.type == pygame.KEYUP:
                    print("keyup")
                    if controlArray.key_mapping['softDrop']:  # Knows when I lift the down key up
                        self.pressing_down = False
                    if controlArray.key_mapping['right'] or pygame.K_RIGHT:
                        self.pressing_right = False
                    if event.key == controlArray.key_mapping['left'] or pygame.K_LEFT:
                        self.pressing_left = False

                # The rest of the code (drawing, button handling, etc.) remains the same
                # ...
            self.w.surface.fill(colours.backgroundColour)

            for i in range(self.tetris.height):
                for j in range(self.tetris.width):
                    pygame.draw.rect(self.w.surface, colours.gridColour, [self.tetris.x + self.scaleWVduDimensionsX * j, self.tetris.y + self.scaleWVduDimensionsY * i, self.scaleWVduDimensionsX, self.scaleWVduDimensionsY], 1)
                    if self.tetris.field[i][j] > 0:
                        pygame.draw.rect(self.w.surface, Figure.colors[self.tetris.field[i][j]],
                                         [self.tetris.x + self.scaleWVduDimensionsX * j + 1, self.tetris.y + self.scaleWVduDimensionsY * i + 1, self.scaleWVduDimensionsX - 2, self.scaleWVduDimensionsY - 1])
            if self.tetris.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in self.tetris.figure.image():
                            pygame.draw.rect(self.w.surface, Figure.colors[self.tetris.figure.color],
                                             [self.tetris.x + self.scaleWVduDimensionsX * (j + self.tetris.figure.x) + 1,
                                              self.tetris.y + self.scaleWVduDimensionsY * (i + self.tetris.figure.y) + 1,
                                              self.scaleWVduDimensionsX - 2, self.scaleWVduDimensionsY - 2])

            spaceYBetween = 10
            for figIndex in range(self.tetris.numUpcomingFigures):
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        figTypeIndex = self.tetris.upcomingFigureTypes[figIndex]
                        figColorIndex = self.tetris.upcomingFigureColors[figIndex]
                        upcomingFigure = Figure(3, 0, figTypeIndex, figColorIndex)
                        if p in upcomingFigure.image():
                            positionAndSize = pygame.Rect(
                                (self.tetris.x + self.scaleWVduDimensionsX * (
                                    j + upcomingFigure.x) + 1) -365,
                                (self.tetris.y + self.scaleWVduDimensionsY * (
                                      i + upcomingFigure.y) + 1) + spaceYBetween,
                                (self.scaleWVduDimensionsX - 2),
                                (self.scaleWVduDimensionsY - 2)
                            )
                            pygame.draw.rect(
                                self.upcomingFiguresDisplay,
                                Figure.colors[figColorIndex],
                                positionAndSize
                            )
                spaceYBetween += 190

            scoreTrackerMessage = fontOpenSansBig.render("Score: ", True, colours.black)
            scoreTracker = fontOpenSansBig.render(str(self.tetris.score), True, colours.forestGreen)

            self.w.surface.blit(scoreTrackerMessage, [10, 0])
            self.w.surface.blit(scoreTracker, [125, 0])

            heldPieceMessage = fontOpenSans.render("Held Piece", True, colours.black)
            self.w.surface.blit(heldPieceMessage, (50, 240))
            heldFigureContainerOuter = pygame.Surface((180, 180))
            heldFigureContainerOuter.fill(self.hudsBorderColors)
            heldFigureContainerOuter.blit(self.heldFigureContainer, (5, 5))

            self.w.surface.blit(heldFigureContainerOuter, (50, 270))

            upcomingFiguresMessage = fontOpenSans.render("Upcoming pieces", True, colours.black)
            self.w.surface.blit(upcomingFiguresMessage, (675, 60))
            self.upcomingFiguresDisplayOuter = pygame.Surface((180, 550))
            self.upcomingFiguresDisplayOuter.fill(self.hudsBorderColors)
            self.upcomingFiguresDisplayOuter.blit(self.upcomingFiguresDisplay, (5, 5))
            self.w.surface.blit(self.upcomingFiguresDisplayOuter, (675, 90))

            if self.heldFigureLocked:
                heldPieceMessage = fontOpenSansItalic.render("Locked", True, colours.black)
                self.w.surface.blit(heldPieceMessage, (100, 455))

            if self.tetris.state.paused():
                pass
            pygame.display.flip()
            self.clock.tick(self.fps)
            if self.tetris.state.gameOver() or self.tetris.state.paused():
                game_running = False
                self.tetris.state = GameStateEnum.QUIT
                self.gameEnded()
                print("The game is over")
        self.gameEnded()

    def refreshUpcomingDisplay(self):
        self.upcomingFiguresDisplay.fill(PauseMenu.hudsDefaultColors)
        pygame.draw.line(
            self.upcomingFiguresDisplay,
            colours.black,
            (15, 160),
            (155, 160)
        )

        pygame.draw.line(
            self.upcomingFiguresDisplay,
            colours.black,
            (15, 365),
            (155, 365)
        )

    def gameEnded(self):
        tokenModifier = TokenModifier()
        lastSession = tokenModifier.get_last_session()
        durationObj = self.secondsToTime(self.defaultTimerDuration - self.timeLeft)
        if lastSession != None:
            GameSaves.storeEndless(
                GameModeEnum.ENDLESS,
                self.tetris.score,
                tokenModifier.get_last_session(),
                durationObj
            )

    def secondsToTime(self, seconds: int) -> time:
        return datetime.time(0, 0, seconds)