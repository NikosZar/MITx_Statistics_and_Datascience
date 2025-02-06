# Parametric Models in Hypothesis Testing

A **parametric model** in hypothesis testing refers to a statistical model that assumes the data follows a specific probability distribution characterized by a finite set of parameters. These models rely on assumptions about the underlying population distribution, such as normality, and use those assumptions to make inferences about the data.

## Key Features of Parametric Models in Hypothesis Testing
1. **Assumption of a Known Distribution**
   - The data is assumed to follow a distribution like Normal, Binomial, Poisson, Exponential, etc.
   - The distribution is characterized by a few parameters (e.g., mean \( \mu \) and variance \( \sigma^2 \) in a normal distribution).

2. **Finite-Dimensional Parameter Space**
   - The hypothesis being tested is formulated in terms of a small number of parameters (e.g., testing whether the mean \( \mu \) of a normal distribution is equal to some value).

3. **More Statistical Power (When Assumptions Hold)**
   - Parametric tests tend to be more powerful than non-parametric tests if the assumptions about the distribution are correct.

## Examples of Parametric Hypothesis Tests
- **Z-test**: Tests hypotheses about the mean of a normally distributed population when the variance is known.
- **T-test**: Tests hypotheses about the mean of a normally distributed population when the variance is unknown.
- **ANOVA (Analysis of Variance)**: Tests differences in means across multiple groups under the assumption of normality.
- **Chi-square test**: Tests hypotheses about categorical data distributions, assuming expected frequencies.
- **F-test**: Compares variances of two or more populations.

## Comparison with Non-Parametric Models
- **Non-parametric models** do not assume a specific probability distribution and are used when distributional assumptions are questionable or unknown.
- Examples include the **Wilcoxon rank-sum test**, **Kruskal-Wallis test**, and **Mann-Whitney U test**.

## Example of a Parametric Hypothesis Test
Suppose we want to test whether the average height of a population is 170 cm. We assume height follows a **normal distribution** with unknown variance. The hypothesis can be formulated as:

- Null hypothesis (\( H_0 \)): \( \mu = 170 \)
- Alternative hypothesis (\( H_a \)): \( \mu \neq 170 \)

Using a **t-test**, we estimate the sample mean and standard deviation and compute a test statistic to determine if we have enough evidence to reject \( H_0 \).

## Conclusion
A parametric model in hypothesis testing is a model that assumes data follows a known probability distribution with parameters. These models allow for **efficient and powerful statistical inference** but require that assumptions about the data distribution hold true.