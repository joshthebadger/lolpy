from typing import Optional
from datetime import datetime

INPUT_DT_FORMAT = '%Y-%m-%d %H:%M:%S'


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


def parse_dt(value: str) -> Optional[datetime]:
    if value is None:
        return None
    try:
        return datetime.strptime(value, INPUT_DT_FORMAT)
    except ValueError:
        return None
