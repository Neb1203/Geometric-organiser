import pygame

from GridDraw import Tetris
from Window import Window
from Colours import Colours
from Figure import Figure

window = Window()

tetris = Tetris(20, 10, window.scaleWVduDimensionsX, window.scaleWVduDimensionsY, window.windowSize)

# Define some colors


# Loop until the user clicks the close button.
countdown = pygame.time.Clock()
fps = 25
iterCounter = 0

sidewaysMovementDistance = 100
sidewaysMovementDelay = 3000

pressingDown = False
pressingRight = False
pressingLeft = False

gameRunning = True
while gameRunning:
    if tetris.figure is None:
        tetris.newFigure()
    iterCounter += 1
    if iterCounter > 100000:
        iterCounter = 0
    if iterCounter % (fps // tetris.level // 2) == 0 or pressingDown:
        if tetris.state.gameStarted():
            tetris.goDown()

    for event in pygame.event.get():
        if event.type == pygame.WINDOWRESIZED:
            window.updateSize()
            # game(20, 10, resizableWindowUpdateVar.scaleWVduDimensionsX, resizableWindowUpdateVar.scaleWVduDimensionsY, resizableWindowUpdateVar.windowSize)

        if event.type == pygame.QUIT:
            gameRunning = False

        if event.type == pygame.KEYDOWN: # When any key is pressed
            if event.key == pygame.K_q:
                tetris.rotateRight()
            if event.key == pygame.K_e:
                tetris.rotateLeft()

            if event.key == pygame.K_s:
                pressingDown = True

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                pygame.key.set_repeat(sidewaysMovementDelay, sidewaysMovementDistance)
                tetris.goSide(-1)

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                pygame.key.set_repeat(sidewaysMovementDelay, sidewaysMovementDistance)
                tetris.goSide(1)

            if event.key == pygame.K_SPACE:
                tetris.goSpace()
            if event.key == pygame.K_ESCAPE:
                tetris.__init__(20, 10)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_s: # Knows when I lift the 's' key up
            pressingDown = False
        if event.key == pygame.K_d or pygame.K_RIGHT:
            pressingRight = False
        if event.key == pygame.K_a or pygame.K_LEFT:
            pressingLeft = False

    window.displaySize.fill(Colours.backgroundColor)

    for i in range(tetris.height):
        for j in range(tetris.width):
            pygame.draw.rect(window.displaySize, Colours.gray, [tetris.x + window.scaleWVduDimensionsX * j, tetris.y + window.scaleWVduDimensionsY * i, window.scaleWVduDimensionsX, window.scaleWVduDimensionsY], 1)
            if tetris.field[i][j] > 0:  # If piece reached bottom
                pygame.draw.rect(window.displaySize, Figure.colors[tetris.field[i][j]],
                                 [tetris.x + window.scaleWVduDimensionsX * j + 1, tetris.y + window.scaleWVduDimensionsY * i + 1, window.scaleWVduDimensionsX - 2, window.scaleWVduDimensionsY - 1])
    if tetris.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in tetris.figure.image():
                    pygame.draw.rect(window.displaySize, Figure.colors[tetris.figure.color],
                                     [tetris.x + window.scaleWVduDimensionsX * (j + tetris.figure.x) + 1,
                                      tetris.y + window.scaleWVduDimensionsY * (i + tetris.figure.y) + 1,
                                      window.scaleWVduDimensionsX - 2, window.scaleWVduDimensionsY - 2])

    fontFredokaOne25 = pygame.font.SysFont('Fredoka One', 25, True, False)
    fontFredokaOne65 = pygame.font.SysFont('Fredoka One', 65, True, False)
    fontAlata25 = pygame.font.SysFont('Alata', 25)
    fontAlata65 = pygame.font.SysFont('Alata', 65)
    textScore = fontAlata25.render("Score: " + str(tetris.score), True, Colours.black)
    textGameOver = fontFredokaOne65.render("Game Over", True, (255, 125, 0))
    textPressEsc = fontFredokaOne65.render("Press ESC", True, (255, 215, 0))

    # Restart game font button
    restartText = fontAlata25.render("Restart with Esc", True, Colours.black)
    window.displaySize.blit(textScore, [0, 0])
    window.displaySize.blit(restartText, [132, 480])
    if tetris.state.gameOver():
        window.displaySize.blit(textGameOver, [20, 200])
        window.displaySize.blit(textPressEsc, [25, 265])

    pygame.display.flip()
    countdown.tick(fps)

pygame.quit()
