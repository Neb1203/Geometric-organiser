import pygame
import button
from mainMenuV4 import menuChanged

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("button images/resumeButton (Custom).png").convert_alpha()
mainMenuImage = pygame.image.load("button images/mainMenuButton (Custom).png").convert_alpha()

#create button instances
resume_button = button.Button(304, 125, resume_img, 1)
mainMenuButton = button.Button(297, 250, mainMenuImage, 1)


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    print('Game paused')
    #check menu state
    if menu_state == "main":
      print('main')
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if mainMenuButton.draw(screen):
        menu_state = "mainMenu"
        print("mainMenu")
  else:
    draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()