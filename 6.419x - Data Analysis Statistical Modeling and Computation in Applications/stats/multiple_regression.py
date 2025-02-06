import numpy as np
from typing import Union, List, Optional
from .data import StatisticalData

class MultipleRegression:
    """
    Multiple linear regression using matrix operations.
    Y = Xβ + ε, where:
    - Y is the target variable (nx1)
    - X is the design matrix (nxp) including column of 1s for intercept
    - β is the coefficient vector (px1)
    - ε is the error term (nx1)
    """

    # at the end of the day it's still just x and y
    def __init__(self, x: Union[List[List], np.ndarray], y: Union[List, np.ndarray]):
        """
        Initialize multiple regression with predictors (x) and target (y).

        Args:
            x: predictor variables (features)
            y: target variable (response)
        """
        self._x = np.array(x)
        self._y = np.array(y)
        self._coefficients = None
        self._r_squared = None

        ones_column = np.ones(len(self._x))

        # Add ones column to X
        self._x_with_intercept = np.column_stack([ones_column, self._x])

    def least_squares_estimator(self) -> np.ndarray:
        """
        Fit the model using ordinary least squares: β = (X'X)⁻¹X'y
        """
        if self._coefficients is None:
            x = self._x_with_intercept
            y = self._y

            xt = np.transpose(x)
            xtx = xt @ x
            xtx_inverse = np.linalg.inv(xtx)
            almost = xtx_inverse @ xt
            self._coefficients = almost @ y

        return self._coefficients

    def prediction(self) -> np.ndarray:
        return self._x_with_intercept @ self.least_squares_estimator()

    def standard_errors(self) -> np.ndarray:
        """
        Calculate standard errors for all coefficients.

        Returns:
            Array of standard errors, where index 0 is intercept
        """
        # Get residuals
        residuals = self._y - self.prediction()

        # Estimate σ²
        n = len(self._y)
        p = self._x_with_intercept.shape[1]
        sigma_squared = np.sum(residuals**2) / (n - p)

        # Get diagonal elements of (X'X)⁻¹
        x = self._x_with_intercept
        xtx_inverse = np.linalg.inv(x.T @ x)
        sigma_jj = np.diag(xtx_inverse)

        # Calculate and print standard errors with labels
        standard_errors = np.sqrt(sigma_squared * sigma_jj)
        labels = ['Intercept'] + [f'X{i}' for i in range(1, p)]

        print("\nStandard Errors:")
        print("-" * 20)
        for label, se in zip(labels, standard_errors):
            print(f"{label:12}: {se:.4f}")

        return standard_errors
