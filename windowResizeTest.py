
import pygame
import pygame_gui

display_size = (800, 600)
pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((display_size) ,pygame.RESIZABLE)

background = pygame.Surface((display_size))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((display_size))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Say Hello',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWRESIZED:
            print("hello")

        if event.type == pygame.K_a:
            display_size(0,0)
            window_surface()

