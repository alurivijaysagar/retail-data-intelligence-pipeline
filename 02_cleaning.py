import pandas as pd

df = pd.read_excel("data/Online Retail.xlsx")

# --- Null Handling ---
df = df.dropna(subset=['CustomerID', 'Description'])
print(df.isnull().sum())

# --- Refund Mask ---
refund_mask = (
    (df['Quantity'] < 0) |
    (df['UnitPrice'] < 0) |
    (df['InvoiceNo'].str.startswith('C'))
)

refunds_df = df[refund_mask].copy()
sales_df = df[~refund_mask].copy()

# --- Duplicate Handling ---
subset_cols = ['InvoiceNo', 'StockCode', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID']
before_sales_dup = sales_df.duplicated(subset = subset_cols).sum()
before_refunds_dup = refunds_df.duplicated(subset=subset_cols).sum()

sales_df = sales_df.drop_duplicates(subset=subset_cols)
refunds_df = refunds_df.drop_duplicates(subset=subset_cols)

after_sales_dup = sales_df.duplicated(subset = subset_cols).sum()
after_refunds_dup = refunds_df.duplicated(subset = subset_cols).sum()
print(f"Before Sales Duplicates: {before_sales_dup}\n Before Refunds Duplicates: {before_refunds_dup}")
print(f"After Sales Duplicates: {after_sales_dup}\n After Refunds Duplicates: {after_refunds_dup}")
# --- Revenue ---
sales_df['Total_Price'] = sales_df['UnitPrice'] * sales_df['Quantity']
refunds_df['Total_Price'] = refunds_df['UnitPrice'] * refunds_df['Quantity']

sales_revenue = sales_df['Total_Price'].sum()
refunds_revenue = refunds_df['Total_Price'].sum()
total_revenue = sales_revenue + refunds_revenue

print(f"Sales Revenue: {sales_revenue}")
print(f"Refund Revenue: {refunds_revenue}")
print(f"Net Revenue: {total_revenue}")
print(sales_df.shape)
print(refunds_df.shape)
# --- Load ---
sales_df.to_csv("sales_clean.csv", index=False)
refunds_df.to_csv("refunds_clean.csv", index=False)


print("ETL Pipeline Complete. Files saved.")
