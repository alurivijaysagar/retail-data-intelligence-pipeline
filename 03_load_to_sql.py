import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus


sales_df = pd.read_csv('sales_clean.csv')
refunds_df = pd.read_csv('refunds_clean.csv')

print("Sucessfully loaded sales and refunds CSV files")

 
 
try:
    print("Trying to connect...")
    password = quote_plus('YOUR_MYSQL PASSWORD')
    engine = create_engine(f'mysql+pymysql://root:{password}@localhost/retail_db')
    print("Engine created...")
    connection = engine.connect()
    print("Connected to MySQL successfully.")
    sales_df.to_sql('sales', con=engine, if_exists='replace', index=False)
    refunds_df.to_sql('refunds', con=engine, if_exists='replace', index=False)
    print("Data loaded into MySQL successfully.")
    connection.close()
except Exception as e:
    print(f"Error: {e}")
 

 