import mysql.connector
import json
import pandas as pd
import pymysql
from pandas.io import sql
from sqlalchemy import create_engine
import numpy as np
from math import isnan

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root", pw="amitbi07", db="project"))

companies = ['MSFT', 'TSLA', 'FB', 'AAPL', 'CSCO']


with open(r'C:\Users\Amit\Desktop\DSCI 551\Project\Data Generation\livedata.csv', 'r') as livedata:
    data = pd.read_csv(livedata)


# df = pd.DataFrame(columns=data.columns)
# df['Datetime'] = data['Datetime']

# for i in range(data.shape[0]):
#     for j in data.columns:
#         if j != 'Datetime':
#             a = data.iloc[i][j]
#             if isinstance(a, str):
#                 a = a.translate({ord(c): "" for c in "[]"}).split(", ")
#                 open_price = round(float(a[0]),3)
#                 df.iloc[i][j] = open_price
# print(data)
data.to_sql(con=engine, name='live', if_exists='replace')
