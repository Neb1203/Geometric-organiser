import pygame
from Colours import Colours

class Window:
    def __init__(self):
        # Initialize the game engine
        pygame.init()
        pygame.display.set_caption("Geometric Organiser")
        self.screenSize = (3)
        self.vduDimensions = (500, 400)
        self.surface = pygame.display.set_mode(self.vduDimensions)

        self.zoomX = (int(self.vduDimensions[0]) / 500) * 20
        self.zoomY = (int(self.vduDimensions[1]) / 400) * 20


    def invisibleGrid(self):
        self.gridColour = self.backgroundColor













