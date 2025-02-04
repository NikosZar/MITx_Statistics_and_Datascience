import math

class Poisson:

    def __init__(self, n: int, p: float, lambda_param: float = None) -> None:
        """
        Args:
            n: Number of trials
            p: probability of success
        """
        if not 0 <= p <= 1:
            raise ValueError("p must be between 0 and 1")
        if n < 0:
            raise ValueError("n must be non-negative")

        self.n = n
        self.p = p
        self.lambda_param = lambda_param if lambda_param is not None else n * p

        if self.lambda_param < 0:
            raise ValueError("lambda_param must be non-negative")

    def mean(self):
        return self.lambda_param

    def variance(self):
        return self.lambda_param

    def pmf(self, k: int) -> float:
        if k < 0:
            return 0

        return (math.pow(self.lambda_param, k) *
            math.exp(-self.lambda_param) /
            math.factorial(k))