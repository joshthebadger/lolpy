from typing import Iterable, Dict, Callable
from datetime import datetime


class Latest:

    def __init__(self, dt: datetime, parser: Callable, rows: Iterable[Dict], attr='date'):
        self.dt = dt
        self.parser = parser
        self.attr = attr
        self.rows = rows

    def __iter__(self) -> Iterable[Dict]:
        for row in self.rows:
            dt = self.parser(row[self.attr])
            # is it later?
            if dt and dt > self.dt:
                yield row
