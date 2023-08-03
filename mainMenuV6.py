import pygame
from Window import Window
from Colours import Colours
from CenterButton import CenterButton

w = Window()
c = Colours()
cb = CenterButton()

surface = w.surface
color = (255, 255, 255)

color_light = (170, 170, 170)
color_dark = (100, 100, 100)

width = w.vduDimensions[0]
height = w.vduDimensions[1]

smallFont = pygame.font.SysFont('Corbel', 35)

text = smallFont.render('wows', True, color)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if mouseBoundrayX and mouseBoundrayY:
                pygame.quit()

    w.surface.fill(c.backgroundColour)
    buttonX = 500
    buttonY = 60
    mouse = pygame.mouse.get_pos()
    totalNumButtons = 1
    margins = 20
    mouseBoundrayX = cb.centerButtonWidth(buttonX) <= mouse[0] <= cb.centerButtonWidth(buttonX) + buttonX
    mouseBoundrayY = cb.centerButtonHeight(buttonY, totalNumButtons, margins, 0) <= mouse[1] <= cb.centerButtonHeight(buttonY,totalNumButtons,margins, 0) + buttonY


    if  mouseBoundrayX and mouseBoundrayY:
        pygame.draw.rect(surface, color_light, [cb.centerButtonWidth(buttonX), cb.centerButtonHeight(buttonY, totalNumButtons, margins, 0), buttonX, buttonY])
    else:
        pygame.draw.rect(surface, color_dark, [cb.centerButtonWidth(buttonX), cb.centerButtonHeight(buttonY, totalNumButtons, margins, 0), buttonX, buttonY])

    surface.blit(text, (cb.centerButtonWidth(buttonX) + 35, cb.centerButtonHeight(buttonY, totalNumButtons, margins, 0)))

    # updates the frames of the game
    pygame.display.update()
