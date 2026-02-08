# Decision Tree: Classifier vs Regressor

## Overview
Decision Trees are supervised learning models used for **classification** and **regression**. The core tree-building logic is similar, but the **target type, split criteria, and outputs** differ.

---

## 1. Type of Target Variable

| Aspect | Decision Tree Classifier | Decision Tree Regressor |
|------|-------------------------|------------------------|
| Target (y) | Categorical | Continuous |
| Examples | survived / not survived, spam / not spam | house price, salary, temperature |

---

## 2. Output at Leaf Node

| | Classifier | Regressor |
|--|-----------|-----------|
| Leaf Output | Class label or class probabilities | Numeric value (mean/median) |

- Classifier leaf → predicts a **class**
- Regressor leaf → predicts a **number**

---

## 3. Split Criterion (How Best Split Is Chosen)

| | Classifier | Regressor |
|--|-----------|-----------|
| Criterion | Gini, Entropy | MSE, MAE, Variance reduction |
| Objective | Reduce class impurity | Reduce prediction error |

**Intuition:**
- Classifier: “Are classes getting purer?”
- Regressor: “Is numeric variance getting smaller?”

---

## 4. Evaluation Metrics

| | Classifier | Regressor |
|--|-----------|-----------|
| Metrics | Accuracy, Precision, Recall, F1, ROC-AUC | MSE, RMSE, MAE, R² |

---

## 5. Same Dataset, Different Use

Example: Titanic dataset

| Target Column | Tree Type |
|--------------|----------|
| survived (0/1) | DecisionTreeClassifier |
| fare (float) | DecisionTreeRegressor |

Same features (age, sex, pclass) but **different objective → different tree structure**.

---

## 6. Code-Level Difference (scikit-learn)

```python
DecisionTreeClassifier(criterion="gini")
DecisionTreeRegressor(criterion="squared_error")
```

Just changing the estimator switches the learning goal.

---

## 7. Interview One-Liner

> Decision Tree Classifiers minimize class impurity, while Decision Tree Regressors minimize numeric prediction error.

---

## 8. Quick Decision Guide

| If your target is... | Use |
|---------------------|-----|
| Category / Label | DecisionTreeClassifier |
| Number / Quantity | DecisionTreeRegressor |

---

**End of file**

