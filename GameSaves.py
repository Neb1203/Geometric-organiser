from GameModeEnum import GameModeEnum
import requests


class GameSaves:
    def store(mode: GameModeEnum, score: int, session: str) -> None:
        data = {'mode': mode.toString(), 'score': score, 'session': session}
        requests.post('http://127.0.0.1:5000/game_saves', params=data)