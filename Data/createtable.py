import mysql.connector
import json
import pandas as pd

db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'amitbi07', database='project')
cursor = db.cursor()

# create company_info table
#'logo_url','symbol','regularMarketPreviousClose'
cursor.execute('CREATE TABLE info_data (symbol VARCHAR(10) PRIMARY KEY,name VARCHAR(100), lastclose FLOAT(20,2), marketCap FLOAT(20,2), website VARCHAR(200), logo VARCHAR(200))')

# create  table
# '''
# tables = ['open', 'high', 'low', 'close', 'volume']
# # for table in tables:
# #     cursor.execute('CREATE TABLE %s (date DATE)' %table) 


# symbols = pd.read_csv(r'C:\Users\Amit\Desktop\DSCI 551\Project\Data Generation\symbols.txt', header=None)
# symbols.columns=['Symbol']

# # set columns

# for table in tables:
#     for symbol in symbols['Symbol']:
#         query = "ALTER TABLE %s ADD COLUMN %s FLOAT(20,2)" %(table,symbol)
#         cursor.execute(query)
# '''
db.commit()

