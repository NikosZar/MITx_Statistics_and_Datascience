import numpy as np
from typing import List, Union, Tuple
from .data import StatisticalData

class CovarianceMatrix:
    """Class for computing and analyzing sample covariance matrices."""

    def __init__(self, vectors: Union[List[np.ndarray], np.ndarray]):
        """
        Initialize with a list of column vectors or matrix of observations.

        Args:
            vectors: List of column vectors or matrix where each row is an observation
        """
        if isinstance(vectors, list):
            self.vectors = [StatisticalData(v).data for v in vectors]
        else:
            self.vectors = vectors

        self._covariance_matrix = None
        self._eigenvalues = None
        self._eigenvectors = None

    def compute(self) -> np.ndarray:
        """
        Calculate the sample covariance matrix.

        Returns:
            np.ndarray: Sample covariance matrix S
        """
        if self._covariance_matrix is None:
            n = len(self.vectors)

            # Calculate empirical mean
            X_bar = np.mean(self.vectors, axis=0)

            # Center the data
            centered_data = self.vectors - X_bar

            # Compute covariance matrix
            self._covariance_matrix = (centered_data.T @ centered_data) / (n - 1)

        return self._covariance_matrix

    def correlation_matrix(self) -> np.ndarray:
        """
        Compute the correlation matrix from the covariance matrix.

        Returns:
            np.ndarray: Correlation matrix
        """
        S = self.compute()
        D = np.diag(1 / np.sqrt(np.diag(S)))
        return D @ S @ D

    def eigendecomposition(self) -> Tuple[np.ndarray, np.ndarray]:
        """ Assuming a symmetric or Hermitian matrix """
        if self._eigenvalues is None or self._eigenvectors is None:
            s = self.compute()
            eigenvalues, eigenvectors = np.linalg.eigh(s)
            self._eigenvalues = eigenvalues
            self._eigenvectors = eigenvectors

        return self._eigenvalues, self._eigenvectors