"""
Exoplanet Analysis using Multiple Linear Regression
------------------------------------------------

This script analyzes the relationships between various exoplanet characteristics
using multiple linear regression. The goal is to understand how different
planetary and stellar properties correlate with a planet's mass.

Features analyzed:
- Planet radius
- Orbital period
- Star metallicity
- Star mass
- Star age

All continuous variables are log-transformed to handle non-linear relationships
and different scales of measurement.

"""

import numpy as np
from stats.descriptive import Descriptive
from stats.regression import Regression
from stats.multiple_regression import MultipleRegression
import matplotlib.pyplot as plt

# Load and prepare the data
# ------------------------
# All continuous variables are log-transformed to linearize relationships

# Target variable: Planet mass (log scale)
LogPlanetMass = np.array([-0.31471074,  1.01160091,  0.58778666,  0.46373402, -0.01005034,
         0.66577598, -1.30933332, -0.37106368, -0.40047757, -0.27443685,
         1.30833282, -0.46840491, -1.91054301,  0.16551444,  0.78845736,
        -2.43041846,  0.21511138,  2.29253476, -2.05330607, -0.43078292,
        -4.98204784, -0.48776035, -1.69298258, -0.08664781, -2.28278247,
         3.30431931, -3.27016912,  1.14644962, -3.10109279, -0.61248928])

# Predictor variables
LogPlanetRadius = np.array([ 0.32497786,  0.34712953,  0.14842001,  0.45742485,  0.1889661 ,
         0.06952606,  0.07696104,  0.3220835 ,  0.42918163, -0.05762911,
         0.40546511,  0.19227189, -0.16251893,  0.45107562,  0.3825376 ,
        -0.82098055,  0.10436002,  0.0295588 , -1.17921515,  0.55961579,
        -2.49253568,  0.11243543, -0.72037861,  0.36464311, -0.46203546,
         0.13976194, -2.70306266,  0.12221763, -2.41374014,  0.35627486])

LogPlanetOrbit = np.array([-2.63108916, -3.89026151, -3.13752628, -2.99633245, -3.12356565,
        -2.33924908, -2.8507665 , -3.04765735, -2.84043939, -3.19004544,
        -3.14655516, -3.13729584, -3.09887303, -3.09004295, -3.16296819,
        -2.3227878 , -3.77661837, -2.52572864, -4.13641734, -3.05018846,
        -2.40141145, -3.14795149, -0.40361682, -3.2148838 , -2.74575207,
        -3.70014265, -1.98923527, -3.35440922, -1.96897409, -2.99773428])

StarMetallicity = np.array([ 0.11 , -0.002, -0.4  ,  0.01 ,  0.15 ,  0.22 , -0.01 ,  0.02 ,
        -0.06 , -0.127,  0.   ,  0.12 ,  0.27 ,  0.09 , -0.077,  0.3  ,
         0.14 , -0.07 ,  0.19 , -0.02 ,  0.12 ,  0.251,  0.07 ,  0.16 ,
         0.19 ,  0.052, -0.32 ,  0.258,  0.02 , -0.17 ])

LogStarMass = np.array([ 0.27002714,  0.19144646, -0.16369609,  0.44468582,  0.19227189,
         0.01291623,  0.0861777 ,  0.1380213 ,  0.49469624, -0.43850496,
         0.54232429,  0.02469261,  0.07325046,  0.42133846,  0.2592826 ,
        -0.09431068, -0.24846136, -0.12783337, -0.07364654,  0.26159474,
         0.07603469, -0.07796154,  0.09440068,  0.07510747,  0.17395331,
         0.28893129, -0.21940057,  0.02566775, -0.09211529,  0.16551444])

LogStarAge = np.array([ 1.58103844,  1.06471074,  2.39789527,  0.72754861,  0.55675456,
         1.91692261,  1.64865863,  1.38629436,  0.77472717,  1.36097655,
         0.        ,  1.80828877,  1.7837273 ,  0.64185389,  0.69813472,
         2.39789527, -0.35667494,  1.79175947,  1.90210753,  1.39624469,
         1.84054963,  2.19722458,  1.89761986,  1.84054963,  0.74193734,
         0.55961579,  1.79175947,  0.91629073,  2.17475172,  1.36097655])

# Prepare data for multiple regression
# ----------------------------------
n_samples = 30
feature_names = ['Intercept', 'Planet Radius', 'Orbital Period',
                'Star Metallicity', 'Star Mass', 'Star Age']

x = np.column_stack([LogPlanetRadius, LogPlanetOrbit, StarMetallicity,
                    LogStarMass, LogStarAge])
y = LogPlanetMass

# Fit multiple regression model
model = MultipleRegression(x, y)
coefficients = model.least_squares_estimator()
errors = model.standard_errors()


# Print results with interpretation
feature_names = ['Intercept', 'LogPlanetRadius', 'LogPlanetOrbit',
                'StarMetallicity', 'LogStarMass', 'LogStarAge']

print("\nMultiple Regression Results:")
print("-" * 70)
print(f"{'Variable':15} {'Coefficient':>10} {'Std Error':>10} {'t-value':>10} {'Reject H₀':>10}")
print("-" * 70)

for name, coef, err in zip(feature_names, coefficients, errors):
    t_value = coef / err
    reject_null = 'Yes' if abs(t_value) > 2 else 'No'
    print(f"{name:15} {coef:10.4f} {err:10.4f} {t_value:10.4f} {reject_null:>10}")

print("-" * 70)
print("Reject H₀: Evidence suggests this variable has a real relationship with planet mass")
print("(at 5% significance level)")

# Visualize results
# ----------------
# Create a bar plot of coefficient magnitudes to show relative importance
# plt.figure(figsize=(10, 6))
# plt.bar(feature_names[1:], np.abs(coefficients[1:]))
# plt.title('Relative Importance of Features in Predicting Planet Mass')
# plt.xticks(rotation=45)
# plt.ylabel('|Coefficient Magnitude|')
# plt.tight_layout()
# plt.show()