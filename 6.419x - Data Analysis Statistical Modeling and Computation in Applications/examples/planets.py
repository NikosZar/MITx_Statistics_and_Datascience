"""
EX 2
Kepler's Third Law of Planetary Motion - Data Analysis

This script demonstrates the relationship between a planet's orbital period
and its distance from the Sun (semi-major axis) using regression analysis.
Kepler's Third Law states that the square of the orbital period is directly
proportional to the cube of the semi-major axis (P² ∝ a³).

By taking the natural logarithm of both sides, we transform this nonlinear
relationship into a linear one that can be analyzed using simple linear regression.
"""

import numpy as np
from stats.descriptive import Descriptive
from stats.regression import Regression
import matplotlib.pyplot as plt

# Planetary orbital data
# Semi-major axis (AU) for each planet, from Mercury to Pluto
x_array = np.array([
    0.387,  # Mercury
    0.723,  # Venus
    1.00,   # Earth
    1.52,   # Mars
    5.20,   # Jupiter
    9.54,   # Saturn
    19.2,   # Uranus
    30.1,   # Neptune
    39.5    # Pluto (dwarf planet)
])

# Orbital period (Earth years) for each planet
y_array = np.array([
    0.241,  # Mercury
    0.615,  # Venus
    1.00,   # Earth
    1.88,   # Mars
    11.9,   # Jupiter
    29.5,   # Saturn
    84.0,   # Uranus
    165.0,  # Neptune
    248     # Pluto
])

# Initial analysis of untransformed data
x_stats = Descriptive(x_array)
y_stats = Descriptive(y_array)

# Calculate correlation coefficient for original data
correlation_coefficient = x_stats.correlation_coefficient_with(y_stats)
print("Original Data Analysis:")
print(f"Correlation Coefficient: {correlation_coefficient:.4f}")

# Data transformation for linear analysis
# Taking natural logarithm of both variables to linearize the relationship
transformed_x = np.log(x_array)  # ln(semi-major axis)
transformed_y = np.log(y_array)  # ln(orbital period)

# Analysis of transformed data
transformed_x_stats = Descriptive(transformed_x)
transformed_y_stats = Descriptive(transformed_y)

# Perform linear regression on transformed data
reg_stats = Regression(transformed_x, transformed_y)

# Calculate and display results
correlation = transformed_x_stats.correlation_coefficient_with(transformed_y_stats)
slope = reg_stats.slope()
intercept = reg_stats.intercept()

print("\nTransformed Data Analysis (Natural Log Scale):")
print(f"Correlation Coefficient: {correlation:.4f}")
print(f"Slope: {slope:.4f}")  # Should be close to 1.5 according to Kepler's Third Law
print(f"Intercept: {intercept:.4f}")

# Note: The slope being close to 1.5 confirms Kepler's Third Law,
# as ln(P) = 1.5*ln(a) + c is equivalent to P² ∝ a³
