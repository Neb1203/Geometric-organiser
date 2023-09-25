from enum import Enum

class GameDifficultyEnum(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

    def getTimerDuration(self):
        match self:
            case self.EASY:
                return 240
            case self.MEDIUM:
                return 150
            case self.HARD:
                return 105

    def getDifficultyLevel(self):
        return self.value

    def getUpcomingPiecesNumber(self):
        match self:
            case self.EASY:
                return 3
            case self.MEDIUM:
                return 2
            case self.HARD:
                return 1
