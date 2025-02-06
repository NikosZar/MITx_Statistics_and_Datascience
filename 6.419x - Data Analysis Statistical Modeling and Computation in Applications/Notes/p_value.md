# Understanding P-values and Statistical Significance

A p-value represents the probability of observing data as extreme as or more extreme than what was actually observed, assuming the null hypothesis is true. In other words, it quantifies how surprising our results would be if there truly was no effect.

## The 0.05 Significance Level

The conventional significance level of α = 0.05 (5%) represents a threshold that researchers commonly use to make decisions about rejecting the null hypothesis. This means:

- If p < 0.05: We reject the null hypothesis (results are "statistically significant")
- If p ≥ 0.05: We fail to reject the null hypothesis (results are "not statistically significant")

The choice of 0.05 is somewhat arbitrary but has become standard practice in many fields. It represents a balance between:
- Type I error (false positives) - rejecting H₀ when it's actually true
- Type II error (false negatives) - failing to reject H₀ when it's actually false

## Type I and Type II Errors

When conducting hypothesis tests, two types of errors can occur:

1. Type I Error (False Positive):
   - Rejecting the null hypothesis when it is actually true
   - The probability of making a Type I error is equal to the significance level α
   - For α = 0.05, there is a 5% chance of incorrectly rejecting a true null hypothesis

2. Type II Error (False Negative):
   - Failing to reject the null hypothesis when it is actually false
   - The probability of making a Type II error is denoted as β
   - Power (1 - β) represents the probability of correctly rejecting a false null hypothesis

The significance level α directly controls the Type I error rate. When we set α = 0.05, we are accepting a 5% probability of making a Type I error in our hypothesis test. This means that even when the null hypothesis is true, we will incorrectly reject it 5% of the time.


## Notes from Slides
- P-value is the probability under the null hypothesis to obtain the observed value or a more extreme value of the test statistic
- Smallest significance level for which the null hypothesis just gets rejected
- Can be used for hypothesis testing: Reject null hypothesis if p-value <= a;pha (significance level).
- Quantifies significance of alternative.
