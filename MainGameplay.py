import pygame

import controlArray
from CenterButton import CenterButton
from Colours import Colours
from Figure import Figure
from GameModeEnum import GameModeEnum
from GameStateEnum import GameStateEnum
from PauseMenu import PauseMenu
from GridDraw import Tetris
from Window import Window

w = Window()
colours = Colours()
cb = CenterButton()

class MainGameplay:
    numUpcomingFigures = 3
    hudsBorderColors = (0, 0, 0)
    upcomingFiguresDisplay = pygame.Surface((150, 450))

    def __init__(self):
        self.scaleWVduDimensionsX = (int(w.vduDimensions[0]) / 500) * 20
        self.scaleWVduDimensionsY = (int(w.vduDimensions[1]) / 400) * 20

        self.tetris = Tetris(10, 20)

        self.clock = pygame.time.Clock()
        self.fps = 25
        self.counter = 0

        self.interval = 100
        self.delay = 300

        self.pressing_down = False
        self.pressing_right = False
        self.pressing_left = False

    def runGame(self, gameMode: GameModeEnum):
        fontOpenSansBig = pygame.font.SysFont('sans', 35)
        fontOpenSans = pygame.font.SysFont('sans', 24)
        fontOpenSansItalic = pygame.font.SysFont('sans', 18)
        fontOpenSansItalic.italic = True

        heldFigureLocked = False
        heldFigureContainer = pygame.Surface((150, 150))
        heldFigureContainer.fill(PauseMenu.hudsDefaultColors)

        self.pauseMenu = PauseMenu()
        self.upcomingFiguresDisplay.fill(PauseMenu.hudsDefaultColors)
        # self.gameplayHelpers.upcomingFiguresDisplay.fill(GameplayHelpers.hudsDefaultColors)
        # self.gameplayHelpers.game.state = GameStateEnum.STARTED
        # self.gameplayHelpers.game = Tetris(10, 20)

        game_running = True
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
                        heldFigureLocked = False
                        self.upcomingFiguresDisplay.fill(PauseMenu.hudsDefaultColors)


            for event in pygame.event.get():  # Move this loop inside the main game loop
                if event.type == pygame.QUIT:
                    game_running = False

                if event.type == pygame.KEYDOWN:  # Down keys for rotating
                    if event.key == controlArray.key_mapping['lockPiece'] and not heldFigureLocked:
                        newHeldPiece = self.tetris.figure
                        self.upcomingFiguresDisplay.fill(PauseMenu.hudsDefaultColors)
                        self.tetris.swapHeldFigure()
                        self.tetris.setHeldFigure(newHeldPiece)
                        heldFigureContainer.fill(PauseMenu.hudsDefaultColors)

                        for i in range(4):
                            for j in range(4):
                                p = i * 4 + j
                                if p in self.tetris.heldFigure.image():
                                    positionAndSize = pygame.Rect(
                                        (self.tetris.x + self.scaleWVduDimensionsX * (
                                            j + self.tetris.heldFigure.x) + 1) - 320,
                                        (self.tetris.y + self.scaleWVduDimensionsY * (
                                              i + self.tetris.heldFigure.y) + 1) + 15,
                                        (self.scaleWVduDimensionsX - 2),
                                        (self.scaleWVduDimensionsY - 2)
                                    )
                                    pygame.draw.rect(
                                        heldFigureContainer,
                                        Figure.colors[self.tetris.heldFigure.color],
                                        positionAndSize
                                    )
                        heldFigureLocked = True
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
                        heldFigureLocked = False
                        self.upcomingFiguresDisplay.fill(PauseMenu.hudsDefaultColors)
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
                            self.pauseMenu.open(w, self)

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
            w.surface.fill(colours.backgroundColour)

            for i in range(self.tetris.height):
                for j in range(self.tetris.width):
                    pygame.draw.rect(w.surface, colours.gridColour, [self.tetris.x + self.scaleWVduDimensionsX * j, self.tetris.y + self.scaleWVduDimensionsY * i, self.scaleWVduDimensionsX, self.scaleWVduDimensionsY], 1)
                    if self.tetris.field[i][j] > 0:
                        pygame.draw.rect(w.surface, Figure.colors[self.tetris.field[i][j]],
                                         [self.tetris.x + self.scaleWVduDimensionsX * j + 1, self.tetris.y + self.scaleWVduDimensionsY * i + 1, self.scaleWVduDimensionsX - 2, self.scaleWVduDimensionsY - 1])
            if self.tetris.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in self.tetris.figure.image():
                            pygame.draw.rect(w.surface, Figure.colors[self.tetris.figure.color],
                                             [self.tetris.x + self.scaleWVduDimensionsX * (j + self.tetris.figure.x) + 1,
                                              self.tetris.y + self.scaleWVduDimensionsY * (i + self.tetris.figure.y) + 1,
                                              self.scaleWVduDimensionsX - 2, self.scaleWVduDimensionsY - 2])

            spaceYBetweenFigs = 20
            for figIndex in range(Tetris.numUpcomingFigures):
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        figTypeIndex = self.tetris.upcomingFigureTypes[figIndex]
                        figColorIndex = self.tetris.upcomingFigureColors[figIndex]
                        upcomingFigure = Figure(3, 0, figTypeIndex, figColorIndex)
                        if p in upcomingFigure.image():
                            positionAndSize = pygame.Rect(
                                (self.tetris.x + self.scaleWVduDimensionsX * (
                                    j + upcomingFigure.x) + 1) - 320,
                                (self.tetris.y + self.scaleWVduDimensionsY * (
                                      i + upcomingFigure.y) + 1) + spaceYBetweenFigs,
                                (self.scaleWVduDimensionsX - 2),
                                (self.scaleWVduDimensionsY - 2)
                            )
                            pygame.draw.rect(
                                self.upcomingFiguresDisplay,
                                Figure.colors[figColorIndex],
                                positionAndSize
                            )
                spaceYBetweenFigs += 150

            scoreTracker = fontOpenSansBig.render("Score: " + str(self.tetris.score), True, colours.black)
            pauseResumeButton = fontOpenSansBig.render("Resume", True, colours.black)

            w.surface.blit(scoreTracker, [0, 0])

            heldPieceMessage = fontOpenSans.render("Held Piece", True, colours.black)
            w.surface.blit(heldPieceMessage, (50, 120))
            heldFigureContainerOuter = pygame.Surface((160, 160))
            heldFigureContainerOuter.fill(self.hudsBorderColors)
            heldFigureContainerOuter.blit(heldFigureContainer, (5, 5))

            w.surface.blit(heldFigureContainerOuter, (50, 150))

            upcomingFiguresMessage = fontOpenSans.render("Upcoming pieces", True, colours.black)
            w.surface.blit(upcomingFiguresMessage, (590, 40))
            self.upcomingFiguresDisplayOuter = pygame.Surface((160, 460))
            self.upcomingFiguresDisplayOuter.fill(self.hudsBorderColors)
            self.upcomingFiguresDisplayOuter.blit(self.upcomingFiguresDisplay, (5, 5))
            w.surface.blit(self.upcomingFiguresDisplayOuter, (590, 70))

            if heldFigureLocked:
                heldPieceMessage = fontOpenSansItalic.render("Locked", True, colours.black)
                w.surface.blit(heldPieceMessage, (100, 315))
            if self.tetris.state.gameOver():
                print("gameState = gameOver")
                self.pauseMenu.quit()
            if self.tetris.state.paused():
                pass
                # square_color = (255, 255, 255)  # Red color
                # square_size = 200
                # square_x = w.vduDimensions[0] // 2 - square_size // 2  # Center the square horizontally
                # square_y = w.vduDimensions[1] // 2 - square_size // 2 - 60
                #
                # # pygame.draw.rect(w.surface, square_color, (square_x, square_y, square_size, square_size))
                #
                # resumePath = "button images/Resume imagee.png"
                # restartPath = "button images/Restart buttonn.png"
                # mainMenuPath = "button images/Quit buttonn.png"
                #
                # totalNumButtons = 2
                # margins = 20
                #
                # resumeImage = pygame.image.load(resumePath).convert_alpha()
                # restartImage = pygame.image.load(restartPath).convert_alpha()
                # mainMenuImage = pygame.image.load(mainMenuPath).convert_alpha()
                #
                # resume_button = button.Button(cb.centerButtonWidth(resumePath), cb.centerButtonHeight(resumePath, totalNumButtons, margins, 0), resumeImage, 1)
                # restartButton = button.Button(cb.centerButtonWidth(restartPath), cb.centerButtonHeight(restartPath, totalNumButtons, margins, 1), restartImage, 1)
                # mainMenuButton = button.Button(cb.centerButtonWidth(mainMenuPath), cb.centerButtonHeight(mainMenuPath, totalNumButtons, margins, 2), mainMenuImage, 1)
                #
                # if resume_button.draw(w.surface):
                #     self.gameplayHelpers.game.state = GameStateEnum.STARTED
                # if restartButton.draw(w.surface):
                #     self.gameplayHelpers.game.__init__(10, 20)
                #     self.gameplayHelpers.game.newFigure()
                # if mainMenuButton.draw(w.surface):
                #     print("Return to main menu button pressed")
            pygame.display.flip()
            self.clock.tick(self.fps)
            if self.tetris.state.gameOver() or self.tetris.state.paused():
                game_running = False
                self.tetris.state = GameStateEnum.QUIT
