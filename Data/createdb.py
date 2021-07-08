import mysql.connector
import json
import pandas as pd

db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'amitbi98')

cursor = db.cursor()

# Create new database
cursor.execute('CREATE DATABASE project') 
