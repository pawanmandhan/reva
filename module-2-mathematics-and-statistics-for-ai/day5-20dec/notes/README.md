# Salary Probability Problem - Normal Distribution Analysis

## Problem Statement

Given a salary distribution with:
- **Mean (μ)** = 10 lakh
- **Standard Deviation (σ)** = 1 lakh

**Find:** What is the probability that a salary falls between 10-12 lakh?

---

## Mathematical Approach

### Understanding Normal Distribution

The salary data follows a **Normal Distribution** (Gaussian Distribution), which is characterized by:
- A bell-shaped curve
- Symmetric around the mean
- Completely defined by mean (μ) and standard deviation (σ)

### Solution Steps

#### **Step 1: Standardize Using Z-Scores**

Convert the given values to standard normal distribution using the Z-score formula:

$$Z = \frac{X - \mu}{\sigma}$$

Where:
- X = the salary value we're interested in
- μ = mean = 10 lakh
- σ = standard deviation = 1 lakh

**For lower bound (X = 10):**
$$Z_{lower} = \frac{10 - 10}{1} = 0$$

**For upper bound (X = 12):**
$$Z_{upper} = \frac{12 - 10}{1} = 2$$

#### **Step 2: Find Cumulative Probabilities**

Use the standard normal cumulative distribution function (CDF) to find:
- P(Z ≤ 0) = 0.500000 (50% of distribution)
- P(Z ≤ 2) = 0.977250 (97.725% of distribution)

These values come from the standard normal table or statistical software.

#### **Step 3: Calculate the Probability**

The probability of salary being between 10-12 lakh is:

$$P(10 \leq X \leq 12) = P(Z \leq 2) - P(Z \leq 0)$$

$$P(10 \leq X \leq 12) = 0.977250 - 0.500000 = 0.477250$$

---

## **ANSWER: 0.4772 or 47.72%**

This means there is approximately a **47.72%** probability that a randomly selected salary falls between 10-12 lakh rupees.

---

## Visual Interpretation

```
                          Normal Distribution
                        (μ=10, σ=1)
                              |
                              |
                     ╱────────┴────────╲
                  ╱                      ╲
                ╱                          ╲
              ╱                              ╲
            ╱                                  ╲
          ╱                  ↓                   ╲
      ───┴──────────────────────────────────────┴───
        5     7     9    10    12    14    16
        |←─────────←────────→─────────→|
        |       50%    |    47.72%    |
        |              |             |
      -3σ           Mean          +2σ
```

The shaded area between 10 and 12 represents the probability we calculated (47.72%).

---

## Key Concepts

### Z-Score
- Measures how many standard deviations a value is from the mean
- Z = 0 means at the mean
- Z > 0 means above the mean
- Z < 0 means below the mean

### Standard Normal Distribution
- A normal distribution with μ = 0 and σ = 1
- Used as a reference for all normal distributions
- Allows comparison of values from different distributions

### CDF (Cumulative Distribution Function)
- Gives the probability that a random variable is less than or equal to a specific value
- Ranges from 0 to 1 (or 0% to 100%)

---

## Implementation

### Using Python with SciPy:

```python
from scipy import stats

# Parameters
mean = 10
std = 1

# Calculate Z-scores
z_lower = (10 - mean) / std  # = 0
z_upper = (12 - mean) / std  # = 2

# Calculate probabilities
prob_at_10 = stats.norm.cdf(z_lower)  # 0.5
prob_at_12 = stats.norm.cdf(z_upper)  # 0.9772

# Find probability between
prob_between = prob_at_12 - prob_at_10  # 0.4772
```

---

## Files Included

1. **salary_probability_solution.py** - Complete Python implementation with step-by-step output
2. **README.md** - This file with full explanation

---

## How to Run

```bash
python salary_probability_solution.py
```

Expected Output:
```
============================================================
SALARY PROBABILITY PROBLEM
============================================================

STEP 1: Convert to Standard Normal Distribution (Z-scores)
  For X = 10 lakh: Z_lower = 0
  For X = 12 lakh: Z_upper = 2

STEP 2: Find Cumulative Probabilities
  P(Z ≤ 0) = 0.500000
  P(Z ≤ 2) = 0.977250

STEP 3: Calculate P(10 ≤ Salary ≤ 12)
  P(10 ≤ Salary ≤ 12) = 0.977250 - 0.500000 = 0.477250

============================================================
FINAL ANSWER
============================================================
  Probability = 0.477250
  Percentage  = 47.7250%
  
There is a 47.73% chance that a salary is between 10 and 12 lakh.
```

---

## Applications

This type of probability calculation is useful for:
- **HR Analytics**: Determine salary ranges and percentiles
- **Risk Management**: Calculate probability of outcomes within ranges
- **Quality Control**: Find defect rates within acceptable ranges
- **Financial Analysis**: Analyze return distributions
- **Healthcare**: Analyze patient measurement distributions

---

## References

- **Normal Distribution**: https://en.wikipedia.org/wiki/Normal_distribution
- **Z-Score**: https://en.wikipedia.org/wiki/Standard_score
- **SciPy Stats Module**: https://docs.scipy.org/doc/scipy/reference/stats.html
- **Standard Normal Table**: Used for manual calculations

---

## Notes

- The calculation assumes salary data is normally distributed
- This is valid for large populations by the Central Limit Theorem
- For small samples, additional validation of normality assumption is recommended
- The probability is symmetric around the mean due to normal distribution properties

---

**Created**: December 20, 2025  
**Problem Type**: Continuous Probability Distribution  
**Method**: Standard Normal Distribution with Z-Score Transformation
