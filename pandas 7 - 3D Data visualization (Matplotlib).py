import pandas as pd
from pandas import DataFrame


import matplotlib.pyplot as plt
# must import
from mpl_toolkits.mplot3d import Axes3D




# CHANGE DF TO ONLY THESE THINGS TO GET AN INDEX....
df = pd.read_csv('sp500_ohlc.csv', parse_dates=True)

#print df.head()

df['H-L'] = df.High - df.Low

df['100MA'] = pd.rolling_mean(df['Close'], 100)


#print df.index


# So let's say we want to compare price, to h-l, and see
# if there's any correlation with h-l and price visually. 
threedee = plt.figure().gca(projection='3d')
threedee.scatter(df.index, df['H-L'], df['Close'])
threedee.set_xlabel('Index')
threedee.set_ylabel('H-L')
threedee.set_zlabel('Close')
plt.show()



# how about h-l, price, and volume?

threedee = plt.figure().gca(projection='3d')
threedee.scatter(df.index, df['H-L'], df['Volume'])
threedee.set_xlabel('Index')
threedee.set_ylabel('H-L')
threedee.set_zlabel('Volume')
plt.show()
