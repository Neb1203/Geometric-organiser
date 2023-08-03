import pygame
from Window import Window

w = Window()
surface = w.surface

colour = (255, 255, 255)
colour_light = (170, 170, 170)
colour_dark = (100, 100, 100)

width = w.vduDimensions[0]

height = w.vduDimensions[1]

smallfont = pygame.font.SysFont('Corbel', 35)

text = smallfont.render('quit', True, colour)

while True:
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()

    surface.fill((60, 25, 60))

    mouse = pygame.mouse.get_pos()

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(surface, colour_light, [width / 2, height / 2, 140, 40])
    else:
        pygame.draw.rect(surface, colour_dark, [width / 2, height / 2, 140, 40])

    surface.blit(text, (width / 2 + 50, height / 2))

    pygame.display.update()
