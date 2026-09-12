```python
import pandas as pd
import os

# 1. Extract
input_file = "data/raw/patient_nutrition_data.csv"
df = pd.read_csv(input_file)

print("Raw data loaded successfully!")
print(df.head())

# 2. Clean
df = df.drop_duplicates()
df = df.dropna()

# Convert numeric columns
numeric_columns = [
    "age",
    "height_cm",
    "weight_kg",
    "calories",
    "protein_g"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.dropna()

# 3. Transform
df["height_m"] = df["height_cm"] / 100

df["bmi"] = df["weight_kg"] / (df["height_m"] ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

df["bmi_category"] = df["bmi"].apply(categorize_bmi)

# 4. Data Quality Validation
df = df[
    (df["height_cm"] > 0) &
    (df["weight_kg"] > 0) &
    (df["bmi"] > 0) &
    (df["bmi"] < 100)
]

# 5. Load
os.makedirs("data/processed", exist_ok=True)

output_file = "data/processed/patient_nutrition_processed.csv"

df.to_csv(output_file, index=False)

print("ETL pipeline completed successfully!")
print(f"Processed data saved to: {output_file}")
```
