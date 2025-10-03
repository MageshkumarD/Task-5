 Data Analysis on CSV Files(sales of product & region)
This guide shows a clear, step-by-step process to read the three CSV files you provided, validate them, compute summaries and checks (roll-ups by product and region), and produce simple visual outputs. The sample code uses Python with pandas and matplotlib/seaborn and is ready to run as a single script or in a notebook.

Required libraries and files
language : Python 
pandas for data manipulation
matplotlib and seaborn for plots (optional)
Files expected in the working directory: sales.csv, sales_by_product.csv, sales_by_region.csvsteps

The steps;
1.Load the three CSV files into pandas DataFrames.
2.Inspect each DataFrame for shape, columns, dtypes, missing values, and sample rows.
3.Clean types if needed (ensure Sales is numeric, Region/Product are strings).
4.Compute aggregations from the raw detailed file (sales.csv): totals by Product and totals by Region.
5.Compare these computed aggregates to the provided summary files (sales_by_product.csv, sales_by_region.csv) and report any mismatches.
6.Produce simple visualizations: bar charts for Sales by Product and Sales by Region.
7.Save or print reconciliation results and plots.

Sample output:
*Computed totals from sales.csv:
By Product: Laptop = 3000, Phone = 2050, Tablet = 1400.
By Region: North = 2100, South = 1750, East = 1400, West = 1200.

*Reconciliation should show no mismatches because the provided summary files match those computed totals exactly.

*Two bar charts: one showing product ranking (Laptop highest) and one showing region totals.
