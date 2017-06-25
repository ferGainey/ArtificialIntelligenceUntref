from __future__ import absolute_import
import unittest
from players import HumanPlayer


class TestHumanPlayer(unittest.TestCase):

    def setUp(self):
        #self.blackjack_game = BlackjackGame()
        self.human_player = HumanPlayer(None, 100)
        #self.human_player = self.blackjack_game.player

    def test_matrix_values(self):
        print self.human_player.fg_values_matrix
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()