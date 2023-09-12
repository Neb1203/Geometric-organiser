import pygame

import controlArray
from CenterButton import CenterButton
from Colours import Colours
from Figure import Figure
from GameModeEnum import GameModeEnum
from GameStateEnum import GameStateEnum
from Menus import Menus
from GridDraw import Tetris
from Window import Window

gameRunning = True
w = Window()
colours = Colours()
cb = CenterButton()

class MainGameplay:
    numUpcomingFigures = 3
    hudsBorderColors = (0, 0, 0)

    def __init__(self):
        self.scaleWVduDimensionsX = (int(w.vduDimensions[0]) / 500) * 20
        self.scaleWVduDimensionsY = (int(w.vduDimensions[1]) / 400) * 20

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
        heldFigureContainer.fill(Menus.hudsDefaultColors)

        self.menus = Menus()
        # self.gameplayHelpers.upcomingFiguresDisplay.fill(GameplayHelpers.hudsDefaultColors)
        # self.gameplayHelpers.game.state = GameStateEnum.STARTED
        # self.gameplayHelpers.game = Tetris(10, 20)

        game_running = True
        while game_running:
            if self.menus.tetris.figure is None:
                self.menus.tetris.newFigure()
            self.counter += 1
            if self.counter > 100000:
                self.counter = 0

            if self.counter % (self.fps // self.menus.tetris.level // 2) == 0 or self.pressing_down:
                if self.menus.tetris.state.gameStarted():
                    reachedBottom = self.menus.tetris.goDown()
                    if reachedBottom:
                        heldFigureLocked = False
                        self.menus.upcomingFiguresDisplay.fill(Menus.hudsDefaultColors)


            for event in pygame.event.get():  # Move this loop inside the main game loop
                if event.type == pygame.QUIT:
                    game_running = False

                if event.type == pygame.KEYDOWN:  # Down keys for rotating
                    if event.key == controlArray.key_mapping['lockPiece'] and not heldFigureLocked:
                        newHeldPiece = self.menus.tetris.figure
                        self.menus.upcomingFiguresDisplay.fill(Menus.hudsDefaultColors)
                        self.menus.tetris.swapHeldFigure()
                        self.menus.tetris.setHeldFigure(newHeldPiece)
                        heldFigureContainer.fill(Menus.hudsDefaultColors)

                        for i in range(4):
                            for j in range(4):
                                p = i * 4 + j
                                if p in self.menus.tetris.heldFigure.image():
                                    positionAndSize = pygame.Rect(
                                        (self.menus.tetris.x + self.scaleWVduDimensionsX * (
                                            j + self.menus.tetris.heldFigure.x) + 1) - 320,
                                        (self.menus.tetris.y + self.scaleWVduDimensionsY * (
                                              i + self.menus.tetris.heldFigure.y) + 1) + 15,
                                        (self.scaleWVduDimensionsX - 2),
                                        (self.scaleWVduDimensionsY - 2)
                                    )
                                    pygame.draw.rect(
                                        heldFigureContainer,
                                        Figure.colors[self.menus.tetris.heldFigure.color],
                                        positionAndSize
                                    )
                        heldFigureLocked = True
                    if event.key == controlArray.key_mapping['rotateRight']:
                        self.menus.tetris.rotateRight()
                    if event.key == controlArray.key_mapping['rotateLeft']:
                        self.menus.tetris.rotateLeft()

                    if event.key == controlArray.key_mapping['softDrop']:
                        self.pressing_down = True

                    if event.key == controlArray.key_mapping['left'] or event.key == pygame.K_LEFT:
                        print("left key pressed")
                        pygame.key.set_repeat(self.delay, self.interval)
                        self.menus.tetris.goSide(-1)

                    if event.key == controlArray.key_mapping['right'] or event.key == pygame.K_RIGHT:
                        pygame.key.set_repeat(self.delay, self.interval)
                        self.menus.tetris.goSide(1)
                    if event.key == controlArray.key_mapping['hardDrop']:
                        self.menus.tetris.goSpace()
                        heldFigureLocked = False
                        self.menus.upcomingFiguresDisplay.fill(Menus.hudsDefaultColors)
                    if event.key == controlArray.key_mapping['pause']:
                        # GameplayHelpers.return_to_main_menu()
                        # self.resume_game()
                        initialState = self.menus.tetris.state
                        if initialState == GameStateEnum.PAUSED:
                            self.menus.resume()
                            self.menus.tetris.state = GameStateEnum.STARTED
                        elif initialState == GameStateEnum.STARTED:
                            print("RUNNING")
                            self.menus.tetris.state = GameStateEnum.PAUSED
                            self.menus.open(w)

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

            for i in range(self.menus.tetris.height):
                for j in range(self.menus.tetris.width):
                    pygame.draw.rect(w.surface, colours.gridColour, [self.menus.tetris.x + self.scaleWVduDimensionsX * j, self.menus.tetris.y + self.scaleWVduDimensionsY * i, self.scaleWVduDimensionsX, self.scaleWVduDimensionsY], 1)
                    if self.menus.tetris.field[i][j] > 0:
                        pygame.draw.rect(w.surface, Figure.colors[self.menus.tetris.field[i][j]],
                                         [self.menus.tetris.x + self.scaleWVduDimensionsX * j + 1, self.menus.tetris.y + self.scaleWVduDimensionsY * i + 1, self.scaleWVduDimensionsX - 2, self.scaleWVduDimensionsY - 1])
            if self.menus.tetris.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in self.menus.tetris.figure.image():
                            pygame.draw.rect(w.surface, Figure.colors[self.menus.tetris.figure.color],
                                             [self.menus.tetris.x + self.scaleWVduDimensionsX * (j + self.menus.tetris.figure.x) + 1,
                                              self.menus.tetris.y + self.scaleWVduDimensionsY * (i + self.menus.tetris.figure.y) + 1,
                                              self.scaleWVduDimensionsX - 2, self.scaleWVduDimensionsY - 2])

            spaceYBetweenFigs = 20
            for figIndex in range(Tetris.numUpcomingFigures):
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        figTypeIndex = self.menus.tetris.upcomingFigureTypes[figIndex]
                        figColorIndex = self.menus.tetris.upcomingFigureColors[figIndex]
                        upcomingFigure = Figure(3, 0, figTypeIndex, figColorIndex)
                        if p in upcomingFigure.image():
                            positionAndSize = pygame.Rect(
                                (self.menus.tetris.x + self.scaleWVduDimensionsX * (
                                    j + upcomingFigure.x) + 1) - 320,
                                (self.menus.tetris.y + self.scaleWVduDimensionsY * (
                                      i + upcomingFigure.y) + 1) + spaceYBetweenFigs,
                                (self.scaleWVduDimensionsX - 2),
                                (self.scaleWVduDimensionsY - 2)
                            )
                            pygame.draw.rect(
                                self.menus.upcomingFiguresDisplay,
                                Figure.colors[figColorIndex],
                                positionAndSize
                            )
                spaceYBetweenFigs += 150

            scoreTracker = fontOpenSansBig.render("Score: " + str(self.menus.tetris.score), True, colours.black)
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
            self.menus.upcomingFiguresDisplayOuter = pygame.Surface((160, 460))
            self.menus.upcomingFiguresDisplayOuter.fill(self.hudsBorderColors)
            self.menus.upcomingFiguresDisplayOuter.blit(self.menus.upcomingFiguresDisplay, (5, 5))
            w.surface.blit(self.menus.upcomingFiguresDisplayOuter, (590, 70))

            if heldFigureLocked:
                heldPieceMessage = fontOpenSansItalic.render("Locked", True, colours.black)
                w.surface.blit(heldPieceMessage, (100, 315))
            if self.menus.tetris.state.gameOver():
                print("gameState = gameOver")
                self.menus.quit()
            if self.menus.tetris.state.paused():
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
            if self.menus.tetris.state.gameOver() or self.menus.tetris.state.paused():
                game_running = False
                gameRunning = False
                self.menus.tetris.state = GameStateEnum.QUIT
