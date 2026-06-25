import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

query = """
SELECT Region,
SUM(Sales) AS TotalSales
FROM sales
GROUP BY Region
"""

df = pd.read_sql(query, conn)

print(df)

df.to_csv("output/sales_summary.csv", index=False)

conn.close()

print("sales_summary.csv created successfully!")