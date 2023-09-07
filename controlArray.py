import pygame
pygame.init()
key_mapping = {
    'left': pygame.K_a,
    'right': pygame.K_d,
    'hardDrop': pygame.K_SPACE,
    'softDrop': pygame.K_s,
    'rotateLeft': pygame.K_q,
    'rotateRight': pygame.K_e,
    'lockPiece': pygame.K_l,
    'pause': pygame.K_ESCAPE
}

def update(target, newValue):
    key_mapping['target'] = newValue
