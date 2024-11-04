import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import numpy as np
import pickle
import os

# Reading files
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    current_dir = os.getcwd()
parent_dir = os.path.join(current_dir, '..')
data_path = os.path.join(parent_dir, 'data', 'analysis_data', 'analysis_data.parquet')
data = pd.read_parquet(data_path)

X = data[['numeric_grade', 'sample_size', 'pollscore']]
y = data['scaled_trump_pct']

# Add a constant (intercept term)
X = sm.add_constant(X)

# Initialize KFold cross-validation
kf = KFold(n_splits=8, shuffle=True, random_state=1)
fold = 1
mse_scores = []

# Perform 8-fold cross-validation
for train_index, test_index in kf.split(X):
    # Split the data into training and testing sets for the current fold
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    # Fit the linear model on the training set
    model = sm.OLS(y_train, X_train).fit()

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Calculate mean squared error for the fold and save it
    mse = mean_squared_error(y_test, y_pred)
    mse_scores.append(mse)

    print(f"Fold {fold}: MSE = {mse}")
    fold += 1

# Calculate the average MSE across all folds
average_mse = np.mean(mse_scores)
print(f"\nAverage MSE over 8 folds: {average_mse}")

# Fit the model on the entire dataset and save it for future predictions
final_model = sm.OLS(y, X).fit()

# Save the final model
model_path = os.path.join(parent_dir, 'models', 'linear_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(final_model, f)
print(f"Final model saved to {model_path}")
