# Statistical Power: One-sided vs Two-sided Tests

## What is Power?

Statistical power is essentially our ability to detect a real effect when it exists. It's 1 - β, where β is the probability of a Type II error (failing to reject a false null hypothesis). I like to think of it as our "detection sensitivity."

## The One-sided vs Two-sided Dilemma

Here's what I've learned about the power differences between one-sided and two-sided tests:

A one-sided test concentrates all the α (significance level) in one tail of the distribution. This means we need a less extreme value to reject H₀ in the direction we're testing. As a result, one-sided tests have more power to detect effects in the predicted direction.

In contrast, a two-sided test splits α between both tails (usually α/2 in each tail). We need more extreme values to reject H₀, which reduces our power compared to a one-sided test.

### The Trade-off

I find this trade-off really interesting:
- One-sided tests: More power, but completely blind to effects in the opposite direction
- Two-sided tests: Less power, but can detect effects in either direction

For example, if we're using α = 0.05:
- One-sided test: Needs |Z| > 1.645 in the predicted direction
- Two-sided test: Needs |Z| > 1.96 in either direction

power in a 2-sided test decreases relative to the power in a 1-side test. There is an exception if the alternative hypothesis is bimodal.
