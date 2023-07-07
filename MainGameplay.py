import pygame
import pygame_menu
from Colours import Colours
from GridDraw import Tetris
from Window import Window
from Figure import Figure
from GamePaused import GamePaused
from GameStateEnum import GameStateEnum
import button

class MainGameplay:
    def __init__(self):
        w = Window()
        colours = Colours()

        scaleWVduDimensionsX = (int(w.vduDimensions[0]) / 500) * 20
        scaleWVduDimensionsY = (int(w.vduDimensions[1]) / 400) * 20

        g = GamePaused()

        game = Tetris(10, 20)

        # Loop until the user clicks the close button.
        gameRunning = True
        clock = pygame.time.Clock()
        fps = 25
        counter = 0

        interval = 100
        delay = 300

        pressing_down = False
        pressing_right = False
        pressing_left = False

        while gameRunning:
            if game.figure is None:
                game.newFigure()
            counter += 1
            if counter > 100000:
                counter = 0

            if counter % (fps // game.level // 2) == 0 or pressing_down:
                if game.state.gameStarted():
                    game.goDown()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameRunning = False

                if event.type == pygame.KEYDOWN: #Down keys for rotating
                    if event.key == pygame.K_q:
                        game.rotateRight()
                    if event.key == pygame.K_e:
                        game.rotateLeft()

                    if event.key == pygame.K_s:
                        pressing_down = True

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        pygame.key.set_repeat(delay, interval)
                        game.goSide(-1)

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        pygame.key.set_repeat(delay, interval)
                        game.goSide(1)
                    if event.key == pygame.K_SPACE:
                        game.goSpace()
                    if event.key == pygame.K_ESCAPE:
                        initialState = game.state
                        if initialState == GameStateEnum.PAUSED:
                            game.state = GameStateEnum.STARTED
                        elif initialState == GameStateEnum.STARTED:
                            game.state = GameStateEnum.PAUSED
                        #game.__init__(10, 20)

                    if event.key == pygame.K_p:
                        pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s: #knows when i lift the down key up
                    pressing_down = False
                if event.key == pygame.K_d or pygame.K_RIGHT:
                    pressing_right = False
                if event.key == pygame.K_a or pygame.K_LEFT:
                    pressing_left = False

            w.surface.fill(colours.backgroundColour)

            for i in range(game.height):
                for j in range(game.width):
                    pygame.draw.rect(w.surface, colours.gridColour, [game.x + scaleWVduDimensionsX * j, game.y + scaleWVduDimensionsY * i, scaleWVduDimensionsX, scaleWVduDimensionsY], 1)
                    if game.field[i][j] > 0:
                        pygame.draw.rect(w.surface, Figure.colors[game.field[i][j]],
                                         [game.x + scaleWVduDimensionsX * j + 1, game.y + scaleWVduDimensionsY * i + 1, scaleWVduDimensionsX - 2, scaleWVduDimensionsY - 1])
            if game.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in game.figure.image():
                            pygame.draw.rect(w.surface, Figure.colors[game.figure.color],
                                             [game.x + scaleWVduDimensionsX * (j + game.figure.x) + 1,
                                              game.y + scaleWVduDimensionsY * (i + game.figure.y) + 1,
                                              scaleWVduDimensionsX - 2, scaleWVduDimensionsY - 2])

            fontOpenSans = pygame.font.SysFont('sans', 35)
            score_tracker = fontOpenSans.render("Score: " + str(game.score), True, colours.black)
            pauseResumeButton = fontOpenSans.render("Resume", True, colours.black)

            w.surface.blit(score_tracker, [0, 0])
            if game.state.gameOver():
                print("gameState = gameOver")
            if game.state.paused():
                square_color = (255, 255, 255)  # Red color
                square_size = 200
                square_x = w.vduDimensions[0] // 2 - square_size // 2  # Center the square horizontally
                square_y = w.vduDimensions[1] // 2 - square_size // 2 - 60

                pygame.draw.rect(w.surface, square_color, (square_x, square_y, square_size, square_size))

                resume_img = pygame.image.load("button images/resumeButton (Custom).png").convert_alpha()
                mainMenuImage = pygame.image.load("button images/mainMenuButton (Custom).png").convert_alpha()

                # create button instances
                resume_button = button.Button(304, 160, resume_img, 1)
                mainMenuButton = button.Button(304, 250, mainMenuImage, 1)

                if resume_button.draw(w.surface):
                    game.state = GameStateEnum.STARTED
                if mainMenuButton.draw(w.surface):
                    print("Return to main menu button pressed")
            pygame.display.flip()
            clock.tick(fps)

        pygame.quit()
MainGameplay()