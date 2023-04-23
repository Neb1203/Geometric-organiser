from enum import Enum

class GameStateEnum(Enum):
    GAME_OVER = 0
    STARTED = 1

    def gameOver(self):
        return self == self.GAME_OVER

    def gameStarted(self):
        return self == self.STARTED
