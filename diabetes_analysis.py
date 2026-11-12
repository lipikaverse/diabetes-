"""Analyze BMI and blood glucose averages by diabetes status."""

from pathlib import Path
import pandas as pd


DATASET_PATH = Path(__file__).with_name("diabetes_prediction_dataset.csv")


def main():
    # Load the dataset
    df = pd.read_csv(DATASET_PATH)

    # Separate patients into two DataFrames
    diabetic_patients = df[df["diabetes"] == 1]
    non_diabetic_patients = df[df["diabetes"] == 0]

    # Calculate mean BMI and mean blood glucose level
    diabetic_mean_bmi = diabetic_patients["bmi"].mean()
    non_diabetic_mean_bmi = non_diabetic_patients["bmi"].mean()

    diabetic_mean_glucose = diabetic_patients["blood_glucose_level"].mean()
    non_diabetic_mean_glucose = non_diabetic_patients["blood_glucose_level"].mean()

    # Display results
    print("DIABETES PROGRESSION METRICS")
    print("-" * 32)

    print("\nPatients with Diabetes:")
    print("Total Patients:", len(diabetic_patients))
    print("Mean BMI:", round(diabetic_mean_bmi, 2))
    print("Mean Blood Glucose Level:", round(diabetic_mean_glucose, 2))

    print("\nPatients without Diabetes:")
    print("Total Patients:", len(non_diabetic_patients))
    print("Mean BMI:", round(non_diabetic_mean_bmi, 2))
    print("Mean Blood Glucose Level:", round(non_diabetic_mean_glucose, 2))


if __name__ == "__main__":
    main()
