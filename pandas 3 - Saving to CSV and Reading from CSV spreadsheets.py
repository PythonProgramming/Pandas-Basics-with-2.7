import pandas as pd
from pandas import DataFrame

import datetime
import pandas.io.data



## grabbing from yahoo finance ###
sp500 = pd.io.data.get_data_yahoo('%5EGSPC', 
                                 start=datetime.datetime(2000, 10, 1), 
                                 end=datetime.datetime(2012, 1, 1))
print sp500.head()

# saving to a csv #
sp500.to_csv('sp500_ohlc.csv')


# reading from the csv #
df = pd.read_csv('sp500_ohlc.csv', index_col='Date', parse_dates=True)
df.head()

print df
