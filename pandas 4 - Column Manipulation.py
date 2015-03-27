import pandas as pd
from pandas import DataFrame

import datetime
import pandas.io.data

#sp500 = pd.io.data.get_data_yahoo('%5EGSPC',
#                                  start = datetime.datetime(2000, 10, 1),
#                                  end = datetime.datetime(2014, 6, 11))

#sp500.to_csv('sp500_ohlc.csv')

df = pd.read_csv('sp500_ohlc.csv', index_col = 'Date', parse_dates=True)

print df.head()

df2 = df['Open']

print df2.head()

df3 = df[['Close','High']]

print df3.head()


df3.rename(columns={'Close': 'CLOSE!!'}, inplace=True)

print df3.head()

df4 = df3[(df3['CLOSE!!'] > 1400)]

print df4
