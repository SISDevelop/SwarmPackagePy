from math import exp
import numpy as np

from . import intelligence


class gsa(intelligence.sw):
    """
    Gravitational Search Algorithm
    """

    def __init__(self, n, function, lb, ub, dimension, iteration, G0=3):
        """
        :param n: number of agents
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: number of iterations
        :param G0: gravity parameter (default value is 3)
        """

        super(gsa, self).__init__()

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        self._points(self.__agents)

        Pbest = self.__agents[np.array([function(x)
                                        for x in self.__agents]).argmin()]
        Gbest = Pbest

        velocity = np.array([[0 for k in range(dimension)] for i in range(n)])

        for t in range(iteration):

            csi = np.random.random((n, dimension))
            eps = np.random.random((1, n))[0]

            fitness = np.array([function(x) for x in self.__agents])

            m = np.array([(function(x) - max(fitness)) /
                       (min(fitness) - max(fitness)) for x in self.__agents])
            M = np.array([i / sum(m) for i in m])

            G = G0 / exp(0.01 * t)
            a = np.array([sum([eps[j] * G * M[j] *
                            (self.__agents[j] - self.__agents[i]) / (
                np.linalg.norm(self.__agents[i] - self.__agents[j]) + 0.001)
                            for j in range(n)]) for i in range(n)])

            velocity = csi * velocity + np.array([a[i] for i in range(n)])
            self.__agents += velocity
            self.__agents = np.clip(self.__agents, lb, ub)
            self._points(self.__agents)

            Pbest = self.__agents[
                np.array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

        self._set_Gbest(Gbest)
