from enum import Enum

class GameStateEnum(Enum):
    GAME_OVER = 0
    STARTED = 1
    PAUSED = 2
    def gameOver(self):
        return self == self.GAME_OVER
    def paused(self):
        return self == self.PAUSED
    def gameStarted(self):
        return self == self.STARTED
