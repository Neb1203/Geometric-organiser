import pygame
from Colours import Colours

class Window:
    def __init__(self):
        # Initialize the game engine
        pygame.init()
        pygame.display.set_caption("Geometric Organiser")

        self.vduDimensions = (800,600)
        self.displaySize = pygame.display.set_mode((self.vduDimensions), pygame.RESIZABLE)

        self.backgroundColor = (255, 154, 0)
        self.gridColour = Colours.gray
    def invisibleGrid(self):
        self.gridColour = self.backgroundColor















