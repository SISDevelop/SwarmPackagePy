#!/usr/bin/env python

import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
import pytest


def pytest_generate_tests(metafunc):
    fdata = [
        # function                          min value  dim      domain
        (tf.cross_in_tray_function,          -2.06261,   2, [-10,   10]),
        (tf.sphere_function,                        0,   2, [-5.12, 5.12]),
        (tf.bohachevsky_function,                   0,   2, [-10,   10]),
        (tf.sum_of_different_powers_function,       0,   2, [-1,    1]),
        (tf.booth_function,                         0,   2, [-10,   10]),
        (tf.matyas_function,                        0,   2, [-10,   10]),
        (tf.six_hump_camel_function,          -1.0316,   2, [-3,    3]),
        (tf.three_hump_camel_function,              0,   2, [-5,    5]),
        (tf.easom_function,                        -1,   2, [-30,   30]),
    ]
    algs = [
        # (algorithm, number of iterations, agents, additional parameters)
        (SwarmPackagePy.aba, 100,  60, []),
        (SwarmPackagePy.ba,  100,  60, []),
        (SwarmPackagePy.bfo, 100,  20, []),
        (SwarmPackagePy.ca,  500,  60, []),
        (SwarmPackagePy.cso, 50,  150, []),
        (SwarmPackagePy.chso, 150, 60, []),
        (SwarmPackagePy.fa,  50,   60, []),
        (SwarmPackagePy.fwa, 20,    3, []),
        (SwarmPackagePy.gsa, 100,  60, []),
        (SwarmPackagePy.gwo, 100,  60, []),
        (SwarmPackagePy.hs,  1500, 60, []),
        (SwarmPackagePy.pso, 50,   60, []),
        (SwarmPackagePy.ssa, 150,  60, []),
        (SwarmPackagePy.wsa, 45,   45, []),
    ]
    tdata = []
    for alg in algs:
        for f in fdata:
            tdata.append((*alg, *f))

    metafunc.parametrize(["alg", "iter", "agents", "params", "f", "val", "dim",
                          "dom"], tdata)


def test_alg(alg, agents, iter, params, f, val, dim, dom):
    alh = alg(agents, f, *dom, dim, iter, *params)
    # print(f(alh.get_Gbest()), val)
    assert abs(f(alh.get_Gbest()) - val) < 0.1
