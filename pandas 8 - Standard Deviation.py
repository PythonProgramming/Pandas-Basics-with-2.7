import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt

from matplotlib import style

style.use('ggplot')


df = pd.read_csv('sp500_ohlc.csv', index_col = 'Date', parse_dates=True)

#print df.head()
df['STD'] = pd.rolling_std(df['Close'], 25, min_periods=1)

ax1 = plt.subplot(2, 1, 1)
df['Close'].plot()
plt.ylabel('Close')


# do not do sharex first
ax2 = plt.subplot(2, 1, 2, sharex = ax1)
df['STD'].plot()
plt.ylabel('Standard Deviation')

plt.show()
