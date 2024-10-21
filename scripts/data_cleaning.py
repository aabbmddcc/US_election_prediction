import pandas as pd
import math
import os
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    current_dir = os.getcwd()
parent_dir = os.path.join(current_dir, '..')
data_path = os.path.join(parent_dir, 'data', 'raw_data', 'president_polls.csv')
raw_data = pd.read_csv(data_path)

# raw_data = pd.read_csv("C:\\Users\\jason\\Desktop\\US_election_prediction\\data\\raw_data\\president_polls.csv")
polls = list(set(raw_data['poll_id']))
response = []
predictors = []

for i in range(len(polls)):
    this_poll = raw_data[raw_data['poll_id'] == polls[i]]
    Trump_pct = this_poll[this_poll['candidate_name'] == 'Donald Trump']['pct'].mean()
    Harris_pct = this_poll[this_poll['candidate_name'] == 'Kamala Harris']['pct'].mean()
    scaled_trump_pct = Trump_pct / (Trump_pct + Harris_pct)
    response.append(scaled_trump_pct)

    i_predictors = []
    i_predictors.append(this_poll['numeric_grade'].mean())
    i_predictors.append(this_poll['sample_size'].mean())
    i_predictors.append(this_poll['pollscore'].mean())
    predictors.append(i_predictors)
    this_poll[this_poll['candidate_name'] == 'Kamala Harris']['pct'].mean()

cleaned_response = []
cleaned_predictors = []
for i in range(len(response)):
    if isinstance(response[i], (int, float)) and not math.isnan(response[i]):  # Check for NaN in response
        if all(isinstance(x, (int, float)) and not math.isnan(x) for x in predictors[i]):  # Check for NaN in predictors
            cleaned_response.append(response[i])
            cleaned_predictors.append(predictors[i])

df = pd.DataFrame(cleaned_predictors, columns=['numeric_grade', 'sample_size', 'pollscore'])
df['scaled_trump_pct'] = cleaned_response  # Add the response (Trump percentage) as a new column

# Output to Excel
output_path = 'C:\\Users\\jason\\Desktop\\US_election_prediction\\data\\analysis_data\\analysis_data.xlsx'  # Specify the desired file name and path
df.to_excel(output_path, index=False)  # Export without row indices

print(f'Data successfully saved to {output_path}')
