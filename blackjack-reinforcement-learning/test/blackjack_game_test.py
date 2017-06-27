from __future__ import absolute_import
import unittest
from main.blackjack_game import BlackjackGame


class TestBlackjackGame(unittest.TestCase):

    def setUp(self):
        self.blackjack_game = BlackjackGame()

    def test_something(self):
        self.assertEqual(1, 1)

#sdffsdfsdfd
if __name__ == '__main__':
    unittest.main()