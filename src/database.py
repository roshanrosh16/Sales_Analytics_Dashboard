import pandas as pd
import sqlite3

# Read CSV file
df = pd.read_csv("data/sales_data.csv", encoding="latin1")

# Create database
conn = sqlite3.connect("sales.db")

# Create table named sales
df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()

print("Database and sales table created successfully!")