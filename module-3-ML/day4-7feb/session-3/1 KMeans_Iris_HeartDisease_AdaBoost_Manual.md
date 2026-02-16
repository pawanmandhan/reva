Here are the notes from the video **"module-3-ml-day-4-session-3"** which covers a machine learning session focused on clustering techniques (K-Means) using Iris and Medical datasets, as well as a detailed manual walkthrough of the AdaBoost algorithm.


### **1. K-Means Clustering: Iris Dataset**

* **Data Preparation:** The session begins with clustering the Iris dataset. Features like sepal length, sepal width, petal length, and petal width are used, while the target labels (Y-variable) are excluded to maintain an unsupervised approach [[12:43](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=763)].
* **Inertia & The Elbow Method:** * Inertia measures how well data points are clustered around their centroids [[13:07](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=787)].
* A range of 1 to 10 clusters was tested to visualize the "Elbow" in the plot [[13:17](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=797)].
* The optimal number of clusters was determined to be **K=3** [[14:01](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=841)].

* **Cluster Interpretation:** The instructor emphasizes naming clusters based on characteristics (e.g., Small, Medium, Large) rather than known labels like "Setosa" since unsupervised learning shouldn't rely on pre-existing labels [[17:31](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=1051)].

### **2. Heart Disease (Medical) Dataset Analysis**

* **Feature Engineering:**
* Students worked on a Cleveland Heart Disease dataset, initially using only numerical columns [[37:59](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=2279)].
* Key variables discussed: **RestBPS** (Systolic Blood Pressure), **Cholesterol**, **CP** (Chest Pain Type), and **Max Heart Rate** [[40:15](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=2415)].

* **Data Imputation Strategies:**
* The instructor advises against using simple mean/mode/median imputation for medical data without consulting domain experts [[49:11](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=2951)].
* For example, if 99% of people are not bankrupt, replacing a missing value with the "mode" of bankrupt would be incorrect [[50:26](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=3026)].

* **Clustering Outcomes:**
* One student identified four clusters based on risk levels (Low Risk vs. High Risk) [[54:42](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=3282)].
* Cluster 2 was noted for high cholesterol, indicating higher heart disease risk [[55:03](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=3303)].

### **3. Manual Walkthrough of AdaBoost**

A student presented a handwritten example of the **AdaBoost (Adaptive Boosting)** algorithm using a "study hours vs. pass/fail" dataset [[59:41](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=3581)]:

* **Initial State:** All samples start with equal weights (1/n) [[01:00:42](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=3642)].
* **Sequential Learning:** Weak learners (Decision Stumps with depth 1) are trained sequentially [[59:41](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=3581)].
* **Weight Updating:**
* If a model misclassifies a point, its weight is increased for the next round [[01:02:23](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=3743)].
* **Alpha Calculation:** This represents the "amount of say" a model has in the final prediction, based on its error rate [[01:03:00](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=3780)].

* **Final Boosted Model:** The final prediction is a weighted sum of all the weak learners' predictions [[01:06:48](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=4008)].

### **4. Key Takeaways & Discussion**

* **Domain Intelligence:** Data intelligence is crucial—knowing that a "160" BP reading refers to systolic pressure because a diastolic reading that high would be fatal [[41:19](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=2479)].
* **Visualization:** Cluster plots should be checked for "jumbled" data; if clusters overlap too much, the features or the number of clusters may need reconsideration [[56:45](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=3405)].

**Next Topic:** Market Basket Analysis and Recommendation Engines [[01:11:45](http://www.youtube.com/watch?v=xWqoKv6VT4E&t=4305)].

**Video Link:** [Watch here](http://www.youtube.com/watch?v=xWqoKv6VT4E)
