import pygame

from GridDraw import Tetris
from Window import Window
from Colours import Colours
from Figure import Figure
class MainGameplay:
    def mainGameplay(width, height, zoomX, zoomY):
        window = Window(3)
        y = 0
        game = Tetris(width,height, zoomX, zoomY)

        # Define some colors


        # Loop until the user clicks the close button.
        gameRunning = True
        clock = pygame.time.Clock()
        fps = 25
        counter = 0

        interval = 100
        delay = 300

        pressingDown = False
        pressingRight = False
        pressingLeft = False

        while gameRunning:
            if game.figure is None:
                game.newFigure()
            counter += 1
            if counter > 100000:
                counter = 0

            if counter % (fps // game.level // 2) == 0 or pressingDown:
                if game.state == "start":
                    game.goDown()

            for event in pygame.event.get():
                    # game(20, 10, resizableWindowUpdateVar.scaleWVduDimensionsX, resizableWindowUpdateVar.scaleWVduDimensionsY, resizableWindowUpdateVar.windowSize)

                if event.type == pygame.QUIT:
                    gameRunning = False

                if event.type == pygame.KEYDOWN: #Down keys for rotating
                    if event.key == pygame.K_q:
                        game.rotateRight()
                    if event.key == pygame.K_e:
                        game.rotateLeft()

                    if event.key == pygame.K_s:
                        pressingDown = True

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        pygame.key.set_repeat(delay, interval)
                        game.goSide(-1)

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        pygame.key.set_repeat(delay, interval)
                        game.goSide(1)

                    if event.key == pygame.K_SPACE:
                        game.goSpace()
                    if event.key == pygame.K_ESCAPE:
                        game.__init__(20, 10)

                    if event.key == pygame.K_p:
                        pygame.quit()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s: #knows when i lift the down key up
                    pressingDown = False
                if event.key == pygame.K_d or pygame.K_RIGHT:
                    pressingRight = False
                if event.key == pygame.K_a or pygame.K_LEFT:
                    pressingLeft = False

            window.setMode.fill(window.backgroundColor)

            for i in range(game.height):
                for j in range(game.width):
                    pygame.draw.rect(window.setMode, window.gridColour, [game.gridX + game.zoomX * j, game.gridY + game.zoomY * i, game.zoomX, game.zoomY], 1)
                    if game.field[i][j] > 0:
                        pygame.draw.rect(window.setMode, Figure.colors[game.field[i][j]],
                                         [game.gridX + game.zoomX * j + 1, game.gridY + game.zoomY * i + 1, game.zoomX - 2, game.zoomY - 1])
            if game.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in game.figure.image():
                            pygame.draw.rect(window.setMode, Figure.colors[game.figure.color],
                                             [game.gridX + game.zoomX * (j + game.figure.x) + 1,
                                              game.gridY + game.zoomY * (i +game.figure.y) + 1,
                                              game.zoomX - 2, game.zoomY - 2])

            fontFredokaOne25 = pygame.font.SysFont('Fredoka One', 25, True, False)
            fontFredokaOne65 = pygame.font.SysFont('Fredoka One', 65, True, False)
            fontAlata25 = pygame.font.SysFont('Alata', 25)
            fontAlata65 = pygame.font.SysFont('Alata', 65)
            scoreTracker = fontAlata25.render("Score: " + str(game.score), True, Colours.black)
            textGameOver = fontFredokaOne65.render("Game Over", True, (255, 125, 0))
            textPressEsc = fontFredokaOne65.render("Press ESC", True, (255, 215, 0))

            #Restart game font button
            restartText = fontAlata25.render("Restart with Esc", True, Colours.black)
            window.setMode.blit(scoreTracker, [0, 0])
            window.setMode.blit(restartText, [132, 480])
            if game.state == "gameover":
                window.setMode.blit(textGameOver, [20, 200])
                window.setMode.blit(textPressEsc, [25, 265])

            pygame.display.flip()
            clock.tick(fps)

        pygame.quit()