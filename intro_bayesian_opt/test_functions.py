"""Test functions for optimization problems. 
A more complete set of functions can be found in this website:
http://infinity77.net/global_optimization/test_functions_1d.html
"""

import math


class Problem05:
    def __init__(self):
        self.bounds = (0, 1.2)

    def __call__(self, x: float) -> float:
        f = (1.4 - 3 * x) * math.sin(18 * x)
        return f


class Problem07:
    def __init__(self):
        self.bounds = (2.7, 7.5)

    def __call__(self, x: float) -> float:
        f = -(math.sin(x) + math.sin(x * (10 / 3)) + math.log(x) - 0.84 * x + 3)
        return f


class Problem09:
    def __init__(self):
        self.bounds = (3.1, 20.4)

    def __call__(self, x: float):
        f = -(math.sin(x) + math.sin(x * (2 / 3)))
        return f


class EggCreate:
    def __init__(self):
        self.bounds = ((-5, -5), (5, 5))

    def __call__(self, x: float, y: float):
        f = -(x ** 2 + y ** 2 + 25 * (math.sin(x) ** 2 + math.sin(y) ** 2))
        return f


class Ursem01:
    def __init__(self):
        self.bounds = ((-2.5, -2), (3, 2))

    def __call__(self, x: float, y: float):
        f = -(-math.sin(2 * x - 0.5 * math.pi) - 3.0 * math.cos(y) - 0.5 * x)
        return f
