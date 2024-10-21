import pandas as pd
import statsmodels.api as sm
import pickle
import os

# Set up paths
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    current_dir = os.getcwd()
parent_dir = os.path.join(current_dir, '..')

# Load the saved model
model_path = os.path.join(parent_dir, 'models', 'linear_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

data_path = os.path.join(parent_dir, 'data', 'analysis_data', 'analysis_data.xlsx')
data = pd.read_excel(data_path)

# Set up predictors
X = data[['numeric_grade', 'sample_size', 'pollscore']]

# Poll-of-polls: average all predictor values
average_predictors = X.mean().to_frame().T
average_predictors = sm.add_constant(average_predictors)
intercept = model.params['const']
coef_numeric_grade = model.params['numeric_grade']
coef_sample_size = model.params['sample_size']
coef_pollscore = model.params['pollscore']

# Get the average values of predictors
average_numeric_grade = average_predictors['numeric_grade'][0]
average_sample_size = average_predictors['sample_size'][0]
average_pollscore = average_predictors['pollscore'][0]

predicted_value = (intercept +
                   coef_numeric_grade * average_numeric_grade +
                   coef_sample_size * average_sample_size +
                   coef_pollscore * average_pollscore)

print(f"The predicted scaled Trump volt received percentage is: {predicted_value:.3f}")
