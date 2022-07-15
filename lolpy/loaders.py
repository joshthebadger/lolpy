from typing import Dict

from lolpy import parsers
from lolpy import dtos


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
    return dtos.PlayerGame(
        load_player(row),
        load_team(row),
        parsers.parse_str(row['position']).lower()
    )


def load_team_game(row: Dict) -> dtos.TeamGame:
    return dtos.TeamGame(
        load_team(row)
    )


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
    status = parsers.parse_str(row['datacompleteness'])
    position = parsers.parse_str(row['position'])
    # what about missing game ids?
    if gameid is None:
        gameid = dtos.Game.generate_game_id(league, date, game)
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
