import pygame
import button
from Window import Window
from CenterButton import CenterButton
from Colours import Colours
running = True
while running:
    w = Window()
    c = Colours()
    cb = CenterButton()
    w.surface.fill(c.backgroundColour)
    square_color = (255, 255, 255)  # Red color
    boxX = 300
    boxY = 150
    square_x = 300
    square_y = 300

    pygame.draw.rect(w.surface, square_color, (square_x, square_y, boxX, boxY))

    resumePath = "button images/Resume imagee.png"

    totalNumButtons = 0
    margins = 20

    resumeImage = pygame.image.load(resumePath).convert_alpha()

    resume_button = button.Button(cb.centerButtonWidth(resumePath), cb.centerButtonHeight(resumePath, totalNumButtons, margins, 0), resumeImage, 1)

    if resume_button.draw(w.surface):
        print("resume button")


    pygame.display.flip()
pygame.quit()