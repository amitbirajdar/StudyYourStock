import yfinance as yf
import json
import pandas as pd
import numpy as np

read_symbols = pd.read_csv('symbols.txt', header=None)
symbols = read_symbols[0].values.tolist()

companies = ['MSFT', 'TSLA', 'FB', 'AAPL', 'CSCO']

final_data = pd.DataFrame()
company = yf.Ticker('MSFT')
df = company.history(start="2021-04-24", end="2021-04-28")
df.reset_index(inplace=True)
final_data['Date'] = df['Date']

j = 0
for i in symbols:
    company = yf.Ticker(i)
    df = company.history(start="2021-04-24", end="2021-04-28")
    # df[i] = df.values.tolist()
    # print(df)
    # df.drop(['Open','High','Low','Close','Volume','Dividends', 'Stock Splits'], axis=1, inplace=True)
    
    df.reset_index(inplace=True)
    
    
    d = pd.DataFrame()
    d['Date'] = df['Date']
    d[i] = df['Volume']
    # # df.drop(['Dividends', 'Stock Splits','Open', 'High', 'Low', 'Volume'], axis=1, inplace=True)    
    # # print(df['Close'])
    # # final_data[i] = df['Close']
    final_data = pd.merge(left=final_data, right=d, how='left', left_on='Date', right_on='Date')
   
print(final_data)


final_data.fillna(np.nan, inplace=True)
final_data.set_index('Date', inplace=True)
with open('livedata.csv', 'w') as f:
    final_data.to_csv(f, header=i, line_terminator='\n')
    



