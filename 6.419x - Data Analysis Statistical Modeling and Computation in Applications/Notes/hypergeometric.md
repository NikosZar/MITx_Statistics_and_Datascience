# The Hypergeometric Distribution

The hypergeometric distribution is a discrete probability distribution that describes the probability of obtaining exactly k successes in n draws, without replacement, from a finite population of size N that contains exactly K successes.

## Key Characteristics

1. **Sampling without Replacement**: Unlike the binomial distribution, each draw changes the probability for subsequent draws since we don't replace items
2. **Fixed Population Size**: The total population (N) is known and finite
3. **Known Success States**: The number of success states (K) in the population is known
4. **Fixed Number of Draws**: The number of items drawn (n) is predetermined

## Mathematical Formula

The probability mass function (PMF) is given by:

P(X = k) = [C(K,k) * C(N-K,n-k)] / C(N,n)

Where:
- N = population size
- K = number of success states in population
- n = number of draws
- k = number of observed successes
- C(a,b) represents combinations (a choose b)

## Properties

1. **Mean**: μ = n * (K/N)
2. **Variance**: σ² = n * (K/N) * ((N-K)/N) * ((N-n)/(N-1))

## Case Study: HIP Mammography Study (1960s)

The Health Insurance Plan (HIP) of Greater New York study was one of the first randomized controlled trials of breast cancer screening. Let's examine how we would set up hypothesis testing using different distributions.

### Hypergeometric Approach

In the HIP study context:
- N = Total study population (62,000 women)
- K = Number of breast cancer cases in population
- n = Number of women screened
- k = Number of breast cancer cases detected in screened group

The hypergeometric distribution would be most appropriate here because:
1. We are sampling without replacement (once a woman is screened, she can't be screened again)
2. The population is finite and known
3. The number of actual breast cancer cases (success states) is fixed

### Comparison with Alternative Approaches

**Binomial Distribution**:
- Would assume each screening is independent
- Assumes probability remains constant (with replacement)
- Less accurate because it doesn't account for the changing probability as women are screened

**Poisson Distribution**:
- Would be appropriate if we were counting rare events in a large population
- Assumes events occur independently at a constant rate
- Doesn't account for the finite population size
- Could be used as an approximation if N is very large and K/N is small

The hypergeometric distribution provides the most accurate model for this scenario because it properly accounts for the finite population and the sampling without replacement nature of screening programs. This becomes particularly important when calculating the probability of false positives and false negatives in screening programs, where the changing composition of the unscreened population affects subsequent probabilities.
