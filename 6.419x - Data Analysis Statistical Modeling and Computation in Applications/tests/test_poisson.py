import unittest
import math
from distributions.poisson import Poisson  # Updated to match your structure

class TestPoisson(unittest.TestCase):
    def setUp(self):
        """Initialize test cases"""
        self.p1 = Poisson(n=1000, p=0.003)  # lambda = 3
        self.p2 = Poisson(n=1000, p=0.003, lambda_param=5)  # override lambda

    def test_initialization(self):
        """Test initialization and parameter calculation"""
        # Test normal initialization
        self.assertEqual(self.p1.lambda_param, 3)

        # Test lambda override
        self.assertEqual(self.p2.lambda_param, 5)

        # Test invalid parameters
        with self.assertRaises(ValueError):
            Poisson(n=-1, p=0.5)  # negative n
        with self.assertRaises(ValueError):
            Poisson(n=100, p=1.5)  # p > 1
        with self.assertRaises(ValueError):
            Poisson(n=100, p=0.5, lambda_param=-1)  # negative lambda

    def test_pmf(self):
        """Test PMF calculations"""
        p = Poisson(n=100, p=0.02)  # lambda = 2

        # Test known values
        self.assertAlmostEqual(p.pmf(0), math.exp(-2), places=10)
        self.assertAlmostEqual(p.pmf(1), 2 * math.exp(-2), places=10)

        # Test negative k
        self.assertEqual(p.pmf(-1), 0)

        # Sum of probabilities should be close to 1
        total_prob = sum(p.pmf(k) for k in range(20))  # Sum first 20 terms
        self.assertAlmostEqual(total_prob, 1, places=6)

    def test_mean_variance(self):
        """Test mean and variance calculations"""
        # For Poisson, mean = variance = lambda
        p = Poisson(n=1000, p=0.004)  # lambda = 4

        self.assertEqual(p.mean(), 4)
        self.assertEqual(p.variance(), 4)
        self.assertEqual(p.mean(), p.variance())

    def test_different_parameterizations(self):
        """Test different ways to get same lambda"""
        p1 = Poisson(n=1000, p=0.002)  # lambda = 2
        p2 = Poisson(n=2000, p=0.001)  # lambda = 2
        p3 = Poisson(n=100, p=0.02)    # lambda = 2

        # All should give same probabilities
        k = 3  # test for k=3 events
        self.assertAlmostEqual(p1.pmf(k), p2.pmf(k))
        self.assertAlmostEqual(p2.pmf(k), p3.pmf(k))

if __name__ == '__main__':
    unittest.main()