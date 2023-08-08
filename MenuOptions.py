import requests
from MainGameplay import MainGameplay

class menuOptions:
    def __init__(self):
        self.user_email = 'null'
        self.user_password = 'null'
        self.user_name = 'null'
        self.user_token = 'null'
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

    def loggedSignin(self):
        if self.selectedAccount != None:
            print(self.selectedAccount)

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
