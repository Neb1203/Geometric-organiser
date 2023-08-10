import requests
from MainGameplay import MainGameplay
from datetime import datetime, timedelta
import json
from tokenModifier import TokenModifier
from removeSpeach import removeSpeach

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
        self.response = requests.post('http://127.0.0.2:5000/player_details', params=signup)

    def validate(self):
        token = removeSpeach(self.sessionToken)
        tokenModifier = TokenModifier()
        tokenTup = {'sessionToken': token,}
        response = requests.get('http://127.0.0.2:5000/validate', params=tokenTup)
        decoded = response.content.decode('utf-8')
        print(decoded)

        data = json.loads(decoded)
        date_time_str = data[0]

        responseTime = datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%S")
        new_date = responseTime + timedelta(days=30)
        if new_date <= datetime.now():
            existing_session_ids = tokenModifier.read_session_ids()

            if existing_session_ids is not None:  # Replace with the session ID you want to remove
                if token in existing_session_ids:
                    existing_session_ids.remove(token)
                    tokenModifier.write_session_ids(existing_session_ids)
                else:
                    print("Session ID not found in the file.")
        else:
            print("valid")
    def cloudLogin(self):
        print("def cloudLogin running")
        login = {'email': self.user_email, 'password': self.user_password}
        response = requests.post('http://127.0.0.2:5000/authenticate', params=login)
        if response.status_code == 200:
                response_content = response.content.decode('utf-8')
                self.sessionToken = response_content
        else:
            print("code not equal to 200")
