from typing import Dict

from lolpy import parsers
from lolpy.dtos import Game


def load_game(row: Dict) -> Game:
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
    # what about missing game ids?
    if gameid is None:
        gameid = Game.generate_game_id(league, date, game)
    instance = Game(
        gameid,
        date,
        duration,
        game,
        league,
        split,
        status,
        playoffs=parsers.parse_bool(row['playoffs'])
    )
    return instance
