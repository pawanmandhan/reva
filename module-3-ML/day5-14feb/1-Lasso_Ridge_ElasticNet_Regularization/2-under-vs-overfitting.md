# 🎯 Underfitting vs Overfitting

Understanding this is **core ML + interview favorite question**.

---

# 📉 Underfitting

## 🔹 What is it?

Model is **too simple** to capture the pattern in data.

## 🔹 What happens?

* High training error
* High test error
* Poor performance everywhere

## 🔹 Why?

* Model too simple (e.g., linear model for nonlinear data)
* Too much regularization
* Not enough features
* Insufficient training

## 🔹 Graph Intuition

![Image](https://miro.medium.com/1%2A_7OPgojau8hkiPUiHoGK_w.png)

![Image](https://images.openai.com/static-rsc-3/ctwE7UEz6KYzHi11mg7hdg4BJK39tgPkzLQPxZhL1MFI-cLv6p32nCbzDk1NCItPas1Hl_W4q-QA-iJ54o8Q7DFCmld8Yqmlvoab5MS3ptA?purpose=fullsize\&v=1)

![Image](https://scikit-learn.org/1.4/_images/sphx_glr_plot_underfitting_overfitting_001.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AW2YPyoOkc0ZIW6ot-VLhWw.png)

Straight line trying to fit curved data.

## 🔹 Bias–Variance

👉 **High Bias, Low Variance**

---

# 📈 Overfitting

## 🔹 What is it?

Model learns **noise + random fluctuations** instead of true pattern.

## 🔹 What happens?

* Very low training error
* High test error
* Poor generalization

## 🔹 Why?

* Model too complex (deep tree, high-degree polynomial)
* Too many features
* Small dataset
* No regularization

## 🔹 Graph Intuition

![Image](https://i.sstatic.net/UHips.jpg)
![alt text](image.png)
![Image](https://www.researchgate.net/publication/341310767/figure/fig2/AS%3A890211840036871%401589254450625/llustrations-of-high-bias-and-high-variance-models-A-toy-dataset-was-generated-from-the.ppm)

![Image](https://i.sstatic.net/L2ApS.png)

![alt text](image-1.png)
![Image](https://www.researchgate.net/publication/331733728/figure/fig2/AS%3A736325191876612%401552565014850/Example-of-overfitting-with-polynomial-regression-Increasing-the-order-of-the-polynomial.png)

Curve wiggles to pass through every point.

## 🔹 Bias–Variance

👉 **Low Bias, High Variance**

---

# ⚖️ Comparison Table

| Feature          | Underfitting        | Overfitting                    |
| ---------------- | ------------------- | ------------------------------ |
| Model Complexity | Too Low             | Too High                       |
| Training Error   | High                | Very Low                       |
| Test Error       | High                | High                           |
| Bias             | High                | Low                            |
| Variance         | Low                 | High                           |
| Fix              | Increase complexity | Reduce complexity / Regularize |

---

# 🧠 Interview 30-Second Answer

“Underfitting occurs when a model is too simple and fails to capture the underlying pattern, leading to high training and test error. Overfitting occurs when a model is too complex and captures noise in the data, resulting in low training error but high test error.”

---

If you want next:

* 📊 Bias–Variance curve explanation
* 🎯 How Cross Validation detects overfitting
* 🐍 Python demo with train/test error plot
* 🚀 FAANG-style tricky follow-up questions
