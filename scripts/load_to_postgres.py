import pandas as pd
from sqlalchemy import create_engine
import os

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, 'data', 'cleaned_expenses.csv')

# PostgreSQL credentials
username = 'postgres'
password = 'admin123'     # use your real password
host = 'localhost'
port = '5432'
database = 'expense_tracker'

engine = create_engine(
    f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
)

# Load data
df = pd.read_csv(csv_path)

# Write to DB
df.to_sql(
    'expenses',
    engine,
    schema='public',
    if_exists='replace',
    index=False
)

engine.dispose()

print("✅ Data successfully loaded into PostgreSQL")
