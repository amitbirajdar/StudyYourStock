import yfinance as yf
import json
import pandas as pd
import numpy as np

read_symbols = pd.read_csv('symbols.txt', header=None)
symbols = read_symbols[0].values.tolist()

company = yf.Ticker("MSFT")
df = company.history(period="max")
df.reset_index(inplace=True)
final_data = pd.DataFrame()
final_data['Date'] = df['Date']

for i in symbols:
    company = yf.Ticker(i)
    df = company.history(period="max")
    df.drop(['Open','High','Low','Close','Volume','Stock Splits'], axis=1, inplace=True)
    df.reset_index(inplace=True)
    df.rename(columns={'Dividends':i}, inplace=True)    
    final_data = pd.merge(left=final_data, right=df, how='left', left_on='Date', right_on='Date')

final_data.set_index('Date', inplace=True)

with open('dividends.csv', 'a') as f:
    final_data.to_csv(f, header=i, line_terminator='\n')
    



