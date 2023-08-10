import pygame
from Window import Window
from Colours import Colours
from CenterButton import CenterButton

w = Window()
cb = CenterButton()
c = Colours()
class ButtonV3():
    def __init__(self, text):
        color = (255, 255, 255)

        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)

        self.width = w.vduDimensions[0]
        self.height = w.vduDimensions[1]

        smallFont = pygame.font.SysFont('Corbel', 35)
        self.text = smallFont.render(text, True, color)
    def draw(self, x, y, totalBut, margins):
        surface = w.surface
        surface.fill(c.backgroundColour)
        self.buttonX = x
        self.buttonY = y
        self.mouse = pygame.mouse.get_pos()

        mouseBoundrayX = cb.centerButtonWidth(self.buttonX) <= self.mouse[0] <= cb.centerButtonWidth(self.buttonX) + self.buttonX
        mouseBoundrayY = cb.centerButtonHeight(self.buttonY, totalBut, margins, 0) <= self.mouse[1] <= cb.centerButtonHeight(self.buttonY, totalBut, margins, 0) + self.buttonY

        if mouseBoundrayX and mouseBoundrayY:
            pygame.draw.rect(surface, self.color_light, [cb.centerButtonWidth(self.buttonX),
                                                    cb.centerButtonHeight(self.buttonY, totalBut, margins, 0),
                                                    self.buttonX, self.buttonY])
        else:
            pygame.draw.rect(surface, self.color_dark, [cb.centerButtonWidth(self.buttonX), cb.centerButtonHeight(self.buttonY, totalBut, margins, 0), self.buttonX, self.buttonY])

        surface.blit(text, (cb.centerButtonWidth(self.buttonX) + 35, cb.centerButtonHeight(self.buttonY, totalBut, margins, 0) + self.buttonY / 4))
ButtonV3 = ButtonV3("hello")
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ButtonV3.draw(500, 600, 0, 20).mouseBoundrayX and ButtonV3.draw(500, 600, 0, 20).mouseBoundrayY:
                pygame.quit()

ButtonV3.draw(500, 600, 0, 20)


    # updates the frames of the game
pygame.display.update()
