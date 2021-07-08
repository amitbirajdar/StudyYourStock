from flask import Flask,jsonify,request
from flask_cors import CORS
import json
import mysql.connector
import pymongo
from pymongo import MongoClient
from pprint import pprint
import pandas as pd
import yfinance as yf
import os
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, SQLContext
from pyspark.context import SparkContext

app = Flask(__name__)

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6'
os.environ['PYSPARK_DRIVER_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6'
os.environ["JAVA_HOME"] = '/Library/Java/JavaVirtualMachines/jdk1.8.0_241.jdk/Contents/Home'

conf = SparkConf().setAppName('sparkcheck.py').setMaster('local[*]')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
sqlCtx = SQLContext(sc)

CORS(app,allow_headers="*")
#session secret key
app.secret_key = 'checkers'

user='root'
password='password'
host='localhost'
database='project'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["news_data"]
mycol = mydb["news_data_json_refined_1"]

dict = {}

mydoc = mycol.find()

df = pd.read_csv('data description.txt', header=None)
df1 = df[0].values.tolist()

i = 0

for x in mydoc:
   dict[df1[i]] = x['Company']
   i = i + 1

dict_company = {}

df_company = pd.read_csv('data_description_1.txt', header=None)
df1 = df_company[0].values.tolist()

i = 2

for x in df1:
   dict_company[x] = i
   i = i + 1

@app.route('/')
def hello_world():
   return jsonify("Hi")

@app.route('/api/company')
def company():
    cnx = mysql.connector.connect(user=user, password=password,host=host,database=database)
    cursor1 = cnx.cursor()
    sql1="SELECT * FROM project.info_data;"
    #sql2="DESCRIBE high;"
    cursor1.execute(sql1)
    res1=cursor1.fetchall()
    info=[]
    for i in res1:
        info.append(i)
    #print(info)
    return jsonify(info)

# @app.route('/api/company_data', methods = ['POST','GET'])
@app.route('/api/company_data/<company>/<from_date>/<end_date>', methods = ['GET'])
def company_data(company,from_date,end_date):
    if request.method=='GET':
        print(request.json)
        cnx = mysql.connector.connect(user=user, password=password,host=host,database=database)
        cursor1 = cnx.cursor()
        sql1="SELECT Date," + company + " FROM close where Date > '" + from_date + "' and Date <= '" + end_date + "' and " + company + " <> 'null' ;"
        # .format(request.json[0],request.json[1],request.json[2])
        #sql2="DESCRIBE high;"
        cursor1.execute(sql1)
        res1=cursor1.fetchall()
        info=[]
        for i in res1:
            info.append(i)
        # print(info)
        return jsonify(info)

@app.route('/api/company_news/<company>', methods = ['GET'])
def company_news(company):
    if request.method=='GET':
        info = []
        if company not in dict:
            return str(info)
        myquery = {"Company": dict[company]}
        mydoc1 = mycol.find(myquery)
        for i in mydoc1:
            for j in i['Statictics']['articles']:
                if j:
                    info.append(j)
                #val = str(j).encode('utf-8')
                #info.append(val.decode("utf-8"))
        if len(info) == 0:
            return str([])
        else:
            return jsonify(info)

@app.route('/api/stats/<start_date>', methods = ['GET'])
def company_stats(start_date):
    if request.method=='GET':
        cnx = mysql.connector.connect(user=user, password=password,host=host,database=database)
        cursor1 = cnx.cursor()
        sql1="SELECT * FROM close where Date > '{}' ;".format(start_date)
        cursor1.execute(sql1)
        res1=cursor1.fetchall()
        a = pd.read_sql(sql1, cnx)
        a.drop(['Date','index'], inplace=True, axis=1)
        a = a.bfill(axis=0)
        a = a.T
        n = len(a.columns)-1
        a['result'] = 100*(a[n]-a[0])/a[0]
        b = pd.DataFrame(index=a.index)
        w = pd.DataFrame(index=a.index)
        b['best'] = a['result']
        w['worst'] = a['result']
        worst = w.sort_values(by='worst')
        best = b.sort_values(by='best', ascending=False)
        best_dict = best[:10].to_dict()
        worst_dict = worst[:10].to_dict()
        best_list = []
        worst_list = []
        for i in best_dict['best']:
            best_list.append([i,best_dict['best'][i]])
        for i in worst_dict['worst']:
            worst_list.append([i,worst_dict['worst'][i]])
        return jsonify([best_list, worst_list])

@app.route('/api/<company>/live', methods = ['GET'])
def live(company):
    comp = yf.Ticker(company)
    data  =comp.history(period='1d', interval='1m')
    d = round(data['Close'],2)
    info = d.values.tolist()
    return jsonify(info)

@app.route('/api/<company>/summary')
def company_summary(company):

    cnx = mysql.connector.connect(user=user, password=password,host=host,database=database)
    cursor1 = cnx.cursor()

    sql1 = "SELECT * FROM close where Date between '2021-01-01' and '2021-04-26'"
    summary = pd.read_sql(sql1, cnx)

    summary_comp = pd.DataFrame()
    summary_comp[company] = summary[company]

    sdf = sqlCtx.createDataFrame(summary_comp)

    res1 = sdf.describe()
    rdd_1 = res1.rdd
    list_a = rdd_1.collect()

    final_dict = {}
    #
    for i in list_a:
         first_str = str(i)
         key_dict = first_str[first_str.find('=') + 2:first_str.find(',') - 1]
         value_dict = first_str[first_str.rfind('=') + 2: -2]
         final_dict[key_dict] = value_dict

    info = []
    for key,value in final_dict.items():
        info.append(round(float(value), 2))

    return jsonify(info)

if __name__ == '__main__':
   app.run(debug=True,port=8000)
