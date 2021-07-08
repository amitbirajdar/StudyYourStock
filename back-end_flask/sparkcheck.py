import mysql.connector
import pandas as pd
import pyspark.sql.functions as fc
import sys
import time
import os
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, SQLContext
from pyspark.context import SparkContext

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6'
os.environ['PYSPARK_DRIVER_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6'
os.environ["JAVA_HOME"] = '/Library/Java/JavaVirtualMachines/jdk1.8.0_241.jdk/Contents/Home'

conf = SparkConf().setAppName('sparkcheck.py').setMaster('local[*]')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
sqlCtx = SQLContext(sc)

time_s = time.time()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="project"
)

mycursor_comp = mydb.cursor()
mycursor_comp.execute("SELECT * FROM close where Date between '2021-01-01' and '2021-04-26'")

#df = sqlCtx.sql("SELECT * FROM close where Date between '2021-01-01' and '2021-04-26'")

dict_company = {}

df_company = pd.read_csv('data_description_1.txt', header=None)
df1 = df_company[0].values.tolist()

i = 2

for x in df1:
   dict_company[x] = i
   i = i + 1

file1 = open("myfile.txt", "w")

res = mycursor_comp.fetchall()
print(res)

for x in mycursor_comp:
    x = str(x)
    file1.write("".join(x))
    file1.write("\n")

file1.close()

data_company = pd.read_csv('myfile.txt', header=None)

sdf = sqlCtx.createDataFrame(data_company)

res = sdf[[str(dict_company['AAPL'])]]
res1 = res.describe()
#print(res1.show())

rdd_1 = res1.rdd
list_a = rdd_1.collect()

final_dict = {}

for i in list_a:
    #print(i)
    first_str = str(i)
    key_dict = first_str[first_str.find('=') + 2:first_str.find(',') - 1]
    value_dict = first_str[first_str.rfind('=') + 2: -2]
    #print(key_dict, value_dict)
    final_dict[key_dict] = value_dict




