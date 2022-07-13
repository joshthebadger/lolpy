import unittest

from lolpy import dtos

from tests import utils


class TestDTOs(unittest.TestCase):

    def test_game_serialisation(self):
        game_dict = utils.get_item('player_game.json')
        game_id = game_dict['gameid']
        game = dtos.Game(
            game_id
        )
        self.assertEqual(game.gameid, game_id)
        output_file = utils.save_item(
            game.as_dict(),
            'game.json'
        )
        print('Game saved to {}'.format(output_file))


if __name__ == '__main__':
    unittest.main()
