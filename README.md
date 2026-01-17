# expense-tracker-powerbi
Personal expense analysis with Python, PostgreSQL, and Power BI dashboards
# 📊 Smart Expense Tracker with Spending Insights
## 📌 Project Overview

The Smart Expense Tracker with Spending Insights is an end-to-end data analytics project that analyzes personal expense data to uncover spending patterns and trends.
The project demonstrates a complete analytics workflow — from raw data ingestion and cleaning to structured storage and interactive dashboard visualization.

This project is designed to showcase Python, SQL, and Power BI skills in a practical, resume-ready format.

## 🎯 Project Objectives
  - Clean and transform raw expense data using Python
  - Store processed data in a relational database (PostgreSQL)
  - Perform category-wise and time-based spending analysis
  - Build an interactive Power BI dashboard with KPIs and filters
  - Generate actionable spending insights

## 🛠️ Tech Stack
  - Python (Pandas)
  - PostgreSQL
  - SQLAlchemy
  - Power BI Desktop
  - DAX

## 📂 Project Structure
  Smart-Expense-Tracker/
    │
    ├── data/
    │   ├── raw_expenses.csv
    │   ├── cleaned_expenses.csv
    │
    ├── scripts/
    │   ├── data_cleaning.py
    │   ├── feature_engineering.py
    │   ├── load_to_postgres.py
    │
    ├── powerbi/
    │   ├── expense_dashboard.pbix
    │
    ├── README.md

## 📥 Data Description

The expense dataset includes the following fields:

| Column Name      | Description                               |
|-----------------|--------------------------------------------|
| Date            | Date of expense                            |
| Amount          | Expense amount                             |
| Category        | Expense category (Food, Rent, Travel, etc.)|
| Payment_Method  | Mode of payment                            |
| Description     | Optional notes                             |
| Month           | Extracted month                            |
| Year            | Extracted year                             |
----------------------------------------------------------------

## 🔄 Data Processing Workflow

### 1️⃣ Data Ingestion
- Raw expense data is loaded from a CSV file.  
- Data represents daily personal spending records.

### 2️⃣ Data Cleaning (Python – Pandas)
- Converted date fields to proper datetime format.  
- Handled missing values in category, amount, and payment method.  
- Removed duplicate records.  
- Standardized category and payment method names.

### 3️⃣ Feature Engineering
- Created additional columns:
  - Month  
  - Year  
- Enabled time-based trend analysis.

### 4️⃣ Data Storage (PostgreSQL)
- Cleaned and enriched data loaded into PostgreSQL using SQLAlchemy.  
- Structured storage enables efficient querying and Power BI integration.

---

## 📊 Power BI Dashboard Features

### 🔹 KPIs
- Total Expenses  
- Average Monthly Spending  
- Highest Spending Category  
- Month-over-Month (MoM) Change

### 🔹 Visualizations
- **Bar Chart:** Category-wise spending  
- **Line Chart:** Monthly spending trend  
- **Donut Chart:** Payment method distribution  
- **Table:** Top 5 highest expenses

### 🔹 Filters (Slicers)
- Date (single-day selection)  
- Expense category  
- Payment method

> All visuals are fully interactive and dynamically update based on slicer selections.
