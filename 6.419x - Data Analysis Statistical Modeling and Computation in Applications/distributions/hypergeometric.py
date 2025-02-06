import numpy as np
from scipy.special import comb

class Hypergeometric:

    """
    Class for the discrete hypergeometric distribution.

    It is the result of an experiment in which a fixed number of trials are performed without replacement on a fixed population.
    There are two possible outcomes (success and failure), and the number of successes is counted.

    """

    def __init__(self, population_size: int, success_count: int, num_draws: int, x: int):
        """
        population_size (N): total size of population
        success_count (K): number of success states in population
        num_draws (n): number of items drawn
        x: value at which to calculate P(X=x)
        """
        if population_size <= 0:
            raise ValueError("the size of the population, population_size, must be positive and non-zero")
        if success_count <= 0:
            raise ValueError("The size of the sub-population of interest, success_count, must be positive and non-zero.")
        if num_draws < 0:
            raise ValueError("The number of targeted outcomes can't be a negative value")
        if x < 0:
            raise ValueError("The target value for P(x = x) myst be greater than 0")

        self.population_size = population_size
        self.success_count = success_count
        self.num_draws = num_draws
        self.x = x

    def pmf(self) -> float:
        return (comb(self.success_count, self.x) * comb(self.population_size - self.success_count, self.num_draws - self.x)) / comb(self.population_size, self.num_draws)

    def mean(self) -> float:
        """Calculate mean: n * (K/N)"""
        return self.num_draws * (self.success_count / self.population_size)

    def variance(self) -> float:
        """
        Calculate variance: n * (K/N) * ((N-K)/N) * ((N-n)/(N-1))

        Returns:
            float: variance of the hypergeometric distribution
        """
        n = self.num_draws
        N = self.population_size
        K = self.success_count

        # Breaking down the formula for clarity
        success_prob = K/N
        failure_prob = (N-K)/N
        correction = (N-n)/(N-1)

        return n * success_prob * failure_prob * correction


