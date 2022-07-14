from datetime import datetime
from dataclasses import dataclass
from collections import OrderedDict

OUTPUT_DT_FORMAT = '%Y-%m-%d %H:%M:%S'
# if we need date times to generate a game id
GAME_ID_FORMAT = '%Y-%m-%d_%H-%M'


@dataclass
class Game:

    @staticmethod
    def generate_game_id(league: str, date: datetime, game: int) -> str:
        return f'{league}_{date.strftime(GAME_ID_FORMAT)}_{game}'

    gameid: str
    date: datetime
    duration: int
    game: int
    league: str
    split: str
    status: str
    playoffs: bool = False

    def as_dict(self) -> OrderedDict:
        return OrderedDict(
            gameid=self.gameid,
            date=self.date.strftime(OUTPUT_DT_FORMAT),
            duration=self.duration,
            game=self.game,
            league=self.league,
            split=self.split,
            status=self.status,
            playoffs=self.playoffs
        )
