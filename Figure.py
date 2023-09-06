import random


class Figure:

    type
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]], #long black ones
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    colors = [
        # The below color is never called, do not touch, otherwise when this color shape is shown it will # disappear when it should freeze
        (0, 0, 0),
        (30, 21, 42),
        (78, 103, 102),
        (90, 177, 187),
        (128, 189, 159),
        (165, 200, 130),
        (206, 211, 122),
        (247, 221, 114),
    ]

    def __init__(self, x, y, type, color):
        self.x = x
        self.y = y
        self.type = type
        self.color = color
        self.rotation = 0


    def image(self):
        return self.figures[self.type][self.rotation]
    def rotateRight(self):
        self.rotation = (self.rotation + -1) % len(self.figures[self.type])

    def resetCoordinates(self):
        self.x = 3
        self.y = 0