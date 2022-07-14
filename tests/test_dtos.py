import unittest
import datetime

from lolpy import dtos
from lolpy import loaders

from tests import utils


class TestDTOs(unittest.TestCase):

    def test_game_serialisation(self):
        game_dict = utils.get_item('player_game.json')
        game_id = game_dict['gameid']
        game = loaders.load_game(game_dict)
        for attr in game.__dict__.keys():
            self.assertIsNotNone(getattr(game, attr))
        self.assertEqual(game.gameid, game_id)
        output_file = utils.save_item(
            game.as_dict(),
            'game.json'
        )
        print('Game saved to {}'.format(output_file))

    def test_game_deserialisation(self):
        game_dict = utils.get_item('player_game.json')
        game = loaders.load_game(game_dict)
        game2 = dtos.Game.from_dict(game.as_dict())
        self.assertEqual(game, game2)

    def test_generate_game_id(self):
        now = datetime.datetime.now()
        league = 'LCS'
        game = 1
        gameid = dtos.Game.generate_game_id(league, now, game)
        self.assertTrue(gameid.startswith(league))
        self.assertTrue(gameid.endswith(str(game)))
        self.assertTrue(now.strftime(dtos.GAME_ID_FORMAT) in gameid)


if __name__ == '__main__':
    unittest.main()
