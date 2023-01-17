import pygame
import random
from Window import Window


colors = [
    (30, 21, 42),#Dark purple
    (78, 103, 102),#Deep Space Sparkle
    (90, 177, 187),#Cadet Blue
    (128, 189, 159),#Eton Blue
    (165, 200, 130),#Pistachio
    (206, 211, 122),#Straw
    (247, 221, 114),#Jasmine
]

class Figure:

    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = self.type
        self.rotation = 0
        self.color = self.type


    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate_right(self): # Defines rotate right/left + or - 1
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
    def rotate_left(self):
        self.rotation = (self.rotation + -1) % len(self.figures[self.type])

class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    # x = (int(windowSize[0]) -)
    # x = 100
    # y = 0
    figure = None

    def __init__(self, height, width, scaleWVduDimensionsX, scaleWVduDimensionsY, windowSize):
        self.height = height
        self.width = width
        self.x = (int(windowSize[0]) - (scaleWVduDimensionsX * 10)) / 2
        self.y = 0
        self.windowSize = pygame.display.get_window_size()
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.figure = Figure(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate_left(self):
        old_rotation = self.figure.rotation
        self.figure.rotate_left()
        if self.intersects():
            self.figure.rotation = old_rotation

    def rotate_right(self):
        old_rotation = self.figure.rotation
        self.figure.rotate_right()
        if self.intersects():
            self.figure.rotation = old_rotation

window = Window()
windowSize = pygame.display.get_window_size()
scaleWVduDimensionsX = (int(windowSize[0]) / 500) * 20
scaleWVduDimensionsY = (int(windowSize[1]) / 400) * 20
game = Tetris(20, 10, scaleWVduDimensionsX, scaleWVduDimensionsY, windowSize)

# Define some colors
black = (0, 0, 0)
white = (255, 154, 0)
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

    window.displaySize.fill(white)
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(window.displaySize, gray, [game.x + scaleWVduDimensionsX * j, game.y + scaleWVduDimensionsY * i, scaleWVduDimensionsX, scaleWVduDimensionsY], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(window.displaySize, colors[game.field[i][j]],
                                 [game.x + scaleWVduDimensionsX * j + 1, game.y + scaleWVduDimensionsY * i + 1, scaleWVduDimensionsX - 2, scaleWVduDimensionsY - 1])
    # scaleWVduDimensionsX === width of whole grid or scaleWVduDimensionsX === width of one square of grid
    # scaleWVduDimensionsY === height of whole grid or scaleWVduDimensionsX === height of one square of grid
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(window.displaySize, colors[game.figure.color],
                                     [game.x + scaleWVduDimensionsX * (j + game.figure.x) + 1,
                                      game.y + scaleWVduDimensionsY * (i + game.figure.y) + 1,
                                      scaleWVduDimensionsX - 2, scaleWVduDimensionsY - 2])

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