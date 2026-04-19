import pandas as pd

df = pd.read_excel("data/Online Retail.xlsx")

# print(df) used to print the whole dataset not recommended. 

#print(df.head())  Used to print the first 5 rows of the dataset to get an Initial idea how the data is stored and what does it describe.

# print(df.head(40)) 

#print(df.tail()) # Used to print the last 5 rows in a dataset or a excel file.

#print(df.tail(10))

#print(df.shape) # Used to tell how big the dataset size 

#print(df.columns) #used to print the columns in the excel file 

#df.info() # gives information about the dataset including the data type 

print(df.describe())

target_value = 0
found_rows = df[df['Quantity','UnitPrice']< target_value]
print(found_rows)