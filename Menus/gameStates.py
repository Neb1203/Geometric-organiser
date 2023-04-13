# import startScreen


class gameStates:
    startScreenState = True
    mainMenuState = False
    is_running = True

    while is_running:
        if startScreenState == True:
            startScreen()