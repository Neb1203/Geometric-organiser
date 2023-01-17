import pygame

class resizableWindowUpdate:
    def __init__(self):
        self.windowSize = pygame.display.get_window_size()
        self.scaleWVduDimensionsX = (int(self.windowSize[0]) / 500) * 20
        self.scaleWVduDimensionsY = (int(self.windowSize[1]) / 400) * 20
    def update(self):
        newscaleWVduDimensionsX = (int(self.windowSize[0]) / 500) * 20
        newscaleWVduDimensionsY = (int(self.windowSize[1]) / 400) * 20
        self.scaleWVduDimensionsX = newscaleWVduDimensionsX
        self.scaleWVduDimensionsY = newscaleWVduDimensionsY
    def reDraw(self, ):
        window.displaySize.fill(Window.orange)