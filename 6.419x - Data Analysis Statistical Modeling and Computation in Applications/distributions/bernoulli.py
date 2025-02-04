class Bernoulli:
    """
    A class representing a Bernoulli Distribution.

    p = probability of success.
    1-p - probability of failure.

    Args:
    - pi_param may be used with poisson statistical models in this class?

    x = 0 or 1 represents the outcomes. Success of failure. if x = 1 then event occurs with probability p.

    Bernoulli pmf = px + (1-p)(1-x).
    Expectation = p
    Variance = p(1-p)

    events are independent and identically distributed (i.i.d)
    """

    def __init__(self, p: float, n: int, k: int, pi_param:int = None):
        # control for p
        if p < 0 or p > 1:
            raise ValueError("p must be between 0 and 1")
        if n<0:
            raise ValueError("n must be non-negative")
        if k < 0:
            raise ValueError("k must be non-negative")

        self.p = p
        self.n = n
        self.k = k

    def pmf(self, k: int) -> float:
        if k not in [0, 1]:
            raise ValueError("k must be 0 or 1 for Bernoulli Distribution")

        return self.p if k==1 else 1- self.p

    def mean(self) -> float:
        return self.pmf

    def variance(self) -> float:
        return self.p * (1 - self.p)