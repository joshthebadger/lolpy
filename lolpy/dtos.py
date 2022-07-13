from dataclasses import dataclass, asdict


@dataclass
class Game:
    gameid: str

    def as_dict(self):
        return asdict(self)
