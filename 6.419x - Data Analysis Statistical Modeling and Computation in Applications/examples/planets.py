import numpy as np
from stats.descriptive import Descriptive
from stats.regression import Regression
import matplotlib.pyplot as plt

# Original data
x_array = np.array([0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5]) #semi-major axis of each planet's orbit around the Sun (AU)/
y_array = np.array([0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248]) #orbital period of the planet measured in Earth years.
n = len(x_array)

x_stats = Descriptive(x_array)
y_stats = Descriptive(y_array)

correlation_coefficient = x_stats.correlation_coefficient_with(y_stats)
print(f"Correlation Coefficient: {correlation_coefficient}")

# import statsmodels.api as sm
# sm.qqplot(y_array, line='s')
# plt.title("Y distribution")
# plt.show()

# Transform X and Y to lnX and lnY
transformed_x = np.log(x_array)
transformed_y = np.log(y_array)

# Create Descriptive objects for transformed data
transformed_x_stats = Descriptive(transformed_x)
transformed_y_stats = Descriptive(transformed_y)

# Create regression with the transformed data arrays (not the Descriptive objects)
reg_stats = Regression(transformed_x, transformed_y)

# Print results
correlation = transformed_x_stats.correlation_coefficient_with(transformed_y_stats)
print(f"Correlation Coefficient: {correlation}")
print(f"Slope: {reg_stats.slope()}")
print(f"Intercept: {reg_stats.intercept()}")
