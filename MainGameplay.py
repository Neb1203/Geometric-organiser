import pygame
import pygame_menu
from Colours import Colours
from GridDraw import Tetris
from Window import Window
from Figure import Figure
from GameStateEnum import GameStateEnum
from CenterButton import CenterButton
import controlArray
gameRunning = True
w = Window()
colours = Colours()
cb = CenterButton()
def initialiseGame():
    pygame.init()
    game = MainGameplay()
    game.runGame()
    pygame.quit()
class MainGameplay:
    numUpcomingFigures = 3

    hudsDefaultColors = (255, 255, 255)
    hudsBorderColors = (0, 0, 0)
    upcomingFiguresDisplay = pygame.Surface((150, 450))

    def __init__(self):
        self.scaleWVduDimensionsX = (int(w.vduDimensions[0]) / 500) * 20
        self.scaleWVduDimensionsY = (int(w.vduDimensions[1]) / 400) * 20

        self.game = Tetris(10, 20)

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

        heldFigureLocked = False
        heldFigureContainer = pygame.Surface((150, 150))
        heldFigureContainer.fill(self.hudsDefaultColors)


        self.upcomingFiguresDisplay.fill(self.hudsDefaultColors)

        game_running = True
        while game_running:
            if self.game.figure is None:
                self.game.newFigure()
            self.counter += 1
            if self.counter > 100000:
                self.counter = 0

            if self.counter % (self.fps // self.game.level // 2) == 0 or self.pressing_down:
                if self.game.state.gameStarted():
                    reachedBottom = self.game.goDown()
                    if reachedBottom:
                        heldFigureLocked = False
                        self.upcomingFiguresDisplay.fill(self.hudsDefaultColors)


            for event in pygame.event.get():  # Move this loop inside the main game loop
                if event.type == pygame.QUIT:
                    game_running = False

                if event.type == pygame.KEYDOWN:  # Down keys for rotating
                    if event.key == controlArray.key_mapping['lockPiece'] and not heldFigureLocked:
                        newHeldPiece = self.game.figure
                        self.upcomingFiguresDisplay.fill(self.hudsDefaultColors)
                        self.game.swapHeldFigure()
                        self.game.setHeldFigure(newHeldPiece)
                        heldFigureContainer.fill(self.hudsDefaultColors)

                        for i in range(4):
                            for j in range(4):
                                p = i * 4 + j
                                if p in self.game.heldFigure.image():
                                    positionAndSize = pygame.Rect(
                                        (self.game.x + self.scaleWVduDimensionsX * (
                                            j + self.game.heldFigure.x) + 1) - 320,
                                        (self.game.y + self.scaleWVduDimensionsY * (
                                              i + self.game.heldFigure.y) + 1) + 15,
                                        (self.scaleWVduDimensionsX - 2),
                                        (self.scaleWVduDimensionsY - 2)
                                    )
                                    pygame.draw.rect(
                                        heldFigureContainer,
                                        Figure.colors[self.game.heldFigure.color],
                                        positionAndSize
                                    )
                        heldFigureLocked = True
                    if event.key == controlArray.key_mapping['rotateRight']:
                        self.game.rotateRight()
                    if event.key == controlArray.key_mapping['rotateLeft']:
                        self.game.rotateLeft()

                    if event.key == controlArray.key_mapping['softDrop']:
                        self.pressing_down = True

                    if event.key == controlArray.key_mapping['left'] or event.key == pygame.K_LEFT:
                        print("left key pressed")
                        pygame.key.set_repeat(self.delay, self.interval)
                        self.game.goSide(-1)

                    if event.key == controlArray.key_mapping['right'] or event.key == pygame.K_RIGHT:
                        pygame.key.set_repeat(self.delay, self.interval)
                        self.game.goSide(1)
                    if event.key == controlArray.key_mapping['hardDrop']:
                        self.game.goSpace()
                        heldFigureLocked = False
                        self.upcomingFiguresDisplay.fill(self.hudsDefaultColors)
                    if event.key == controlArray.key_mapping['pause']:
                        # self.return_to_main_menu()
                        # self.resume_game()
                        initialState = self.game.state
                        if initialState == GameStateEnum.PAUSED:
                            self.resume_game()
                        elif initialState == GameStateEnum.STARTED:
                            self.pauseMenu()

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

            for i in range(self.game.height):
                for j in range(self.game.width):
                    pygame.draw.rect(w.surface, colours.gridColour, [self.game.x + self.scaleWVduDimensionsX * j, self.game.y + self.scaleWVduDimensionsY * i, self.scaleWVduDimensionsX, self.scaleWVduDimensionsY], 1)
                    if self.game.field[i][j] > 0:
                        pygame.draw.rect(w.surface, Figure.colors[self.game.field[i][j]],
                                         [self.game.x + self.scaleWVduDimensionsX * j + 1, self.game.y + self.scaleWVduDimensionsY * i + 1, self.scaleWVduDimensionsX - 2, self.scaleWVduDimensionsY - 1])
            if self.game.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in self.game.figure.image():
                            pygame.draw.rect(w.surface, Figure.colors[self.game.figure.color],
                                             [self.game.x + self.scaleWVduDimensionsX * (j + self.game.figure.x) + 1,
                                              self.game.y + self.scaleWVduDimensionsY * (i + self.game.figure.y) + 1,
                                              self.scaleWVduDimensionsX - 2, self.scaleWVduDimensionsY - 2])

            spaceYBetweenFigs = 20
            for figIndex in range(Tetris.numUpcomingFigures):
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        figTypeIndex = self.game.upcomingFigureTypes[figIndex]
                        figColorIndex = self.game.upcomingFigureColors[figIndex]
                        upcomingFigure = Figure(3, 0, figTypeIndex, figColorIndex)
                        if p in upcomingFigure.image():
                            positionAndSize = pygame.Rect(
                                (self.game.x + self.scaleWVduDimensionsX * (
                                    j + upcomingFigure.x) + 1) - 320,
                                (self.game.y + self.scaleWVduDimensionsY * (
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
            scoreTracker = fontOpenSansBig.render("Score: " + str(self.game.score), True, colours.black)
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
            upcomingFiguresDisplayOuter = pygame.Surface((160, 460))
            upcomingFiguresDisplayOuter.fill(self.hudsBorderColors)
            upcomingFiguresDisplayOuter.blit(self.upcomingFiguresDisplay, (5, 5))

            w.surface.blit(upcomingFiguresDisplayOuter, (590, 70))

            if heldFigureLocked:
                heldPieceMessage = fontOpenSansItalic.render("Locked", True, colours.black)
                w.surface.blit(heldPieceMessage, (100, 315))
            if self.game.state.gameOver():
                print("gameState = gameOver")
                self.returnToMainMenu()
            if self.game.state.paused():
                pass
            pygame.display.flip()
            self.clock.tick(self.fps)

            if self.game.state.gameOver() or self.game.state.paused():
                game_running = False
                gameRunning = False

    def returnToMainMenu(self):
        self.pause_menu.disable()
        self.pause_menu.clear()
    def restartGame(self):
        self.pause_menu.disable()
        self.pause_menu.clear()
        self.game.state = GameStateEnum.STARTED
        self.game.__init__(10, 20)
        self.game.newFigure()
        self.upcomingFiguresDisplay.fill(self.hudsDefaultColors)
        global gameRunning
        gameRunning = False

    def pauseMenu(self):
        self.game.state = GameStateEnum.PAUSED
        # Create a pause menu
        self.pause_menu = pygame_menu.Menu('Pause Menu', w.vduDimensions[0], w.vduDimensions[1], theme=w.mainTheme)

        # Add items to the pause menu (e.g., resume and quit options)
        self.pause_menu.add.button('Resume', self.resume_game)
        self.pause_menu.add.button('Restart', self.restartGame)
        self.pause_menu.add.button('Quit', self.returnToMainMenu)
        # Run the pause menu
        self.pause_menu.mainloop(w.surface)

    def resume_game(self):
        global gameRunning
        gameRunning = True
        self.game.state = GameStateEnum.STARTED
        self.pause_menu.disable()
        self.pause_menu.clear()



if __name__ == "__main__":
    initialiseGame()