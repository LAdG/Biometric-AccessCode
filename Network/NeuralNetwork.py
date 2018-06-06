"""
Module neural network
"""

import numpy as np
import functools
from scipy.optimize import linprog
import Network.Neuron as Neuron

class NeuralNetwork():
    def __init__(self, w = None, mu = None, W = None, main_channels = [6, 7, 8, 9], h = 14, g = 256,
                 components = 15, n1 = 320, n2 = 256, in1 = [], in2 = []):
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
        self.signs_w = []
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
        self.J = components

        # count neurons in layer 1
        self.n1 = n1
        # count neurons in layer 2
        self.n2 = n2

        self.in1 = in1
        self.in2 = in2

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
        self.signs_w = self.__calculate_signs_weights1(Mmain, Madv, k1)
        self.in1 = self.__generate_in1()
        self.mu = self.__calculate_mu(Mmain, self.w, k1, self.in1)

        self.in2 = self.__generate_in2()
        self.W = self.__calculate_weights2(self.in2, k1, k2)
    
    def get_key(self, form):
        out1 = self.__get_res_layer1(form, self.in1)
        out2 = self.__get_res_layer2(out1, self.in2)

        return out2

    # private

    def __calculate_math_expects(self, forms):
        n = len(forms)

        math_expects = np.zeros((self.I, self.J))

        for i in range(self.I):
            for j in range(self.J):
                for form in forms:
                    math_expects[i][j] += form[i][j]
                math_expects[i][j] /= n

        return math_expects

    def __calculate_standart_deviations(self, forms, math_expects):
        n = len(forms)

        standart_deviations = np.zeros((self.I, self.J))

        for i in range(self.I):
            for j in range(self.J):
                for form in forms:
                    standart_deviations[i][j] += (form[i][j] - math_expects[i][j]) ** 2
                standart_deviations[i][j] = np.sqrt(standart_deviations[i][j]) / (n - 1)

        return standart_deviations

    def __calculate_weights1(self, Mmain, Madv, Varmain, Varadv):
        w = np.zeros((self.I, self.J))

        for i in range(self.I):
            for j in range(self.J):
                w[i][j] = np.fabs(Mmain[i][j] - Madv[i][j]) / (Varmain[i][j] * Varadv[i][j])

        return w

    def __calculate_signs_weights1(self, Mmain, Madv, k1):
        signs_w = [[] for i in range(self.n1)]
        
        for l in range(self.n1):
            signs_w[l] = np.zeros((self.I, self.J))
            for i in range(self.I):
                for j in range(self.J):
                    signs_w[l][i][j] = np.sign(Mmain[i][j] - Madv[i][j])

                    if k1[l] == -1:
                        signs_w[l][i][j] *= -1

        return signs_w

    def __calculate_mu(self, Mmain, w, k1, in1):
        v = np.zeros(self.I)
        mu = np.zeros(self.n1)

        x = np.zeros(self.n1)

        for i in range(self.I):
            for j in range(self.J):
                v[i] += Mmain[i][j] * w[i][j]

        for i in range(self.n1):
            for j in range(self.h):
                x[i] += v[in1[i][j]]

        minv = np.fabs(np.amin(v))
        maxv = np.fabs(np.amax(v))

        for i in range(self.n1):
            if x[i] < 0 and k1[i] == 1:
                mu[i] =  minv
            elif x[i] < 0 and k1[i] == -1:
                mu[i] = maxv
            elif x[i] >= 0 and k1[i] == 1:
                mu[i] = -minv
            elif x[i] >= 0 and k1[i] == -1:
                mu[i] = -maxv

        return mu

    def __calculate_weights2(self, in2, k1, k2):
        b = [0] * len(k2)
        c = [0] * len(k1)

        A = np.multiply(k1, in2)

        for i in range(len(k2)):
            if k2[i] > 0:
                A[i] *= -1
                b[i] = -1

        res = linprog(c, A_ub=A, b_ub=b, method='interior-point')

        # TODO sign?
        
        return res.x
    
    def __generate_in(self, num_rows, num_cols, vals, replace = False):
        gen_in = []

        for i in range(num_rows):
            while True:
                gen_row = np.random.choice(vals, num_cols, replace=replace)

                isGood = True
                for i in range(len(gen_in)):
                    if np.array_equal(gen_in[i], gen_row):
                        isGood = False
                        break

                if isGood:
                    gen_in.append(gen_row)
                    break

        return gen_in

    def __generate_in1(self):
        while(True):
            in1 = self.__generate_in(self.n1, self.h, self.h)
            
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
        return self.__generate_in(self.n2, self.g, 2, True)

    def __get_res_layer1(self, m, in1):
        out1 = np.zeros(self.n1)

        for l in range(self.n1):
            v = [0] * self.h
            for i in range(self.h):
                for j in range(self.J):
                    v[i] += m[i][j] * self.w[i][j] * self.signs_w[l][i][j]

            out1[l] = Neuron.neuron1_calc(v, self.mu[i], in1[i])

        return out1

    def __get_res_layer2(self, out1, in2):
        return [Neuron.neuron2_calc(self.W, out1, in2[i]) for i in range(self.n2)]
