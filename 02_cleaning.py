import pandas as pd

# ── Extract  
df = pd.read_excel(r"C:\online-retail-project\data\Online Retail.xlsx")

# ── Null Handling  
print("Null values before cleaning:")
print(df.isnull().sum())

df = df.dropna(subset=['CustomerID'])
df = df.dropna(subset=['Description'])

print("\nNull values after cleaning:")
print(df.isnull().sum())

# ── Duplicate Detection  
duplicates_df = df[df.duplicated(
    subset=['InvoiceNo', 'StockCode', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID'],
    keep=False
)].sort_values(by=['InvoiceNo', 'StockCode'])

print(f"\nDuplicate records found: {len(duplicates_df)}")

# ── Revenue Feature  
df['revenue'] = df['Quantity'] * df['UnitPrice']

# ── Separate Sales vs Refunds 
refund_mask = (
    (df['Quantity'] < 0) |
    (df['UnitPrice'] < 0) |
    (df['InvoiceNo'].str[0] == 'C')
)

refunds_df = df[refund_mask]
sales_df = df[~refund_mask]

# ── Revenue Metric 
sales_revenue = (sales_df['Quantity'] * sales_df['UnitPrice']).sum()
refunds_revenue = (refunds_df['Quantity'] * refunds_df['UnitPrice']).sum()
net_revenue = sales_revenue + refunds_revenue

print(f"\nSales records: {len(sales_df)}")
print(f"Refund records: {len(refunds_df)}")
print(f"Net Revenue: £{net_revenue:,.2f}")

# ── Load  
sales_df.to_csv('sales_clean.csv', index=False)
refunds_df.to_csv('refunds_clean.csv', index=False)

summary_df = pd.DataFrame([{
    'Total Sales Revenue': sales_revenue,
    'Total Refunds': refunds_revenue,
    'Net Revenue': net_revenue
}])
summary_df.to_csv('revenue_summary.csv', index=False)

print("\nETL Pipeline Complete. Files saved.")