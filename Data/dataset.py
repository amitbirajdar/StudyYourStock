import json
import yfinance as yf
import pandas as pd
import numpy as np

read_symbols = pd.read_csv('symbols.txt', header=None)
symbols = read_symbols[0].values.tolist()

file = 'company_recommendations.json'

result = []
dict = {}

for i in symbols:
    company = yf.Ticker(i)
    info = company.recommendations
    if str(type(info))=="<class 'NoneType'>":
        continue
    else:
        info.reset_index(inplace=True)
        info_json = info.to_json() 
        j_object = json.dumps(info_json, indent=3)
        j_obj_new = json.loads(j_object)
        if i not in dict:
            dict[i] = j_obj_new

with open(file, 'w') as outfile:
    json.dump(dict, outfile, indent=3)


