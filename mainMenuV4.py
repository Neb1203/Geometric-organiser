import pygame_menu

from tokenModifier import TokenModifier
from GridDraw import Tetris
from MenuOptions import menuOptions
from UsernamesModel import UsernamesModel
from Window import Window
from hashGenerator import HashingGenerator
from MenuOptions import menuOptions

# pygame.mixer.init()
# pygame.mixer.music.load('mmm.mp3')
# pygame.mixer.music.play(-1, 0)
mainTheme = pygame_menu.themes.THEME_SOLARIZED
window = Window()
Tetris = Tetris(10, 20)
hashGenerator = HashingGenerator()
csvInstance = UsernamesModel()
subwindow = (300, 200)

subTheme = pygame_menu.themes.THEME_SOLARIZED

window.mainTheme.widget_margin = (20, 15)
window.mainTheme.widget_alignment = pygame_menu.locals.ALIGN_LEFT

signupState = False
loginState = False
tokenModifier = TokenModifier()
availableTokens = tokenModifier.read_session_ids()
# TODO refactor to have a better syntax than using the len() function
lastTokenIndex = len(availableTokens)-1
latestToken = availableTokens[lastTokenIndex]
menuOptions = menuOptions()
isLoggedIn = menuOptions.validate(latestToken)

if isLoggedIn:
    pass
else:
    surface = window.surface

    signup = pygame_menu.Menu('signup Screen', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
    login = pygame_menu.Menu('Login screen', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
    startScreen = pygame_menu.Menu('Start Screen', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
    playMenu = pygame_menu.Menu('Play', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
    settings = pygame_menu.Menu('settings', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
    playerProfile = pygame_menu.Menu('Change player Profiles', window.vduDimensions[0], window.vduDimensions[1],
                                     theme=window.mainTheme)
    mainMenu = pygame_menu.Menu('Main Menu', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
    accountSwitcher = pygame_menu.Menu('Account switcher', window.vduDimensions[0], window.vduDimensions[1],
                                       theme=window.mainTheme)
    campaign = pygame_menu.Menu('Campaign', window.vduDimensions[0], window.vduDimensions[1], theme = window.mainTheme)
    playerStatistics = pygame_menu.Menu('Player stats:', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
    signup.set_onbeforeopen(lambda current, menu: menuChanged(current, 'signup'))
    login.set_onbeforeopen(lambda current, menu: menuChanged(current, 'login'))
    startScreen.set_onbeforeopen(lambda current, menu: menuChanged(current, 'startScreen'))
    playMenu.set_onbeforeopen(lambda current, menu: menuChanged(current, 'playMenu'))
    settings.set_onbeforeopen(lambda current, menu: menuChanged(current, 'settings'))
    playerProfile.set_onbeforeopen(lambda current, menu: menuChanged(current, 'playerProfile'))
    mainMenu.set_onbeforeopen(lambda current, menu: menuChanged(current, 'mainMenu'))

    # signup screen
    signup.add.text_input('User name: ', copy_paste_enable=True, onchange=menuOptions.userName)
    signup.add.text_input('Email: ', copy_paste_enable=True, onchange=menuOptions.email)
    signup.add.text_input('Password: ', copy_paste_enable=True, password=True, onchange=menuOptions.password)
    signupButton = signup.add.button('Signup', mainMenu)
    signup.add.button('Back', pygame_menu.events.BACK)
    # login screen)
    login.add.text_input('Email: ', copy_paste_enable=True, onchange=menuOptions.email)
    login.add.text_input('Password: ', copy_paste_enable=True, password=True, onchange=menuOptions.password)
    loginButton = login.add.button('Login', mainMenu)

    login.add.button('back', pygame_menu.events.BACK)

    # create buttons for startScreen
    middle_label = startScreen.add.label('Geometric Organiser')
    middle_label.set_alignment(pygame_menu.locals.ALIGN_CENTER)
    middle_label.set_font(font=pygame_menu.font.FONT_8BIT, font_size=35, color=(0, 0, 0), selected_color=(140, 94, 88),
                          readonly_color=(203, 243, 240), readonly_selected_color=(203, 243, 240),
                          background_color=(255, 247, 248))
    startScreen.add.button('Login', login)
    startScreen.add.button('SignUp', signup)
    startScreen.add.button('validateTest', menuOptions.validate)
    startScreen.add.button('Quit', pygame_menu.events.EXIT)

    # create buttons for mainMenu
    mainMenu.add.button('Play', playMenu)
    mainMenu.add.button('Settings', settings)
    mainMenu.add.button('Back', pygame_menu.events.BACK)

    # settings
    settings.add.range_slider('Set screen size',
                              range_values=[1, 2, 3, 4, 5],
                              default=3,
                              onchange=menuOptions.screenSize)
    campaign.add.label('Campaign attempts: x')
    campaign.add.label('Campaign completion rate: y')
    campaign.add.dropselect('Level selector:', [('Level 1: Completed', 1), ('Level 2: Start', 2), ('Level 3: locked', 3), ('Level 4: locked', 4)], onchange=menuOptions.setDifficulty)
    campaign.add.button('Start level')

    # Create buttons for playMenu
    playMenu.add.selector('Gamemode : ', [('Campaign', True), ('Endless', False)], onchange=menuOptions.pickGameMode)
    playMenu.add.dropselect('Difficulty :', [('Hard', 1), ('Normal', 2), ('Easy', 3)],
                            onchange=menuOptions.setDifficulty)
    playMenu.add.button('Start Game', menuOptions.startGame)
    playMenu.add.button('back', pygame_menu.events.BACK)
    settings.add.toggle_switch('Mute sounde effects', state_text=('Unmuted', 'Muted'))
    # buttons for player profiles
    playerProfile.add.button('signup', signup)
    playerProfile.add.button('login', login)
    playerProfile.add.button('back', pygame_menu.events.BACK)
    # buttons for logged in accountslabel
    displayLabel = accountSwitcher.add.label('Pick a player profile:')
    displayLabel.set_alignment(pygame_menu.locals.ALIGN_CENTER)
    dict = []

    usernamesModel = UsernamesModel()
    allUsernames = usernamesModel.read()
    allUsernamesFlipped = [(username, token) for token, username in allUsernames]

    accountSwitcher.add.dropselect(title="Logged in usernames: ", items=allUsernamesFlipped,
                                   onchange=menuOptions.selectAccount)
    playerStatistics.add.label("Time played: timePlayed")
    playerStatistics.add.label("Lifetime score: lifetimeScore")
    playerStatistics.add.label("Games played: roundsPlayed")
    playerStatistics.add.label("Campaign attempts: campaignAttempts")
    playerStatistics.add.label("Campaign Completion Rate: campaignAttemps / campaignLosses")
    playerStatistics.add.label("High score in endless: highScore")
    playerStatistics.add.label("Number of game overs: deaths")
    playerStatistics.add.button('back', pygame_menu.events.BACK)
    # onchange = menuOptions.selectAccount
    # accountSwitcher.add.button('Log-in with selected account', menuOptions.login)
    darren = startScreen
    if __name__ == "__main__":
        if darren.is_enabled():
            darren.mainloop(surface)


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
    elif menu == 'paused':
        print('paused')
    elif menu == 'resume':
        print('resume')
    elif menu == 'quitPauseMenu':
        print('quitPauseMenu')
    elif menu == 'mainMenu':
        print('mainMenu')
        mainMenu.add.label(menuOptions.user_name)
        if signupState == True:
            menuOptions.signup()
            loginState = False
            signupState = False
        elif loginState == True:
            menuOptions.cloudLogin()
            loginState = False
            signupState = False

