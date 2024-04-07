import pandas as pd 
import pyarrow as pa 
import os
import pyarrow.parquet as pq 


#converting the Customer_demographics data into parquet

acc_data_path = os.path.join('Data', 'csv', 'customer_demographics.csv')

# parquet_data_dir = os.path.join.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'parquet_data'))

customer_info =pd.read_csv(acc_data_path)
customer_info.to_parquet('customer_info.parquet', index= False)



# convert accunt data to parquet
customer_data_path = os.path.join('Data', 'csv', 'Acc_data.csv')
Acc_data = pd.read_csv(customer_data_path)
Acc_data.to_parquet('Acc_data.parquet', index= False)

print("conversion successful") 




