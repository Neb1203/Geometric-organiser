from enum import Enum

class GameStateEnum(Enum):
    GAME_OVER = 0
    STARTED = 1
    PAUSED = 2
    INITIALISED = 3
    QUIT = 4
    def gameOver(self):
        return self == self.GAME_OVER
    def paused(self):
        return self == self.PAUSED
    def gameStarted(self):
        return self == self.STARTED
    def initialised(self):
        return self == self.INITIALISED
    def quit(self):
        return self == self.QUIT
