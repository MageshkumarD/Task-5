

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales.csv")

print("First 5 rows of dataset:")
print(data.head(), "\n")

print("Dataset Info:")
print(data.info(), "\n")

print("Summary Statistics:")
print(data.describe(), "\n")

if 'Product' in data.columns and 'Sales' in data.columns:
    sales_by_product = data.groupby("Product")["Sales"].sum().reset_index()
    print("Total Sales by Product:")
    print(sales_by_product, "\n")

    plt.figure(figsize=(8,5))
    plt.bar(sales_by_product["Product"], sales_by_product["Sales"], color="purple")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if 'Region' in data.columns and 'Sales' in data.columns:
    sales_by_region = data.groupby("Region")["Sales"].sum().reset_index()
    print("Total Sales by Region:")
    print(sales_by_region, "\n")

    plt.figure(figsize=(8,5))
    plt.bar(sales_by_region["Region"], sales_by_region["Sales"], color="black")
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

sales_by_product.to_csv("sales_by_product.csv", index=False)
sales_by_region.to_csv("sales_by_region.csv", index=False)

print("Analysis complete! Grouped results saved as CSV files.")
