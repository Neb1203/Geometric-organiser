import pygame
from Figure import Figure
from GameStateEnum import GameStateEnum

class Tetris:
    level = 2
    score = 0
    state = GameStateEnum.STARTED
    field = []
    figure = None

    def __init__(self, gridHeight, gridWidth, scaleWVduDimensionsX, scaleWVduDimensionsY, windowSize):
        self.gridHeight = gridHeight
        self.gridWidth = gridWidth
        self.x = (windowSize[0] - (scaleWVduDimensionsX * 10)) / 2
        self.y = 0
        self.windowSize = pygame.display.get_window_size()
        for squareHeight in range(gridHeight):
            newColumn = []
            for squareWidth in range(gridWidth):
                newColumn.append(0)
            self.field.append(newColumn)

    def newFigure(self):
        self.figure = Figure(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.gridHeight - 1 or \
                            j + self.figure.x > self.gridWidth - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def reachedBottom(self):
        lines = 0
        for i in range(1, self.gridHeight):
            zeros = 0
            for j in range(self.gridWidth):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.gridWidth):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def hardDrop(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def moveDown(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.reachedBottom()
        self.newFigure()
        if self.intersects():
            self.state = GameStateEnum.GAME_OVER

    def goSide(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotateRight(self):
        old_rotation = self.figure.rotation
        self.figure.rotateRight()
        if self.intersects():
            self.figure.rotation = old_rotation

    def rotateLeft(self):
        old_rotation = self.figure.rotation
        self.figure.rotateRight()
        if self.intersects():
            self.figure.rotation = old_rotation
