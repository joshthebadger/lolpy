from typing import Optional


def parse_str(value: str, default=None) -> Optional[str]:
    if value is None or value.strip() == '':
        return default
    return value.strip()
