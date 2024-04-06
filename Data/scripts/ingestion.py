import boto3
import pandas as pd 
import pyarrow as pa 
import pyarrow.parquet as pq 


# first Converting the csv files into parquet

customer_data_path = "/Users/james/FBN_Bank/Data/csv/customer_demographics.csv"
acc_data_path = "/Users/james/FBN_Bank/Data/csv/Acc_data.csv"


# convert accunt data to parquet
Acc_data = pd.read_csv(acc_data_path)
Account_data = pa.Table.from_pandas(Acc_data)

Account_parquet_path = "/Users/James/FBN_Bank/Data/parquet/acc_data.parquet"
pq.write_table(Account_data, Account_parquet_path)


