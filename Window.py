import pygame
from Colours import Colours
import pygame_menu

class Window:
    def __init__(self):
        # Initialize the game engine
        pygame.init()
        pygame.display.set_caption("Geometric Organiser")
        self.screenSize = (5)
        self.vduDimensions = (self.screenSize * 160, self.screenSize * 120)
        self.surface = pygame.display.set_mode(self.vduDimensions)

        self.zoomX = (int(self.vduDimensions[0]) / 500) * 20
        self.zoomY = (int(self.vduDimensions[1]) / 400) * 20

        self.mainTheme = pygame_menu.themes.Theme(background_color=(255, 166, 158),
                                                 title_font_antialias=True,
                                                 title_background_color=(252, 100, 88),
                                                 selection_color=(140, 94, 88),
                                                 widget_background_color=(255, 247, 248),
                                                 widget_font_antialias=True,
                                                 title_close_button=False,
                                                 widget_selection_effect=pygame_menu.widgets.HighlightSelection(),
                                                 title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
                                                 widget_font=pygame_menu.font.FONT_OPEN_SANS_LIGHT)
        self.noTitle = pygame_menu.themes.Theme(background_color=(255, 166, 158),
                                                selection_color=(140, 94, 88),
                                                widget_background_color=(255, 247, 248),
                                                widget_font_antialias=True,
                                                title_close_button=False,
                                                title_font_color=(0, 0, 0),
                                                widget_selection_effect=pygame_menu.widgets.HighlightSelection(),
                                                title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
                                                widget_font=pygame_menu.font.FONT_OPEN_SANS_LIGHT)
    def invisibleGrid(self):
        self.gridColour = self.backgroundColor













