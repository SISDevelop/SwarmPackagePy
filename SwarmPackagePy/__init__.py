"""
SwarmPackagePy
==============


Provides:
    1. Swarm optimization algorithms.
    2. Test functions for swarm algorithms.
    3. Animation of algorithm computation.


To compute any algorithm you need to create an object like below
----------------------------------------------------------------

  >>> alh = SwarmPackagePy.alg(n, function, lb, ub, dimension, iteration)

Where:
    alg:        name of required algorithm
    n:          number of agents
    function:   test function (function must be an object, that accepts
                               coordinates of a point as init parameter)
    lb:         lower limits for plot axes
    ub:         upper limits for plot axes
    dimension:  space dimension
    iteration:  number of iterations

!Note: almost every algorithm has additional parameters. But they are all
have default value. To view additional parameters of any algorithm type:

  >>> help(SwarmPackagePy.alg)


Example of computation pso algorithm for 2 dimensions with easom function
-------------------------------------------------------------------------

  >>> function = SwarmPackagePy.testFunctions.easom_function
  >>> alh = SwarmPackagePy.pso(15, function, -10, 10, 2, 20)

To get the best position of an algorithm use "get_Gbest()" method:

  >>> alh.get_Gbest()

To watch animation for algorithm:

  >>> animation(alh.get_agents(), function, 10, -10, sr=False)


3D version
----------

    >>> function = SwarmPackagePy.testFunctions.easom_function
    >>> alh = SwarmPackagePy.pso(15, function, -10, 10, 3, 20)
    >>> animation3D(alh.get_agents(), function, 10, -10, sr=False)

Avaible test functions (in SwarmPackagePy.testFunctions)
--------------------------------------------------------

    ackley_function
    bukin_function
    cross_in_tray_function
    sphere_function
    bohachevsky_function
    sum_squares_function
    sum_of_different_powers_function
    booth_function
    matyas_function
    mccormick_function
    dixon_price_function
    six_hump_camel_function
    three_hump_camel_function
    easom_function
    michalewicz_function
    beale_function
    drop_wave_function
"""

from SwarmPackagePy.aba import aba
from SwarmPackagePy.ba import ba
from SwarmPackagePy.bfo import bfo
from SwarmPackagePy.chso import chso
from SwarmPackagePy.cso import cso
from SwarmPackagePy.fa import fa
from SwarmPackagePy.fwa import fwa
from SwarmPackagePy.gsa import gsa
from SwarmPackagePy.gwo import gwo
from SwarmPackagePy.pso import pso
from SwarmPackagePy.ca import ca
from SwarmPackagePy.hs import hs
from SwarmPackagePy.ssa import ssa
from SwarmPackagePy.wsa import wsa
from SwarmPackagePy.animation import animation, animation3D

_version_ = '1.0.0'
