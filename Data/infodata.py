import yfinance as yf
import json
import pandas as pd
import numpy as np

final_data = pd.DataFrame(columns={'Insiders', 'Institutions','Float', 'Number of Institutions Holding Shares'})
read_symbols = pd.read_csv('symbols.txt', header=None)
symbols = read_symbols[0].values.tolist()

company = yf.Ticker(symbols[0])
infoT = (company.major_holders).T




for i in symbols[1:]:
    company = yf.Ticker(i)
    info1T = (company.major_holders).T
    infoT = pd.concat([infoT.iloc[0], info1T.iloc[0]], ignore_index=True, axis=1)
    
print(infoT)