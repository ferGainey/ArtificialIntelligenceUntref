import unittest
from main.matrix_updater import MatrixUpdater

class MatrixUpdaterTest(unittest.TestCase):

    def test_matrix_move_up(self):
        matrix = [['1','2','3'], ['0','4','5'], ['6','7','8']]
        matrix_updater = MatrixUpdater()
        result = matrix_updater.update_matrix(matrix, 'up')
        matrix_expected = [['0','2','3'], ['1','4','5'], ['6','7','8']]
        self.assertEqual(result, matrix_expected)


    def test_matrix_move_down(self):
        matrix = [['1','2','3'], ['0','4','5'], ['6','7','8']]
        matrix_updater = MatrixUpdater()
        result = matrix_updater.update_matrix(matrix, 'down')
        matrix_expected = [['1','2','3'], ['6','4','5'], ['0','7','8']]
        self.assertEqual(result, matrix_expected)

    def test_matrix_move_right(self):
        matrix = [['1','2','3'], ['0','4','5'], ['6','7','8']]
        matrix_updater = MatrixUpdater()
        result = matrix_updater.update_matrix(matrix, 'right')
        matrix_expected = [['1','2','3'], ['4','0','5'], ['6','7','8']]
        self.assertEqual(result, matrix_expected)


    def test_matrix_move_left(self):
        matrix = [['1','2','3'], ['5','4','8'], ['6','7','0']]
        matrix_updater = MatrixUpdater()
        result = matrix_updater.update_matrix(matrix, 'left')
        matrix_expected = [['1','2','3'], ['5','4','8'], ['6','0','7']]
        self.assertEqual(result, matrix_expected)



if __name__ == '__main__':
        unittest.main()