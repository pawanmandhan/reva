Based on the lecture video "Module 3 ML Day 4 Session 2," here are the detailed notes with timestamps. This session covers **Random Forest Optimization**, **Threshold Optimization**, and an introduction to **Unsupervised Learning (K-Means Clustering)**.

### **1. Random Forest & Parameter Optimization**

* **Recap of Random Forest Performance:** Students shared results with accuracies around 79–81% and discussions on precision/recall [[01:38](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=98)].
* **Best Parameters:** The instructor emphasizes that "best" depends on the business objective (e.g., maximizing recall vs. precision). A forest doesn't always need hundreds of trees; sometimes 10 trees provide the best recall [[21:53](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=1313)].
* **Hyperparameters for Tuning [[19:02](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=1142)]:**
* `n_estimators`: Number of trees in the forest.
* `max_depth`: Depth of the trees.
* `min_samples_split`: Minimum samples to split a node.
* `class_weight='balanced'`: Helps the model learn from both classes equally, which can boost recall for the minority class [[19:43](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=1183)].

---

### **2. Threshold Optimization**

* **Default Behavior:** Classification models typically use a **50% (0.5)** probability threshold for binary classification. If the probability of survival is >0.5, the person is classified as "Survived" [[27:18](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=1638)].
* **Probability Prediction (`predict_proba`):** Instead of just getting 0 or 1, the model returns the raw probability for each class [[26:25](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=1585)].
* **Dropping the Threshold (Increasing Recall):**
* By lowering the threshold to **0.25**, anyone with even a 25% chance of survival is flagged as "Survived."
* **Result:** Recall jumped from ~72% to 80% [[34:39](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=2079)].

* **Raising the Threshold (Increasing Precision):**
* By raising the threshold to **0.90**, only those with a 90% certainty are flagged as "Survived."
* **Result:** Precision for survival becomes very high (near 100%), but recall drops significantly (38%) [[39:34](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=2374)].

* **Business Use Case (Fraud/Security):** In fraud detection or national security, you might drop the threshold to 5% or 10% because it is better to investigate a "false alarm" than to miss a real threat (High Recall) [[41:23](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=2483)].

---

### **3. Unsupervised Learning: Clustering**

* **Definition:** Clustering is used when there are **no labels** (no "Ground Truth"). It helps find natural groups or "clusters" in the data [[01:04:00](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=3840)].
* **Clustering vs. Classification:**
* Classification (Supervised): "Is this a default or not?" (We know the answer).
* Clustering (Unsupervised): "Form groups of similar people." (We don't know the groups beforehand) [[01:07:45](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=4065)].

* **Business Examples:**
* **Marketing (STP):** Segmentation, Targeting, and Positioning. Companies like Maruti target fuel-conscious buyers, while Land Rover targets luxury/lifestyle segments [[01:10:06](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=4206)].
* **Google News:** Grouping thousands of live articles into buckets like "Finance," "Sports," or "Technology" on the fly [[01:15:22](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=4522)].

---

### **4. K-Means Clustering Algorithm**

* **Mechanism:**

1. **K:** The number of clusters (user-defined).
2. **Centroids:** Random "anchors" are dropped in the data space [[01:18:26](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=4706)].
3. **Assignment:** Every data point calculates its distance (Euclidean) to each centroid and joins the closest one [[01:19:18](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=4758)].
4. **Movement:** The centroid moves to the actual center of its new members. This repeats until the centroids stop moving [[01:20:45](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=4845)].

* **Sensitivity:** The algorithm is sensitive to **outliers** because it relies on distance. It requires data **scaling/normalization** before running [[01:28:36](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=5316)].

---

### **5. Evaluating Clusters**

* **Inertia (SSE):** The sum of squared distances of samples to their closest cluster center. Lower is better (tighter clusters) [[01:27:42](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=5262)].
* **The Elbow Method:** A plot of Inertia vs. Number of Clusters (K). The point where the "drop" in error slows down significantly (the "elbow") is usually the ideal number of clusters [[01:35:33](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=5733)].
* **Silhouette Score:** Measures how well a point fits in its own cluster vs. the next closest one. A score closer to 1 means high cluster quality [[01:39:27](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=5967)].
* **Naming Clusters:** A successful clustering model should be explainable in plain English (e.g., "Bargain Hunters," "Premium Buyers") [[01:23:51](http://www.youtube.com/watch?v=LWiRnQLd5m0&t=5031)].

**Video Link:** [https://www.youtube.com/watch?v=LWiRnQLd5m0](https://www.youtube.com/watch?v=LWiRnQLd5m0)
