import pandas as pd

# Read the raw patient data
df = pd.read_csv("data/raw/patient_nutrition_data.csv")

# Show the first rows
print("Original Data:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate patients
df = df.drop_duplicates(subset=["patient_id"])

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

# Convert follow-up date
df["follow_up_date"] = pd.to_datetime(
    df["follow_up_date"],
    errors="coerce"
)

# Calculate BMI
df["BMI"] = df["weight_kg"] / (df["height_cm"] / 100) ** 2

# Create BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

df["BMI_Category"] = df["BMI"].apply(bmi_category)

# Round BMI
df["BMI"] = df["BMI"].round(2)

# Show processed data
print("\nProcessed Data:")
print(df)

print("\nETL pipeline completed successfully!")
