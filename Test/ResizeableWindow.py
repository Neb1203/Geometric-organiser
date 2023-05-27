import pygame
from gridDraw import Tetris
from Window import Window
class resizableWindowUpdate:
    def __init__(self):
        self.windowSize = pygame.display.get_window_size()
        self.scaleX = (int(self.windowSize[0]) / 500) * 20
        self.scaleY = (int(self.windowSize[1]) / 400) * 20
    def update(self):
        print("CUM")
        # Window().invisibleGrid()
        newScaleWVduDimensionsX = (int(self.windowSize[0]) / 500) * 20
        newScaleWVduDimensionsY = (int(self.windowSize[1]) / 400) * 20

        Tetris(20, 10, newScaleWVduDimensionsX, newScaleWVduDimensionsY, self.windowSize)

    # def reDraw(self,):
    #     Figure.Tetris()