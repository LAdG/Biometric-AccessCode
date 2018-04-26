"""
Testing module
"""

import os
import pytest
import IncludeProject
from DataHandler.Reader import read_matrix_file, list_to_matrix, read_k1, read_k2
from DataHandler.Writer import write_list_to_file

DATA_PATH = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'Data' + os.sep

class TestReader:
    def test_read_k1(self):
        assert(read_k1(DATA_PATH + 'input_k1.txt') == [1, -1, -1, 1, 1])

    def test_read_k2(self):
        assert(read_k2(DATA_PATH + 'input_k2.txt') == [1, 0, 0, 1, 1])

class TestWriter:
    def setup_class(self):
        self.file_path = DATA_PATH + 'write_key.txt'

    def test_write_k1_to_file(self):
        k1_list = [1, -1, -1, 1, 1]

        write_list_to_file(k1_list, self.file_path)
        assert(read_k1(self.file_path) == k1_list)

    def test_write_2_to_file(self):
        k2_list = [0, 1, 1, 0, 0]

        write_list_to_file(k2_list, self.file_path)
        assert(read_k1(self.file_path) == k2_list)
