import pygame

from Colours import Colours
from GridDraw import Tetris
from Window import Window
from ResizeableWindow import resizableWindowUpdate
from Figure import Figure

class MainGameplay:
    def __init__(self):
        window = Window()
        colours = Colours()

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
                        game.__init__(10, 20)

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
                    pygame.draw.rect(window.surface, colours.gridColour, [game.x + resizableWindowUpdateVar.scaleWVduDimensionsX * j, game.y + resizableWindowUpdateVar.scaleWVduDimensionsY * i, resizableWindowUpdateVar.scaleWVduDimensionsX, resizableWindowUpdateVar.scaleWVduDimensionsY], 1)
                    if game.field[i][j] > 0:
                        pygame.draw.rect(window.surface, Figure.colors[game.field[i][j]],
                                         [game.x + resizableWindowUpdateVar.scaleWVduDimensionsX * j + 1, game.y + resizableWindowUpdateVar.scaleWVduDimensionsY * i + 1, resizableWindowUpdateVar.scaleWVduDimensionsX - 2, resizableWindowUpdateVar.scaleWVduDimensionsY - 1])
            if game.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in game.figure.image():
                            pygame.draw.rect(window.surface, Figure.colors[game.figure.color],
                                             [game.x + resizableWindowUpdateVar.scaleWVduDimensionsX * (j + game.figure.x) + 1,
                                              game.y + resizableWindowUpdateVar.scaleWVduDimensionsY * (i + game.figure.y) + 1,
                                              resizableWindowUpdateVar.scaleWVduDimensionsX - 2, resizableWindowUpdateVar.scaleWVduDimensionsY - 2])

            font_Fredoka_one_25 = pygame.font.SysFont('Fredoka One', 25, True, False)
            font_Fredoka_one_65 = pygame.font.SysFont('Fredoka One', 65, True, False)
            font_Alata_25 = pygame.font.SysFont('Alata', 25)
            font_Alata_65 = pygame.font.SysFont('Alata', 65)
            score_tracker = font_Alata_25.render("Score: " + str(game.score), True, colours.black)
            text_game_over = font_Fredoka_one_65.render("Game Over", True, (255, 125, 0))
            text_game_over1 = font_Fredoka_one_65.render("Press ESC", True, (255, 215, 0))

            #Restart game font button
            restart_text = font_Alata_25.render("Restart with Esc", True, colours.black)
            window.surface.blit(score_tracker, [0, 0])
            window.surface.blit(restart_text, [132, 480])
            if game.state == "gameover":
                window.surface.blit(text_game_over, [20, 200])
                window.surface.blit(text_game_over1, [25, 265])

            pygame.display.flip()
            clock.tick(fps)

        pygame.quit()