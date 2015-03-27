import pandas as pd
from pandas import DataFrame
import random

df = pd.read_csv('sp500_ohlc.csv', index_col = 'Date', parse_dates=True)
df['H-L'] = df.High - df.Low

def function(data):
    x = random.randrange(0,5)
    return data*x

df['Multiple'] = map(function, df['Close'])


print(df.head())

