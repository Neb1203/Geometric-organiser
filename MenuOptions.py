import requests
from MainGameplay import MainGameplay
from datetime import datetime, timedelta
import json
from tokenModifier import TokenModifier
from removeSpeach import removeSpeach
from keyChanger import keyChanger
keyChanger = keyChanger()
class menuOptions:
    def __init__(self):
        self.user_email = 'null'
        self.user_password = 'null'
        self.user_name = 'null'
        self.sessionToken = 'null'

    def setDifficulty(self, value, difficulty):
        # Do the job here
        # window(50)
        pass
    def setNewKey(self):
        print(keyChanger.get_pressed_key())

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
    def pickGameMode(self, value, gameMode):
        global gameModeSelected
        gameModeSelected = gameMode

    def selectAccount(self, data, value):
        self.selectedAccount = value


    def startGame(self):
        print("CUM")
        global gameModeSelected
        gameModeSelected = False

        if gameModeSelected == False:
            game = MainGameplay()
            game.run_game()

            # If the game loop has exited (returned to main menu), you can perform any post-game actions here.
        elif gameModeSelected == True:
            print("cum")

    def signup(self):
        # menuChanged()
        # mainMenu.set_current()
        print("def signup running")
        signup = {'email': self.user_email, 'password': self.user_password, 'user_name': self.user_name}
        self.response = requests.post('http://127.0.0.1:5000/player_details', params=signup)

    def validate(self, session):
        # token = removeSpeach(self.sessionToken)
        print("session: " + session)
        tokenTup = {'sessionToken': session,}
        response = requests.get('http://127.0.0.1:5000/validate', params=tokenTup)
        print(response)
        if response.status_code != 200:
            return False
        return True

    def cloudLogin(self):
        print("def cloudLogin running")
        login = {'email': self.user_email, 'password': self.user_password}
        response = requests.post('http://127.0.0.1:5000/authenticate', params=login)
        if response.status_code == 200:
                response_content = response.content.decode('utf-8')
                with open("tokens.txt", "a") as file:
                    file.write(response_content + "\n")
                self.sessionToken = response_content
        else:
            print("code not equal to 200")
