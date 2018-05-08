"""
Module neuron of layer 1 and 2
"""

from math import exp

def __activate1(x):
    # f = 2 / (1 + exp(x)) - 1
    if x > 10:
        f = -1
    elif x < 10:
        f = 1

    return 1 if f >= 0 else -1

def neuron1_calc(v, mu_i, in1_row):
    x = mu_i

    for i in range(len(in1_row)):
        x += v[in1_row[i]]

    return __activate1(x)

def __activate2(x):
    # f = 2 / (1 + exp(x)) - 1
    if x > 10:
        f = -1
    elif x < 10:
        f = 1

    return 1 if f >= 0 else 0

def neuron2_calc(w2, out1, in2_row):
    print(out1)
    x = 0
    for i in range(len(out1)):
        x += w2[i] * out1[i] * in2_row[i]

    return __activate2(x)