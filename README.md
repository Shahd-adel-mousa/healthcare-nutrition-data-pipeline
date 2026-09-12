# Healthcare Nutrition Data Engineering Pipeline

An end-to-end data engineering project that processes synthetic healthcare and nutrition data through an ETL pipeline.

The project demonstrates how raw patient nutrition data can be extracted, cleaned, transformed, validated, and prepared for analytics and database storage.

> **Note:** This project uses fully synthetic patient data for educational purposes. No real patient or personally identifiable information is used.

---

## Project Overview

Healthcare and nutrition data often comes from different sources and may contain missing values, duplicate records, inconsistent formats, and data quality issues.

This project simulates a healthcare nutrition data pipeline that transforms raw patient data into a clean and analysis-ready dataset.

### Data Pipeline

```text
Raw Patient Data
       ↓
    Extract
       ↓
     Clean
       ↓
   Transform
       ↓
Data Validation
       ↓
Processed Dataset
       ↓
  SQL Database
       ↓
   Analytics
Project Objectives
Build a practical ETL pipeline using Python and Pandas
Clean and validate healthcare-related nutrition data
Calculate BMI from patient height and weight
Categorize patients based on BMI
Produce a structured processed dataset
Prepare data for SQL database storage
Demonstrate data engineering concepts in a healthcare and nutrition context
Dataset

The dataset contains fully synthetic patient nutrition information.

Raw Data Columns
Column	Description
patient_id	Unique patient identifier
age	Patient age
gender	Patient gender
height_cm	Height in centimeters
weight_kg	Weight in kilograms
diagnosis	General health/nutrition diagnosis
calories	Daily calorie target
protein_g	Daily protein target in grams
activity_level	Patient activity level
follow_up_date	Scheduled follow-up date
Processed Data Columns

The ETL pipeline generates additional features:

Column	Description
height_m	Height converted from centimeters to meters
bmi	Body Mass Index
bmi_category	BMI classification
ETL Pipeline
1. Extract

The pipeline loads raw patient nutrition data using Pandas.

df = pd.read_csv("data/raw/patient_nutrition_data.csv")
2. Clean

The cleaning stage includes:

Removing duplicate records
Handling missing values
Converting numeric columns to appropriate data types
Validating patient measurements
3. Transform

The pipeline transforms the data by:

Converting height from centimeters to meters
Calculating BMI
Creating BMI categories

BMI is calculated using:

BMI = weight (kg) / height (m)²

BMI categories used in this educational project:

Underweight
Normal
Overweight
Obese
4. Data Quality Validation

The pipeline validates important measurements and removes invalid records.

Validation rules include:

Height must be greater than zero
Weight must be greater than zero
Calories must be greater than zero
Protein must be greater than zero
BMI must be within a reasonable range
5. Load

The cleaned and transformed dataset is exported as:

data/processed/patient_nutrition_processed.csv

The processed dataset is ready for further analysis or loading into a SQL database.

Project Structure
healthcare-nutrition-data-pipeline/
│
├── data/
│   ├── raw/
│   │   └── patient_nutrition_data.csv
│   │
│   └── processed/
│       └── patient_nutrition_processed.csv
│
├── src/
│   └── etl_pipeline.py
│
└── README.md
Technologies Used
Python
Pandas
SQL
MySQL
ETL
Data Cleaning
Data Transformation
Data Quality Validation
Git
GitHub
Skills Demonstrated
Data Engineering
ETL pipeline development
Data extraction
Data cleaning
Data transformation
Data validation
Structured data processing
CSV data processing
Python
Pandas
DataFrames
Functions
Loops
Conditional logic
File handling
Healthcare & Nutrition
Patient nutrition data modeling
BMI calculation
Nutrition-related metrics
Healthcare data processing
Version Control
Git
GitHub
Repository organization
Project documentation
Future Improvements

The project can be extended by adding:

MySQL database integration
SQL tables and analytical queries
Apache Airflow orchestration
Data quality monitoring
Power BI dashboard
Healthcare nutrition analytics
Automated ETL scheduling
Microsoft Azure integration
Apache Spark for large-scale data processing
Project Status

Current Status: ETL Pipeline Completed

The project currently includes:

Synthetic raw healthcare nutrition data
Python ETL pipeline
Data extraction
Data cleaning
Data transformation
BMI calculation
BMI categorization
Data quality validation
Processed dataset
Next Stage

The next stage will focus on:

SQL Database → Analytics → Data Visualization → Cloud Integration

Author

Shahd Adel Mousa

Clinical Nutrition | Data Engineering

Interested in building data engineering solutions for healthcare and nutrition.

Disclaimer

This project is created for educational and portfolio purposes.

All patient information used in this project is synthetic and does not represent real individuals or real clinical records.
