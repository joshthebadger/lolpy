from datetime import datetime
from dataclasses import dataclass, field
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
    duration: int = field(repr=False)
    game: int = field(repr=False)
    league: str
    split: str = field(repr=False)
    status: str = field(repr=False)
    playoffs: bool = field(default=False, repr=False)

    @classmethod
    def from_dict(cls, data: OrderedDict):
        game = cls(
            data['gameid'],
            datetime.strptime(data['date'], OUTPUT_DT_FORMAT),
            data['duration'],
            data['game'],
            data['league'],
            data['split'],
            data['status'],
            data['playoffs']
        )
        return game

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
