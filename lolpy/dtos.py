from dataclasses import dataclass, asdict
from collections import OrderedDict


@dataclass
class Game:
    gameid: str

    def as_dict(self):
        return asdict(self)
