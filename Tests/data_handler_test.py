"""
Testing module
"""

import unittest
import IncludeProject
from DataHandler.Reader import read_matrix_file, list_to_matrix, read_k1, read_k2

DATA_PATH = '/home/tikhon/Documents/Biometric-AccessCode/Tests/Data/'

class TestReader(unittest.TestCase):
    def setUp(self):
        self.input_list = read_matrix_file(DATA_PATH + 'input_matrix.txt')

    def test_reading_file(self):
        self.assertEqual(self.input_list, [1.1, 2.12, 3.123, 4.1234])

    def test_list_to_matrix(self):
        self.assertEqual(list_to_matrix(self.input_list, 2, 2), [[1.1, 2.12], [3.123, 4.1234]])

    def test_list_to_matrix_exc(self):
        list_len = len(self.input_list)
        self.assertRaises(IndexError, list_to_matrix, self.input_list, list_len, list_len)

    def test_read_k1(self):
        self.assertEqual(read_k1(DATA_PATH + 'input_k1.txt'), [1, -1, -1, 1, 1])

    def test_read_k2(self):
        self.assertEqual(read_k2(DATA_PATH + 'input_k2.txt'), [1, 0, 0, 1, 1])

if __name__ == '__main__':
    unittest.main()
        