# Deriving the Poisson Distribution from the Binomial Distribution

The Poisson distribution can be derived as a limit of the Binomial distribution when:
- The number of trials n approaches infinity
- The probability p of success approaches 0
- The expected value np remains constant (let's call it λ)

## Starting with the Binomial Distribution

The probability mass function for the Binomial distribution is:

$P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$

## Making Substitutions

Since $np = \lambda$ is constant, we can write $p = \frac{\lambda}{n}$

Substituting this into the Binomial formula:

$P(X = k) = \binom{n}{k}(\frac{\lambda}{n})^k(1-\frac{\lambda}{n})^{n-k}$

## Expanding the Combination

$P(X = k) = \frac{n!}{k!(n-k)!}(\frac{\lambda}{n})^k(1-\frac{\lambda}{n})^{n-k}$

$= \frac{n(n-1)(n-2)...(n-k+1)}{k!} \cdot \frac{\lambda^k}{n^k} \cdot (1-\frac{\lambda}{n})^{n-k}$

## Taking the Limit as n → ∞

As n approaches infinity:
1. $\frac{n(n-1)(n-2)...(n-k+1)}{n^k} \to 1$
2. $(1-\frac{\lambda}{n})^n \to e^{-\lambda}$
3. $(1-\frac{\lambda}{n})^{-k} \to 1$

Therefore:

$\lim_{n \to \infty} P(X = k) = \frac{\lambda^k}{k!}e^{-\lambda}$


This is the Poisson distribution with parameter $\lambda$, which gives the probability of k events occurring in a fixed interval when the average rate is $\lambda$.

When data follows a binomial distribution with large $n$ (number of trials) and small $p$ (probability of success), Poisson(np) is a good approximation of Binomial(n, p).

Another interpretation of the Poisson random variable is in terms of a random process called the Poisson process. This is defined as a process where events can occur at any time in continuous time, with an average rate given by the parameter $\lambda$ and satisfying the following conditions:

- Events occur independently of each other
- The probability that an event occurs in a given length of time is contanst.






