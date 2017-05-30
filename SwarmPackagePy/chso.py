from math import ceil, exp
import numpy as np
from random import choice, shuffle
import warnings

from . import intelligence


warnings.filterwarnings("ignore")


class chso(intelligence.sw):
    """Chicken Swarm Optimization"""

    def __init__(self, n, function, lb, ub, dimension, iteration, G=5, FL=0.5):
        """
        :param n: number of agents
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: number of iterations
        :param G: after what time relationship will be upgraded (default
        value is 5)
        :param FL: parameter, which means that the chick would follow its
        mother to forage for food (0 < FL < 2. Default value is 0.5)
        """

        super(chso, self).__init__()

        rn = ceil(0.15 * n)
        hn = ceil(0.7 * n)
        cn = n - rn - hn
        mn = ceil(0.2 * n)

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        pbest = self.__agents
        self._points(self.__agents)

        fitness = [function(x) for x in self.__agents]
        pfit = fitness

        Pbest = self.__agents[np.array(fitness).argmin()]
        Gbest = Pbest

        for t in range(iteration):

            if t % G == 0:

                chickens = self.__update_relationship(n, function, rn, hn,
                                                      cn, mn)
                roosters, hines, chicks = chickens

            for i in roosters:

                k = choice(roosters)
                while k == i:
                    k = choice(roosters)

                if pfit[i] <= pfit[k]:
                    sigma = 1
                else:
                    sigma = exp((pfit[k] - pfit[i]) / (abs(pfit[i]) + 0.01))

                self.__agents[i] = pbest[i] * (1 + np.random.normal(0, sigma,
                                                                    dimension))

            for i in hines:

                r1 = i[1]
                r2 = choice([choice(roosters), choice(hines)[0]])
                while r2 == r1:
                    r2 = choice([choice(roosters), choice(hines)[0]])

                s1 = exp((pfit[i[0]] - pfit[r1]) / (abs(pfit[i[0]]) + 0.01))

                try:
                    s2 = exp(pfit[r2] - pfit[i[0]])
                except OverflowError:
                    s2 = float('inf')

                rand1 = np.random.random((1, dimension))[0]
                rand2 = np.random.random((1, dimension))[0]

                self.__agents[i[0]] = pbest[i[0]] + s1 * rand1 * (
                    pbest[r1] - pbest[i[0]]) + s2 * rand2 * (
                    pbest[r2] - pbest[i[0]])

            for i in chicks:
                self.__agents[i[0]] = pbest[i[0]] * FL * (pbest[i[1]] -
                                                          pbest[i[0]])

            self.__kill(n, function, lb, ub, dimension)

            self.__agents = np.clip(self.__agents, lb, ub)
            self._points(self.__agents)

            fitness = [function(x) for x in self.__agents]

            for i in range(n):
                if fitness[i] < pfit[i]:
                    pfit[i] = fitness[i]
                    pbest[i] = self.__agents[i]

            Pbest = self.__agents[np.array(fitness).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

        self._set_Gbest(Gbest)

    def __update_relationship(self, n, function, rn, hn, cn, mn):

        fitness = [(function(self.__agents[i]), i) for i in range(n)]
        fitness.sort()

        chickens = [i[1] for i in fitness]
        roosters = chickens[:rn]
        hines = chickens[rn:-cn]
        chicks = chickens[-cn:]

        shuffle(hines)
        mothers = hines[:mn]

        for i in range(cn):
            chicks[i] = chicks[i], choice(mothers)

        for i in range(hn):
            hines[i] = hines[i], choice(roosters)

        return roosters, hines, chicks

    def __kill(self, n, function, lb, ub, dimension):

        for i in range(n):

            fit = None

            try:
                fit = function(self.__agents[i])
            except OverflowError:
                for j in range(dimension):
                    self.__agents[i][j] = round(self.__agents[i][j])

            if str(fit) == 'nan':
                self.__agents[i] = np.random.uniform(lb, ub, (1, dimension))
