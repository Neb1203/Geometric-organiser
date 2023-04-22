import pygame
from GridDraw import Tetris
from Window import Window
class ResizeableWindow:
    def __init__(self):
        self.windowSize = pygame.display.get_window_size()
        self.scaleWVduDimensionsX = (int(self.windowSize[0]) / 500) * 20
        self.scaleWVduDimensionsY = (int(self.windowSize[1]) / 400) * 20
    def update(self):
        print("CUM")
        # Window().invisibleGrid()
        newScaleWVduDimensionsX = (int(self.windowSize[0]) / 500) * 20
        newScaleWVduDimensionsY = (int(self.windowSize[1]) / 400) * 20

        Tetris(20, 10, newScaleWVduDimensionsX, newScaleWVduDimensionsY, self.windowSize)

    # def reDraw(self,):
    #     Figure.Tetris()