import pygame
from Window import Window
from Figure import Figure
from Tetris import Tetris

colors = [
    (30, 21, 42), #Dark purple
    (78, 103, 102), #Deep Space Sparkle
    (90, 177, 187), #Cadet Blue
    (128, 189, 159), #Eton Blue
    (165, 200, 130),
    (206, 211, 122), #Straw
    (247, 221, 114), #Jasmine
]

window = Window()

class resizableWindowUpdate:
    def __init__(self):
        self.windowSize = pygame.display.get_window_size()
        self.scaleWVduDimensionsX = (int(self.windowSize[0]) / 500) * 20
        self.scaleWVduDimensionsY = (int(self.windowSize[1]) / 400) * 20
    def update(self):
        newscaleWVduDimensionsX = (int(self.windowSize[0]) / 500) * 20
        newscaleWVduDimensionsY = (int(self.windowSize[1]) / 400) * 20
        self.scaleWVduDimensionsX = newscaleWVduDimensionsX
        self.scaleWVduDimensionsY = newscaleWVduDimensionsY
    def reDraw(self, ):
        window.displaySize.fill(Window.orange)

resizableWindowUpdateVar = resizableWindowUpdate()


game = Tetris(20, 10, resizableWindowUpdateVar.scaleWVduDimensionsX, resizableWindowUpdateVar.scaleWVduDimensionsY, resizableWindowUpdateVar.windowSize)

# Define some colors
black = (0, 0, 0)
gray = (128, 128, 128)

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
counter = 0

speed = 1
delay = 400000

pressing_down = False
pressing_right = False
pressing_left = False

while not done:
    print(pygame.display.get_window_size())
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    if pressing_right == True: #Used for hold to move
        game.go_side(1)
    if pressing_left == True:
        game.go_side(-1)

    for event in pygame.event.get():

        if event.type == pygame.WINDOWRESIZED:
            resizableWindowUpdateVar.update()
            game(20, 10, resizableWindowUpdateVar.scaleWVduDimensionsX, resizableWindowUpdateVar.scaleWVduDimensionsY, resizableWindowUpdateVar.windowSize)

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN: #Down keys for rotating
            if event.key == pygame.K_q:
                game.rotate_right()
            if event.key == pygame.K_e:
                game.rotate_left()

            if event.key == pygame.K_s:
                pressing_down = True

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                pressing_left = True
                pygame.key.set_repeat(delay, speed)
                game.go_side(-1)

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                pressing_right = True
                pygame.key.set_repeat(delay, speed)
                game.go_side(1)

            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

            if event.key == pygame.K_p:
                pygame.quit()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_s: #knows when i lift the down key up
            pressing_down = False
        if event.key == pygame.K_d or pygame.K_RIGHT:
            pressing_right = False
        if event.key == pygame.K_a or pygame.K_LEFT:
            pressing_left = False

    window.displaySize.fill(window.orange)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(window.displaySize, gray, [game.x + resizableWindowUpdateVar.scaleWVduDimensionsX * j, game.y + resizableWindowUpdateVar.scaleWVduDimensionsY * i, resizableWindowUpdateVar.scaleWVduDimensionsX, resizableWindowUpdateVar.scaleWVduDimensionsY], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(window.displaySize, colors[game.field[i][j]],
                                 [game.x + resizableWindowUpdateVar.scaleWVduDimensionsX * j + 1, game.y + resizableWindowUpdateVar.scaleWVduDimensionsY * i + 1, resizableWindowUpdateVar.scaleWVduDimensionsX - 2, resizableWindowUpdateVar.scaleWVduDimensionsY - 1])
    #
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(window.displaySize, colors[game.figure.color],
                                     [game.x + resizableWindowUpdateVar.scaleWVduDimensionsX * (j + game.figure.x) + 1,
                                      game.y + resizableWindowUpdateVar.scaleWVduDimensionsY * (i + game.figure.y) + 1,
                                      resizableWindowUpdateVar.scaleWVduDimensionsX - 2, resizableWindowUpdateVar.scaleWVduDimensionsY - 2])

    font_Fredoka_one_25 = pygame.font.SysFont('Fredoka One', 25, True, False)
    font_Fredoka_one_65 = pygame.font.SysFont('Fredoka One', 65, True, False)
    font_Alata_25 = pygame.font.SysFont('Alata', 25)
    font_Alata_65 = pygame.font.SysFont('Alata', 65)
    score_tracker = font_Alata_25.render("Score: " + str(game.score), True, black)
    text_game_over = font_Fredoka_one_65.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font_Fredoka_one_65.render("Press ESC", True, (255, 215, 0))

    #Restart game font button
    restart_text = font_Alata_25.render("Restart with Esc", True, black)
    window.displaySize.blit(score_tracker, [0, 0])
    window.displaySize.blit(restart_text, [132, 480])
    if game.state == "gameover":
        window.displaySize.blit(text_game_over, [20, 200])
        window.displaySize.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()