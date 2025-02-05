import numpy as np
from typing import Union, List, Optional
from .data import BivariateSample
from .descriptive import Descriptive

class Regression:
    """
    A class for performing linear regression analysis
    """

    def __init__(self, x: Union[List, np.ndarray], y: Union[List, np.ndarray]):
        """
        Initialie regression with predictor(x) and response (y)

        x: Independent variable data
        y: depdendent variable data
        """

        self._bivariate_data = BivariateSample(x, y)
        self._slope: Optional[float] = None
        self._intercept: Optional[float] = None
        self._r_quared: Optional[float] = None

        @property
        def x(self) -> np.ndarray:
            return self._bivariate_data.x.data

        @property
        def y(self) -> np.ndarray:
            return self._bivariate_data.y.data

    def slope(self) -> float:
        """
        slope between x and y.
        """
        if self._slope is None:
            x_stats = Descriptive(self._bivariate_data.x.data)
            y_stats = Descriptive(self._bivariate_data.y.data)

            correlation = x_stats.correlation_coefficient_with(y_stats)
            self._slope = correlation * (y_stats.std() / x_stats.std())

        return self._slope

    def intercept(self) -> float:
        # y_mean - slope*x_mean
        if self._intercept is None:
            x_stats = Descriptive(self._bivariate_data.x.data)
            y_stats = Descriptive(self._bivariate_data.y.data)

            x_mean = x_stats.mean()
            y_mean = y_stats.mean()

            self._intercept = y_mean - (self.slope() * x_mean)

        return self._intercept

    def r_squared(self) -> float:
        """
        Calculate and cache the coefficient of determination (R²).

        In simple linear regression, R² equals the square of
        the correlation coefficient.

        Returns:
            float: R² value between 0 and 1
        """
        if self._r_squared is None:
            x_stats = Descriptive(self._bivariate_data.x.data)
            y_stats = Descriptive(self._bivariate_data.y.data)

            correlation = x_stats.correlation_coefficient_with(y_stats)
            self._r_squared = correlation ** 2

        return self._r_squared