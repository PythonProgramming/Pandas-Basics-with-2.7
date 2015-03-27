import pandas as pd
from pandas import DataFrame

####
import matplotlib.pyplot as plt


df = pd.read_csv('sp500_ohlc.csv', index_col = 'Date', parse_dates=True)

print(df.head())

df['H-L'] = df.High - df.Low

df['100MA'] = pd.rolling_mean(df['Close'], 100)

print(df[200:210])

# do initially df.plot 
df[['Open','High','Low','Close','100MA']].plot()
plt.show()
