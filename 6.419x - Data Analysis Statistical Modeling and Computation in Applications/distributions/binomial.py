from scipy.special import comb

class Binomial:

    def __init__(self, p: float, n: int, k: int):
        """
        Initialize Binomial distribution.

        Args:
            p (float): probability of success
            n (int): number of trials
            k (int): number of successes

        Raises:
            ValueError: If p is not between 0 and 1
            ValueError: If n is negative
            ValueError: If k is negative or greater than n
        """
        if not 0 <= p <= 1:
            raise ValueError("Probability has to be between 0 and 1")
        if n < 0:
            raise ValueError("Number of trials must be non-negative")
        if k < 0 or k > n:
            raise ValueError("Number of successes must be between 0 and n")
        self.p = p
        self.n = n
        self.k = k

    def pmf(self):
        """
        Calculate the Probability Mass Function for the Binomial distribution.

        Returns:
            float: The probability of exactly k successes in n trials
        """
        return comb(self.n, self.k)*(self.p**self.k)*(1-self.p)**(self.n-self.k)

    def mean(self) -> float:
        return self.n * self.p

    def variance(self) -> float:
        return self.n * self.p * (1 - self.p)