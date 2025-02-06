A high-level summary of hypothesis testing is that it involves calculating the probability, under a given model, that an observation equal to or more extreme than what is observed in the treatment group is obtained, conditioned on the treatment having no effect.

Steps:
- Determine a model
- Determine a mutualy exclusive null hypothesis and alternative hypothesis
- Dtermine a test statistic (quantity that can differentiate between null and alternative hypothesis, and whose distribution under the null hypothesis you can compute).
- Determine a significance level. This is the error we are okay with making.

## On Null and Alternative Hypotheses

I was thinking today about how we frame scientific questions as competing hypotheses. It's like having two possibilities:

The null hypothesis (H₀) - this is our default position, representing what we currently believe or assume. When comparing treatments, we assume they have equal effects (μ₁ = μ₂). For relationships between variables, we start by assuming there aren't any (ρ = 0).

Then there's the alternative hypothesis (H₁) - what we think might actually be happening. Sometimes we specify a direction (μ₁ > μ₂), other times we just suspect there's some difference (μ₁ ≠ μ₂). In an intent-to-treat analysis think of the control group observations as becoming the parameter and corresponding values for a null hypothesis.

E.g offering mammography leads to a reduction in deaths caused by breast cancer. In the control group the rate of death = 0.01 and in the treatment group we observe a rate of death of 0.001. the value of 0.01 can be the value of the death rate in our null hypothesis.

We reject the null hypothesis if we deem it relatively unlikely for the null hypothesis to be true, given the observations.

We fail to reject the null hypothesis if we do not have sufficient evidence from the observation to discredit the null hypothesis.

## Reflections on Parametric Models

I've been working through how we model uncertainty mathematically. We use probability distributions with parameters θ to represent random processes. The density function f(x|θ) basically describes how we think the data is being generated.

The Normal distribution is probably the most widely used, with its formula:
$f(x|\mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

The Binomial distribution is great for counting successes in repeated trials:
$P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$

And the Poisson distribution works really well for rare events:
$P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$

## On Estimating the Unknown

There are two main approaches to figuring out parameters - Maximum Likelihood and Method of Moments. Maximum Likelihood tries to maximize:
$\ell(\theta|x) = \sum_{i=1}^n \log f(x_i|\theta)$

While Method of Moments uses the fact that sample means approximate population means: $\bar{X} = \mathbb{E}[X]$

## The Testing Framework

When we test hypotheses, we calculate test statistics that measure evidence against H₀:

The Z-statistic is straightforward: $Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}$
The t-statistic handles unknown variance better: $t = \frac{\bar{X} - \mu_0}{s/\sqrt{n}}$
The F-statistic compares different sources of variation: $F = \frac{MS_{between}}{MS_{within}}$

## On Model Selection

I've found these two metrics really useful when choosing between models:

AIC = -2ln(L) + 2k
BIC = -2ln(L) + k·ln(n)

They help balance model fit against complexity.

When it comes down to it, choosing between parametric and non-parametric methods depends on our assumptions, sample size, and how much statistical power we need. Each approach has its strengths and weaknesses.

Statistical power (1 - β) measures our ability to detect real effects when they're present. It's a crucial tradeoff - we want to minimize both Type I errors (false positives) and Type II errors (false negatives). Finding the right balance depends on the context and consequences of each type of error.

## Test Statistic
Determine a Test Statistic (quantity that can differentiate between Null and Alternate Hypothesis, and whose distribution under null you can compute).