import requests

from Campaign import Campaign
from GameDifficultyEnum import GameDifficultyEnum
from GameModeEnum import GameModeEnum
from Endless import Endless
from controlArray import *
from keyChanger import keyChanger
import time
class menuOptions:
    def __init__(self):
        self.user_email = 'null'
        self.user_password = 'null'
        self.user_name = 'null'
        self.sessionToken = 'null'
        self.gameMode = GameModeEnum.CAMPAIGN
        self.difficulty = GameDifficultyEnum.EASY

    def setDifficulty(self, name, difficulty: GameDifficultyEnum):
        self.difficulty = difficulty


    def screenSize(self, screenSize):
        # window.newScreenSize = screenSize
        pass

    def userName(self, userName):
        self.user_name = userName
        # mainMenu.add.label(self.user_name)

    def password(self, password):
        self.user_password = password

    def email(self, email):
        self.user_email = email
    def setGameMode(self, selector, gameMode):
        self.gameMode = gameMode

    def selectAccount(self, data, value):
        self.selectedAccount = value


    def startGame(self):
        if self.gameMode == GameModeEnum.ENDLESS:
            endless = Endless(self.difficulty.getDifficultyLevel())
            endless.runGame()
        else:
            campaign = Campaign(self.difficulty.getTimerDuration())
            campaign.runGame()

    def signup(self):
        # menuChanged()
        # mainMenu.set_current()
        print("def signup running")
        signup = {'email': self.user_email, 'password': self.user_password, 'user_name': self.user_name}
        self.response = requests.post('http://127.0.0.1:5000/player_details', params=signup)

    def validate(self, session):
        tokenTup = {'sessionToken': session,}
        response = requests.get('http://127.0.0.1:5000/validate', params=tokenTup)
        if response.status_code != 200:
            return False
        return True

    def cloudLogin(self):
        login = {'email': self.user_email, 'password': self.user_password}
        response = requests.post('http://127.0.0.1:5000/authenticate', params=login)
        print("cloudLogin response code is " + str(response.status_code))
        if response.status_code == 200:
                response_content = response.content.decode('utf-8')
                with open("tokens.txt", "a") as file:
                    file.write(response_content + "\n")
                self.sessionToken = response_content
        else:
            print("code not equal to 200")
keyChanger = keyChanger()
update = update()
class updateKey:
    def __init__(self):
        self.delay_seconds = 0.15
    def left(self):
        time.sleep(self.delay_seconds)
        print("updateKey.left")
        targetKey = 'left'
        update.update(targetKey, keyChanger.get_pressed_key())

    def right(self):
        time.sleep(self.delay_seconds)
        targetKey = 'right'
        update.update(targetKey, keyChanger.get_pressed_key())

    def hardDrop(self):
        time.sleep(self.delay_seconds)
        targetKey = 'hardDrop'
        update.update(targetKey, keyChanger.get_pressed_key())

    def softDrop(self):
        time.sleep(self.delay_seconds)
        targetKey = 'softDrop'
        update.update(targetKey, keyChanger.get_pressed_key())

    def rotateLeft(self):
        time.sleep(self.delay_seconds)
        targetKey = 'rotateLeft'
        update.update(targetKey, keyChanger.get_pressed_key())

    def rotateRight(self):
        time.sleep(self.delay_seconds)
        targetKey = 'rotateRight'
        update.update(targetKey, keyChanger.get_pressed_key())

    def lockPiece(self):
        time.sleep(self.delay_seconds)
        targetKey = 'lockPiece'
        update.update(targetKey, keyChanger.get_pressed_key())
    def pause(self):
        time.sleep(self.delay_seconds)
        targetKey = 'pause'
        update.update(targetKey, keyChanger.get_pressed_key())

