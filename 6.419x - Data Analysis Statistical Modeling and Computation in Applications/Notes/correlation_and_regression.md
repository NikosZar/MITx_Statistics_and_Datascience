# Understanding Correlation Between X and X²

## Basic Relationship
The relationship Y = X² is deterministic - for any value of X, we know exactly what Y will be. This creates a parabola when plotted, with some interesting properties:

- Perfect U-shape curve
- Symmetric around the Y-axis
- Always non-negative (Y ≥ 0)
- Minimum value at X = 0

## Why Correlation Can Be Zero
When X follows a symmetric distribution (like Normal distribution):

### For Negative X Values:
- As X becomes more negative
- Y becomes larger
- Creates negative contribution to correlation

### For Positive X Values:
- As X becomes more positive
- Y becomes larger
- Creates positive contribution to correlation

### Net Effect:
- Negative and positive contributions cancel out
- Results in correlation near zero
- Despite perfect deterministic relationship!

## When Correlation Is Positive
If we only consider X > 0:
- We only see "half" the parabola
- As X increases, Y always increases
- Creates consistent positive relationship
- Results in positive correlation

## Key Insights

### 1. Correlation ≠ Relationship
- Zero correlation doesn't mean no relationship
- Variables can be perfectly related but uncorrelated

### 2. Linearity Matters
- Correlation only measures linear relationships
- Poor measure for curved relationships
- Can miss important patterns

### 3. Independence vs Correlation
- Uncorrelated doesn't mean independent
- X and X² are dependent but can be uncorrelated
- Perfect example of correlation's limitations

This example demonstrates why we must be careful when interpreting correlation coefficients, especially with non-linear relationships!

## Linear Regression Summary

Linear regression is a fundamental statistical method that models the relationship between a dependent variable (Y) and one or more independent variables (X) using a linear equation.

### Key Components
- Fits a straight line through data points
- Line equation: Y = β₀ + β₁X
  - β₀: Y-intercept (value of Y when X=0)
  - β₁: Slope (change in Y per unit change in X)

### Important Properties
1. **Least Squares Method**
   - Minimizes sum of squared residuals
   - Residuals are vertical distances from points to line
   - Produces "best fit" line through data

2. **Correlation's Role**
   - Slope β₁ is proportional to correlation coefficient
   - β₁ = r * (σy/σx), where:
     - r is correlation coefficient
     - σy, σx are standard deviations

### Critical Assumptions
1. **Linearity**
   - Relationship must be approximately linear
   - Most crucial assumption
   - Violation leads to misleading results

2. **Independence**
   - Observations should be independent
   - No systematic patterns in residuals

3. **Homoscedasticity**
   - Constant variance in residuals
   - Equal spread around regression line

### ⚠️ Cautions and Limitations

1. **Non-linear Relationships**
   - Linear regression can severely misrepresent non-linear patterns
   - Example: Using linear regression on Y = X² relationship
   - Can lead to poor predictions and incorrect conclusions

2. **Correlation Requirements**
   - High correlation doesn't guarantee good fit
   - Low correlation doesn't always mean no relationship
   - Always visualize data before regression

3. **Common Mistakes**
   - Forcing linear fit on curved relationships
   - Ignoring outliers
   - Extrapolating beyond data range

### Best Practices
1. Always plot data before regression
2. Check residual plots
3. Consider transformations for non-linear data
4. Use appropriate diagnostic tools
5. Consider non-linear models when appropriate

Remember: Linear regression is powerful but not universal. The method's simplicity makes it attractive, but its assumptions must be respected for valid results.

### Summary From Lecture
A regression line:
- interpolates conditional averages of y given x
- solves lease squares problem
- slope: r * (Sy/Sx)
- caution: linear relationship does not imply causaility
- caution: ecological correlations - correlations observed at group/aggregate level may not hold for individuals. For example, countries with higher average income may have lower life satisfaction, even though wealthier individuals tend to be more satisfied.
