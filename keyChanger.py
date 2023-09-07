import pygame
import time
class keyChanger:
    def __init__(self):
        pygame.init()
        self.running = True
        self.pressed_key = None
        self.inputKey = None
    def get_pressed_key(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    # Check if a key is pressed
                    self.pressed_key = event.key
                    self.running = False# Exit the loop on key press
        if self.pressed_key is not None:
            self.running = True
            return self.keyDictionary(pygame.key.name(self.pressed_key))
        else:
            return None
    def keyDictionary(self, inputKey):
        key_mapping = {
            'a': pygame.K_a,
            'b': pygame.K_b,
            'c': pygame.K_c,
            'd': pygame.K_d,
            'e': pygame.K_e,
            'f': pygame.K_f,
            'g': pygame.K_g,
            'h': pygame.K_h,
            'i': pygame.K_i,
            'j': pygame.K_j,
            'k': pygame.K_k,
            'l': pygame.K_l,
            'm': pygame.K_m,
            'n': pygame.K_n,
            'o': pygame.K_o,
            'p': pygame.K_p,
            'q': pygame.K_q,
            'r': pygame.K_r,
            's': pygame.K_s,
            't': pygame.K_t,
            'u': pygame.K_u,
            'v': pygame.K_v,
            'w': pygame.K_w,
            'x': pygame.K_x,
            'y': pygame.K_y,
            'z': pygame.K_z,
            '0': pygame.K_0,
            '1': pygame.K_1,
            '2': pygame.K_2,
            '3': pygame.K_3,
            '4': pygame.K_4,
            '5': pygame.K_5,
            '6': pygame.K_6,
            '7': pygame.K_7,
            '8': pygame.K_8,
            '9': pygame.K_9,
            'space': pygame.K_SPACE,
            'tab': pygame.K_TAB,
            'return': pygame.K_RETURN,
            'esc': pygame.K_ESCAPE,
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'up': pygame.K_UP,
            'down': pygame.K_DOWN,
            'ctrl': pygame.K_LCTRL,
            'alt': pygame.K_LALT,
            'shift': pygame.K_LSHIFT,
            'backspace': pygame.K_BACKSPACE,
            'delete': pygame.K_DELETE,
            'insert': pygame.K_INSERT,
            'home': pygame.K_HOME,
            'end': pygame.K_END,
            'pageup': pygame.K_PAGEUP,
            'pagedown': pygame.K_PAGEDOWN,
            'f1': pygame.K_F1,
            'f2': pygame.K_F2,
            'f3': pygame.K_F3,
            'f4': pygame.K_F4,
            'f5': pygame.K_F5,
            'f6': pygame.K_F6,
            'f7': pygame.K_F7,
            'f8': pygame.K_F8,
            'f9': pygame.K_F9,
            'f10': pygame.K_F10,
            'f11': pygame.K_F11,
            'f12': pygame.K_F12,
            # Add more keys as needed
        }
        self.pressed_key = None
        inputKey = inputKey.lower()
        if inputKey in key_mapping:
            return key_mapping[inputKey]
        else:
            return None