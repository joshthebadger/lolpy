import unittest

from datetime import datetime

from lolpy import iterfactory

from tests import utils


class TestLIterators(unittest.TestCase):

    def test_latest_iterator(self):
        latest = datetime(
            2022, 1, 10, 7, 45, 0
        )
        num_rows = 0
        with open(utils.get_games_file_csv('game_rows.csv')) as finput:
            for row in iterfactory.csv_latest_iterator(latest, finput):
                num_rows += 1
        self.assertEqual(num_rows, 24)


if __name__ == '__main__':
    unittest.main()
