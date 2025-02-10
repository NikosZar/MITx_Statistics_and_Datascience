# Paired Test Design

## Overview
A paired test (also known as a paired difference test or repeated measures design) is a statistical method used when data points are naturally paired or matched. This design is powerful because it controls for extraneous variables by using the same subjects or matched pairs of subjects.

## Key Characteristics

1. **Sample Structure**
   - Each data point has two measurements (before/after, left/right, etc.)
   - Observations are not independent
   - Sample size refers to number of pairs, not individual measurements

2. **Advantages**
   - Reduces variability between groups
   - Controls for confounding variables
   - Generally requires fewer subjects than unpaired designs
   - More statistically powerful than unpaired tests

3. **Common Applications**
   - Before/after treatment studies
   - Twin studies
   - Matched case-control studies
   - Cross-over trials
   - Same subject under different conditions

## Statistical Analysis

### Hypothesis Testing
- H₀: μd = 0 (difference between pairs has mean zero)
- H₁: μd ≠ 0 (two-tailed) or μd > 0 or μd < 0 (one-tailed)

### Test Statistics
1. **Paired t-test**
   - Most common analysis method
   - Assumes differences are normally distributed
   - Uses within-pair differences: d = x₁ - x₂

2. **Wilcoxon Signed-Rank Test**
   - Non-parametric alternative
   - Used when normality assumption is violated
   - Based on ranks of absolute differences

## Design Considerations

1. **Sample Size**
   - Power analysis should account for paired nature
   - Generally needs fewer subjects than unpaired design
   - Consider expected correlation between pairs

2. **Potential Issues**
   - Missing data more problematic than unpaired designs
   - Carryover effects in crossover studies
   - Order effects need to be considered
   - Time-dependent changes between measurements

## Example Applications

1. **Clinical Trials**
   - Blood pressure before and after treatment
   - Pain scores pre- and post-intervention
   - Weight loss studies

2. **Psychology**
   - Memory tests under different conditions
   - Reaction times with/without stimulus
   - Learning outcomes before/after intervention

3. **Quality Control**
   - Product measurements from two machines
   - Performance metrics before/after process change
   - Paired comparisons of measurement methods
