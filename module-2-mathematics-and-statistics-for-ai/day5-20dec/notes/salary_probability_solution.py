import numpy as np
from scipy import stats

# Given parameters
mean = 10  # lakh
std = 2    # lakh

print("="*60)
print("SALARY PROBABILITY PROBLEM")
print("="*60)
print()
print("Given:")
print(f"  Mean salary (μ) = {mean} lakh")
print(f"  Standard deviation (σ) = {std} lakh")
print(f"  Find: P(10 ≤ Salary ≤ 12) lakhs")
print()
print("="*60)
print("SOLUTION - STEP BY STEP")
print("="*60)
print()

# Step 1: Calculate Z-scores
z_lower = (10 - mean) / std
z_upper = (12 - mean) / std

print("STEP 1: Convert to Standard Normal Distribution (Z-scores)")
print("-" * 60)
print(f"  Formula: Z = (X - μ) / σ")
print()
print(f"  For X = 10 lakh:")
print(f"    Z_lower = (10 - {mean}) / {std} = {z_lower}")
print()
print(f"  For X = 12 lakh:")
print(f"    Z_upper = (12 - {mean}) / {std} = {z_upper}")
print()

# Step 2: Calculate probabilities using CDF
prob_at_10 = stats.norm.cdf(z_lower)
prob_at_12 = stats.norm.cdf(z_upper)

print("STEP 2: Find Cumulative Probabilities using Standard Normal CDF")
print("-" * 60)
print(f"  P(Z ≤ {z_lower}) = {prob_at_10:.6f}")
print(f"  P(Z ≤ {z_upper}) = {prob_at_12:.6f}")
print()

# Step 3: Calculate probability between 10-12 lakh
prob_between = prob_at_12 - prob_at_10

print("STEP 3: Calculate P(10 ≤ Salary ≤ 12)")
print("-" * 60)
print(f"  Formula: P(a ≤ X ≤ b) = P(Z ≤ z_upper) - P(Z ≤ z_lower)")
print()
print(f"  P(10 ≤ Salary ≤ 12) = P(Z ≤ {z_upper}) - P(Z ≤ {z_lower})")
print(f"  P(10 ≤ Salary ≤ 12) = {prob_at_12:.6f} - {prob_at_10:.6f}")
print(f"  P(10 ≤ Salary ≤ 12) = {prob_between:.6f}")
print()

print("="*60)
print("FINAL ANSWER")
print("="*60)
print(f"  Probability = {prob_between:.6f}")
print(f"  Percentage  = {prob_between*100:.4f}%")
print(f"  Rounded     = {prob_between:.4f} or {prob_between*100:.2f}%")
print("="*60)
print()
print("Interpretation:")
print(f"  There is a {prob_between*100:.2f}% chance that a salary is")
print(f"  between 10 and 12 lakh rupees.")
