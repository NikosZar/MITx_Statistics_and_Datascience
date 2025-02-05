import numpy as np
from typing import Union, List

class StatisticalData:
    """
    Base class for handling statistical data arrays.
    Provides core data management and validation.
    """
    def __init__(self, data: Union[List, np.ndarray]):
        self._data = np.array(data) if not isinstance(data, np.ndarray) else data
        if len(self._data) == 0:
            raise ValueError("Empty data provided")

    @property
    def data(self) -> np.ndarray:
        """Get the data array (read-only)."""
        return self._data

    def __len__(self) -> int:
        return len(self._data)

class BivariateSample:
    """
    Class to handle paired statistical data (x,y coordinates).
    """
    def __init__(self, x: Union[List, np.ndarray], y: Union[List, np.ndarray]):
        self.x = StatisticalData(x)
        self.y = StatisticalData(y)

        if len(self.x) != len(self.y):
            raise ValueError("x and y must have the same length")
