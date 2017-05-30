import numpy as np

from . import intelligence


class wsa(intelligence.sw):
    """
    Whale Swarm Algorithm
    """

    def __init__(self, n, function, lb, ub, dimension, iteration, ro0=2,
                 eta=0.005):
        """
        :param n: number of agents
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: the number of iterations
        :param ro0: intensity of ultrasound at the origin of source
	(default value is 2)
        :param eta: probability of message distortion at large distances
	(default value is 0.005)
        """

        super(wsa, self).__init__()

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        self._points(self.__agents)

        Pbest = self.__agents[np.array([function(x)
                                        for x in self.__agents]).argmin()]
        Gbest = Pbest

        for t in range(iteration):
            new_agents = self.__agents
            for i in range(n):
                y = self.__better_and_nearest_whale(i, n, function)
                if y:
                    new_agents[i] += np.dot(
                        np.random.uniform(0, ro0 *
                            np.exp(-eta * self.__whale_dist(i, y))),
                        self.__agents[y] - self.__agents[i])
            self.__agents = new_agents
            self.__agents = np.clip(self.__agents, lb, ub)
            self._points(self.__agents)

            Pbest = self.__agents[np.array([function(x)
                                            for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

        self._set_Gbest(Gbest)

    def __whale_dist(self, i, j):
        return np.linalg.norm(self.__agents[i] - self.__agents[j])

    def __better_and_nearest_whale(self, u, n, function):
        temp = float("inf")

        v = None
        for i in range(n):
            if function(self.__agents[i]) < function(self.__agents[u]):
                dist_iu = self.__whale_dist(i, u)
                if dist_iu < temp:
                    v = i
                    temp = dist_iu
        return v
