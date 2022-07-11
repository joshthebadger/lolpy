import unittest

from lolpy import dtos


class TestDTOs(unittest.TestCase):

    def test_game_serialisation(self):
        game = dtos.Game('1234')
        self.assertIsNotNone(game.gameid)


if __name__ == '__main__':
    unittest.main()
