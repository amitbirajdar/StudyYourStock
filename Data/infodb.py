import mysql.connector
import json
import pandas as pd
import yfinance as yf
import sys

db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'amitbi07', database='project')

cursor = db.cursor()

with open (r"C:\Users\Amit\Desktop\DSCI 551\Project\Data Generation\symbols.txt") as infofile:
    symbols = (infofile.read().splitlines())


args = sys.argv

value = []


query = "UPDATE info_data SET lastclose = (%s) WHERE symbol = '(%s)'"

for symbol in symbols:
    vals = []
    company = yf.Ticker(symbol)
    info = company.info
    vals.append(info['previousClose'])
    vals.append(symbol)
    cursor.execute(query, tuple(vals))

# vals.append('AESE')
# vals.append(info['shortName'])
# vals.append(info['previousClose'])
# vals.append(info['marketCap'])
# #vals.append(None)
# vals.append(info['website'])
# vals.append(info['logo_url'])
# sql = "INSERT INTO info_data (symbol, name, lastclose, marketCap, website, logo_url) VALUES (%s, %s, %s, %s, %s, %s)"
# cursor.execute(sql, tuple(vals))


# for i in range(0, 101):
#     vals = []
#     symbol = symbols[i]
#     company = yf.Ticker(symbol)
#     info = company.info
#     vals.append(symbol)
#     vals.append(info['shortName'])
#     vals.append(info['previousClose'])
#     vals.append(info['marketCap'])
#     #vals.append(None)
#     vals.append(info['website'])
#     vals.append(info['logo_url'])
#     sql = "INSERT INTO info_data (symbol, name, lastclose, marketCap, website, logo_url) VALUES (%s, %s, %s, %s, %s, %s)"
#     cursor.execute(sql, tuple(vals))
#value.append(tuple(vals))


# for i in value:
#     cursor.execute(sql, i)

db.commit()