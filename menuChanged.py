import pygame_menu

class menuChanged:
    def menuChanged (menu, current):
        print('menuChanged', menu, current)
        # signupState = False
        # loginState = False
        if menu == 'signup':
            print('signup')
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
                print('signup')
                menuOptions.signup()
            elif loginState == True:
                print('login')
                menuOptions.login()
