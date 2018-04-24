"""
Module neuron of layer 1 and 2
"""

def __activate1(x):
    f = 2 / (1 + exp(x)) - 1

    return 1 if f >= 0 else -1

def neuron1_calc(v, in1_row):
    x = 0

    for i in range(len(in1_row)):
        x += v[in1_row[i]]

    return __activate1(x)

def __activate2(x):
    f = 2 / (1 + exp(x)) - 1

    return 1 if f >= 0 else 0

def neuron2_calc(w2, out1, in2_row):
    x = 0

    for e in range(len(in2_row)):
        i = in2_row[e]
        x += w2[i] * out1[i]

    return __activate2(x)