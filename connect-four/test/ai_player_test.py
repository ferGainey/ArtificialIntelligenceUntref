import unittest
from main.connect_four_board import ConnectFourBoard
from main.ai_player import AIPlayer
from main.human_player import HumanPlayer

class TestAiPlayer(unittest.TestCase):

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

    def test_check_horizontal_four_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, self.color_X, self.color_X, self.color_X, ' ', ' ', ' ']
        ]
        horizontal_list = self.connect_four.players[1].find_horizontal_line_beta(grid, self.color_X)
        horizontal_fours = horizontal_list[2]
        self.assertEqual(horizontal_fours, 1)


    def test_check_multiple_horizontal_four_AI(self):
        grid = [
            [' ', self.color_X, self.color_X, self.color_X, self.color_X, self.color_X, self.color_X],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, self.color_X, self.color_X, self.color_X, self.color_X, self.color_O, ' '],
            [self.color_X, self.color_X, self.color_X, self.color_X, ' ', ' ', ' '],
            [self.color_X, self.color_O, self.color_X, self.color_X, self.color_X, self.color_X, ' '],
            [self.color_X, self.color_X, self.color_X, self.color_X, ' ', ' ', ' '],
        ]
        horizontal_list = self.connect_four.players[1].find_horizontal_line_beta(grid, self.color_X)
        horizontal_fours = horizontal_list[2]
        self.assertEqual(horizontal_fours, 5)


    def test_check_horizontal_three_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, self.color_X, self.color_X, self.color_X, ' ', ' ', ' ']
        ]
        horizontal_list = self.connect_four.players[1].find_horizontal_line_beta(grid, self.color_X)
        horizontal_threes = horizontal_list[1]
        self.assertEqual(horizontal_threes, 0)


    def test_check_horizontal_three_AI_2(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, self.color_X, self.color_X, ' ', ' ', ' ', ' ']
        ]
        horizontal_list = self.connect_four.players[1].find_horizontal_line_beta(grid, self.color_X)
        horizontal_threes = horizontal_list[1]
        self.assertEqual(horizontal_threes, 1)


    def test_check_multiple_horizontal_three_AI_1(self):
        grid = [
            [' ', self.color_X, self.color_X, self.color_X, self.color_X, self.color_X, self.color_X],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, self.color_X, self.color_X, self.color_X, self.color_X, self.color_O, ' '],
            [self.color_X, self.color_X, self.color_X, self.color_X, ' ', ' ', ' '],
            [self.color_X, self.color_O, self.color_X, self.color_X, self.color_X, self.color_X, ' '],
            [self.color_X, self.color_X, self.color_X, self.color_X, ' ', ' ', ' '],
        ]
        horizontal_list = self.connect_four.players[1].find_horizontal_line_beta(grid, self.color_X)
        horizontal_threes = horizontal_list[1]
        self.assertEqual(horizontal_threes, 0)


    def test_check_multiple_horizontal_three_AI_2(self):
        grid = [
            [' ', ' ', ' ', ' ', self.color_X, self.color_X, self.color_X],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', self.color_X, self.color_X, self.color_X, self.color_O, ' '],
            [self.color_O, self.color_X, self.color_X, self.color_X, ' ', ' ', ' '],
            [self.color_X, self.color_O, self.color_O, self.color_X, self.color_X, self.color_X, ' '],
            [self.color_X, ' ', self.color_X, ' ', ' ', ' ', ' '],
        ]
        horizontal_list = self.connect_four.players[1].find_horizontal_line_beta(grid, self.color_X)
        horizontal_threes = horizontal_list[1]
        self.assertEqual(horizontal_threes, 4)


    def test_check_horizontal_two_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, self.color_X, self.color_X, ' ', ' ', ' ', ' ']
        ]
        horizontal_list = self.connect_four.players[1].find_horizontal_line_beta(grid, self.color_X)
        horizontal_twos = horizontal_list[0]
        self.assertEqual(horizontal_twos, 0)


    def test_check_horizontal_two_AI_2(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, self.color_X, ' ', ' ', ' ', ' ', ' ']
        ]
        horizontal_list = self.connect_four.players[1].find_horizontal_line_beta(grid, self.color_X)
        horizontal_twos = horizontal_list[0]
        self.assertEqual(horizontal_twos, 1)


    def test_check_multiple_horizontal_two_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', self.color_X, self.color_X, self.color_X],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', self.color_X, self.color_X, self.color_X, self.color_O, ' '],
            [self.color_O, self.color_X, self.color_X, self.color_X, ' ', ' ', ' '],
            [self.color_X, self.color_O, self.color_O, self.color_X, self.color_X, self.color_X, ' '],
            [self.color_X, ' ', self.color_X, ' ', ' ', ' ', ' '],
        ]
        horizontal_list = self.connect_four.players[1].find_horizontal_line_beta(grid, self.color_X)
        horizontal_two = horizontal_list[0]
        self.assertEqual(horizontal_two, 0)


    def test_check_multiple_horizontal_two_AI_2(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', self.color_X, self.color_X],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', self.color_X, self.color_X, self.color_O, ' '],
            [self.color_O, self.color_X, self.color_O, self.color_X, ' ', ' ', ' '],
            [self.color_X, self.color_O, self.color_O, self.color_O, self.color_X, self.color_X, ' '],
            [self.color_X, ' ', self.color_X, self.color_X, ' ', ' ', ' '],
        ]
        horizontal_list = self.connect_four.players[1].find_horizontal_line_beta(grid, self.color_X)
        horizontal_two = horizontal_list[0]
        self.assertEqual(horizontal_two, 4)


    def test_check_vertical_four_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        vertical_list = self.connect_four.players[1].find_vertical_line_beta(grid, self.color_X)
        self.assertEqual(vertical_list[2], 1)


    def test_check_multiple_vertical_four_AI(self):
        grid = [
            [' ', self.color_X, ' ', ' ', self.color_X, self.color_X, self.color_X],
            [' ', ' ', self.color_X, self.color_X, ' ', ' ', self.color_X],
            [self.color_X, self.color_X, self.color_X, self.color_X, self.color_X, self.color_O, ' '],
            [self.color_X, self.color_X, self.color_X, self.color_X, ' ', self.color_O, ' '],
            [self.color_X, self.color_O, self.color_X, self.color_X, self.color_X, self.color_X, ' '],
            [self.color_X, self.color_X, self.color_O, ' ', ' ', ' ', ' '],
        ]
        vertical_list = self.connect_four.players[1].find_vertical_line_beta(grid, self.color_X)
        self.assertEqual(vertical_list[2], 3)


    def test_check_vertical_three_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        vertical_list = self.connect_four.players[1].find_vertical_line_beta(grid, self.color_X)
        vertical_threes = int(vertical_list[1])
        self.assertEqual(vertical_threes, 0)


    def test_check_vertical_three_AI_2(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        vertical_list = self.connect_four.players[1].find_vertical_line_beta(grid, self.color_X)
        vertical_threes = vertical_list[1]
        self.assertEqual(vertical_threes, 1)


    def test_check_multiple_vertical_three_AI_1(self):
        grid = [
            [' ', self.color_O, ' ', ' ', self.color_X, self.color_X, self.color_X],
            [' ', self.color_X, ' ', self.color_X, ' ', ' ', self.color_X],
            [self.color_X, self.color_X, self.color_X, self.color_X, self.color_X, self.color_O, self.color_X],
            [self.color_X, self.color_X, self.color_X, self.color_X, ' ', self.color_O, ' '],
            [self.color_X, self.color_O, self.color_X, self.color_O, self.color_X, self.color_X, ' '],
            [self.color_X, self.color_X, self.color_O, ' ', ' ', ' ', ' '],
        ]
        vertical_list = self.connect_four.players[1].find_vertical_line_beta(grid, self.color_X)
        vertical_threes = vertical_list[1]
        self.assertEqual(vertical_threes, 4)


    def test_check_multiple_vertical_three_AI_2(self):
        grid = [
            [' ', ' ', ' ', ' ', self.color_X, self.color_X, self.color_X],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', self.color_X, self.color_X, self.color_X, self.color_O, ' '],
            [self.color_O, self.color_X, self.color_X, self.color_O, ' ', ' ', ' '],
            [self.color_X, self.color_O, self.color_O, self.color_X, self.color_X, self.color_X, ' '],
            [self.color_X, ' ', self.color_X, ' ', ' ', ' ', ' '],
        ]
        vertical_list = self.connect_four.players[1].find_vertical_line_beta(grid, self.color_X)
        vertical_threes = vertical_list[1]
        self.assertEqual(vertical_threes, 0)


    def test_check_vertical_two_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        vertical_list = self.connect_four.players[1].find_vertical_line_beta(grid, self.color_X)
        vertical_twos = vertical_list[0]
        self.assertEqual(vertical_twos, 0)


    def test_check_vertical_two_AI_2(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        vertical_list = self.connect_four.players[1].find_vertical_line_beta(grid, self.color_X)
        vertical_twos = vertical_list[0]
        self.assertEqual(vertical_twos, 1)


    def test_check_multiple_vertical_two_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', self.color_X, self.color_X, self.color_X],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', self.color_X, self.color_X, self.color_X, self.color_O, ' '],
            [self.color_O, self.color_X, self.color_X, self.color_X, ' ', ' ', ' '],
            [self.color_X, self.color_O, self.color_O, self.color_X, self.color_X, self.color_X, ' '],
            [self.color_X, ' ', self.color_X, ' ', ' ', ' ', ' '],
        ]
        vertical_list = self.connect_four.players[1].find_vertical_line_beta(grid, self.color_X)
        vertical_two = vertical_list[0]
        self.assertEqual(vertical_two, 2)


    def test_check_multiple_vertical_two_AI_2(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', self.color_X, self.color_X],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', self.color_X, self.color_X, self.color_O, ' '],
            [self.color_O, self.color_X, self.color_X, self.color_O, ' ', ' ', ' '],
            [self.color_X, self.color_O, self.color_O, self.color_O, self.color_X, self.color_X, ' '],
            [self.color_O, ' ', self.color_X, self.color_X, ' ', ' ', ' '],
        ]
        vertical_list = self.connect_four.players[1].find_vertical_line_beta(grid, self.color_X)
        vertical_two = vertical_list[0]
        self.assertEqual(vertical_two, 0)


    def test_check_diagonal_positive_four_AI_1(self):
        grid = [
            ['a5 ', 'b4 ', 'c5 ', ' ', ' ', ' ', ' '],
            ['a4 ', 'b3 ', 'c4 ', ' ', ' ', ' ', ' '],
            ['a3 ', 'b2 ', 'c3 ', self.color_X, ' ', ' ', ' '],
            ['a2', 'b1 ', self.color_X, ' ', ' ', ' ', ' '],
            ['a1 ', self.color_X, ' ', ' ', ' ', ' ', ' '],
            [self.color_X, 'c0 ', ' ', ' ', ' ', ' ', ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_four = diagonal_list[2]
        self.assertEqual(diagonal_four, 1)


    def test_check_diagonal_positive_four_AI_2(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', self.color_X, ' ', ' ', ' '],
            [' ', ' ', self.color_X, ' ', ' ', ' ', ' '],
            [' ', self.color_X, ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_four = diagonal_list[2]
        self.assertEqual(diagonal_four, 1)


    def test_check_diagonal_positive_four_AI_3(self):
        grid = [
            [' ', ' ', ' ', ' ', self.color_X, ' ', ' '],
            [' ', ' ', ' ', self.color_X, ' ', ' ', ' '],
            [' ', ' ', self.color_X, ' ', ' ', ' ', ' '],
            [' ', self.color_O, ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_four = diagonal_list[2]
        self.assertEqual(diagonal_four, 0)


    def test_check_diagonal_positive_threes_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', self.color_X, ' ', ' '],
            [' ', ' ', ' ', self.color_X, ' ', ' ', ' '],
            [' ', ' ', self.color_X, ' ', ' ', ' ', ' '],
            [' ', self.color_O, ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_three = diagonal_list[1]
        self.assertEqual(diagonal_three, 1)


    def test_check_diagonal_positive_twos_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', self.color_X, ' ', ' ', ' '],
            [' ', ' ', self.color_X, ' ', ' ', ' ', ' '],
            [' ', self.color_O, ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_two = diagonal_list[0]
        self.assertEqual(diagonal_two, 1)


    def test_check_diagonal_negative_four_AI_1(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', self.color_X, ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', self.color_X, ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', self.color_X, ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', self.color_X]
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_four = diagonal_list[2]
        self.assertEqual(diagonal_four, 1)


    def test_check_diagonal_negative_four_AI_2(self):
        grid = [
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', self.color_X, ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', self.color_X, ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', self.color_X, ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', self.color_X, ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_four = diagonal_list[2]
        self.assertEqual(diagonal_four, 1)


    def test_check_diagonal_negative_four_AI_3(self):
        grid = [
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', self.color_X, ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', self.color_O, ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', self.color_X, ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', self.color_X, ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_four = diagonal_list[2]
        self.assertEqual(diagonal_four, 0)


    def test_check_diagonal_negative_four_AI_4(self):
        grid = [
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', self.color_X, ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', self.color_O, ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', self.color_X, ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', self.color_X, ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', self.color_X, ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_four = diagonal_list[2]
        self.assertEqual(diagonal_four, 0)


    def test_check_diagonal_positive_four_AI_1(self):
        grid = [
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, self.color_X, ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', self.color_O, ' ', ' ', ' ', self.color_X],
            [' ', ' ', ' ', ' ', ' ', self.color_X, ' '],
            [' ', ' ', ' ', ' ', self.color_X, ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_four = diagonal_list[2]
        self.assertEqual(diagonal_four, 0)


    def test_check_diagonal_positive_four_AI_4(self):
        grid = [
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', self.color_X, ' ', ' ', ' ', self.color_X, self.color_X],
            [' ', ' ', self.color_O, ' ', self.color_X, self.color_X, self.color_X],
            [' ', ' ', ' ', self.color_O, self.color_X, ' ', ' '],
            [' ', ' ', ' ', self.color_X, self.color_O, ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_four = diagonal_list[2]
        self.assertEqual(diagonal_four, 1)


    def test_check_diagonal_positive_four_AI_5(self):
        grid = [
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, self.color_X, ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', self.color_O, ' ', ' ', ' ', self.color_X],
            [' ', ' ', ' ', ' ', ' ', self.color_X, ' '],
            [' ', ' ', ' ', ' ', self.color_X, ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        diagonal_list = self.connect_four.players[1].find_diagonal_line_beta(grid, self.color_X)
        diagonal_four = diagonal_list[2]
        self.assertEqual(diagonal_four, 0)


    def test_simulate_move_1(self):
        initial_grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        expected_grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        generated_grid = self.connect_four.players[1].simulate_move(initial_grid, 0, self.color_O)
        self.assertEqual(generated_grid, expected_grid)


    def test_simulate_move_2(self):
        initial_grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        expected_grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        generated_grid = self.connect_four.players[1].simulate_move(initial_grid, 0, self.color_O)
        self.assertEqual(generated_grid, expected_grid)


    def test_simulate_move_3(self):
        initial_grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        expected_grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        generated_grid = self.connect_four.players[1].simulate_move(initial_grid, 0, self.color_O)
        self.assertEqual(generated_grid, expected_grid)


    def test_simulate_move_4(self):
        initial_grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        expected_grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', self.color_O]
        ]
        generated_grid = self.connect_four.players[1].simulate_move(initial_grid, 6, self.color_O)
        self.assertEqual(generated_grid, expected_grid)


    def test_simulate_move_5(self):
        initial_grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', self.color_O]
        ]

        expected_grid = [
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', self.color_O]
        ]
        generated_grid = self.connect_four.players[1].simulate_move(initial_grid, 0, self.color_X)
        self.assertEqual(generated_grid, expected_grid)


    def test_simulate_move_6(self):
        initial_grid = [
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_X, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', ' '],
            [self.color_O, ' ', ' ', ' ', ' ', ' ', self.color_O]
        ]

        expected_grid = None
        generated_grid = self.connect_four.players[1].simulate_move(initial_grid, 0, self.color_X)
        generated_grid = self.connect_four.players[1].simulate_move(initial_grid, 0, self.color_O)
        self.assertEqual(generated_grid, expected_grid)

if __name__ == '__main__':
    unittest.main()