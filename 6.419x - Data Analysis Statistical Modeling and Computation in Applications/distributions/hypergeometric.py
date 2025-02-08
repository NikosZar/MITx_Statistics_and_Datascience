import numpy as np
from scipy.special import comb, logsumexp, gammaln

class Hypergeometric:

    """
    Class for the discrete hypergeometric distribution.

    It is the result of an experiment in which a fixed number of trials are performed without replacement on a fixed population.
    There are two possible outcomes (success and failure), and the number of successes is counted.

    """

    def __init__(self, population_size: int, success_count: int, num_draws: int, x: int = None):
        """
        Initialize Hypergeometric distribution.

        Args:
            population_size (N): total size of population
            success_count (K): number of success states in population
            num_draws (n): number of items drawn
            x: value at which to calculate P(X=x), optional
        """
        # Validate inputs
        if population_size <= 0:
            raise ValueError("Population size must be positive")
        if success_count <= 0 or success_count > population_size:
            raise ValueError("Success count must be positive and not exceed population size")
        if num_draws < 0 or num_draws > population_size:
            raise ValueError("Number of draws must be between 0 and population size")
        if x is not None:
            if x < 0 or x > min(success_count, num_draws):
                raise ValueError("x must be between 0 and min(success_count, num_draws)")

        self.population_size = population_size
        self.success_count = success_count
        self.num_draws = num_draws
        self.x = x

    def pmf(self, x: int = None) -> float:
        """
        Calculate probability mass function P(X = x) using log-gamma for large numbers.

        Args:
            x: number of successes to calculate probability for

        Returns:
            float: P(X = x)
        """
        calc_x = x if x is not None else self.x
        if calc_x is None:
            raise ValueError("x must be provided either at initialization or in pmf call")

        # Check if x is in valid range
        if calc_x < max(0, self.num_draws - (self.population_size - self.success_count)) or \
           calc_x > min(self.success_count, self.num_draws):
            return 0.0

        # Use log-gamma for large number calculations
        try:
            log_pmf = (
                # log(C(success_count, x))
                gammaln(self.success_count + 1) - gammaln(calc_x + 1) - gammaln(self.success_count - calc_x + 1) +
                # log(C(population_size - success_count, num_draws - x))
                gammaln(self.population_size - self.success_count + 1) -
                gammaln(self.num_draws - calc_x + 1) -
                gammaln(self.population_size - self.success_count - (self.num_draws - calc_x) + 1) -
                # log(C(population_size, num_draws))
                (gammaln(self.population_size + 1) -
                 gammaln(self.num_draws + 1) -
                 gammaln(self.population_size - self.num_draws + 1))
            )
            return np.exp(log_pmf)
        except (OverflowError, ValueError):
            return 0.0

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

# example = Hypergeometric(62000, 31000, 102, 39)
# pmf = example.pmf(39)
# print(pmf)


