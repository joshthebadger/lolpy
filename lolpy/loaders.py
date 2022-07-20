from typing import Iterable, Dict, List

from lolpy import parsers
from lolpy import dtos


def set_attrs(item, row: Dict, attrs: List[str], parser=parsers.parse_int):
    for attr in attrs:
        setattr(item, attr, parser(row[attr]))


def load_player(row: Dict) -> dtos.Player:
    playerid = parsers.parse_id(row['playerid'])
    name = parsers.parse_str(row['playername'])
    return dtos.Player(
        playerid,
        name
    )


def load_team(row: Dict) -> dtos.Team:
    teamid = parsers.parse_id(row['teamid'])
    name = parsers.parse_str(row['teamname'])
    return dtos.Team(
        teamid,
        name
    )


def load_player_game(row: Dict) -> dtos.PlayerGame:
    player_game = dtos.PlayerGame(
        load_player(row),
        load_team(row),
        parsers.parse_str(row['position']).lower(),
        parsers.parse_str(row['champion'])
    )
    set_attrs(player_game, row, dtos.PlayerGame.INTEGER_ATTRS)
    return player_game


def load_team_game(row: Dict) -> dtos.TeamGame:
    team_game = dtos.TeamGame(
        load_team(row),
        parsers.parse_str(row['side'][0].upper())
    )
    set_attrs(team_game, row, dtos.TeamGame.INTEGER_ATTRS)
    set_attrs(team_game, row, dtos.TeamGame.BOOL_ATTRS, parsers.parse_bool)
    return team_game


def load_game(row: Dict) -> dtos.Game:
    '''
    Parses game data from a spreadsheet row represented as a dictionary
    '''
    gameid = parsers.parse_str(row['gameid'])
    date = parsers.parse_dt(row['date'])
    duration = parsers.parse_int(row['gamelength'])
    game = parsers.parse_int(row['game'])
    league = parsers.parse_str(row['league'])
    split = parsers.parse_str(row['split'])
    status = parsers.parse_str(row['datacompleteness'], default='unknown')
    position = parsers.parse_str(row['position'])
    # what about missing game ids?
    if gameid is None:
        gameid = dtos.Game.generate_game_id(league, date, game)
    if split is None:
        split = dtos.Game.generate_split(date)
    instance = dtos.Game(
        gameid,
        date,
        duration,
        game,
        league,
        split,
        status,
        playoffs=parsers.parse_bool(row['playoffs'])
    )
    if position.lower() == 'team':
        instance.teamgames.append(load_team_game(row))
    else:
        instance.playergames.append(load_player_game(row))
    return instance


class GameIterator:

    def __init__(self, rows: Iterable[Dict]):
        self.rows = rows
        self.current_game: dtos.Game = None

    def __iter__(self) -> Iterable[dtos.Game]:
        for row in self.rows:
            game: dtos.Game = load_game(row)
            if self.current_game is None:
                self.current_game = game
            elif game.gameid == self.current_game.gameid:
                # same game - update the team and player games
                self.current_game.playergames.extend(game.playergames)
                self.current_game.teamgames.extend(game.teamgames)
            else:
                # its new. yield what we have
                yield self.current_game
                # start a new game
                self.current_game = game
        # don't forget the last one
        if self.current_game is not None:
            yield self.current_game
