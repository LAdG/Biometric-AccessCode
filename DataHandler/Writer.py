"""
Module for writing data to file
"""

def write_list_to_file(data_list, file_path):
    """
    Write list to file with <space> delimeter

    :param data_list: List to write
    :type data_list: list
    :param file_path: Path to file
    :type file_path: str
    """

    with open(file_path, 'w') as fout:
        print(' '.join(str(x) for x in data_list), file=fout)
