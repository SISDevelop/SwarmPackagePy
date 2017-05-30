import numpy as np

from . import intelligence


class gwo(intelligence.sw):
    """
    Grey Wolf Optimizer
    """

    def __init__(self, n, function, lb, ub, dimension, iteration):
        """
        :param n: number of agents
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: number of iterations
        """

        super(gwo, self).__init__()

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        self._points(self.__agents)
        alpha, beta, delta = self.__get_abd(n, function)

        Gbest = alpha

        for t in range(iteration):

            a = 2 - 2 * t / iteration

            r1 = np.random.random((n, dimension))
            r2 = np.random.random((n, dimension))
            A1 = 2 * r1 * a - a
            C1 = 2 * r2

            r1 = np.random.random((n, dimension))
            r2 = np.random.random((n, dimension))
            A2 = 2 * r1 * a - a
            C2 = 2 * r2

            r1 = np.random.random((n, dimension))
            r2 = np.random.random((n, dimension))
            A3 = 2 * r1 * a - a
            C3 = 2 * r2

            Dalpha = abs(C1 * alpha - self.__agents)
            Dbeta = abs(C2 * beta - self.__agents)
            Ddelta = abs(C3 * delta - self.__agents)

            X1 = alpha - A1 * Dalpha
            X2 = beta - A2 * Dbeta
            X3 = delta - A3 * Ddelta

            self.__agents = (X1 + X2 + X3) / 3

            self.__agents = np.clip(self.__agents, lb, ub)
            self._points(self.__agents)

            alpha, beta, delta = self.__get_abd(n, function)
            if function(alpha) < function(Gbest):
                Gbest = alpha

        self._set_Gbest(Gbest)
        alpha, beta, delta = self.__get_abd(n, function)
        self.__leaders = list(alpha), list(beta), list(delta)

    def __get_abd(self, n, function):

        result = []
        fitness = [(function(self.__agents[i]), i) for i in range(n)]
        fitness.sort()

        for i in range(3):
            result.append(self.__agents[fitness[i][1]])

        return result

    def get_leaders(self):
        """Return alpha, beta, delta leaders of grey wolfs"""

        return list(self.__leaders)
