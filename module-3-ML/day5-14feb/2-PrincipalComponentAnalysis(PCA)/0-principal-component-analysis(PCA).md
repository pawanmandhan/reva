## 📊 Principal Component Analysis (PCA) using Scikit-Learn

### 🔹 What is PCA?

**Principal Component Analysis (PCA)** is a **dimensionality reduction** technique.

👉 It transforms high-dimensional data into fewer dimensions
👉 While preserving **maximum variance (information)**
👉 Creates new features called **Principal Components**

---

## 🧠 Intuition (Interview Ready – 30 sec)

> PCA finds new axes (directions) in the data such that:
>
> * 1st PC → captures maximum variance
> * 2nd PC → captures next maximum variance (orthogonal to 1st)
> * and so on…

It’s based on **eigenvectors & eigenvalues** of the covariance matrix.

---

## ⚙️ PCA using Scikit-Learn

We’ll use:

* `StandardScaler` (very important step)
* `PCA` from sklearn

---

## ✅ Step-by-Step Example (Iris Dataset)

### 📌 Code (Clean & Interview Ready)

```python
# Step 1: Import libraries
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

# Step 2: Load dataset
data = load_iris()
X = data.data
y = data.target

# Step 3: Standardize data (VERY IMPORTANT)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Apply PCA (reduce to 2 dimensions)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Step 5: Convert to DataFrame (optional)
df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])

print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Total Variance Captured:", sum(pca.explained_variance_ratio_))
```

---

## 📌 Output Meaning

### `explained_variance_ratio_`

Example:

```
[0.73, 0.23]
```

Means:

* PC1 captures **73%** of variance
* PC2 captures **23%**
* Total = **96% information retained**

🔥 Only 2 features now instead of 4!

---

## 🎯 Important Parameters

```python
PCA(
    n_components=2,        # Number of principal components
    svd_solver='auto',     
    random_state=42
)
```

### Special Case

```python
PCA(n_components=0.95)
```

➡ Keeps enough components to retain **95% variance automatically**

---

## 📈 Visualization

```python
import matplotlib.pyplot as plt

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - Iris Dataset")
plt.show()
```

You’ll see class separation in 2D space.

---

## 🧪 When to Use PCA?

✅ Before clustering (KMeans)
✅ Before logistic regression (reduce noise)
✅ When features are highly correlated
✅ For visualization (reduce to 2D/3D)

---

## ⚠️ Important Notes

❌ PCA is **not feature selection**
✔ It creates new synthetic features

❌ Don’t forget scaling
✔ Always use `StandardScaler`

❌ Not good if interpretability is required
✔ Components are linear combinations of original features

---

## 🏆 Interview 60-Second Explanation

> PCA reduces dimensionality by projecting data onto orthogonal axes that maximize variance. It computes eigenvectors of the covariance matrix and selects top components based on eigenvalues. In sklearn, we standardize data, apply PCA, and choose components using explained variance ratio.

---

## 🔥 Bonus: Choosing Number of Components (Scree Plot)

```python
pca_full = PCA()
pca_full.fit(X_scaled)

plt.plot(range(1, len(pca_full.explained_variance_ratio_) + 1),
         pca_full.explained_variance_ratio_,
         marker='o')
plt.xlabel("Number of Components")
plt.ylabel("Explained Variance Ratio")
plt.title("Scree Plot")
plt.show()
```

Look for **elbow point**.

---

If you want, I can also give:

* 🔹 PCA mathematical derivation
* 🔹 PCA vs LDA comparison
* 🔹 PCA interview cheat sheet
* 🔹 PCA from scratch (NumPy only)
* 🔹 PCA in Titanic dataset end-to-end

Tell me your goal (interview / project / theory).
