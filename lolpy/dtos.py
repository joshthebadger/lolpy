from typing import Dict, List

from datetime import datetime
from dataclasses import dataclass, field
from collections import OrderedDict

OUTPUT_DT_FORMAT = '%Y-%m-%d %H:%M:%S'
# if we need date times to generate a game id
GAME_ID_FORMAT = '%Y-%m-%d_%H-%M'


@dataclass
class Player:
    playerid: str
    name: str

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            data['playerid'],
            data['name']
        )

    def as_dict(self) -> OrderedDict:
        return OrderedDict(
            playerid=self.playerid,
            name=self.name
        )


@dataclass
class Team:
    teamid: str
    name: str

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            data['teamid'],
            data['name']
        )

    def as_dict(self) -> OrderedDict:
        return OrderedDict(
            teamid=self.teamid,
            name=self.name
        )


@dataclass
class PlayerGame:
    player: Player
    team: Team
    position: str

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            Player.from_dict(data['player']),
            Team.from_dict(data['team']),
            data['position']
        )

    def as_dict(self) -> OrderedDict:
        return OrderedDict(
            player=self.player.as_dict(),
            team=self.team.as_dict(),
            position=self.position
        )


@dataclass
class TeamGame:
    team: Team

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            Team.from_dict(data['team'])
        )

    def as_dict(self) -> OrderedDict:
        return OrderedDict(
            team=self.team.as_dict()
        )


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
    playergames: List[PlayerGame] = field(init=False, default_factory=list)
    teamgames: List[TeamGame] = field(init=False, default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict):
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
        game.playergames.extend([
            PlayerGame.from_dict(item) for item in data['playergames']
        ])
        game.teamgames.extend([
            TeamGame.from_dict(item) for item in data['teamgames']
        ])
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
            playoffs=self.playoffs,
            playergames=[p.as_dict() for p in self.playergames],
            teamgames=[t.as_dict() for t in self.teamgames]
        )
