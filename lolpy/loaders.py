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
    game = Game(
        gameid,
        date,
        duration
    )
    return game
