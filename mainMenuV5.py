import pygame
import button
from Window import Window
from CenterButton import CenterButton
while True:
    w = Window()
    cb = CenterButton()
    resumePath = "button images/Resume imagee.png"

    totalNumButtons = 0
    margins = 20

    resumeImage = pygame.image.load(resumePath).convert_alpha()

    resume_button = button.Button(cb.centerButtonWidth(resumePath), cb.centerButtonHeight(resumePath, totalNumButtons, margins, 0), resumeImage, 1)

    if resume_button.draw(w.surface):
        print("resume button")