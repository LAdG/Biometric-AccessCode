"""
Module for reading input files
"""

import re

def read_file(file_path):
    """
    Read file and convert to float list
    """
    with open(file_path, 'r') as fin:
        return list(map(float, re.split('[ \n\t]+', fin.read().strip())))


def list_to_matrix(input_data, n_el, m_com):
    """
    Convert list to Matrix[n, m]
    """

    if n_el * m_com > len(input_data):
        raise IndexError

    output_matrix = [[0 for j in range(0, m_com)] for i in range(0, n_el)]
    for i in range(0, n_el):
        for j in range(0, m_com):
            output_matrix[i][j] = input_data[i * m_com + j]

    return output_matrix
