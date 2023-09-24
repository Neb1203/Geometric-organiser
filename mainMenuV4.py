import json

import pygame_menu

from GameDifficultyEnum import GameDifficultyEnum
from GameModeEnum import GameModeEnum
from GameSaves import GameSaves
from MenuOptions import menuOptions, updateKey
from UsernamesModel import UsernamesModel
from Window import Window
from hashGenerator import HashingGenerator
from tokenModifier import TokenModifier

mainTheme = pygame_menu.themes.THEME_SOLARIZED
window = Window()
hashGenerator = HashingGenerator()
csvInstance = UsernamesModel()
menuOptions = menuOptions()
keyChanger = updateKey()

window.mainTheme.widget_margin = (20, 15)
window.mainTheme.widget_alignment = pygame_menu.locals.ALIGN_LEFT

window.noTitle.widget_margin = (0, 8)
# window.mainTheme.widget_alignment = pygame_menu.locals.ALIGN_LEFT

signupState = False
loginState = False
tokenModifier = TokenModifier()
latestSession = tokenModifier.get_last_session()
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
            login = menuOptions.cloudLogin()
            loginState = False
            signupState = False

# pygame.mixer.init()
# pygame.mixer.music.load('mmm.mp3')
# pygame.mixer.music.play(-1, 0)

# TODO refactor to have a better syntax than using the len() function
isLoggedIn = False
if latestSession:
    isLoggedIn = menuOptions.validate(latestSession)

surface = window.surface

signup = pygame_menu.Menu('signup Screen', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
login = pygame_menu.Menu('Login screen', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
startScreen = pygame_menu.Menu('Start Screen', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
playMenu = pygame_menu.Menu('Play', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
settings = pygame_menu.Menu('settings', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
changeControls = pygame_menu.Menu("", window.vduDimensions[0], window.vduDimensions[1], theme=window.noTitle)
playerProfile = pygame_menu.Menu('Change player Profiles', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
mainMenu = pygame_menu.Menu('Main Menu', window.vduDimensions[0], window.vduDimensions[1], theme=window.mainTheme)
accountSwitcher = pygame_menu.Menu('Account switcher', window.vduDimensions[0], window.vduDimensions[1], theme = window.mainTheme)
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
mainMenu.add.button('Player statistics', playerStatistics)
mainMenu.add.button('Settings', settings)
mainMenu.add.button('Back', pygame_menu.events.BACK)

# settings
settings.add.clock()
settings.add.range_slider('Set screen size',
                          range_values=[1, 2, 3, 4, 5],
                          default=3,
                          onchange=menuOptions.screenSize)
settings.add.button('Change controls', changeControls)

text = "Click the key you want to change\nand then the press the key you want to change it to."
textBox = changeControls.add.label(text, max_char=-1, font_size=15)

changeControls.add.button('Left movement', keyChanger.left)
changeControls.add.button('Right movement', keyChanger.right)
changeControls.add.button('Instantly drop', keyChanger.hardDrop)
changeControls.add.button('Slowly drop', keyChanger.softDrop)
changeControls.add.button('Rotate left', keyChanger.rotateLeft)
changeControls.add.button('Rotate right', keyChanger.rotateRight)
changeControls.add.button('Hold piece', keyChanger.lockPiece)
changeControls.add.button('Pause', keyChanger.pause)
changeControls.add.button('back', pygame_menu.events.BACK)

campaign.add.label('Campaign attempts: x')
campaign.add.label('Campaign completion rate: y')
campaign.add.dropselect('Level selector:', [('Level 1: Completed', 1), ('Level 2: Start', 2), ('Level 3: locked', 3), ('Level 4: locked', 4)], onchange=menuOptions.setDifficulty)
campaign.add.button('Start level')

# Create buttons for playMenu
playMenu.add.selector('Gamemodes: ', [('Campaign', GameModeEnum.CAMPAIGN), ('Endless', GameModeEnum.ENDLESS)], onchange=menuOptions.setGameMode)
playMenu.add.dropselect('Difficulty :', [('Easy', GameDifficultyEnum.EASY), ('Normal', GameDifficultyEnum.MEDIUM), ('Hard', GameDifficultyEnum.HARD)],
                        onchange=menuOptions.setDifficulty, default=0)
playMenu.add.button('Start Game', menuOptions.startGame)
playMenu.add.button('back', pygame_menu.events.BACK)
settings.add.toggle_switch('Mute sounde effects', state_text=('Unmuted', 'Muted'))
settings.add.button('back', pygame_menu.events.BACK)
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
if len(allUsernames) >= 1:
    allUsernamesFlipped = [(username, token) for token, username in allUsernames]

    accountSwitcher.add.dropselect(title="Logged in usernames: ", items=allUsernamesFlipped,
                                   onchange=menuOptions.selectAccount)

gameSaves = GameSaves()
tokenModifier = TokenModifier()
lastSession = tokenModifier.get_last_session()
if lastSession != None:
    savesObj = gameSaves.get(lastSession)
    playerAnalysis = savesObj.getPlayerAnalysis()

    playerStatistics.add.label("Time played: " + str(playerAnalysis["totalTime"]))
    playerStatistics.add.label("Lifetime score: " + str(playerAnalysis["lifetimeScore"]))
    playerStatistics.add.label("Games played: " + str(playerAnalysis["roundsPlayed"]))
    playerStatistics.add.label("Campaign attempts: " + str(playerAnalysis["campaignRoundsPlayed"]))
    playerStatistics.add.label("Campaign Completion Rate: " + str(playerAnalysis["campaignCompletionRate"]))
    playerStatistics.add.label("High score in endless: " + str(playerAnalysis["endlessHighScore"]))
    playerStatistics.add.button('back', pygame_menu.events.BACK)

if isLoggedIn:
    screenToShow = mainMenu
else:
    screenToShow = startScreen
if __name__ == "__main__":
    if screenToShow.is_enabled():
        screenToShow.mainloop(surface)

