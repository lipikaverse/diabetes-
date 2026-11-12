# Diabetes Progression Metrics

A beginner-friendly Python data analysis mini-project using the Kaggle Diabetes Prediction Dataset. The program separates records into diabetic and non-diabetic groups and calculates the mean BMI and mean blood glucose level for each group.

## Dataset

Download the CSV file from:
https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset

Place the downloaded file in the same folder as `diabetes_analysis.py`, with the filename:
`diabetes_prediction_dataset.csv`

## Requirements

- Python 3
- pandas

Install the dependency:

```bash
pip install -r requirements.txt
```

## Run

```bash
python diabetes_analysis.py
```

## What the program does

1. Loads the CSV dataset with Pandas.
2. Creates separate DataFrames for `diabetes == 1` and `diabetes == 0`.
3. Calculates mean BMI and mean blood glucose level for both groups.
4. Prints the patient counts and calculated averages.

## Dataset columns used

- `diabetes`: target indicator (1 = diabetes, 0 = no diabetes)
- `bmi`: body mass index
- `blood_glucose_level`: blood glucose level

## Note

The script prints results from the dataset file you download. Numerical results are intentionally not hard-coded because they should be calculated from the actual CSV.

## Reference

Kaggle, [Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset).
