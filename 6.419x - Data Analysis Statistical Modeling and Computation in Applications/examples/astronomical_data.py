import numpy as np
from stats.descriptive import Descriptive

"""
The -axis is the apparent velocity, measured in kilometers per second.
Positive velocities are galaxies moving away from us, negative velocities are galaxies that are moving towards us.
The -axis is the distance of the galaxy from us, measured in mega-parsecs (Mpc)
"""

x_array = np.array([
    0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503,
    0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41,
    1.72, 2.03, 2.02, 2.02, 2.02
])

y_array = np.array([
    -19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 320.0,
    373.0, 93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 608.0, 1040.0,
    1100.0, 840.0, 801.0, 519.0
])

def calculate_sample_statistic(data):
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    return mean, std_dev

x_stats = Descriptive(x_array)
y_stats = Descriptive(y_array)

print(x_stats.maximum_covariance_with(y_stats))
print(x_stats.correlation_with(y_stats))

correlation_coefficient = x_stats.correlation_coefficient_with(y_stats)
print(f"Correlation Coefficient: {correlation_coefficient}")

slope = x_stats.slope_with(y_stats)
print(f"slope is {slope}")