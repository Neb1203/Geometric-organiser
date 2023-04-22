
import pygame
import pygame_gui

displaySize = (800, 600)
pygame.init()

pygame.display.set_caption('Quick Start')
windowSurface = pygame.display.set_mode((displaySize), pygame.RESIZABLE)

background = pygame.Surface((displaySize))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((displaySize))

helloButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                           text='Say Hello',
                                           manager=manager)

clock = pygame.time.Clock()
isRunning = True

while isRunning:
    timeDelta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == helloButton:
                print('Hello World!')

        manager.process_events(event)

    manager.update(timeDelta)

    windowSurface.blit(background, (0, 0))
    manager.draw_ui(windowSurface)

    pygame.display.update()


while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWRESIZED:
            print("hello")

        if event.type == pygame.K_a:
            displaySize(0, 0)
            windowSurface()

