# Exoplanet Mass Prediction: Multiple Regression Analysis and Feature Selection

## Overview
This analysis explores the relationships between various exoplanet characteristics and planetary mass using multiple linear regression. The goal is to identify which features are most predictive of an exoplanet's mass and develop a robust statistical model.

## Methodology

### Data Preparation
The analysis uses a dataset of 30 exoplanets with the following features:
- Planet radius (log-transformed)
- Orbital period (log-transformed)
- Star metallicity
- Star mass (log-transformed)
- Star age (log-transformed)

Log transformations were applied to handle non-linear relationships and different scales of measurement, helping to satisfy the linear regression assumptions.

### Multiple Linear Regression Model
The model takes the form:

Y = Xβ + ε

Where:
- Y is the log-transformed planet mass (nx1 vector)
- X is the design matrix (nx6 matrix, including intercept)
- β is the coefficient vector (6x1)
- ε is the error term (nx1)

### Statistical Testing Framework

#### Full Rank Requirement
The design matrix X must be full rank to ensure (X'X) is invertible, allowing us to compute β = (X'X)⁻¹X'Y. This requirement was verified before proceeding with the analysis.

#### Hypothesis Testing Using t-statistics
For each coefficient βᵢ, we test:
- H₀: βᵢ = 0 (feature has no effect)
- H₁: βᵢ ≠ 0 (feature has significant effect)

The t-statistic for each coefficient is:
t = βᵢ / SE(βᵢ)

Where SE(βᵢ) is calculated as:
SE(βᵢ) = √[σ²(X'X)⁻¹ᵢᵢ]

Using a 5% significance level (α = 0.05) and n-p degrees of freedom, we reject H₀ when |t| > 2 (approximate critical value).

## Results and Interpretation

The analysis revealed the following t-statistics and significance:
| Feature          | Coefficient | Std Error | t-value | Reject Null |
|-----------------|------------|-----------|---------|-------------|
| Intercept        | 0.1538     | 1.3890    | 0.1107  | No         |
| Planet Radius    | 1.4021     | 0.2865    | 4.8946  | Yes         |
| Orbital Period   | -0.1410    | 0.3598    | -0.3919 | No          |
| Star Metallicity | -1.5995    | 1.2506    | -1.2790 | No          |
| Star Mass        | -0.9561    | 1.1169    | -0.8560 | No          |
| Star Age        | -0.4618    | 0.3716    | -1.2428 | No          |
Reject H₀: Evidence suggests this variable has a real relationship with planet mass
(at 5% significance level)

### Key Findings:

1. **Strong Predictors** (|t| > 2):
   - Planet Radius (strongest relationship)

2. **Weak Predictors** (|t| < 2):
   - Star Metallicity
   - Star Age
   - Intercept
   - Orbital Period
   - Star Mass


### Feature Selection Implications
Based on the t-tests, we can confidently:
1. Retain Planet Radius as the only statistically significant predictor (t = 4.89)
2. Remove Intercept first

## Conclusions
The analysis revealed that Planet Radius is the only statistically significant predictor of exoplanet mass in our dataset. With a t-value of 4.89, it shows a strong positive relationship with planet mass, while all other variables failed to demonstrate statistical significance at the 5% level.

This finding suggests that a simpler model using only Planet Radius as a predictor might be more appropriate than the full model. The lack of significance in other variables indicates they may not provide meaningful additional predictive power, despite their theoretical importance in planetary science.

This approach demonstrates the value of hypothesis testing in feature selection, helping us distinguish between truly important predictors and those that may only add noise to our model. However, before completely discarding the non-significant variables, it would be prudent to consider whether the sample size (n=30) provides adequate power to detect smaller but potentially meaningful effects.