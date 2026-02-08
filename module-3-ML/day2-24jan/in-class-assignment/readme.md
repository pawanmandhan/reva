# Medical Insurance Cost Prediction

## Objective

The goal of this project is to build a **Linear Regression model** that predicts individual medical insurance costs based on personal, demographic, and lifestyle attributes such as age, BMI, smoking status, gender, and region.

---

## Part 1: Data Preparation & Exploration

### 1. Data Loading & Cleaning

* Import the dataset and perform an initial inspection. 
* Check for and address any missing values or duplicate entries to ensure data quality. 
#### Exploratory Data Analysis (EDA): 
* Visualizing Relationships: Create charts to understand how different variables (like age, BMI, or smoking status) relate to the medical charges. 
* Look for strong positive or negative correlations. 
  * Distribution Analysis: Plot the distribution of the insurance charges. If the data is heavily skewed (mostly low costs with a few very high costs), consider applying a transformation to make the data distribution more normal/symmetrical.
  * Categorical Analysis: Compare the average costs across different groups (e.g., different regions or genders) to see if significant differences exist.

---

### 2. Exploratory Data Analysis (EDA)

#### a. Visualizing Relationships

* Create visualizations to analyze how key variables relate to medical charges:

  * **Age vs Charges**
  * **BMI vs Charges**
  * **Smoking Status vs Charges**
* Identify strong **positive or negative correlations** between predictors and insurance costs.

#### b. Distribution Analysis

* Plot the distribution of insurance charges.
* Observe whether the data is **right-skewed** (many low values with a few very high values).
* If heavily skewed, consider applying a **log transformation** to make the distribution more normal and improve model performance.

#### c. Categorical Analysis

* Compare **average medical costs** across categorical groups such as:

  * Gender
  * Region
  * Smoking status
* Identify whether significant cost differences exist between these groups.

---

## Part 2: Preprocessing

### 1. Handling Categorical Data

* Convert categorical variables into numerical representations so the model can process them.
* Use appropriate encoding techniques:

  * **Binary encoding** for variables like gender and smoker status.
  * **One-hot encoding** for multi-category variables such as region.

---

### 2. Outlier Management

* Analyze continuous variables (e.g., BMI) for extreme or unusual values.
* Determine whether these outliers represent:

  * Legitimate but rare cases, or
  * Data entry errors.
* Decide whether to retain, remove, or cap outliers to prevent distortion of the model.

---

### 3. Feature Scaling

* Scale numerical features such as age and BMI.
* Ensure all features are on a similar scale so no variable dominates the model due to larger numeric values.
* This step improves model stability and interpretability.

---

## Part 3: Model Building & Evaluation

### 1. Training the Model

* Split the dataset into:

  * **Training set** – used to fit the model.
  * **Testing set** – used to evaluate performance on unseen data.
* Train a **Linear Regression model** using the processed training data.

---

### 2. Evaluation

* Evaluate the model on the testing dataset.
* Calculate standard regression metrics:

  * **Mean Absolute Error (MAE)** or **Root Mean Squared Error (RMSE)** to measure average prediction error.
  * **R-squared (R²)** to measure how much variance in medical costs is explained by the model.

---

## Part 4: Analysis (Expected Findings)

### 1. Best Predictors

* **Smoking Status** emerges as the strongest predictor of medical insurance costs.

  * Smokers incur significantly higher charges compared to non-smokers.
* **Age** and **BMI** are also important predictors.
* Variables like **gender** and **region** typically have a much smaller impact on overall costs.

---

### 2. Error Rate

* **Model Accuracy (R²):** Expected to be between **0.70 and 0.80**.
* **Prediction Error:** On average, predictions may differ from actual values by approximately **$4,000**.

---

### 3. Is This a Good Model?

* The model serves as a **decent baseline**, but it is not optimal.

#### Why?

* Linear Regression assumes a **linear relationship** between inputs and output.
* Medical costs often exhibit **non-linear behavior**, such as:

  * Costs increasing sharply when a person is both a smoker and has a high BMI.
* These interaction effects are not fully captured by a simple linear model.

#### Conclusion

* Linear Regression provides a **good first approximation**.
* More advanced models (e.g., decision trees, random forests, or polynomial regression) could better capture complex relationships and improve predictive accuracy.

