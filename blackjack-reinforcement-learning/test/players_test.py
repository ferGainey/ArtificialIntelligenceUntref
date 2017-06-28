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

    def test_obtaining_maximum_from_vector(self):
        vector = {4: 'stand', 5: 'continue', 8: 'double bet', 1: 'split'}
        max = self.human_player.calculate_maximum_from_vector(vector)
        self.assertEqual(8, max)


if __name__ == '__main__':
    unittest.main()