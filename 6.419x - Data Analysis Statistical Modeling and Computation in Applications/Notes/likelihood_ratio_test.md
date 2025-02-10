# Likelihood Ratio Test & Maximum Likelihood Estimation

## Maximum Likelihood Estimation (MLE)

### Overview
Maximum likelihood estimation is a method of estimating the parameters of a probability distribution by maximizing a likelihood function. It finds the parameter values that make the observed data most probable.

### Mathematical Formulation

For independent observations x₁, x₂, ..., xₙ from a distribution with parameter θ:

1. Likelihood Function:
   L(θ; x₁, ..., xₙ) = ∏ᵢ f(xᵢ|θ)

2. Log-Likelihood Function (often easier to work with):
   ℓ(θ) = ln L(θ; x₁, ..., xₙ) = ∑ᵢ ln f(xᵢ|θ)

3. MLE is found by solving:
   ∂ℓ(θ)/∂θ = 0

### Properties of MLE
- Consistency: θ̂ₙ → θ as n → ∞
- Asymptotic normality: √n(θ̂ₙ - θ) → N(0, I⁻¹(θ))
- Asymptotic efficiency: Achieves Cramér-Rao lower bound
- Invariance: If θ̂ is MLE of θ, then g(θ̂) is MLE of g(θ)

## Likelihood Ratio Test (LRT)

### Definition
The likelihood ratio test compares the fit of two models, one of which (the null model) is a special case of the other (the alternative model).

### Test Statistic
λ = L(θ₀)/L(θ̂)

where:
- L(θ₀) is the likelihood under null hypothesis
- L(θ̂) is the likelihood under alternative hypothesis

More commonly used form:
Λ = -2ln(λ) = -2[ln L(θ₀) - ln L(θ̂)]

### Asymptotic Distribution
Under H₀, Λ follows a chi-square distribution:
Λ → χ²(df)

where df = difference in dimensionality between H₁ and H₀

## Neyman-Pearson Lemma

### Statement
For testing simple H₀: θ = θ₀ vs H₁: θ = θ₁, the likelihood ratio test:

λ(x) = L(θ₁|x)/L(θ₀|x)

is the most powerful test of size α.

### Mathematical Form
For a critical value k:
- Reject H₀ if λ(x) > k
- Accept H₀ if λ(x) < k

where k is chosen to achieve significance level α:
P(λ(x) > k|H₀) = α

## Real-World Example: HIP Mammography Study (1960s)

### Background
The Health Insurance Plan (HIP) of Greater New York conducted a study to evaluate the effectiveness of mammography screening in reducing breast cancer mortality.

### Data
- Study group (screened): n₁ = 31,000 women
- Control group (not screened): n₂ = 31,000 women
- Deaths in study group: x₁ = 39
- Deaths in control group: x₂ = 63

### Hypothesis Test
H₀: p₁ = p₂ (screening has no effect)
H₁: p₁ ≠ p₂ (screening has an effect)

### Maximum Likelihood Estimation

1. Under H₁ (separate proportions):
   p̂₁ = 39/31,000 = 0.00126
   p̂₂ = 63/31,000 = 0.00203
   L(p̂₁,p̂₂) = (0.00126)³⁹(0.99874)³⁰⁹⁶¹ × (0.00203)⁶³(0.99797)³⁰⁹³⁷

2. Under H₀ (common proportion):
   p̂ = (39+63)/(62,000) = 0.00165
   L(p̂,p̂) = (0.00165)¹⁰²(0.99835)⁶¹⁸⁹⁸

### Likelihood Ratio Test

λ = L(p̂,p̂)/L(p̂₁,p̂₂)
Λ = -2ln(λ) = 6.37

### Decision
At α = 0.05, critical value for χ²(1) = 3.841
Since 6.37 > 3.841, reject H₀

### Interpretation
The likelihood ratio test provides strong evidence (p < 0.05) that mammography screening was effective in reducing breast cancer mortality. The death rate in the screened group (0.126%) was significantly lower than in the control group (0.203%).

This example demonstrates how the likelihood ratio test can be applied to real-world medical research, helping to establish the effectiveness of screening programs and inform public health policy.

