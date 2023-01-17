import pygame

class Window:

    colors = [
        (30, 21, 42),  # Dark purple
        (78, 103, 102),  # Deep Space Sparkle
        (90, 177, 187),  # Cadet Blue
        (128, 189, 159),  # Eton Blue
        (165, 200, 130),
        (206, 211, 122),  # Straw
        (247, 221, 114),  # Jasmine
    ]
    def __init__(self):
        # Initialize the game engine
        pygame.init()
        pygame.display.set_caption("Geometric Organiser")

        self.vduDimensions = (800,600)
        self.displaySize = pygame.display.set_mode((self.vduDimensions), pygame.RESIZABLE)

        self.orange = (255, 154, 0)















