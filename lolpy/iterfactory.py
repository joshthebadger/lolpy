import csv
from datetime import datetime

from . import iterators
from . import parsers


def csv_latest_iterator(latest: datetime, input) -> iterators.Latest:
    return iterators.Latest(
        latest,
        parsers.parse_dt,
        csv.DictReader(input)
    )
