import pandas as pd
import statsmodels.api as sm
import pickle
import os

#Reading files
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

# Fit the linear model
model = sm.OLS(y, X).fit()

model_path = os.path.join(parent_dir, 'models', 'linear_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)
print(f"Model saved to {model_path}")
