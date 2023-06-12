import pygame
import pygame_menu
from MainGameplay import MainGameplay
from Window import Window
import requests
import pprint
from hashGenerator import HashingGenerator

subTheme = pygame_menu.themes.THEME_SOLARIZED

mainTheme = pygame_menu.themes.THEME_ORANGE
window = Window()
hashGenerator = HashingGenerator()

subWindow = (300,200)



class menuOptions:
    def __init__(self):
        self.user_email = 'null'
        self.user_password = 'null'
        self.user_name = 'null'
    def setDifficulty(self, value, difficulty):
        # Do the job here
        # Window(50)
        pass

    def screenSize(self, screenSize):
        # Window.newScreenSize = screenSize
        pass

    def userName(self, userName):
        self.user_name = userName

    def password(self, password):
        self.user_password = password


    def email(self, email):
        self.user_email = email

    def pickGameMode(self, value, gameMode):
        global gameModeSelected
        gameModeSelected = gameMode
    def startGame(self):
        # Do the job here !
        if gameModeSelected == False:
            MainGameplay()
        elif gameModeSelected == True:
            print("cum")

    def confirmProfile(self):
        print(self.user_email, self.user_password)
        signup = {'email': self.user_email, 'password': self.user_password, 'user_name': self.user_name}

        r = requests.post('http://127.0.0.2:5000/player_details', params=signup)

        # payload = {'james'}
        # r = requests.post('127.0.0.2:5000/playerDetails', params=payload)
    def profileCreation():
        pass
menuOptions = menuOptions()
surface = window.surface

signup = pygame_menu.Menu('signup Screen',
                               window.vduDimensions[0],
                               window.vduDimensions[1],
                            theme=mainTheme)
startScreen = pygame_menu.Menu('Start Screen',
                               window.vduDimensions[0],
                               window.vduDimensions[1],
                            theme=mainTheme)
playMenu = pygame_menu.Menu('Play',
                            window.vduDimensions[0],
                            window.vduDimensions[1],
                            theme=mainTheme)
settings = pygame_menu.Menu('settings',
                            window.vduDimensions[0],
                            window.vduDimensions[1],
                            theme=mainTheme)
playerProfile = pygame_menu.Menu('Change player Profiles',
                            window.vduDimensions[0],
                            window.vduDimensions[1],
                            theme=mainTheme)
mainMenu = pygame_menu.Menu('Main Menu',
                            window.vduDimensions[0],
                            window.vduDimensions[1],
                            theme=mainTheme)

#signup screen
signup.add.text_input('User name :', copy_paste_enable=True, onchange=menuOptions.userName)
signup.add.text_input('Email :', copy_paste_enable=True, onchange=menuOptions.email)
signup.add.text_input('Password :', copy_paste_enable=True, onchange=menuOptions.password)
signup.add.button('Signup', menuOptions.confirmProfile)
#create buttons for startScreen
startScreen.add.label("Geometric Organiser")
startScreen.add.button('Go to main menu', mainMenu)
startScreen.add.button('Change player profile', playerProfile)
startScreen.add.button('Quit', pygame_menu.events.EXIT)

#create buttons for mainMenu
mainMenu.add.button('Play', playMenu)
mainMenu.add.button('Settings', settings)
mainMenu.add.button('Back', pygame_menu.events.BACK)

#settings
settings.add.range_slider('Set screen size',
                          range_values=[1,2,3,4,5],
                          default=3,
                          onchange = menuOptions.screenSize)

#Create buttons for playMenu
playMenu.add.selector('Gamemode : ', [('Campaign', True), ('Endless', False)], onchange = menuOptions.pickGameMode)
playMenu.add.selector('Difficulty :', [('Hard', 1), ('Normal', 2), ('Easy', 3)], onchange = menuOptions.setDifficulty)
playMenu.add.button('Start Game', menuOptions.startGame)
playMenu.add.button('back', pygame_menu.events.BACK)

#buttons for player profiles
playerProfile.add.button('Create a profile', menuOptions.profileCreation)
playerProfile.add.button('back', pygame_menu.events.BACK)

#buttons for profile creation
# profileCreation.add.text_input('User Name :', onchange=confirmProfile)
# profileCreation.add.text_input('Email :', onchange=email)
# profileCreation.add.button('confirm', confirmProfile)

#world map


if signup.is_enabled():
    signup.mainloop(surface)