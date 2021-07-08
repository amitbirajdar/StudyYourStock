from alpha_vantage.timeseries import TimeSeries
import urllib.request, json 
import pandas as pd

# "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=IBM&apikey=60W7PE08GH2UZE3N"



api_key = open('AlphaVantage_API_Key.txt', 'r').readline()

read_symbols = pd.read_csv('symbols.txt', header=None)
symbols = read_symbols[0].values.tolist()

with urllib.request.urlopen(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=IBM&apikey={api_key}") as url:
        data = json.loads(url.read().decode())
df = pd.DataFrame(data['Time Series (Daily)']).T
df = df.rename({'1. open':'open', '2. high':'high', '3. low':'low', '4. close': 'close', '5. volume':'volume'}, axis='columns')

final_data = pd.DataFrame(index=df.index, columns=symbols)


for i in symbols:
    with urllib.request.urlopen(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={i}&apikey={api_key}") as url:
        data = json.loads(url.read().decode())
    df = pd.DataFrame(data['Time Series (Daily)']).T
    df = df.rename({'1. open':'open', '2. high':'high', '3. low':'low', '4. close': 'close', '5. volume':'volume'}, axis='columns')
    df = df.drop(['open','high', 'low', 'volume'], axis='columns')
    final_data[i] = df
    print(final_data.head(1))



#df = df.drop(['open','high','low','' ], axis=1)
#print(df.head())

# for i in range(symbols.shape[0]):
#     with urllib.request.urlopen(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={symbol[0][i]}&apikey={api_key}") as url:
#         data = json.loads(url.read().decode())
#     df1 = pd.DataFrame(data['Time Series (Daily)']).T
#     df1 = df1.drop([''])
#     df1 = df1.rename({'1. open':'open', '2. high':'high', '3. low':'low', '4. close': 'close', '5. volume':'volume'}, axis='columns')


