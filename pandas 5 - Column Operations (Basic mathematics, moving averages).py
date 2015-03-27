import pandas as pd
from pandas import DataFrame


df = pd.read_csv('sp500_ohlc.csv', index_col = 'Date', parse_dates=True)


#notice what i did, since it is an object
df['H-L'] = df.High - df.Low

print df.head()


df['100MA'] = pd.rolling_mean(df['Close'], 100)

# must do a slice, since there will be no value for 100ma until 100 points
print df[200:210]

df['Difference'] = df['Close'].diff()


print df.head()

