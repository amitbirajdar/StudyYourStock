import mysql.connector
import pandas as pd

db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'amitbi07', database='project')

afile = open(r"C:\Users\Amit\Desktop\DSCI 551\Project\Data Generation\livedata.csv", 'r')

data = []
for line in afile:
    data.append(line)
val = data[1].split(',')
vals = [8851]
vals = vals + val
print(len(tuple(vals)))
cursor = db.cursor()
query = "INSERT INTO close VALUES ({})".format(tuple(vals))
cursor.execute(query)
db.commit()