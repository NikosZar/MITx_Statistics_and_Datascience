"""
EX 1
Hubble's Law - Galaxy Velocity vs Distance Analysis

This script analyzes the relationship between galaxy velocities and their distances
from Earth using real astronomical data. This demonstrates Hubble's Law, which shows
that galaxies further from Earth are moving away faster, indicating an expanding universe.

The data consists of:
- Distances measured in mega-parsecs (Mpc)
- Velocities measured in kilometers per second (km/s)
  - Positive values indicate galaxies moving away from Earth
  - Negative values indicate galaxies moving towards Earth

The slope of the regression line gives us the Hubble constant (H₀),
which represents the expansion rate of the universe.
"""

import numpy as np
from stats.descriptive import Descriptive
from stats.regression import Regression

# Galaxy distance data in mega-parsecs (Mpc)
x_array = np.array([
    0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503,
    0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41,
    1.72, 2.03, 2.02, 2.02, 2.02
])

# Galaxy velocity data in kilometers per second (km/s)
y_array = np.array([
    -19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 320.0,
    373.0, 93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 608.0, 1040.0,
    1100.0, 840.0, 801.0, 519.0
])

# Create statistical analysis objects
x_stats = Descriptive(x_array)
y_stats = Descriptive(y_array)

# Perform linear regression analysis
reg_stats = Regression(x_array, y_array)

# Calculate and display the Hubble constant (slope)
hubble_constant = reg_stats.slope()
print(f"Hubble constant (H₀): {hubble_constant:.2f} km/s/Mpc")

# Calculate and display the y-intercept
# In theory, this should be close to zero as galaxies at distance 0 should have velocity 0
intercept = reg_stats.intercept()
print(f"Y-intercept: {intercept:.2f} km/s")

# The R² value indicates how well the data fits the linear relationship
r_squared = reg_stats.r_squared()
print(f"R² value: {r_squared:.4f}")