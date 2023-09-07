import pygame

def get_pressed_key():
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    pygame.display.set_caption("Key Detector")

    running = True
    pressed_key = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Check if a key is pressed
                pressed_key = event.key
                running = False  # Exit the loop on key press

        # Clear the screen
        screen.fill((255, 255, 255))
        pygame.display.flip()

    pygame.quit()

    if pressed_key is not None:
        return pressed_key
    else:
        return None

# Example usage:
pressed_key = get_pressed_key()
if pressed_key is not None:
    print(f"The pressed key is: {pygame.key.name(pressed_key)} (pygame.K_{pygame.key.name(pressed_key).upper()})")
else:
    print("No key was pressed.")
# print({pygame.key.name(pressed_key)})