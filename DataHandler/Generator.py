"""
Module for generation input data
"""

import random

K1_LEN = 320
K2_LEN = 256

def generate_key(possible_values, key_len):
    """Generate key

    :param possible_values: Elements of key
    :type possible_values: list
    :param key_len: Length of key
    :type key_len: int
    :returns: list
    """

    return [random.choice(possible_values) for i in range(key_len)]

def generate_k1(key_len):
    """Generate key 'k1'

    :param key_len: Length of key
    :type key_len: int
    :returns: list -- key 'k1'
    """

    return generate_key([1, -1], key_len)

def generate_k2(key_len):
    """Generate key 'k2'

    :param key_len: Length of key
    :type key_len: int
    :returns: list -- key 'k2'
    """

    return generate_key([0, 1], key_len)
