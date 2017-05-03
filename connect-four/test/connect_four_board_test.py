import unittest
from main.connect_four_board import ConnectFourBoard
from main.ai_player import AIPlayer
from main.human_player import HumanPlayer


class TestConnectFourBoard(unittest.TestCase):

    def setUp(self):
        self.connect_four = ConnectFourBoard()
        self.color_O = self.connect_four.colors[0]
        self.color_X = self.connect_four.colors[1]
        self.connect_four.players[0] = HumanPlayer(self.connect_four.colors[0])
        self.connect_four.players[1] = AIPlayer(self.connect_four.colors[1], self.connect_four)
        self.connect_four.matrix = []
        for i in xrange(self.connect_four.board_height):
            self.connect_four.matrix.append([])
            for j in xrange(self.connect_four.board_width):
                self.connect_four.matrix[i].append(' ')

    def test_check_vertical_four(self):
        grid = [
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        self.connect_four.matrix = grid
        self.assertEqual(self.connect_four._is_connect_four(), True)

    def test_check_horizontal_four(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, self.color_O, self.color_O, self.color_O, ' ', ' ', ' ']
        ]
        self.connect_four.matrix = grid
        self.assertEqual(self.connect_four._is_connect_four(), True)

    def test_check_diagonal_positive_four(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', self.color_O, ' ', ' ', ' '],
            [' ', ' ', self.color_O, ' ', ' ', ' ', ' '],
            [' ', self.color_O, ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        self.connect_four.matrix = grid
        self.assertEqual(self.connect_four._is_connect_four(), True)

    def test_check_diagonal_negative_four(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', self.color_O, ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', self.color_O, ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', self.color_O, ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', self.color_O]
        ]
        self.connect_four.matrix = grid
        self.assertEqual(self.connect_four._is_connect_four(), True)

    def test_is_full(self):
        self.connect_four._round = self.connect_four.board_width * self.connect_four.board_height + 1
        self.assertEqual(self.connect_four._is_full(), True)

if __name__ == '__main__':
    unittest.main()