import numpy as np
from scipy.special import comb

class Hypergeometric:

    """
    Class for the discrete hypergeometric distribution
    """

    def __init__(self, n: int, k: int, t: int ):
        """
        n: size of population
        k: size of sub-population of interest
        t: the number of targeted outcomes
        """
        if n <= 0:
            raise ValueError("the size of the population, n, must be positive and non-zero")
        if k <= 0:
            raise ValueError("The size of the sub-population of interest, k, must be positive and non-zero.")
        if t < 0:
            raise ValueError("The number of targeted outcomes can't be a negative value")

        self.n = n
        self.k = k
        self.t = t

        def pmf(self) -> float:
            pass


