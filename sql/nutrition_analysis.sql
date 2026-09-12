-- Healthcare Nutrition Data Pipeline
-- SQL Analytics

-- Create patients nutrition table
CREATE TABLE patient_nutrition (
    patient_id INTEGER PRIMARY KEY,
    age INTEGER,
    gender VARCHAR(20),
    height_cm DECIMAL(5,2),
    weight_kg DECIMAL(5,2),
    diagnosis VARCHAR(100),
    calories INTEGER,
    protein_g DECIMAL(6,2),
    activity_level VARCHAR(20),
    follow_up_date DATE,
    height_m DECIMAL(5,2),
    bmi DECIMAL(5,2),
    bmi_category VARCHAR(20)
);

-- ==========================================
-- Basic Analysis
-- ==========================================

-- 1. Number of patients
SELECT COUNT(*) AS total_patients
FROM patient_nutrition;

-- 2. Average BMI
SELECT ROUND(AVG(bmi), 2) AS average_bmi
FROM patient_nutrition;

-- 3. Average weight
SELECT ROUND(AVG(weight_kg), 2) AS average_weight
FROM patient_nutrition;

-- 4. Average daily calories
SELECT ROUND(AVG(calories), 2) AS average_calories
FROM patient_nutrition;

-- ==========================================
-- Healthcare Analysis
-- ==========================================

-- 5. Patients by diagnosis
SELECT
    diagnosis,
    COUNT(*) AS patient_count
FROM patient_nutrition
GROUP BY diagnosis
ORDER BY patient_count DESC;

-- 6. BMI category distribution
SELECT
    bmi_category,
    COUNT(*) AS patient_count
FROM patient_nutrition
GROUP BY bmi_category
ORDER BY patient_count DESC;

-- 7. Average BMI by diagnosis
SELECT
    diagnosis,
    ROUND(AVG(bmi), 2) AS average_bmi
FROM patient_nutrition
GROUP BY diagnosis
ORDER BY average_bmi DESC;

-- 8. Average calories by activity level
SELECT
    activity_level,
    ROUND(AVG(calories), 2) AS average_calories
FROM patient_nutrition
GROUP BY activity_level
ORDER BY average_calories DESC;

-- 9. Patients with BMI above 30
SELECT
    patient_id,
    age,
    gender,
    weight_kg,
    bmi,
    diagnosis
FROM patient_nutrition
WHERE bmi >= 30
ORDER BY bmi DESC;

-- 10. Patients requiring follow-up
SELECT
    patient_id,
    diagnosis,
    bmi,
    follow_up_date
FROM patient_nutrition
ORDER BY follow_up_date;
