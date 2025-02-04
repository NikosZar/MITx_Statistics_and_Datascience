# Population vs Sample Standard Deviation

## Formulas

### Population Standard Deviation (ddof=0)
The population standard deviation formula is:
σ = √(Σ(x - μ)² / N)

Where:
- σ (sigma) is the population standard deviation
- x is each value in the dataset
- μ (mu) is the population mean
- N is the total number of values

### Sample Standard Deviation (ddof=1)
The sample standard deviation formula is:
s = √(Σ(x - x̄)² / (N-1))

Where:
- s is the sample standard deviation
- x is each value in the dataset
- x̄ is the sample mean
- n is the sample size

## NumPy Implementation

In NumPy's `std()` function:

- `ddof=0` (default): Calculates population standard deviation, dividing by N
- `ddof=1`: Calculates sample standard deviation, dividing by N-1

The key difference is that sample standard deviation uses N-1 degrees of freedom (ddof=1) instead of N in the denominator. This is known as Bessel's correction and helps account for the fact that we're using a sample to estimate the population parameter.

Using N-1 makes the sample standard deviation a less biased estimator of the population standard deviation, especially for small sample sizes.
