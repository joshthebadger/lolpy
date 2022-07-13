from datetime import datetime
from dataclasses import dataclass
from collections import OrderedDict

OUTPUT_DT_FORMAT = '%Y-%m-%d %H:%M:%S'


@dataclass
class Game:
    gameid: str
    date: datetime
    duration: int

    def as_dict(self) -> OrderedDict:
        return OrderedDict(
            gameid=self.gameid,
            date=self.date.strftime(OUTPUT_DT_FORMAT),
            duration=self.duration
        )
