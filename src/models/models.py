import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import ShuffleSplit, GridSearchCV
from sklearn.metrics import r2_score, make_scorer
import joblib

# Load dataset
data = pd.read_csv('C:/Users/hp/Desktop/predicting-boston-housing-prices/src/data/housing.csv')

features = data[['RM', 'LSTAT', 'PTRATIO']]
prices = data['MEDV']

# Setup cross-validation and grid search for decision tree
cv_sets = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
regressor = DecisionTreeRegressor(random_state=42)
params = {'max_depth': range(1, 11)}
scoring_fnc = make_scorer(r2_score)

grid = GridSearchCV(regressor, params, scoring=scoring_fnc, cv=cv_sets)
grid.fit(features, prices)

best_model = grid.best_estimator_

# Save trained model to disk
joblib.dump(best_model, 'boston_housing_model.pkl')
print("Model trained and saved successfully to 'boston_housing_model.pkl'")