import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# aws s3 bucket details

bucket_name = 'fbn-bank-bucket'
folder_name = 'customer-data'
key1= f'{folder_name}/Acc_data.parquet'
key2= f'{folder_name}/customer_info.parquet'

# getting aws credentials from env variables

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key =os.getenv('AWS_SECRET_ACCESS_KEY')

# S3 client

s3 = boto3.client('s3', aws_access_key_id= aws_access_key_id, aws_secret_access_key=aws_secret_access_key)


file1 = '/Users/james/FBN_Bank/Data/parquet_data/Acc_data.parquet' 
file2 = '/Users/james/FBN_Bank/Data/parquet_data/customer_info.parquet'
#uploading to the the bucket

s3.upload_file(file1, bucket_name, key1)
s3.upload_file(file2, bucket_name, key2)

print("parquet files uploaded to s3 bucket successfully")

import os
print(os.path.abspath('Acc_data.parquet'))
