from math import ceil, exp, floor
import numpy as np
from random import random

from . import intelligence


class ssa(intelligence.sw):
    """
    Social Spider Optimization
    """

    def __init__(self, n, function, lb, ub, dimension, iteration, pf=0.4):
        """
        :param n: number of agents
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: the number of iterations
        :param pf: random parameter from 0 to 1 (default value is 0.4)
        """

        super(ssa, self).__init__()

        self.__agents = np.random.uniform(lb, ub, (n, dimension))

        nf = floor((0.9 - random() * 0.25) * n)
        nm = n - nf

        Nf = self.__agents[:nf]
        Nm = self.__agents[nf:]

        r = (ub - lb) / 2

        pb = np.array([function(x) for x in self.__agents]).argmin()
        pw = np.array([function(x) for x in self.__agents]).argmax()
        Pbest = self.__agents[pb]
        Pworst = self.__agents[pw]
        Gbest = Pbest

        for t in range(iteration):

            W = (np.array([function(i) for i in self.__agents]) -
                 function(Pworst)) / (function(Pbest) - function(Pworst))
            Wf = W[:nf]
            Wm = W[nf:]

            Distf = [self.__nearest_spider(i, Nf) for i in Nm]
            Vibrf = np.array([W[i[1]] * exp(-i[0]**2) for i in Distf])

            Distb = [np.linalg.norm(i - Pbest) for i in self.__agents]
            Vibrb = np.array([W[pb] * exp(-i**2) for i in Distb])

            Distc = [[(np.linalg.norm(self.__agents[i] - self.__agents[j]), j)
                     for j in range(n)] for i in range(n)]
            for i in range(len(Distc)):
                Distc[i].sort()
            Vibrc = []
            for i in range(n):
                for j in range(1, n):
                    dist = Distc[i][j][0]
                    k = Distc[i][j][1]
                    if W[k] < W[i]:
                        Vibrc.append(W[k] * exp(-dist**2))
                        break
                else:
                    Vibrc.append(W[i])
            Vibrc = np.array(Vibrc)

            fitness = [(function(Nm[i]), i) for i in range(nm)]
            fitness.sort()
            cent_male = Nm[fitness[ceil(nm/2)][1]]
            a = sum([Nm[j] * Wm[j] for j in range(nm)]) / sum([Wm[j] for j
                                                               in range(nm)])
            for i in range(n):

                alpha = np.random.random((1, dimension))[0]
                betta = np.random.random((1, dimension))[0]
                gamma = np.random.random((1, dimension))[0]

                r1 = np.random.random((1, dimension))[0]
                r2 = np.random.random((1, dimension))[0]
                r3 = np.random.random((1, dimension))[0]

                if i < nf:
                    if random() < pf:
                        k = Distc[i][1][1]
                        self.__agents[i] += alpha * Vibrc[i] * \
                            (self.__agents[k] - self.__agents[i]) + betta * \
                                Vibrb[i] * (Pbest - self.__agents[i]) + \
                                            gamma * (r1 - 0.5)
                    else:
                        k = Distc[i][1][1]
                        self.__agents[i] -= alpha * Vibrc[i] * \
                            (self.__agents[k] - self.__agents[i]) - betta * \
                                Vibrb[i] * (Pbest - self.__agents[i]) + \
                                            gamma * (r2 - 0.5)
                else:
                    if function(cent_male) > function(self.__agents[i]):
                        m = i - nf - 1
                        k = Distf[m][1]
                        self.__agents[i] += alpha * Vibrf[m] * \
                            (self.__agents[k] - self.__agents[i]) +\
                                            gamma * (r3 - 0.5)
                    else:
                        self.__agents[i] += alpha * (a - self.__agents[i])

            Nf = self.__agents[:nf]
            Nm = self.__agents[nf:]

            best = Nm[np.array([function(x) for x in Nm]).argmin()]
            indexes = [i for i in range(nf)
                       if np.linalg.norm(Nf[i] - best) <= r]
            nearest = [Nf[i] for i in indexes]
            L = len(nearest)

            if L:
                P = [Wf[i] / sum([Wf[i] for i in indexes]) for i in indexes]
                new_spiders = best + sum([P[i] * nearest[i] for i in range(L)])
                if function(new_spiders) < function(Pworst):
                    self.__agents[pw] = new_spiders

            self.__agents = np.clip(self.__agents, lb, ub)
            self._points(self.__agents)

            pb = np.array([function(x) for x in self.__agents]).argmin()
            pw = np.array([function(x) for x in self.__agents]).argmax()
            Pbest = self.__agents[pb]
            Pworst = self.__agents[pw]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

        self._set_Gbest(Gbest)

    def __nearest_spider(self, spider, spiders):

        spudis = list(spiders)

        try:
            pos = spudis.index(spider)
            spudis.pop(pos)
        except ValueError:
            pass

        dists = np.array([np.linalg.norm(spider - s) for s in spudis])
        m = dists.argmin()
        d = dists[m]

        return d, m
