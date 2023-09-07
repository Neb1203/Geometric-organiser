from Figure import Figure
from Window import Window
from GameStateEnum import GameStateEnum
import random

class Tetris:
    level = 2
    score = 0
    field = []
    x = (int(Window().vduDimensions[0]) - (Window().zoomX * 10)) / 2
    y = 0
    figure = None
    heldFigure = None
    numUpcomingFigures = 3
    upcomingFigureTypes = []

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = GameStateEnum.STARTED
        self.upcomingFigureTypes = []
        self.upcomingFigureColors = []
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)
        for i in range(self.numUpcomingFigures):
            self.upcomingFigureTypes.append(self.newFigureType())
            self.upcomingFigureColors.append(self.newFigureColor())

    def newFigureType(self):
        return random.randint(0, len(Figure.figures) - 1)
    def newFigureColor(self):
        return random.randint(1, len(Figure.colors) - 1)
    def newFigure(self):
        self.figure = Figure(3, 0, self.upcomingFigureTypes[0], self.upcomingFigureColors[0])
        self.upcomingFigureTypes.pop(0)
        self.upcomingFigureColors.pop(0)
        self.upcomingFigureTypes.append(self.newFigureType())
        self.upcomingFigureColors.append(self.newFigureColor())

    def swapHeldFigure(self):
        self.figure = self.heldFigure
        self.upcomingFigureTypes.pop(0)
        self.upcomingFigureColors.pop(0)
        self.upcomingFigureTypes.append(self.newFigureType())
        self.upcomingFigureColors.append(self.newFigureColor())
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
        self.score += 1/2 * (lines * (lines+1))

    def goSpace(self):
        if self.state.gameStarted():
            while not self.intersects():
                self.figure.y += 1
            self.figure.y -= 1
            self.freeze()

    def goDown(self):
        if self.state.gameStarted():
            self.figure.y += 1
            if self.intersects():
                self.figure.y -= 1
                self.freeze()
                return True

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.breakLines()
        self.newFigure()
        if self.intersects():
            self.state = GameStateEnum.GAME_OVER

    def goSide(self, dx):
        if self.state.gameStarted():
            old_x = self.figure.x
            self.figure.x += dx
            if self.intersects():
                self.figure.x = old_x

    def rotateLeft(self):
        if self.state.gameStarted():
            old_rotation = self.figure.rotation
            self.figure.rotateRight()
            if self.intersects():
                self.figure.rotation = old_rotation

    def rotateRight(self):
        if self.state.gameStarted():
            old_rotation = self.figure.rotation
            self.figure.rotateRight()
            if self.intersects():
                self.figure.rotation = old_rotation

    def setHeldFigure(self, heldPiece):
        if self.heldFigure == None:
            self.heldFigure = heldPiece
            self.heldFigure.resetCoordinates()
            self.newFigure()
        else:
            # Swap the held piece for the current piece onscreen
            currentPiece = heldPiece
            currentPiece.resetCoordinates()
            self.figure = self.heldFigure
            self.heldFigure = currentPiece

