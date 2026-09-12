```python
import pandas as pd
import os

# Read raw data
input_file = "data/raw/patient_nutrition_data.csv"

df = pd.read_csv(input_file)

print("Raw data loaded successfully!")
print(df.head())

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Convert height from cm to meters
df["Height_m"] = df["Height_cm"] / 100

# Calculate BMI
df["BMI"] = df["Weight_kg"] / (df["Height_m"] ** 2)

# Categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

df["BMI_Category"] = df["BMI"].apply(categorize_bmi)

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Save processed data
output_file = "data/processed/patient_nutrition_processed.csv"

df.to_csv(output_file, index=False)

print("ETL pipeline completed successfully!")
print(f"Processed data saved to: {output_file}")
```

