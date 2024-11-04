import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Model parameters (intercept and coefficients) from trained model
intercept = 0.5324
coef_numeric_grade = -0.0160
coef_sample_size = -2.28e-06
coef_pollscore = -0.0064

# Simulation assumptions based on the histograms and additional details
num_simulations = 1000

# Generate simulated predictor values based on assumed distributions
np.random.seed(42)  # For reproducibility
simulated_data = pd.DataFrame({
    'numeric_grade': np.random.normal(2.0, 0.7, num_simulations),  # Assuming normal distribution
    'sample_size': np.random.lognormal(np.log(1800), 1.2, num_simulations),  # Log-normal for skew
    'pollscore': np.random.normal(-0.3, 0.7, num_simulations),  # Normal distribution
})

# Predict Trump's vote share for each simulated data point
simulated_data['predicted_trump_pct'] = (
        intercept +
        coef_numeric_grade * simulated_data['numeric_grade'] +
        coef_sample_size * simulated_data['sample_size'] +
        coef_pollscore * simulated_data['pollscore']
)

# Analyze simulation results
mean_prediction = simulated_data['predicted_trump_pct'].mean()
std_dev_prediction = simulated_data['predicted_trump_pct'].std()
conf_interval = (mean_prediction - 1.96 * std_dev_prediction / np.sqrt(num_simulations),
                 mean_prediction + 1.96 * std_dev_prediction / np.sqrt(num_simulations))

print(f"Mean Predicted Trump Vote Share: {mean_prediction:.3f}")
print(f"Standard Deviation of Predictions: {std_dev_prediction:.3f}")
print(f"95% Confidence Interval: {conf_interval[0]:.3f}, {conf_interval[1]:.3f}")


plt.figure(figsize=(10, 6))
sns.histplot(x=np.array(simulated_data['predicted_trump_pct']), bins=30)
plt.xlabel("Simulated Trump Vote Share")
plt.ylabel("Frequency")
plt.title("Distribution of Simulated Trump Vote Share")
plt.show()

# Define the path to save the file
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    current_dir = os.getcwd()
parent_dir = os.path.join(current_dir, '..')
output_path = os.path.join(parent_dir, 'data', 'simulation_data', 'simulated_predictions.parquet')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
simulated_data.to_parquet(output_path, index=False)
print(f"Simulated data saved to {output_path}")
