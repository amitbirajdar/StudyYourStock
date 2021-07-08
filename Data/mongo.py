import pymongo
import json
from pymongo import MongoClient
from pprint import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print(myclient.list_database_names())

db = myclient["news_data"]

Collection = db["news_data_json_refined"]

with open('news_dataset_3.json') as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)

mydb = myclient["news_data"]
mycol = mydb["news_data_json_refined"]

myquery = {"Company": "apple"}

mydoc = mycol.find(myquery)

for x in mydoc:
   pprint(x)