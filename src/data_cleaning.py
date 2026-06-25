import pandas as pd

df = pd.read_csv("data/sales_data.csv", encoding="latin1")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove rows with missing values
df.dropna(inplace=True)

# Save cleaned data
df.to_csv("output/cleaned_sales.csv", index=False)

print("Data cleaned successfully!")