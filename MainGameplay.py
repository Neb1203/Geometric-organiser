import pygame
import pygame_menu
from Colours import Colours
from GridDraw import Tetris
from Window import Window
from Figure import Figure
from GameStateEnum import GameStateEnum
import button
from PIL import Image
from CenterButton import CenterButton
gameRunning = True
w = Window()
colours = Colours()
cb = CenterButton()



def start_game():
    pygame.init()
    game = MainGameplay()
    game.run_game()
    pygame.quit()
class MainGameplay:

    heldFigureLocked = False
    heldFigureContainerBorderColor = (0, 0, 0)
    heldFigureContainerColor = (255, 255, 255)
    heldFigureContainer = pygame.Surface((150, 150))
    heldFigureContainer.fill(heldFigureContainerColor)

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

    def run_game(self):
        fontOpenSansBig = pygame.font.SysFont('sans', 35)
        fontOpenSans = pygame.font.SysFont('sans', 24)
        fontOpenSansItalic = pygame.font.SysFont('sans', 18)
        fontOpenSansItalic.italic = True

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
                        self.heldFigureLocked = False


            for event in pygame.event.get():  # Move this loop inside the main game loop
                if event.type == pygame.QUIT:
                    game_running = False

                if event.type == pygame.KEYDOWN:  # Down keys for rotating
                    if event.key == pygame.K_l and not self.heldFigureLocked:
                        self.game.setHeldPiece()
                        self.heldFigureContainer.fill(self.heldFigureContainerColor)

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
                                        self.heldFigureContainer,
                                        Figure.colors[self.game.heldFigure.color],
                                        positionAndSize
                                    )
                        self.heldFigureLocked = True
                    if event.key == pygame.K_q:
                        self.game.rotateRight()
                    if event.key == pygame.K_e:
                        self.game.rotateLeft()

                    if event.key == pygame.K_s:
                        self.pressing_down = True

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        pygame.key.set_repeat(self.delay, self.interval)
                        self.game.goSide(-1)

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        pygame.key.set_repeat(self.delay, self.interval)
                        self.game.goSide(1)
                    if event.key == pygame.K_SPACE:
                        self.game.goSpace()
                        self.heldFigureLocked = False
                    if event.key == pygame.K_ESCAPE:
                        # self.return_to_main_menu()
                        # self.resume_game()
                        initialState = self.game.state
                        if initialState == GameStateEnum.PAUSED:
                            self.resume_game()
                        elif initialState == GameStateEnum.STARTED:
                            self.pauseMenu()

                        # game.__init__(10, 20)

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_s:  # Knows when I lift the down key up
                            self.pressing_down = False
                        if event.key == pygame.K_d or pygame.K_RIGHT:
                            self.pressing_right = False
                        if event.key == pygame.K_a or pygame.K_LEFT:
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

            scoreTracker = fontOpenSansBig.render("Score: " + str(self.game.score), True, colours.black)
            pauseResumeButton = fontOpenSansBig.render("Resume", True, colours.black)

            w.surface.blit(scoreTracker, [0, 0])

            heldFigureContainerOuter = pygame.Surface((160, 160))
            heldFigureContainerOuter.fill(self.heldFigureContainerBorderColor)
            heldFigureContainerOuter.blit(self.heldFigureContainer, (5, 5))
            w.surface.blit(heldFigureContainerOuter, (50, 150))
            heldPieceMessage = fontOpenSans.render("Held Piece", True, colours.black)
            w.surface.blit(heldPieceMessage, (50, 120))
            if self.heldFigureLocked:
                heldPieceMessage = fontOpenSansItalic.render("Locked", True, colours.black)
                w.surface.blit(heldPieceMessage, (100, 315))
            if self.game.state.gameOver():
                print("gameState = gameOver")
                self.return_to_main_menu()
            if self.game.state.paused():
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
                #     self.game.state = GameStateEnum.STARTED
                # if restartButton.draw(w.surface):
                #     self.game.__init__(10, 20)
                #     self.game.newFigure()
                # if mainMenuButton.draw(w.surface):
                #     print("Return to main menu button pressed")
            pygame.display.flip()
            self.clock.tick(self.fps)

            if self.game.state.gameOver() or self.game.state.paused():
                game_running = False
                gameRunning = False

    def return_to_main_menu(self):
        print("return to main menu")
        self.pause_menu.disable()
        self.pause_menu.clear()
    def restartGame(self):
        print("def return_to_main_menu")
        self.pause_menu.disable()
        self.pause_menu.clear()
        self.game.state = GameStateEnum.STARTED
        self.game.__init__(10, 20)
        self.game.newFigure()
        global gameRunning
        gameRunning = False

    def pauseMenu(self):
        print("def pauseMenu")
        self.game.state = GameStateEnum.PAUSED
        # Create a pause menu
        self.pause_menu = pygame_menu.Menu('Pause Menu', w.vduDimensions[0], w.vduDimensions[1], theme=w.mainTheme)

        # Add items to the pause menu (e.g., resume and quit options)
        self.pause_menu.add.button('Resume', self.resume_game)
        self.pause_menu.add.button('Restart', self.restartGame)
        self.pause_menu.add.button('Quit', self.return_to_main_menu)
        # Run the pause menu
        self.pause_menu.mainloop(w.surface)

    def resume_game(self):
        # print("def resume")
        # if self.game.state.paused():
        #     print("paused")
        global gameRunning
        gameRunning = True
        self.game.state = GameStateEnum.STARTED
        self.pause_menu.disable()
        self.pause_menu.clear()



if __name__ == "__main__":
    start_game()