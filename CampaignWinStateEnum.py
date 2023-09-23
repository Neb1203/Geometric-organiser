from enum import Enum

class CampaignWinStateEnum(Enum):
    LOSS = 0
    WIN = 1

    def toString(self):
        return self.name
