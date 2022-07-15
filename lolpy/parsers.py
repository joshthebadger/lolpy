from typing import Optional
from datetime import datetime
import re

INPUT_DT_FORMAT = '%Y-%m-%d %H:%M:%S'


OE_ID_REGEX = re.compile(r'oe:(team|player):(?P<id>.+)$')


def parse_str(value: str, default=None) -> Optional[str]:
    if value is None or value.strip() == '':
        return default
    return value.strip()


def parse_int(value: str, default=0) -> int:
    if value:
        try:
            return int(value)
        except ValueError:
            pass
    return default


def parse_bool(value: str) -> bool:
    return bool(parse_int(value))


def parse_dt(value: str) -> Optional[datetime]:
    if value is None:
        return None
    try:
        return datetime.strptime(value, INPUT_DT_FORMAT)
    except ValueError:
        return None


def parse_id(value: str) -> Optional[str]:
    m = OE_ID_REGEX.match(value)
    if m:
        return m.groupdict()['id']
    return value
