from CampaignWinStateEnum import CampaignWinStateEnum
from GameModeEnum import GameModeEnum
import requests


class GameSaves:
    def storeEndless(mode: GameModeEnum, score: int, session: str) -> None:
        data = {'mode': mode.toString(), 'score': score, 'session': session}
        requests.post('http://127.0.0.1:5000/game_saves', params=data)

    def storeCampaign(mode: GameModeEnum, score: int, session: str, campaignLevel: int, campaignWinOrLoss: CampaignWinStateEnum) -> None:
        data = {
            'mode': mode.toString(),
            'score': score,
            'session': session,
            'campaignLevel': campaignLevel,
            'campaignWinOrLoss': campaignWinOrLoss.toString()
        }
        requests.post('http://127.0.0.1:5000/game_saves', params=data)