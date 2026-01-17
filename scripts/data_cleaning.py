import pandas as pd
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_path = os.path.join(BASE_DIR, 'data', 'raw_expenses.csv')
cleaned_path = os.path.join(BASE_DIR, 'data', 'cleaned_expenses.csv')

# Load raw data
df = pd.read_csv(raw_path)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Handle missing values
df['Category'] = df['Category'].fillna('Unknown')
df['Payment_Method'] = df['Payment_Method'].fillna('Unknown')
df['Amount'] = df['Amount'].fillna(0)

# Remove duplicates
df = df.drop_duplicates()

# Standardize text
df['Category'] = df['Category'].str.title()
df['Payment_Method'] = df['Payment_Method'].str.title()

# Save cleaned data
df.to_csv(cleaned_path, index=False)

print("✅ cleaned_expenses.csv created successfully")
