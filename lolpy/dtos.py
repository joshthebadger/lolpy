from itertools import chain
from typing import Dict, List

from datetime import datetime
from dataclasses import dataclass, field
from collections import OrderedDict

OUTPUT_DT_FORMAT = '%Y-%m-%d %H:%M:%S'
# if we need date times to generate a game id
GAME_ID_FORMAT = '%Y-%m-%d_%H-%M'


def get_attrs(item, attrs: List[str]) -> Dict[str, int]:
    return dict([
        (attr, getattr(item, attr)) for attr in attrs
    ])


def set_attrs(item, attrs: List[str], data: Dict):
    for attr in attrs:
        setattr(item, attr, data[attr])


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
    champion: str
    kills: int = 0
    deaths: int = 0
    assists: int = 0
    damagetochampions: int = 0
    visionscore: int = 0
    totalgold: int = 0
    golddiffat15: int = 0

    INTEGER_ATTRS = (
        'kills', 'deaths', 'assists', 'damagetochampions', 'visionscore', 'totalgold', 'golddiffat15'
    )

    @classmethod
    def from_dict(cls, data: Dict):
        item = cls(
            Player.from_dict(data['player']),
            Team.from_dict(data['team']),
            data['position'],
            data['champion']
        )
        set_attrs(item, cls.INTEGER_ATTRS, data)
        return item

    def as_dict(self) -> OrderedDict:
        return OrderedDict(
            player=self.player.as_dict(),
            team=self.team.as_dict(),
            position=self.position,
            champion=self.champion,
            **get_attrs(self, self.INTEGER_ATTRS)
        )


@dataclass
class TeamGame:
    team: Team
    side: str
    result: bool = False
    dragons: int = 0
    elders: int = 0
    heralds: int = 0
    barons: int = 0
    towers: int = 0
    firstblood: bool = False
    firstdragon: bool = False
    firstherald: bool = False
    firstbaron: bool = False
    firsttower: bool = False

    BOOL_ATTRS = (
        'result',
        'firstblood',
        'firstdragon',
        'firstherald',
        'firstbaron',
        'firsttower'
    )

    INTEGER_ATTRS = (
        'dragons',
        'elders',
        'heralds',
        'barons',
        'towers',
    )

    @classmethod
    def from_dict(cls, data: Dict):
        team_game = cls(
            Team.from_dict(data['team']),
            data['side']
        )
        set_attrs(team_game, chain(cls.INTEGER_ATTRS, cls.BOOL_ATTRS), data)
        return team_game

    def as_dict(self) -> OrderedDict:
        team_game = OrderedDict(
            team=self.team.as_dict(),
            side=self.side,
            **get_attrs(self, chain(self.INTEGER_ATTRS, self.BOOL_ATTRS))
        )
        return team_game


@dataclass
class Game:

    @staticmethod
    def generate_game_id(league: str, date: datetime, game: int) -> str:
        return f'{league}_{date.strftime(GAME_ID_FORMAT)}_{game}'

    @staticmethod
    def generate_split(date: datetime):
        return f"Q{(date.month // 4) + 1}"

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
