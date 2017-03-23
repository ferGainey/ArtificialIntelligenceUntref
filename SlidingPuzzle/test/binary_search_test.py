import unittest
from main.binary_search import MatrixConverter

class BinarySearchTest(unittest.TestCase):

    def test_convert_matrix_to_number(self):
        matrix = [['3', '0', '2'], ['0', '7', '5'], ['0', '4', '2']]
        binary_search = MatrixConverter()
        number_obtained = binary_search.convert_matrix_to_number(matrix)
        number_expected = 302075042
        self.assertEqual(number_obtained, number_expected)

    def test_search_an_existant_element(self):
        binary_search = MatrixConverter()
        sorted_list = [1,2,3,4,5,6,7,8,9,11,13,15,17,23,45,33,36,45,48,52,56,62,65,78,89,90,91]
        matrix = [['0','0','0'], ['0', '0', '0'], ['0','6','2']]
        self.assertEqual(binary_search.do_search(sorted_list, matrix), True)

    def test_search_an_inexistant_element(self):
        binary_search = MatrixConverter()
        sorted_list = [1,2,3,4,5,6,7,8,9,11,13,15,17,23,45,33,36,45,48,52,56,62,65,78,89,90,91]
        matrix = [['0','0','2'], ['0', '0', '0'], ['0','4','2']]
        self.assertEqual(binary_search.do_search(sorted_list, matrix), False)

if __name__ == '__main__':
        unittest.main()