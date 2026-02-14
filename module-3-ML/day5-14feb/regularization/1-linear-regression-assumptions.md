## 📈 Linear Regression Assumptions (Interview-Ready)

When we use **Linear Regression**, we assume the following:

---

### 1️⃣ Linearity

**Assumption:**
The relationship between independent variables (X) and dependent variable (Y) is linear.

**Meaning:**
[
Y = β₀ + β₁X₁ + β₂X₂ + ... + ε
]

✔️ Change in X → proportional change in Y
❌ If relationship is curved → model underfits

---

### 2️⃣ Independence of Errors

**Assumption:**
Residuals (errors) are independent of each other.

✔️ No correlation between errors
❌ Common violation in time-series data

🔎 Checked using: **Durbin-Watson test**

---

### 3️⃣ Homoscedasticity

**Assumption:**
Constant variance of errors across all levels of X.

✔️ Equal spread of residuals
❌ Funnel shape = Heteroscedasticity

If violated → unreliable confidence intervals.

---

### 4️⃣ Normality of Residuals

**Assumption:**
Errors should be normally distributed.

✔️ Important for hypothesis testing
❌ Skewed residuals affect p-values

🔎 Checked using:

* Histogram of residuals
* Q-Q plot
* Shapiro-Wilk test

---

### 5️⃣ No Multicollinearity

**Assumption:**
Independent variables should not be highly correlated.

✔️ Features independent
❌ High correlation → unstable coefficients

🔎 Checked using:

* VIF (Variance Inflation Factor)
* Correlation matrix

---

### 6️⃣ No Perfect Autocorrelation

Especially important in time-series.

Errors should not follow patterns over time.

---

# 🧠 Interview 30-Second Answer

“Linear regression assumes linearity between X and Y, independent errors, constant variance of residuals, normally distributed errors, and no multicollinearity among predictors.”

---

If you want, I can also give:

* 📊 Visual intuition explanation
* 🧪 How to check each assumption in Python
* 🎯 Bias-Variance connection
* 🚀 Interview tricky follow-up questions

Just tell me 👌
