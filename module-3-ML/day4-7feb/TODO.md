1. Compare parameters for cross validation in Decision tree vs Random forest.


```
1.Decision Tree classifier
param_grid = {
    "max_depth": [None, 3, 5, 7, 10],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 5],
    "criterion": ["gini", "entropy"]
}

grid = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1
)
grid.fit(X_train, y_train)

grid.best_params_, grid.best_score_

# Best model evaluation
best_dt = grid.best_estimator_
y_pred_best = best_dt.predict(X_test)
```

```
2.Random Forest
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

Define parameter grid
param_dist = {
    'n_estimators': [100, 200, 300],        # Number of trees
    'max_depth': [5, 10, None],             # Max depth of tree
    'min_samples_split': [2, 5, 10],        # Min samples to split a node
    'max_features': ['sqrt', 'log2']        # Features to consider at split
}

Initialize Random Forest
rf = RandomForestClassifier(random_state=42)

Run Randomized Search
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



2. In both the cases there are multiple trees created based on parameters passed

3. How decision tree and Random forest are linked 


4. mind map for Decision Tree and Random Forest

