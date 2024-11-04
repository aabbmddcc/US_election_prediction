import pandas as pd
import math
import os

# Reading files
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    current_dir = os.getcwd()
parent_dir = os.path.join(current_dir, '..')
data_path = os.path.join(parent_dir, 'data', 'raw_data', 'president_polls.csv')
raw_data = pd.read_csv(data_path)


# Initializing variables
polls = list(set(raw_data['poll_id']))
response = []
predictors = []

print(len(polls))

# Gain all possible use data
for i in range(len(polls)):

    #Returning exactly one poll according to its id
    this_poll = raw_data[raw_data['poll_id'] == polls[i]]

    #Averaging the percentage if found multiple counts in a poll
    Trump_pct = this_poll[this_poll['candidate_name'] == 'Donald Trump']['pct'].mean()
    Harris_pct = this_poll[this_poll['candidate_name'] == 'Kamala Harris']['pct'].mean()

    #Scale the percentage that Trump + Harris = 100%
    scaled_trump_pct = Trump_pct / (Trump_pct + Harris_pct)
    response.append(scaled_trump_pct)

    #Do the similar to response variable
    i_predictors = []
    i_predictors.append(this_poll['numeric_grade'].mean())
    i_predictors.append(this_poll['sample_size'].mean())
    i_predictors.append(this_poll['pollscore'].mean())
    predictors.append(i_predictors)
    this_poll[this_poll['candidate_name'] == 'Kamala Harris']['pct'].mean()

#Arranging gained response and predictors in a new list
cleaned_response = []
cleaned_predictors = []

for i in range(len(response)):
    if isinstance(response[i], (int, float)) and not math.isnan(response[i]):
        if all(isinstance(x, (int, float)) and not math.isnan(x) for x in predictors[i]):
            cleaned_response.append(response[i])
            cleaned_predictors.append(predictors[i])

print(len(cleaned_predictors))

df = pd.DataFrame(cleaned_predictors, columns=['numeric_grade', 'sample_size', 'pollscore'])
df['scaled_trump_pct'] = cleaned_response

#Set up output file and output path
output_dir = os.path.join(parent_dir, 'data', 'analysis_data')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'analysis_data.parquet')
df.to_parquet(output_path, index=False)

print(f'Data successfully saved to {output_path}')
