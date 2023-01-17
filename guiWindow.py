import pygame
import pygame_gui
from Window import Window


menuWindow = Window()

background = pygame.Surface((menuWindow.vduDimensions))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((menuWindow.vduDimensions))

buttonLayoutRect = pygame.Rect(30, 20, 100, 20)
hello_button = pygame_gui.elements.UIButton(relative_rect=buttonLayoutRect,
                                        text='Say Hello',
                                        manager=manager,
                                        container=menuWindow.displaySize)

clock = pygame.time.Clock()
isRunning = True

while isRunning:
    time_delta = clock.tick(60) / 1000.0 #Tick should be called once per frame. IT computes how many miliseconds passed since the previous call
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    menuWindow.displaySize.blit(background, (0, 0))
    manager.draw_ui(menuWindow.displaySize)

    pygame.display.update()
