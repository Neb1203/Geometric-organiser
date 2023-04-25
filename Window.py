import pygame
from Colours import Colours

class Window:
    def __init__(self):
        # Initialize the game engine
        pygame.init()
        pygame.display.set_caption("Geometric Organiser")
        screenSize = 50
        self.vduDimensions = (8 * screenSize, 9 * screenSize)
        self.setMode = pygame.display.set_mode(self.vduDimensions)

        self.backgroundColor = (255, 154, 0)
        self.gridColour = Colours.gray
    def invisibleGrid(self):
        self.gridColour = self.backgroundColor















