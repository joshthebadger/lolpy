from typing import Dict

from lolpy import parsers
from lolpy.dtos import Game


def load_game(row: Dict) -> Game:
    '''
    Parses game data from a spreadsheet row represented as a dictionary
    '''
    gameid = parsers.parse_str(row['gameid'])
    game = Game(
        gameid
    )
    return game
