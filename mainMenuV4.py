import pygame
import pygame_menu
from MainGameplay import MainGameplay
from Window import Window
import requests
from hashGenerator import HashingGenerator
# pygame.mixer.init()
# pygame.mixer.music.load('mmm.mp3')
# pygame.mixer.music.play(-1, 0)

subTheme = pygame_menu.themes.THEME_SOLARIZED
mainTheme = pygame_menu.themes.Theme(background_color=(255, 166, 158),
                                     title_font_antialias = True,
                                     title_background_color=(252, 100, 88),
                                     selection_color=(140, 94, 88),
                                     widget_background_color=(255, 247, 248),
                                     widget_font_antialias = True,
                                     title_close_button = False,
                                     widget_selection_effect=pygame_menu.widgets.HighlightSelection(),
                                     title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
                                     widget_font=pygame_menu.font.FONT_OPEN_SANS_LIGHT)

mainTheme.widget_margin = (20, 15)
mainTheme.widget_alignment = pygame_menu.locals.ALIGN_LEFT

window = Window()
hashGenerator = HashingGenerator()
subWindow = (300,200)

signupState = False
loginState = False

class menuOptions:
    def __init__(self):
        self.user_email = 'null'
        self.user_password = 'null'
        self.user_name = 'null'
        self.user_token = 'null'
    def setDifficulty(self, value, difficulty):
        # Do the job here
        # Window(50)
        pass

    def screenSize(self, screenSize):
        # Window.newScreenSize = screenSize
        pass

    def userName(self, userName):
        self.user_name = userName
        update_label_widget()

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

    def signup(self):
        # menuChanged()
        # mainMenu.set_current()
        print("def signup running")
        signup = {'email': self.user_email, 'password': self.user_password, 'user_name': self.user_name}
        self.response = requests.post('http://127.0.0.2:5000/player_details', params=signup)
        labelDisplay().labelDisplay(self.user_name)

    def login(self):
        print("def login running")
        login = {'email': self.user_email, 'password': self.user_password}

        response = requests.get('http://127.0.0.2:5000/player_details', params=login)

        if response.status_code == 200:
            try:
                response_content = response.content.decode('utf-8')  # Decode the response content from bytes to a string
                if response_content == 'null': # Handle the case when the response is 'null'
                    print('No account with details')
                else:
                    jsonResponse = response.json()  # Parse the response content as JSON
                    print("Response JSON:", jsonResponse)

                    if isinstance(jsonResponse, dict):
                        user_name = jsonResponse.get('username')
                        print("Extracted username:", user_name)
                        self.user_token = jsonResponse.get('token')
                        print("Extracted token:", self.user_token)
                        return self.user_token
                    else: # Handle the case when the response is not a JSON object
                        print("The data isn't in JSON")
            except ValueError: # Handle the case when the response content cannot be parsed as JSON
                pass
        else: # Handle the case when the request was not successful
            pass

    def profileCreation():
        pass

def update_label_widget():
    print('def update_label_widget', menuOptions.user_name)


menuOptions = menuOptions()
surface = window.surface

signup = pygame_menu.Menu('signup Screen', window.vduDimensions[0], window.vduDimensions[1], theme=mainTheme)
login = pygame_menu.Menu('Login screen', window.vduDimensions[0], window.vduDimensions[1], theme=mainTheme)
startScreen = pygame_menu.Menu('Start Screen', window.vduDimensions[0], window.vduDimensions[1], theme=mainTheme)
playMenu = pygame_menu.Menu('Play', window.vduDimensions[0], window.vduDimensions[1], theme=mainTheme)
settings = pygame_menu.Menu('settings', window.vduDimensions[0], window.vduDimensions[1], theme=mainTheme)
playerProfile = pygame_menu.Menu('Change player Profiles', window.vduDimensions[0], window.vduDimensions[1], theme=mainTheme)
mainMenu = pygame_menu.Menu('Main Menu', window.vduDimensions[0], window.vduDimensions[1], theme=mainTheme)

def menuChanged(current, menu):
    global signupState
    global loginState
    if menu == 'signup':
        print('signUp')
        signupState = True
    elif menu == 'login':
        print('login')
        loginState = True
    elif menu == 'startScreen':
        print('startscreen')
    elif menu == 'playMenu':
        print('playMenu')
    elif menu == 'settings':
        print('settings')
    elif menu == 'playerProfile':
        print('playerProfile')
    elif menu == 'mainMenu':
        print('mainMenu')
        if signupState == True:
            menuOptions.signup()
            loginState = False
            signupState = False
        elif loginState == True:
            menuOptions.login()
            loginState = False
            signupState = False

signup.set_onbeforeopen(lambda current, menu: menuChanged(current, 'signup'))
login.set_onbeforeopen(lambda current, menu: menuChanged(current, 'login'))
startScreen.set_onbeforeopen(lambda current, menu: menuChanged(current, 'startScreen'))
playMenu.set_onbeforeopen(lambda current, menu: menuChanged(current, 'playMenu'))
settings.set_onbeforeopen(lambda current, menu: menuChanged(current, 'settings'))
playerProfile.set_onbeforeopen(lambda current, menu: menuChanged(current, 'playerProfile'))
mainMenu.set_onbeforeopen(lambda current, menu: menuChanged(current, 'mainMenu'))

#signup screen
signup.add.text_input('User name: ', copy_paste_enable=True, onchange=menuOptions.userName)
signup.add.text_input('Email: ', copy_paste_enable=True, onchange=menuOptions.email)
signup.add.text_input('Password: ', copy_paste_enable=True, password=True, onchange=menuOptions.password)
signupButton = signup.add.button('Signup', mainMenu)
signup.add.button('Back', pygame_menu.events.BACK)
#login screen)
login.add.text_input('Email: ', copy_paste_enable=True, onchange=menuOptions.email)
login.add.text_input('Password: ', copy_paste_enable=True, password=True, onchange=menuOptions.password)
loginButton = login.add.button('Login', mainMenu)

login.add.button('back', pygame_menu.events.BACK)



#create buttons for startScreen
middle_label = startScreen.add.label('Geometric Organiser')
middle_label.set_alignment(pygame_menu.locals.ALIGN_CENTER)
middle_label.set_font(font=pygame_menu.font.FONT_8BIT, font_size=35, color=(0, 0, 0), selected_color=(140, 94, 88), readonly_color=(203, 243, 240), readonly_selected_color=(203, 243, 240), background_color=(255, 247, 248))
startScreen.add.button('Login', login)
startScreen.add.button('SignUp', signup)

startScreen.add.button('Quit', pygame_menu.events.EXIT)

#create buttons for mainMenu
mainMenu.add.button('Play', playMenu)
mainMenu.add.button('Settings', settings)
mainMenu.add.button('Back', pygame_menu.events.BACK)
class labelDisplay:
    def labelDisplay(self, userName):
        user_label = mainMenu.add.label(userName)

#settings
settings.add.range_slider('Set screen size',
                          range_values=[1,2,3,4,5],
                          default=3,
                          onchange = menuOptions.screenSize)

#Create buttons for playMenu
playMenu.add.selector('Gamemode : ', [('Campaign', True), ('Endless', False)], onchange = menuOptions.pickGameMode)
playMenu.add.dropselect('Difficulty :', [('Hard', 1), ('Normal', 2), ('Easy', 3)], onchange = menuOptions.setDifficulty)
playMenu.add.button('Start Game', menuOptions.startGame)
playMenu.add.button('back', pygame_menu.events.BACK)
# settings.add.toggle_switch('Game music muted', [('Muted',False), ('Unmuted', True)])
settings.add.toggle_switch('Mute sounde effects', state_text=('Unmuted', 'Muted'))
#buttons for player profiles
playerProfile.add.button('Create a profile', signup)
playerProfile.add.button('back', pygame_menu.events.BACK)

#world map


if __name__ == "__main__":
    if startScreen.is_enabled():
        startScreen.mainloop(surface)
