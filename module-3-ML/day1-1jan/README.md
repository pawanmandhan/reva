# EDA: Missing Values, Outliers & Pandas Profiling - Titanic Dataset

## 📋 Overview
This notebook performs **Exploratory Data Analysis (EDA)** on the Titanic dataset, focusing on:
- Loading and understanding the dataset
- Identifying and handling missing values
- Detecting and removing outliers
- Data preprocessing and transformation
- Building a decision tree classifier

## 📊 Dataset
- **Source**: Seaborn built-in Titanic dataset
- **Rows**: ~891 passengers
- **Columns**: Various features including age, fare, gender, class, embarkation port, etc.

## 🔍 Key Sections

### 1. **Data Loading & Exploration**
- Load Titanic dataset from Seaborn
- Check dataset shape, info, and head
- Explore available datasets in Seaborn

### 2. **Data Cleaning**
- Drop unnecessary columns (who, adult_male, embark_town, alone, alive, class, deck)
- Rename columns for clarity (sex→gender, sibsp→siblings, parch→parents_child)
- Check for missing values

### 3. **Handling Missing Values**
- **Categorical variables**: Replace with mode (embarked → 'S')
- **Numerical variables**: Replace with median (age)
- Multiple imputation strategies demonstrated

### 4. **Outlier Detection & Treatment**
- Calculate quantiles (1st, 5th, 95th, 99th percentiles)
- Use IQR (Interquartile Range) method with 1.5 × IQR rule
- Floor and cap outliers using `np.clip()`

### 5. **Data Transformation**
- Convert categorical variables to numeric using `pd.Categorical()`
- Create dummy variables for class and embark port
- Feature engineering (PersonType - Child/Woman/Man)

### 6. **Exploratory Visualizations**
- Histograms for age distribution
- Box plots for outlier visualization
- Scatter plots (age vs fare)
- Heatmaps for correlation analysis
- Factor plots for survival analysis

### 7. **Model Building**
- Decision Tree Classifier with max_depth=2
- Train-test split (75-25)
- Model evaluation with classification report
- Feature importance analysis
- Tree visualization using Graphviz

## 🛠️ Technologies Used
- **Python 3.x**
- **Pandas**: Data manipulation
- **NumPy**: Numerical operations
- **Matplotlib & Seaborn**: Data visualization
- **Scikit-learn**: Machine learning (Decision Tree)
- **Graphviz**: Tree visualization

## ⚠️ Known Issues & Notes
1. Some cells use uppercase column names (Embarked, Age) - inconsistent with earlier lowercase versions
2. Iris dataset code section (flooring/capping) may require 'Iris.csv' file
3. A few cells have undefined variables (by_gender_class, impute_median) - these appear to be exploratory code

## 📈 Main Findings
- Age and fare have significant outliers
- Survival rate varies by passenger class and gender
- Missing values: Age (~177), Embarked (2)
- Feature importance: fare and siblings/pclass are key predictors

## 🚀 How to Use
1. Ensure you have required libraries installed
2. Run cells sequentially from top to bottom
3. The notebook saves a decision tree visualization as 'tree.dot'
4. Modify parameters as needed for different analysis

## 📝 Next Steps
- Implement more complex models (Random Forest, Logistic Regression)
- Handle class imbalance if needed
- Cross-validation for robust evaluation
- Hyperparameter tuning

<https://nlpfy.com/machine-learning-and-data-science-intro-and-faqs/>

<https://www.linkedin.com/posts/ratnakarpandey_ml-project-lifecycle-a-typical-machine-learning-activity-7112314863225376769-iHza>


# Linear regression models (6 steps)
https://nlpfy.com/2017/10/31/python-machine-learning-linear-regression-with-scikit-learn/

# visual representation for probability
<https://seeing-theory.brown.edu/compound-probability/index.html>

# ML models cheatsheet
https://www.datacamp.com/cheat-sheet/machine-learning-cheat-sheet



TODO :

https://nlpfy.com/2017/10/22/
articles - 28,29,30,31,32,35,36,37

next class topics:

PCA
k means
MBA
ensemble
timeseries

explain SHAP 
Autogluon library or H2O