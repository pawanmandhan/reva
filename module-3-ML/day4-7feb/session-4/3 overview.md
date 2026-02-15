Here is a structured **README** file summarizing the concepts and implementation details from the lecture. This can be used as documentation for a study repository or a project reference.

---

# Module 3: Ensemble Learning & Random Forest

**Video Reference:** [Module 3 ML Day 4 Session 1](https://www.youtube.com/watch?v=tgiQbPv2qKY)

**Topic:** Machine Learning, Ensemble Methods, Bias-Variance Tradeoff, Random Forest Classifier

**Dataset:** Titanic Survival Prediction

---

## 📖 Overview

This module focuses on improving machine learning model performance using **Ensemble Learning**. It transitions from simple models (like Linear Regression and single Decision Trees) to robust "forests" of models. The core implementation involves applying the **Random Forest** algorithm to the Titanic dataset to predict passenger survival, utilizing `RandomizedSearchCV` for hyperparameter optimization.

---

## 🧠 Core Concepts

### 1. Bias vs. Variance Tradeoff

To build robust models, one must understand the sources of error:

* **Underfitting (High Bias):** The model is too simple (e.g., linear line for curved data). It misses the signal.
* **Overfitting (High Variance):** The model is too complex. It captures noise and fails to generalize to new data.
* **The Goal:** A "Best Fit" model that balances bias and variance—capturing the signal without the noise.

### 2. Ensemble Learning

Ensemble methods combine multiple "weak learners" to create a "strong learner."

* **Bagging (Bootstrap Aggregating):** Trains models in **parallel** on random subsets of data. The final prediction is an average (regression) or majority vote (classification). *Example: Random Forest.*
* **Boosting:** Trains models **sequentially**. Each new model corrects the errors of the previous one. *Examples: AdaBoost, XGBoost.*
* **Stacking:** Uses a "meta-learner" model to combine predictions from several different base models.

---

## 🌲 The Random Forest Algorithm

Random Forest is a **Bagging** technique that builds a "forest" of Decision Trees.

### Key Mechanisms

1. **Bootstrapping:** Each tree is trained on a random sample of the dataset (with replacement).
2. **Feature Randomness:** At each split in a tree, only a random subset of features (usually ) is considered.
3. **Aggregation:**

* **Classification:** Majority vote (e.g., if 70 trees say "Survive" and 30 say "Die", the prediction is "Survive").
* **Regression:** Average of all tree outputs.

### Pros & Cons

| Pros | Cons |
| --- | --- |
| **Robustness:** Handles outliers and non-linear data well. | **Black Box:** Harder to interpret individual decisions compared to a single tree. |
| **Accuracy:** Generally higher accuracy than single models. | **Computational Cost:** Slower to train and predict due to multiple trees. |
| **Feature Importance:** Automatically ranks variables. | **Complexity:** Not ideal for strictly regulated industries (e.g., Banking) requiring full transparency. |

---

## ⚙️ Implementation Details

The session implements a Random Forest Classifier on the **Titanic dataset**.

### Prerequisites

* Python 3.x
* Scikit-Learn (`sklearn`)
* Pandas
* NumPy

### Key Code Highlights

#### 1. Hyperparameter Tuning

Instead of guessing parameters, use **`RandomizedSearchCV`** to efficiently search for the best configuration:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

# Define parameter grid
param_dist = {
    'n_estimators': [100, 200, 300],        # Number of trees
    'max_depth': [5, 10, None],             # Max depth of tree
    'min_samples_split': [2, 5, 10],        # Min samples to split a node
    'max_features': ['sqrt', 'log2']        # Features to consider at split
}

# Initialize Random Forest
rf = RandomForestClassifier(random_state=42)

# Run Randomized Search
random_search = RandomizedSearchCV(
    estimator=rf,
    param_distributions=param_dist,
    n_iter=10,
    cv=5, 
    n_jobs=-1,  # Use all available CPU cores
    verbose=2
)

random_search.fit(X_train, y_train)

```

#### 2. Feature Importance

After training, extract which features contributed most to the decision:

```python
import pandas as pd

# Get best estimator
best_rf = random_search.best_estimator_

# Plot feature importance
feature_importances = pd.Series(best_rf.feature_importances_, index=X_train.columns)
feature_importances.nlargest(10).plot(kind='barh')

```

### Observations from Lecture

* **Dominant Features:** `Sex`, `Fare`, and `Age` were the most significant predictors for survival.
* **Performance:** The Random Forest model typically outperforms a single Decision Tree on the test set due to reduced variance.

---

## 🚀 Usage

1. **Clone the Repository:**

```bash
git clone https://github.com/your-repo/module-3-ensemble-learning.git

```

1. **Install Dependencies:**

```bash
pip install -r requirements.txt

```

1. **Run the Notebook:**
Launch Jupyter Notebook and open `Random_Forest_Titanic.ipynb`.

```bash
jupyter notebook

```

---

## 📝 Assignment

* **Task:** Implement Random Forest on the Titanic dataset.
* **Objective:** Compare the accuracy and confusion matrix of the Random Forest model against a single Decision Tree model.
* **Experiment:** Try changing `n_estimators` and `max_depth` to see how it affects the Bias-Variance tradeoff.
