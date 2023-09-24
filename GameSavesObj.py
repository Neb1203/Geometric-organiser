import json
from datetime import timedelta

from GameModeEnum import GameModeEnum


class GameSavesObj:
    def __init__(self, savesJson: str):
        gameSaves = []
        for save in savesJson:
            # get save and remove first and last char
            save = save[0][1:-1]
            saveObj = json.loads(save)
            saveObj['duration'] = self.convertToTimeDelta(saveObj['duration'])
            gameSaves.append(saveObj)
        self.saves = gameSaves

    def getPlayerAnalysis(self) -> dict:
        analysis = {}
        totalTime = timedelta()
        lifetimeScore = 0
        roundsPlayed = 0
        campaignRoundsPlayed = 0
        endlessHighScore = 0
        # number of campaign attempts/ number of campaign losses
        campaignLosses = 0
        campaignHighScore = 0
        for save in self.saves:
            duration = save["duration"]
            totalTime = totalTime + duration

            lifetimeScore += save["score"]
            roundsPlayed += 1
            if save["mode"] == GameModeEnum.CAMPAIGN:
                campaignRoundsPlayed += 1
                if save["score"] > campaignHighScore:
                    campaignHighScore = save["score"]
                else:
                    campaignLosses += 1
            elif save["mode"] == GameModeEnum.ENDLESS and save["score"] > endlessHighScore:
                endlessHighScore = save["score"]


        analysis['totalTime'] = totalTime
        analysis['lifetimeScore'] = lifetimeScore
        analysis['roundsPlayed'] = roundsPlayed
        analysis['campaignRoundsPlayed'] = campaignRoundsPlayed
        analysis['endlessHighScore'] = endlessHighScore
        analysis['campaignCompletionRate'] = campaignRoundsPlayed / campaignLosses

        return analysis


    def convertToTimeDelta(self, duration: str) -> timedelta:
        hours, minutes, seconds_microseconds = duration.split(':')
        seconds, microseconds = seconds_microseconds.split('.')
        microseconds = int(microseconds)

        return timedelta(
            hours=int(hours),
            minutes=int(minutes),
            seconds=int(seconds),
            microseconds=microseconds
        )