# US Election Prediction

## Overview

This repository contains the files and code used to build a linear model to predict the outcome of the upcoming US presidential election using poll-of-polls data. The project involves cleaning, analyzing, and modeling data from various sources, including polling data obtained from FiveThirtyEight and The Bullfinch Group. The analysis explores the effect of variables such as pollster ratings, sample size, and poll score on the predicted vote percentage for Donald Trump, with a focus on creating reproducible workflows.

## File Structure

The repository is organized as follows:

- `data/raw_data`: Contains the raw data as obtained from sources such as FiveThirtyEight and The Bullfinch Group.
- `data/analysis_data`: Contains the cleaned dataset used for analysis and modeling.
- `models`: Contains the fitted models, including saved models in `.pkl` format.
- `other/llm_usage`: Documents any assistance from ChatGPT-4o.
- `paper`: Contains the files used to generate the final paper.
    - `paper.qmd`: The Quarto document that includes the analysis and narrative.
    - `paper.pdf`: The compiled version of the paper.
    - `references.bib`: Bibliography file with references cited in the paper.
- `scripts`: Contains the Python scripts used in the project.
    - `data_cleaning.py`: Clean the data to extract those for fitting model.
    - `model_fitting.py`: Output a fitted model in `.pkl` format.
    - `prediction.py`: Use polls-and-polls to predict percentage of vote of Donald Trump.


## Statement on LLM usage

Aspects of the code were written with the help of the auto-complete tool. Some conceptual clarifications and coding assistance were provided by ChatGPT, and the relevant conversation logs are documented in `other/llm_usage`. However, the core analysis and modeling were designed and executed by the author.

## Methodology

### Data Sources

The polling data was sourced from:
- FiveThirtyEight: [2024 National Presidential General Election Polls](https://projects.fivethirtyeight.com/polls/president-general/2024/national/)
- Bullfinch Group: [Public Release of Bullfinch Q3 Nationwide Survey](https://www.thebullfinchgroup.com/post/public-release-of-bullfinch-q3-nationwide-survey-2)

### Key Steps

1. **Data Cleaning**: The raw data from FiveThirtyEight and Bullfinch Group was cleaned and processed to prepare it for analysis.
3. **Modeling**: A linear model was fitted using predictors like `numeric_grade`, `sample_size`, and `pollscore` to predict the percentage of votes for Donald Trump. 
4. **Prediction**: The election prediction was made by averaging predictor values and applying them to the fitted model.


Feel free to explore the repository and reach out if you have any questions or suggestions.
