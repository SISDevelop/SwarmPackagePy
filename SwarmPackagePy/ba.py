from math import exp
import numpy as np
from random import random

from . import intelligence


class ba(intelligence.sw):
    """
    Bat Algorithm
    """

    def __init__(self, n, function, lb, ub, dimension, iteration, r0=0.9,
                 V0=0.5, fmin=0, fmax=0.02, alpha=0.9, csi=0.9):
        """
        :param n: number of agents
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: number of iterations
        :param r0: level of impulse emission (default value is 0.9)
        :param V0: volume of sound (default value is 0.5)
        :param fmin: min wave frequency (default value is 0)
        :param fmax: max wave frequency (default value is 0.02)
            fmin = 0 and fmax =0.02 - the bests values
        :param alpha: constant for change a volume of sound
         (default value is 0.9)
        :param csi: constant for change a level of impulse emission
         (default value is 0.9)
        """

        super(ba, self).__init__()

        r = [r0 for i in range(n)]

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        self._points(self.__agents)

        velocity = np.zeros((n, dimension))
        V = [V0 for i in range(n)]

        Pbest = self.__agents[np.array([function(i)
                                        for i in self.__agents]).argmin()]
        Gbest = Pbest

        f = fmin + (fmin - fmax)

        for t in range(iteration):

            sol = self.__agents

            F = f * np.random.random((n, dimension))
            velocity += (self.__agents - Gbest) * F
            sol += velocity

            for i in range(n):
                if random() > r[i]:
                    sol[i] = Gbest + np.random.uniform(-1, 1, (
                        1, dimension)) * sum(V) / n

            for i in range(n):
                if function(sol[i]) < function(self.__agents[i]) \
                        and random() < V[i]:
                    self.__agents[i] = sol[i]
                    V[i] *= alpha
                    r[i] *= (1 - exp(-csi * t))

            self.__agents = np.clip(self.__agents, lb, ub)
            self._points(self.__agents)

            Pbest = self.__agents[
                np.array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

        self._set_Gbest(Gbest)
