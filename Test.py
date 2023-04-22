import pygame
import pygame_gui


pygame.init()

pygame.display.set_caption('Quick Start')
windowSurface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

# hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
#                                              text='Say Hello',
#                                              manager=manager)

clock = pygame.time.Clock()
isRunning = True

while isRunning:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        # if event.type == pygame_gui.UI_BUTTON_PRESSED:
        #     if event.ui_element == hello_button:
        #         print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    windowSurface.blit(background, (0, 0))
    manager.draw_ui(windowSurface)

    pygame.display.update()