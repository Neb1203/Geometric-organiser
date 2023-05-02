import pygame
from Colours import Colours

class Window:
    def __init__(self, screenSize):
        # Initialize the game engine
        pygame.init()
        pygame.display.set_caption("Geometric Organiser")
        self.screenSize = screenSize
        print(self.screenSize)
        self.vduDimensions = (((1080/5)*(4/5)) * screenSize, (1080/5) * screenSize)
        self.setMode = pygame.display.set_mode(self.vduDimensions)

        self.backgroundColor = (255, 154, 0)
        self.gridColour = Colours.gray
    def invisibleGrid(self):
        self.gridColour = self.backgroundColor













