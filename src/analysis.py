import pandas as pd

df = pd.read_csv("output/cleaned_sales.csv")

print(df.head())

print(df.describe())

print(df.groupby("Category")["Sales"].sum())

print(df.groupby("Region")["Profit"].sum())