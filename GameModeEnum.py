from enum import Enum

class GameModeEnum(Enum):
    ENDLESS = 0
    CAMPAIGN = 1

    def toString(self):
        return self.name
