import numpy as np
from typing import Union, List, Optional
from .data import StatisticalData

class Descriptive:
    """Class for univariate descriptive statistics."""

    def __init__(self, data: Union[List, np.ndarray]):
        """
        Initialize statistical calculations with data.

        Args:
            data: Input data as list or numpy array
        """
        self._statistical_data = StatisticalData(data)
        self._mean: Optional[float] = None
        self._std: Optional[float] = None

    @property
    def data(self) -> np.ndarray:
        return self._statistical_data.data

    def mean(self) -> float:
        """Calculate and cache mean of the data."""
        if self._mean is None:
            self._mean = np.mean(self.data)
        return self._mean

    def std(self) -> float:
        """Calculate and cache sample standard deviation."""
        if self._std is None:
            self._std = np.std(self.data, ddof=1)
        return self._std

    def covariance_with(self, other: 'Descriptive') -> float:
        """
        Calculate covariance between this dataset and another.

        Args:
            other: Another Descriptive object to calculate covariance with
        """
        if len(self.data) != len(other.data):
            raise ValueError("Both arrays need to be of same length")

        return np.sum((self.data - self.mean()) * (other.data - other.mean())) / (len(self.data) - 1)

    def maximum_covariance_with(self, other: 'Descriptive') -> float:
        # maximum covariance occurs when this dataset is perfectly correlated with the other dataset
        return self.std() * other.std()

    def minimum_covariance_with(self, other: 'Descriptive') -> float:
        return -self.std() * other.std()

    def correlation_with(self, other: 'Descriptive') -> float:
        """
        Calculate correlation between this dataset and another
        """
        correlation = self.covariance_with(other) / (self.std() * other.std())
        return correlation

    def correlation_coefficient_with(self, other: 'Descriptive') -> float:
        # between -1 and 1. The covariance is scaled by it's maximum value
        return self.covariance_with(other) / self.maximum_covariance_with(other)