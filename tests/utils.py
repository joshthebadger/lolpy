from typing import Dict
from pathlib import Path

import json

TESTS_DIR = Path(__file__).parent
FIXTURES_DIR = TESTS_DIR / 'fixtures'
OUTPUT_DIR = TESTS_DIR / 'output'


def save_item(item: Dict, filename: str) -> str:
    path = Path(OUTPUT_DIR, filename)
    with open(path, 'w') as foutput:
        json.dump(item, foutput, indent=4)
    return path.as_posix()


def get_item(filename: str) -> Dict:
    path = Path(FIXTURES_DIR, filename)
    with open(path, 'r') as finput:
        return json.load(finput)[0]
