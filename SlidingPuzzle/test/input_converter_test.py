import unittest
from main.input_converter import InputConverter

class InputConverterTest(unittest.TestCase):

    def test_convert_an_input(self):
        numbers_list = "0,2,1,3,4,6,5,7,9,8"
        input_converter = InputConverter()
        expected = ['0','2','1','3','4','6','5','7','9','8']
        result = input_converter.convert_input(numbers_list)
        self.assertEqual(expected, result)

    def test_create_3x3_matrix(self):
        numbers_list = "0,2,1,3,4,6,5,7,8"
        input_converter = InputConverter()
        user_input_list = input_converter.convert_input(numbers_list)
        expected = [['0', '2', '1'], ['3', '4', '6'], ['5', '7', '8']]
        result = input_converter.create_matrix(user_input_list)
        self.assertEqual(expected, result)

    def test_create_4x4_matrix(self):
        numbers_list = "0,2,1,3,4,6,5,7,8,9,10,11,12,13,14,15"
        input_converter = InputConverter()
        user_input_list = input_converter.convert_input(numbers_list)
        expected = [['0', '2', '1','3'], ['4', '6', '5', '7'], ['8', '9', '10', '11'], ['12', '13', '14', '15']]
        result = input_converter.create_matrix(user_input_list)
        self.assertEqual(expected, result)

if __name__ == '__main__':
        unittest.main()