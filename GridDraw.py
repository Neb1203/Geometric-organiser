import pygame
from Figure import Figure
from Window import Window
class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    x = (int(Window().vduDimensions[0]) - (Window().zoomX * 10)) / 2
    y = 0
    figure = None

    def __init__(self, width, height):
        self.height = height
        self.width = width

        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def newFigure(self):
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

    def breakLines(self):
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

    def goSpace(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def goDown(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.breakLines()
        self.newFigure()
        if self.intersects():
            self.state = "gameover"

    def goSide(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotateLeft(self):
        old_rotation = self.figure.rotation
        self.figure.rotateRight()
        if self.intersects():
            self.figure.rotation = old_rotation

    def rotateRight(self):
        old_rotation = self.figure.rotation
        self.figure.rotateRight()
        if self.intersects():
            self.figure.rotation = old_rotation
