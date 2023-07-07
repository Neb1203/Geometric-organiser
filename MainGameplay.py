import pygame
import pygame_menu
from Colours import Colours
from GridDraw import Tetris
from Window import Window
from ResizeableWindow import resizableWindowUpdate
from Figure import Figure

class MainGameplay:
    def __init__(self):
        window = Window()
        colours = Colours()

        scaleWVduDimensionsX = (int(window.vduDimensions[0]) / 500) * 20
        scaleWVduDimensionsY = (int(window.vduDimensions[1]) / 400) * 20

        resizableWindowUpdateVar = resizableWindowUpdate()


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
                if game.state == "start":
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
                        pygame_menu.events.BACK

                    if event.key == pygame.K_p:
                        pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s: #knows when i lift the down key up
                    pressing_down = False
                if event.key == pygame.K_d or pygame.K_RIGHT:
                    pressing_right = False
                if event.key == pygame.K_a or pygame.K_LEFT:
                    pressing_left = False

            window.surface.fill(colours.backgroundColour)

            for i in range(game.height):
                for j in range(game.width):
                    pygame.draw.rect(window.surface, colours.gridColour, [game.x + scaleWVduDimensionsX * j, game.y + scaleWVduDimensionsY * i, scaleWVduDimensionsX, scaleWVduDimensionsY], 1)
                    if game.field[i][j] > 0:
                        pygame.draw.rect(window.surface, Figure.colors[game.field[i][j]],
                                         [game.x + scaleWVduDimensionsX * j + 1, game.y + scaleWVduDimensionsY * i + 1, scaleWVduDimensionsX - 2, scaleWVduDimensionsY - 1])
            if game.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in game.figure.image():
                            pygame.draw.rect(window.surface, Figure.colors[game.figure.color],
                                             [game.x + scaleWVduDimensionsX * (j + game.figure.x) + 1,
                                              game.y + scaleWVduDimensionsY * (i + game.figure.y) + 1,
                                              scaleWVduDimensionsX - 2, scaleWVduDimensionsY - 2])

            fontOpenSans = pygame.font.SysFont('sans', 35)
            score_tracker = fontOpenSans.render("Score: " + str(game.score), True, colours.black)


            window.surface.blit(score_tracker, [0, 0])
            if game.state == "gameover":
                pass

            pygame.display.flip()
            clock.tick(fps)

        pygame.quit()