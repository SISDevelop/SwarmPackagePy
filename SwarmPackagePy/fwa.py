import numpy as np
import random

from . import intelligence


class fwa(intelligence.sw):
    """
    Firework Algorithm
    """
    def __init__(self, n, function, lb, ub, dimension, iteration, m1=7, m2=7, eps=0.001, amp=2, a=0.3, b=3):

        """
        :param n: number of fireworks
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: the number of iterations
        :param m1: parameter controlling the number of normal sparks
	(default value is 7)
        :param m2: parameter controlling the number of Gaussian sparks 
	(default value is 7)
        :param eps: constant used to avoid division by zero (default value is 0.001)
        :param amp: amplitude of normal explosion (default value is 2)
        :param a: parameter controlling the lower bound for number of normal sparks
	(default value is 0.3)
        :param b: parameter controlling the upper bound for number of normal sparks,
	 b must be greater than a (b is set to 3 by default)
        """

        super(fwa, self).__init__()

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        self._points(self.__agents)

        Pbest = self.__agents[
            np.array([function(x) for x in self.__agents]).argmin()]
        Gbest = Pbest


        for i in range(iteration):
            Ymin = function(Pbest)
            Ymax = max([function(x) for x in self.__agents])
            sparks = []
            for fw in self.__agents:
                self.__explosion_operator(sparks, fw, function, dimension, m1, eps, amp, Ymin, Ymax, a, b)
                self.__gaussian_mutation(sparks, fw, dimension, m2)

            self.__mapping_rule(sparks, lb, ub, dimension)
            self.__selection(sparks, n, function)
            self._points(self.__agents)

            Pbest = self.__agents[
                np.array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

        self._set_Gbest(Gbest)


    def __explosion_operator(self, sparks, fw, function, dimension, m, eps, amp, Ymin, Ymax, a, b):
        sparks_num = self.__round(m*(Ymax - function(fw) + eps /\
                           (sum([Ymax-function(fwk) for fwk in self.__agents]) + eps)), m, a, b)

        amplitude = amp * (function(fw) - Ymax + eps) /\
                    (sum([function(fwk) - Ymax for fwk in self.__agents]) + eps)

        for j in range(int(sparks_num)):
            sparks.append(np.array(fw))
            for k in range(dimension):
                if (random.choice([True, False])):
                    sparks[-1][k] += random.uniform(-amplitude, amplitude)

    def __gaussian_mutation(self, sparks, fw, dimension, m):
        for j in range(m):
            g = np.random.normal(1, 1)
            sparks.append(np.array(fw))
            for k in range(dimension):
                if(random.choice([True, False])):
                    sparks[-1][k] *= g

    def __mapping_rule(self, sparks, lb, ub, dimension):
        for i in range(len(sparks)):
            for j in range(dimension):
                if(sparks[i][j] > ub or sparks[i][j] < lb):
                    sparks[i][j] = lb + (sparks[i][j]-lb) % (ub-lb)

    def __selection(self, sparks, n, function):
        self.__agents = sorted(np.concatenate((self.__agents,sparks)), key=function)[:n]

    def __round(self, s, m, a, b):
        if   (s < a*m):
            return round(a*m)
        elif (s > b*m): 
            return round(b*m)
        else:
            return round(s)

