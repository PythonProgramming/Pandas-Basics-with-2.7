import pandas as pd
from pandas import DataFrame

df = pd.read_csv('sp500_ohlc.csv', index_col = 'Date', parse_dates=True)
df['H-L'] = df.High - df.Low

# Giving us count (rows), mean (avg), std (standard deviation for the entire
# set), minimum for the set, maximum for the set, and some %s in that range.
print( df.describe())

x = input('enter to cont')

# gives us correlation data. Remember the 3d chart we plotted?
# now you can see if correlation of H-L and Volume also is correlated
# with price swings. Correlations for your correlations
print( df.corr())
x = input('enter to cont')

# covariance... now plenty of people know what correlation is, but what in the
# heck is covariance.

# Let's defined the two.
# covariance is the measure of how two variables change together.
# correlation is the measure of how two variables move in relation to eachother.

# so covariance is  a more direct assessment of the relationship between two variables.
# Maybe a better way to put it is that covariance is the measure of the strength of correlation.

print( df.cov())
x = input('enter to cont')

print( df[['Volume','H-L']].corr())
x = input('enter to cont')

# see how it makes a table?
# so now, we can actually perform a service that some people actually pay for
# I once had a short freelance gig doing this

# so a popular form of analysis within especially forex is to compare correlations between
# the currencies. The idea here is that you pace one currency with another.
# 


import datetime
import pandas.io.data

C = pd.io.data.get_data_yahoo('C', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
AAPL = pd.io.data.get_data_yahoo('AAPL', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
MSFT = pd.io.data.get_data_yahoo('MSFT', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
TSLA = pd.io.data.get_data_yahoo('TSLA', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))


print( C.head())
x = input('enter to cont')

del C['Open']
# , 'high', 'low', 'close', 'volume'
del C['High']
del C['Low']
del C['Close']
del C['Volume']



corComp = C



corComp.rename(columns={'Adj Close': 'C'}, inplace=True)

corComp['AAPL'] = AAPL['Adj Close']
corComp['MSFT'] = MSFT['Adj Close']
corComp['TSLA'] = TSLA['Adj Close']

print( corComp.head())
x = input('enter to cont')

print( corComp.corr())
x = input('enter to cont')


C = pd.io.data.get_data_yahoo('C', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
AAPL = pd.io.data.get_data_yahoo('AAPL', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
MSFT = pd.io.data.get_data_yahoo('MSFT', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
TSLA = pd.io.data.get_data_yahoo('TSLA', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
BAC = pd.io.data.get_data_yahoo('BAC', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
BBRY = pd.io.data.get_data_yahoo('BBRY', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
CMG = pd.io.data.get_data_yahoo('CMG', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
EBAY = pd.io.data.get_data_yahoo('EBAY', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
JPM = pd.io.data.get_data_yahoo('JPM', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
SBUX = pd.io.data.get_data_yahoo('SBUX', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
TGT = pd.io.data.get_data_yahoo('TGT', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))
WFC = pd.io.data.get_data_yahoo('WFC', 
                                 start=datetime.datetime(2011, 10, 1), 
                                 end=datetime.datetime(2014, 1, 1))

x = input('enter to cont')
print( C.head())

del C['Open']
# , 'high', 'low', 'close', 'volume'
del C['High']
del C['Low']
del C['Close']
del C['Volume']



corComp = C



corComp.rename(columns={'Adj Close': 'C'}, inplace=True)

corComp['BAC'] = BAC['Adj Close']
corComp['MSFT'] = MSFT['Adj Close']
corComp['TSLA'] = TSLA['Adj Close']

corComp['AAPL'] = AAPL['Adj Close']
corComp['BBRY'] = BBRY['Adj Close']
corComp['CMG'] = CMG['Adj Close']
corComp['EBAY'] = EBAY['Adj Close']
corComp['JPM'] = JPM['Adj Close']
corComp['SBUX'] = SBUX['Adj Close']
corComp['TGT'] = TGT['Adj Close']
corComp['WFC'] = WFC['Adj Close']


print( corComp.head())
x = input('enter to cont')

print( corComp.corr())

x = input('enter to cont')

fancy = corComp.corr()
fancy.to_csv('bigmoney.csv')





