import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cleaned_path = os.path.join(BASE_DIR, 'data', 'cleaned_expenses.csv')

df = pd.read_csv(cleaned_path)

df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%B')
df['Day'] = df['Date'].dt.day

df.to_csv(cleaned_path, index=False)

print("✅ Feature engineering completed successfully")
