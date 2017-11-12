"""
Testing module
"""

import unittest
import IncludeProject
from DataHandler.Reader import read_file, list_to_matrix

DATA_PATH = '/home/tikhon/Documents/Biometric-AccessCode/Tests/Data/'

class TestReader(unittest.TestCase):
    def test_reading_file(self):
        self.assertEqual(read_file(DATA_PATH + 'input.txt'), [1.1, 2.12, 3.123, 4.1234])

    def test_list_to_matrix(self):
        input_list = read_file(DATA_PATH + 'input.txt')
        self.assertEqual(list_to_matrix(input_list, 2, 2), [[1.1, 2.12], [3.123, 4.1234]])

if __name__ == '__main__':
    unittest.main()
        