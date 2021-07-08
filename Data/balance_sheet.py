import yfinance as yf
import json
import pandas as pd
import numpy as np

company = yf.Ticker('MSFT')
f = company.dividends
d = str(f.index[0])
a = d.split('-')
c = a[0]+'-'+a[1]
print(c)

# symbols = pd.read_csv(r'C:\Users\Amit\Desktop\DSCI 551\Project\Data Generation\symbols.txt', header=None)
# symbols.columns=['Symbol']
#print(symbols)
# dict = {i:{} for i in symbols["Symbol"]}

# for symbol in symbols["Symbol"]:
#     company = yf.Ticker(symbol)
#     financials = company.institutional_holders
    
#     if financials is not None:
#         financials['Date Reported'] = financials['Date Reported'].astype(str)
#         financials.index = np.arange(1, len(financials) + 1)
#         financials = financials.T
#         fin = financials.to_dict()
#         dict[symbol] = fin
#     fin = {}

# print(dict)
# with open("holdings.json", "w") as outfile:  
#     json.dump(dict, outfile, indent=4) 