An end-to-end ETL pipeline that processes 541,000+ real-world retail 
transactions — from raw messy Excel data to a clean, query-ready MySQL 
analytics database.

## What This Project Does

Raw retail data is messy. Invoices are duplicated, refunds are mixed 
with sales, customer IDs are missing. This pipeline solves that.

It extracts raw data, applies intelligent transformation logic, and 
loads clean, separated datasets into a production MySQL database — 
ready for business intelligence queries.

## Pipeline Architecture

| Step | Description |
|------|-------------|
| 1 | Raw Excel input (541,909 rows) |
| 2 | Extract & load into Pandas |
| 3 | Detect & flag duplicates |
| 4 | Separate Sales vs Refunds (3-condition logic) |
| 5 | Calculate revenue metrics |
| 6 | Export clean CSVs |
| 7 | Load into MySQL (530,033 sales + 10,414 refunds) |

## Key Technical Decisions

**Refund Detection Logic**
Refunds were identified using 3 conditions — not just one:
- InvoiceNo starting with 'C' (cancellation)
- Quantity less than 0
- UnitPrice less than 0

Using all 3 conditions catches edge cases that a single filter misses.

**Deduplication Strategy**
Used subset-based deduplication on meaningful columns only 
(InvoiceNo, StockCode, Quantity, UnitPrice, CustomerID) instead of 
full row matching — preventing deletion of legitimate transactions 
that share some but not all values.

## Tech Stack

- Python 3.13
- Pandas
- NumPy  
- SQLAlchemy
- PyMySQL
- MySQL 8.4

## Results

| Metric | Value |
|--------|-------|
| Raw transactions processed | 541,909 |
| Clean sales records | 530,033 |
| Refund transactions isolated | 10,414 |
| Database | MySQL retail_db |

## Project Structure

```
retail-data-intelligence-pipeline/
├── src/
│   ├── 01_extract.py        # Load raw Excel data
│   ├── 02_cleaning.py       # Transform and clean
│   └── 03_load_to_sql.py    # Load into MySQL
├── data/
│   └── processed/           # Clean CSVs output
└── README.md
```

## Author

A.V.M. Vijay Sagar  
B.Tech CSE — KL University Hyderabad  
[LinkedIn](https://www.linkedin.com/in/aluri-vijay-sagar-75a5342b8/)
