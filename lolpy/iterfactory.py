import csv
from datetime import datetime

from . import iterators
from . import parsers
from . import loaders


def csv_latest_iterator(latest: datetime, input) -> iterators.Latest:
    return iterators.Latest(
        latest,
        parsers.parse_dt,
        csv.DictReader(input)
    )


def csv_game_iterator(input) -> loaders.GameIterator:
    return loaders.GameIterator(
        csv.DictReader(input)
    )


def csv_latest_game_iterator(latest: datetime, input) -> loaders.GameIterator:
    return loaders.GameIterator(
        csv_latest_iterator(latest, input)
    )
