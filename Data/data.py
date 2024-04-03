#This Script generate data for internal_data used by FBN Bank. They top internal source of data is customer demographics

from faker import Faker
import pandas as pd 
from random import randint
import csv
import uuid
import random
from datetime import datetime, timedelta



fake = Faker('en_GH')

# Firs =, we will generate customer demographics data
# colums for the Demographicsn table are [ID, Name, DOB, Phone, Address, Ghana Card_no ]

# Account table = [customerID, account_no, account_type, balance]


# Firstly, create account let create a list that contain example of the data we want and then create synthetic version of it

# phone prefixes for phone numbers
phone_prefixes = ['55', '54', '25', '24', '20', '50', '27', '59', '57']
the_prefix = random.choice(phone_prefixes)

data = None

def customer_demographics(x):

    #create a dataframe

    global data 
    data = pd.DataFrame()

    for i in range(x):
        if i % 2000 == 0:  # Print progress every 1000 records
            print(f"Generated {i} records out of {x}")
        data.loc[i, 'ID'] = fake.uuid4()[:10]
        data.loc[i, 'Name'] = fake.name()
        data.loc[i, 'DOB'] = fake.date_of_birth(minimum_age= 18, maximum_age =65)
        data.loc[i, 'Phone'] = '233'+ str(the_prefix) + str(fake.random_number(digits =7))
        data.loc[i, 'Address'] = fake.address()
        data.loc[i, 'Nationality'] = "Ghanaian"
        data.loc[i, 'Ghana_Card'] = "GHA-" + str(fake.random_number(digits=9)) + "-" + str(randint(0, 10))
    return data

Faker.seed(18)
customer_demographics(100000)
data.to_csv("customer_demographics.csv", index = False)
print("data generated successfully")
