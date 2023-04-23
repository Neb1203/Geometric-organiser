import pygame
from Colours import Colours

class Window:
    def __init__(self):
        # Initialize the game engine
        pygame.init()
        pygame.display.set_caption("Geometric Organiser")
        appIcon = pygame.image.load("geometric-organiser-logo.jpg")
        pygame.display.set_icon(appIcon)

        self.vduDimensions = (800,600)
        self.displaySize = pygame.display.set_mode((self.vduDimensions), pygame.RESIZABLE)

        self.windowSize = pygame.display.get_window_size()
        self.scaleWVduDimensionsX = (int(self.windowSize[0]) / 500) * 20
        self.scaleWVduDimensionsY = (int(self.windowSize[1]) / 400) * 20
    def invisibleGrid(self):
        self.gridColour = Colours.backgroundColor

    def updateSize(self):
        # Window().invisibleGrid()
        newScaleWVduDimensionsX = (int(self.windowSize[0]) / 500) * 20
        newScaleWVduDimensionsY = (int(self.windowSize[1]) / 400) * 20















