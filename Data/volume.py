import mysql.connector
import json
import pandas as pd
import pymysql
from pandas.io import sql
from sqlalchemy import create_engine
import numpy as np
from math import isnan

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root", pw="amitbi98", db="project"))

symbols = pd.read_csv(r'C:\Users\Amit\Desktop\DSCI 551\Project\Data Generation\symbols.txt', header=None)
symbols.columns=['Symbol']

with open(r'C:\Users\Amit\Desktop\DSCI 551\Project\Data Generation\stockdata.csv', 'r') as stockdata:
    data = pd.read_csv(stockdata)

df = pd.DataFrame(columns=data.columns)
df['Date'] = data['Date']


for i in range(data.shape[0]):
    for j in data.columns:
        if j != 'Date':
            a = data.iloc[i][j]
            open_price = round(float(a[4]),3)
            df.iloc[i][j] = open_price

df.to_sql(con=engine, name='volume', if_exists='replace')


for i in range(data.shape[0]):
    for j in data.columns:
        if j != 'Date':
            a = data.iloc[i][j]
            if isinstance(a, str):
                a = a.translate({ord(c): "" for c in "[]"}).split(", ")
                open_price = round(float(a[4]),3)
                df.iloc[i][j] = open_price

df.to_sql(con=engine, name='volume', if_exists='replace')
