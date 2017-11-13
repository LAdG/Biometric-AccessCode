"""
Module for reading input files
"""

import re

def read_matrix_file(file_path):
    """Read file and convert to float list

    :param file_path: Path to file
    :type file_path: str
    :returns: list of float
    """

    with open(file_path, 'r') as fin:
        return list(map(float, re.split('[ \n\t]+', fin.read().strip())))


def list_to_matrix(input_data, n_el, m_com):
    """Convert list to Matrix[n, m]

    :param input_data: List of data
    :type input_data: list
    :param n_el: Rows number
    :type n_el: int
    :param m_com: Columns number
    :type m_com: int
    :returns: list of lists of float
    """

    if n_el * m_com > len(input_data):
        raise IndexError

    output_matrix = [[0 for j in range(0, m_com)] for i in range(0, n_el)]
    for i in range(0, n_el):
        for j in range(0, m_com):
            output_matrix[i][j] = input_data[i * m_com + j]

    return output_matrix

def read_k1(file_path):
    """Read k1 string from file and convert to integer list

    :param file_path: Path to file
    :type file_path: str
    :returns: list of int
    """

    with open(file_path, 'r') as fin:
        return list(map(int, re.split('[ \n\t]+', fin.read().strip())))

def read_k2(file_path):
    """Read k2 string from file and convert to integer list

    :param file_path: Path to file
    :type file_path: str
    :returns: list of int
    """

    with open(file_path, 'r') as fin:
        return list(map(int, re.split('[ \n\t]+', fin.read().strip())))
