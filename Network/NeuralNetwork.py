"""
Module neural network
"""

import numpy as np
import functools
from scipy.optimize import linprog
import Neuron

class NeuralNetwork():
    def __init__(self, w = None, mu = None, W = None, main_channels = [1, 2, 3, 4], h = 16, g = 256,
                 components = 16, n1 = 320, n2 = 256):
        """Initialize neural network

        :param w1: Matrix of weights layer 1
        :type w1: matrix
        :param mu: List of biases
        :type mu: list
        :param W: List of weights layer 2
        :type W: list
        :param h: Count inputs of neuron 1
        :type h: int
        :param g: Count inputs of neuron 2
        :type g: int
        """

        self.w = w
        self.mu = mu
        self.W = W
        self.main_channels = main_channels

        # count inputs in layer 1
        self.h = h
        # count inputs in layer 2
        self.g = g

        # count electrodes
        self.I = h
        # count components
        self.J = None

        # count neurons in layer 1
        self.n1 = n1
        # count neurons in layer 2
        self.n2 = n2

    # public

    def learn(self, k1, k2, ours, aliens):
        """Learn neural network

        :param k1: List of '1' and '0' (len = count of neurons in layer 1)
        :type k1: list
        :param ours: List of matrix (ours form)
        :type ours: list of matrix
        :param aliens: List of matrix (aliens form)
        :type aliens: list of matrix
        """

        self.I = len(ours[0])
        self.J = len(ours[0][0])

        Mmain = self.__calculate_math_expects(ours)
        Madv = self.__calculate_math_expects(aliens)

        Varmain = self.__calculate_standart_deviations(ours, Mmain)
        Varadv = self.__calculate_standart_deviations(aliens, Madv)

        self.w = self.__calculate_weights1(Mmain, Madv, Varmain, Varadv)
        self.mu = self.__calculate_mu(Mmain, self.w, k1)

        in2 = self.__generate_in2()
        self.W = self.__calculate_weights2(in2, k1, k2)
    
    def get_key(self, form):
        in1 = self.__generate_in1()
        in2 = self.__generate_in2()

        out1 = self.__get_res_layer1(form, in1)
        out2 = self.__get_res_layer2(out1, in2)

        return out2

    # private

    def __calculate_math_expects(self, forms):
        n = len(forms)

        math_expects = np.zeros(self.I, self.J)

        for i in range(self.I):
            for j in range(self.J):
                for form in forms:
                    math_expects[i][j] += form[i][j]
                math_expects[i][j] /= n

        return math_expects

    def __calculate_standart_deviations(self, forms, math_expects):
        n = len(forms)

        standart_deviations = np.zeros(self.I, self.J)

        for i in range(self.I):
            for j in range(self.J):
                for form in forms:
                    standart_deviations[i][j] += (forms[i][j] - math_expects[i][j]) ** 2
                standart_deviations[i][j] = np.sqrt(standart_deviations[i][j]) / (n - 1)

        return standart_deviations

    def __calculate_weights1(self, Mmain, Madv, Varmain, Varadv):
        w = np.zeros(self.I, self.J)

        for i in range(self.I):
            for j in range(self.J):
                Q = np.fabs(Mmain[i][j] - Madv[i][j]) / Varmain[i][j]
                w[i][j] = Q / Varadv[i][j]

        return w

    def __calculate_mu(self, Mmain, w, k1):
        v = np.zeros(self.I)
        mu = np.zeros(self.n1)

        for i in range(self.I):
            for j in range(self.J):
                v[i] += Mmain[i][j] * w[i][j]

            for r in range(self.n1):
                if v[i] < 0 and k1[r] == 1:
                    mu[i] = np.fabs(np.amin(v[i]))
                elif v[i] < 0 and k1[r] == -1:
                    mu[i] = np.fabs(np.amax(v[i]))
                elif v[i] >= 0 and k1[r] == 1:
                    mu[i] = -np.fabs(np.amin(v[i]))
                elif v[i] >= 0 and k1[r] == -1:
                    mu[i] = -np.fabs(np.amax(v[i]))

        return mu

    def __calculate_weights2(self, in2, k1, k2):
        b = [0] * len(k1)
        c = [0] * len(k1)
        A = np.multiply(in2, k1)

        for i in range(len(k2)):
            if k2[i] > 0:
                A[i] *= -1
                b[i] = -1

        return linprog(c, A_ub=A, b_ub=b).x
    
    def __generate_in(self, num_rows, num_cols, vals):
        while(True):
            in2 = [[0 for j in range(num_cols)] for i in range(num_rows)]
            freeInRows = [[j for j in range(vals)] for i in range(num_rows)]
            freeInCols = [[j for j in range(vals)] for i in range(num_cols)]

            isGood = True
            for i in range(num_rows):
                for j in range(num_cols):
                    frows = freeInRows[i]
                    fcols = freeInCols[j]
                    frees = set(frows) & set(fcols)

                    if len(frees) == 0:
                        isGood = False
                        break

                    gen = list(frees)[np.random.randint(len(frees))]
                    in2[i][j] = gen

                    freeInRows[i].remove(gen)
                    freeInCols[j].remove(gen)

                if not isGood:
                    break

            if isGood:
                return in2
                break

    def __generate_in1(self):
        while(True):
            in1 = self.__generate_in(self.n1, self.h, self.I)
            
            isGood = True
            
            for i in range(self.n1):
                set_main = set(self.main_channels)
                set_row = set(in1[i])

                if len(set_main & set_row) == 0:
                    isGood = False
                    break

            if isGood:
                return in1

    def __generate_in2(self):
        return self.__generate_in(self.n2, self.g, self.n1)

    def __get_res_layer1(self, m, in1)
        v = [0] * self.h

        for i in range(self.h):
            for j in range(self.J):
                v[i] += m[i][j] * self.w[i][j]

            v[i] += mu[i]

        return [Neuron.neuron1_calc(v, in1[i]) for i in range(self.n1)]

    def __get_res_layer2(self, out1, in2):
        return [Neuron.neuron2_calc(self.W, out1, in2[i]) for i in range(self.n2)]
