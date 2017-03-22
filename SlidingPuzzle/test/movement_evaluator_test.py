import unittest
from main.movement_evaluator import MovementEvaluator

class MovementEvaluatorTest(unittest.TestCase):

    def test_the_possible_movements_are_right_and_down(self):
        matrix = [['0','1','2'], ['3','4','5'], ['6','7','8']]
        movement_evaluator = MovementEvaluator()
        possible_movements = movement_evaluator.get_possible_movements(matrix)
        expected = ['right', 'down']
        self.assertEqual(possible_movements, expected)

    def test_the_possible_movements_are_down_and_left(self):
        matrix = [['1','2','0'], ['3','4','5'], ['6','7','8']]
        movement_evaluator = MovementEvaluator()
        possible_movements = movement_evaluator.get_possible_movements(matrix)
        expected = ['down', 'left']
        self.assertEqual(possible_movements, expected)

    def test_the_possible_movements_for_a_four_x_four_matrix(self):
        matrix = [['1', '2', '9', '10'], ['3', '4', '0', '12'], ['6', '7', '8', '13'],['14', '15', '11', '5']]
        movement_evaluator = MovementEvaluator()
        possible_movements = movement_evaluator.get_possible_movements(matrix)
        expected = ['up', 'right','down', 'left']
        self.assertEqual(possible_movements, expected)


if __name__ == '__main__':
        unittest.main()