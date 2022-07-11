import unittest

from lolpy import dtos

from tests import utils


class TestDTOs(unittest.TestCase):

    def test_game_serialisation(self):
        game = dtos.Game('1234')
        self.assertIsNotNone(game.gameid)
        output_file = utils.save_item(
            game.as_dict(),
            'game.json'
        )
        print('Game saved to {}'.format(output_file))


if __name__ == '__main__':
    unittest.main()
